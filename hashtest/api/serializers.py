from rest_framework import serializers
from hashid_field.rest import HashidSerializerCharField
from ..models import HashItem, HashItemReferencingItem


class HashItemSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(source_field='hashtest.HashItem.id')

    class Meta:
        model = HashItem
        fields = ('id', 'item_owner')




class HashItemReferencingItemSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(pk_field=HashidSerializerCharField(source_field='hashtest.HashItem.id'), read_only=True)

    class Meta:
        model = HashItemReferencingItem
        fields = ('item', 'item_uid')
