from ..models import Game

from .serializers import GameSerializer

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
# from rest_framework import authentication, permissions, serializers


class GameCreateAPIView(CreateAPIView):
    queryset = Game.objects.all()
    # renderer_classes = (JSONRenderer, )
    # authentication_classes = (authentication.SessionAuthentication,)
    # permission_classes = ()#(permissions.IsAuthenticated,)
    serializer_class = GameSerializer
    # 	serializer_class = GuestBookSerializer
    def perform_create(self, serializer):
        game = self.request.data
        print(game)
        _ = serializer.save(game=game)
        return Response(_)
