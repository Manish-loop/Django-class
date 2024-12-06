from django_filters import rest_framework as filters
from teacher.models import SchoolClass

class SchoolFilters(filters.FilterSet):
    class Meta:
        model = SchoolClass
        fields = ['is_active']