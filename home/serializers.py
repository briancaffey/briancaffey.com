from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from home.models import GuestBook

class GuestBookSerializer(ModelSerializer):

    message = serializers.CharField(allow_blank=False, required=True)

    class Meta:
        model = GuestBook
        fields = [
            'message',
            # 'user',

        ]
        # extra_kwargs = {'message': {'required':True}}
