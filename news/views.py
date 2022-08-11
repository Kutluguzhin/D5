from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.forms import forms
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView,  DeleteView, TemplateView

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView

# импортируем недавно написанный фильтр
from .filters import PostFilter, F, C, D
from .forms import PostForm, ProfileUserForm  # импортируем нашу форму
from .models import Post, Comment, Category, Author, User


class PostList(ListView):
    model = Post
    ordering = 'time_create'
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    queryset = Post.objects.order_by('-time_create')
    form_class = PostForm
    paginate_by = 10 # вот так мы можем указать количество записей на странице

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['categories'] = Category.objects.all()
        context['form'] = PostForm
        return context


class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельной новости
    model = Post
    # Используем другой шаблон — news_one.html
    template_name = 'news_one.html'
    # Название объекта, в котором будет выбранная пользователем новость
    context_object_name = 'news_one'


class ProfileUserUpdate(LoginRequiredMixin, UpdateView):
    form_class = ProfileUserForm
    model = User
    template_name = 'profile_edit.html'
    success_url = '/news/'


class HomePageView(View):
    template_name = "index.html"


class SearchNews(ListView):
    template_name = 'search.html'
    context_object_name = 'search_news'
    queryset = Post.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['categories'] = Category.objects.all()
        context['form'] = PostForm
        return context


class PostCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = '/news/'

    permission_required = ('news.add_post')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_author = Author.objects.get(authorUsername=self.request.user)
        # print(self.request.user)
        self.object.save()
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = '/news/'

    permission_required = ('news.change_post')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = "/news/"

    permission_required = ('news.delete_post')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
# Create your views here.
