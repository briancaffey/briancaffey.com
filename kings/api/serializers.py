from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Game

class GameSerializer(ModelSerializer):

    id = serializers.ReadOnlyField()

    class Meta:
        model = Game
        fields = [
            'id',
            'game',
        ]
