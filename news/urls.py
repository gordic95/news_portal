from django.urls import path
from django.views.generic import TemplateView

from . views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CategoryListView, CategoryDetailView
from . views import SubscribersListView, SubscribersDetailView, subscribe


app_name = 'news'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts_list'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post_detail'),

    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('articles/create/', PostCreateView.as_view(), name='articles_create'),
    path('articles/<int:pk>/update/', PostUpdateView.as_view(), name='articles_update'),
    path('articles/<int:pk>/delete/', PostDeleteView.as_view(), name='articles_delete'),

    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),

    path('subscribers/', SubscribersListView.as_view(), name='subscribers_list'),
    path('subscribers/<int:pk>/', SubscribersDetailView.as_view(), name='subscribers_detail'),
    path('subscribers/<int:pk>/subscribe/', subscribe, name='subscribe'),

    path('about/', TemplateView.as_view(template_name='news/about.html'))
]


