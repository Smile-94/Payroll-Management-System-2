import django_filters
from django import forms
from datetime import datetime

from accounts.models import User
from authority.models import PayrollMonth


class EmployeeListFilter(django_filters.FilterSet):
    email = django_filters.CharFilter(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = {
            'email': {'exact'},
        }


class PayrollMonthListFilter(django_filters.FilterSet):
    current_year = datetime.now().year
    year_choices = [(year, year) for year in range(current_year-5, current_year+5)]
    year = django_filters.ChoiceFilter(choices=year_choices, empty_label='Year')
    
    class Meta:
       model= PayrollMonth
       fields = {
            'month' : {'exact'},
            'year'  : {'exact'}
       }
        