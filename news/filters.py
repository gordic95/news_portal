from django_filters import FilterSet, BooleanFilter, DateFromToRangeFilter
from django_filters.widgets import BooleanWidget

from .models import Post
import django_filters

class PostFilter(django_filters.FilterSet):
    date_create = django_filters.DateFilter(lookup_expr='gt')
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author': ['exact'],
        }
#доделать тут

