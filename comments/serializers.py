from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from comments.models import Comment

class CommentSerializer(ModelSerializer):

    # message = serializers.CharField(allow_blank=False, required=True)

    class Meta:
        model = Comment
        fields = [
            'content',
            'object_id',
            'content_type',
            'user',
        ]

        extra_kwargs = {'message': {'required':True},
                        'object_id': {'read_only': True},
                        'content_type': {'read_only': True},
                        'user':{'read_only':True},
                        }
