from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post

# Create your views here.

# API HOME ------------------
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'URLS': 'List of all urls',
        
        'post-list' : 'To List all posts....',
        
        'post-detail' : 'To view post detail by ID',
        
        'post-create' : 'To create a post',
        
        'post-update' : 'To update post by ID',
        
        'post-delete' : 'To delete post by ID '
    }
    
    return Response(api_urls)

# Post List ------------------------
@api_view(['GET'])
def postList(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

# Post Detail -----------------------
@api_view(['GET'])
def postDetail(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)
    

# Post Create -----------------------
@api_view(['POST'])
def postCreate(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)


# Post Update -----------------------
@api_view(['POST'])
def postUpdate(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)


# Post Delete -----------------------
@api_view(['DELETE'])
def postDelete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
        
    return Response('Post Deleted Successfully')