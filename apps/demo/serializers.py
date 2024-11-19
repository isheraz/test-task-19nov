from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['text', 'timestamp', 'user']

class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    comments = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['text', 'timestamp', 'user', 'comment_count', 'comments']

    def get_comments(self, obj):
        # Fetch up to 3 latest comments
        comments = obj.comments.all().order_by('-timestamp')[:3]
        return CommentSerializer(comments, many=True).data

    def get_comment_count(self, obj):
        # Count total comments for the post
        return obj.comments.count()
