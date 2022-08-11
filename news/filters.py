from django_filters import FilterSet, CharFilter, ModelChoiceFilter, DateFilter,DateFromToRangeFilter, NumberFilter, ChoiceFilter, AllValuesFilter
from django.contrib.auth.models import User
from django import forms

from .models import Post, Author, Category, Comment
# создаём фильтр
class PostFilter(FilterSet):
    time_create = DateFilter(label='Дата публикации', lookup_expr='gte', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    rating = NumberFilter(label='Рейтинг', lookup_expr='gte')
    title = CharFilter(label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-control pure-input-1-2',  'placeholder': 'Post Title'}))
    class Meta:
        model = Post
        fields = ['author__user_author',  'category_type', 'title']


class F(FilterSet):
  username = CharFilter(method='my_filter')
  class Meta:
    model = User
    fields = ['username']

  def my_filter(self, queryset, name, value):
    return queryset.filter(**{name: value})

class C(FilterSet):
    category = ModelChoiceFilter(queryset=Category.objects.all())

    class Meta:
      model = Post
      fields = ['category']

class D(FilterSet):
    date = DateFromToRangeFilter()

    class Meta:
      model = Comment
      fields = ['date']

