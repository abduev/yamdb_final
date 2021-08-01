from django_filters import FilterSet, CharFilter, NumberFilter

from .models import Title


class TitleFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    year = NumberFilter(field_name='year')
    category = CharFilter(field_name='category__slug')
    genre = CharFilter(field_name='genre__slug')

    class Meta:
        fields = ('name', 'year', 'category', 'genre')
        model = Title
