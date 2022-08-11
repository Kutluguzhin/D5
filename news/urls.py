from django.urls import path
from .views import PostList, PostDetail, SearchNews, PostCreate, PostUpdate, PostDelete, ProfileUserUpdate

urlpatterns = [
    path('news/', PostList.as_view()),
    path('news/<int:pk>', PostDetail.as_view()),
    path('news/search', SearchNews.as_view(), name='search_news'),
    path('news/create/', PostCreate.as_view(), name='post_create'),
    path('news/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('profile/<int:pk>/update/', ProfileUserUpdate.as_view(), name='profile_user_update'),
]
