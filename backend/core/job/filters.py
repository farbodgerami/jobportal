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
        # fields=('education','jobType','experience','min_salary','max_salary',"keyword",'location')
        fields={} 











# class PropertyFilter(django_filters.FilterSet):
# city = django_filters.ModelMultipleChoiceFilter(queryset=City.objects.all(), widget = CheckboxSelectMultiple)
# trade_type = django_filters.ModelMultipleChoiceFilter(queryset=Trade.objects.all(), widget = CheckboxSelectMultiple)

# class Meta:
#     model = Property
#     fields = ['city', 'trade_type']


# class CustomFilterList(django_filters.Filter):
#     def filter(self, qs, value):
#         if value not in (None, ''):
#             values = [v for v in value.split(',')]
#             return qs.filter(**{'%s__%s' % (self.name, self.lookup_type): values})
#         return qs

# class PropertyFilter(django_filters.FilterSet):
#     city = django_filters.ModelMultipleChoiceFilter(queryset=City.objects.all(), widget = CheckboxSelectMultiple)
#     trade_type = django_filters.ModelMultipleChoiceFilter(queryset=Trade.objects.all(), widget = CheckboxSelectMultiple)
#     cities = CustomFilterList(name="city", lookup_type="in")

#     class Meta:
#         model = Property
#         fields = ['cities', 'city', 'trade_type']


