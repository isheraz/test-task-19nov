from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer

class PostListView(APIView):
    def get(self, request):
        # Fetch posts ordered by timestamp (latest first)
        posts = Post.objects.all().order_by('-timestamp')

        # Add pagination
        paginator = PageNumberPagination()
        paginator.page_size = 10  # Adjust page size as needed
        paginated_posts = paginator.paginate_queryset(posts, request)

        # Serialize data
        serializer = PostSerializer(paginated_posts, many=True)
        return paginator.get_paginated_response(serializer.data)
