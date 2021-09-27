from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from REST_fr.models import Messages


class DefaultViewSerializer(ModelSerializer):
    owner = serializers.ReadOnlyField(source='created.username')
    class Meta:
        model = Messages
        fields = ['id', 'status', 'created', 'message', 'owner']

