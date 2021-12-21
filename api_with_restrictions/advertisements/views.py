from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.filters import AdvertisementDateFilter
from advertisements.serializers import AdvertisementSerializer
from advertisements.permissions import IsOwner

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = AdvertisementDateFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in "create":
            return [IsAuthenticated()]
        if self.action in ["destroy", "update", "partial_update"]:
            return [IsOwner()]
        return []