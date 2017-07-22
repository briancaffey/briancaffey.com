from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Game

class GameSerializer(ModelSerializer):

    # message = serializers.CharField(allow_blank=False, required=True)

    class Meta:
        model = Game
        fields = [
            'game'
        ]
