import django_filters
from .models import Student

class CityFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(field_name='city', lookup_expr='icontains')

    class Meta:
        model = Student
        fields =['city']