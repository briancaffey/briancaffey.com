from rest_framework.serializers import ModelSerializer


from home.models import GuestBook

class GuestBookSerializer(ModelSerializer):
  class Meta:
    model = GuestBook
    fields = [
        'message',

    ]
