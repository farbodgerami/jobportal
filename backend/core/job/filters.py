from django_filters import rest_framework as filters

from .models import *

import django_filters
class JobsFilter(django_filters.FilterSet):
    keyword=filters.CharFilter(field_name='title',lookup_expr='icontains')
    location=filters.CharFilter(field_name='address',lookup_expr='icontains')
    min_salary=filters.NumberFilter(field_name="salary" or 0,lookup_expr='gte')
    max_salary=filters.NumberFilter(field_name="salary" or 1000000,lookup_expr='lte')
    jobType=django_filters.MultipleChoiceFilter(choices=JobType.choices)
 
    class Meta:
        model=Job
     
        fields={} 







 