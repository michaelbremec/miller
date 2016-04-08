import json
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework import serializers,viewsets
from rest_framework.response import Response

from miller.models import Story, Tag, Document, Caption


class CaptionSerializer(serializers.HyperlinkedModelSerializer):
  document_id    = serializers.ReadOnlyField(source='document.id')
  type  = serializers.ReadOnlyField(source='document.type')
  title = serializers.ReadOnlyField(source='document.title')
  slug  = serializers.ReadOnlyField(source='document.slug')
  src   = serializers.ReadOnlyField(source='document.attachment.url')
  short_url = serializers.ReadOnlyField(source='document.short_url')
  copyrights = serializers.ReadOnlyField(source='document.copyrights')
  caption = serializers.ReadOnlyField(source='contents')

  class Meta:
    model = Caption
    fields = ('id', 'document_id', 'title', 'slug', 'type', 'copyrights', 'caption', 'short_url', 'src')

# tag represnetation in many to many
class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = ('id', 'category', 'name')

# serializer the authors.
class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'first_name', 'last_name', 'is_staff', 'url')


# Serializers define the API representation.
class StorySerializer(serializers.HyperlinkedModelSerializer):
  authors = AuthorSerializer(many=True)
  owner = AuthorSerializer()
  tags = TagSerializer(many=True)
  documents = CaptionSerializer(source='caption_set', many=True)
  class Meta:
    model = Story
    fields = ('id','url', 'short_url', 'title', 'abstract', 'documents', 'contents', 'date', 'status', 'cover', 'cover_copyright', 'authors', 'tags', 'owner')

class LiteStorySerializer(serializers.HyperlinkedModelSerializer):
  authors = AuthorSerializer(many=True)
  owner = AuthorSerializer()
  tags = TagSerializer(many=True)
  class Meta:
    model = Story
    fields = ('id','url', 'short_url', 'title', 'abstract', 'date', 'status', 'cover', 'cover_copyright', 'authors', 'tags', 'owner')


    
# ViewSets define the view behavior. Filter by status
class StoryViewSet(viewsets.ModelViewSet):
  queryset = Story.objects.all()
  serializer_class = LiteStorySerializer


  def list(self, request):
    filters = self.request.query_params.get('filters', None)
    
    if filters is not None:
      print filters
      try:
        filters = json.loads(filters)
        print "filters,",filters
      except Exception, e:
        print e
        filters = {}
    else:
      filters = {}
    
    if request.user.is_authenticated():
      stories = self.queryset.filter(Q(owner=request.user) | Q(authors=request.user) | Q(status=Story.PUBLIC)).filter(**filters).distinct()
    else:
      stories = self.queryset.filter(status=Story.PUBLIC).filter(**filters).distinct()
    print stories.query
    page    = self.paginate_queryset(stories)

    serializer = LiteStorySerializer(stories, many=True,
        context={'request': request}
    )
    return self.get_paginated_response(serializer.data)

  def retrieve(self, request, pk=None):
    if request.user.is_authenticated():
      queryset = self.queryset.filter(Q(owner=request.user) | Q(authors=request.user) | Q(status=Story.PUBLIC))
    else:
      queryset = self.queryset.filter(status=Story.PUBLIC)

    story = get_object_or_404(queryset, pk=pk)

    # // serialize with text content

    serializer = StorySerializer(story,
        context={'request': request}
    )
    return Response(serializer.data)