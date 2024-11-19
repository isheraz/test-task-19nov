from rest_framework import serializers
from random import sample
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

    def get_comments(self, obj):
        # Fetch all comments
        all_comments = list(obj.comments.all())

        # Randomly sample up to 3 comments
        random_comments = sample(all_comments, min(3, len(all_comments)))
        return CommentSerializer(random_comments, many=True).data

    def get_comment_count(self, obj):
        # Count total comments for the post
        return obj.comments.count()
