from ..models import HashItem, HashItemReferencingItem
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from .serializers import HashItemSerializer, HashItemReferencingItemSerializer


class HashItemListAPIView(ListAPIView):
    queryset = HashItem.objects.all()
    serializer_class = HashItemSerializer


class HashReferencingListAPIView(ListAPIView):
    queryset = HashItemReferencingItem.objects.all()
    serializer_class = HashItemReferencingItemSerializer
