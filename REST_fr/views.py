from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from REST_fr.models import Messages
from REST_fr.serializers import DefaultViewSerializer


# How to №1
class ModelViewSetclass(ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = DefaultViewSerializer


# How to №2
class ListAPIViewclass(ListAPIView):
    queryset = Messages.objects.all()
    serializer_class = DefaultViewSerializer


class RetrieveAPIViewclass(RetrieveAPIView):
    queryset = Messages.objects.all()
    serializer_class = DefaultViewSerializer


class CreateAPIViewclass(CreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = DefaultViewSerializer


class UpdateAPIViewclass(UpdateAPIView):
    queryset = Messages.objects.all()
    serializer_class = DefaultViewSerializer


class DestroyAPIViewclass(DestroyAPIView):
    queryset = Messages.objects.all()
    serializer_class = DefaultViewSerializer
