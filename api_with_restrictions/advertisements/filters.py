from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementDateFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()
    creator = filters.NumberFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator']

