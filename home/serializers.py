from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from home.models import GuestBook

class GuestBookSerializer(ModelSerializer):

    # message = serializers.CharField(allow_blank=False, required=True)

    class Meta:
        model = GuestBook
        fields = [
            'message',
            'user',
            'city',
            'state',

        ]
        extra_kwargs = {'message': {'required':False},
                        'city': {'read_only': True},
                        'state': {'read_only': True},
                        'user':{'read_only':True},
                        }
