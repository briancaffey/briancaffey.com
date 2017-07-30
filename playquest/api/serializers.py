from rest_framework import serializers
from hashid_field.rest import HashidSerializerCharField
from ..models import Game, GamePlay


from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Game


class GameSaveSerializer(ModelSerializer):

    id = serializers.SerializerMethodField()
    class Meta:
        model = Game
        fields = [
            'id'
            'game_data',

        ]

    def get_id(self, obj):
        return str(obj.id)






class GameSerializer(ModelSerializer):

    id = HashidSerializerCharField(source_field='playquest.Game.id')

    class Meta:
        model = Game
        fields = [
            'id',
            'game_data',
            'game_owner',
        ]


class GamePlaySerializer(ModelSerializer):
    game_id = serializers.PrimaryKeyRelatedField(pk_field=HashidSerializerCharField(source_field='playquest.Game.id'), read_only=True)

    class Meta:
        model = GamePlay
        fields = [
            'game_id',
            'player',
            'gameplay_uid',
        ]
