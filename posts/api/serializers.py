from rest_framework.serializers import ModelSerializer

from posts.models import Post

class PostCreateSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish',
        ]

class PostListSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish',
            'user',
        ]



class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish',
        ]
