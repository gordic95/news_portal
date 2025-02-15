from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import PostFilter
from .forms import PostForm
from .models import Post, Category, Subscribers, PostCategory


class PostListView(ListView):
    model = Post
    template_name = 'news/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_create']
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'news/post_detail.html'
    context_object_name = 'post'


class PostCreateView(PermissionRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news/post_create.html'
    permission_required = 'news.add_post'



    def form_valid(self, form):
        posts = form.save(commit=False)
        if self.request.path == 'posts/create/':
            posts.post_type = 'NE'
        else:
            posts.post_type = 'AR'
        posts.save()
        return super().form_valid(form)


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news/post_create.html'
    permission_required = 'news.change_post'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'news/post_delete.html'
    success_url = reverse_lazy('posts_list')


class CategoryListView(ListView):
    model = Category
    template_name = 'news/category_list.html'
    context_object_name = 'categories'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['not_cubscriber'] = self.request.user not in Subscribers.objects.all()
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'news/category_detail.html'
    context_object_name = 'category'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.object  # текущий объект категории
        posts = Post.objects.filter(categories__category=category).distinct()
        context['posts'] = posts
        return context





class SubscribersListView(ListView):
    model = Subscribers
    template_name = 'news/subscribers_list.html'
    context_object_name = 'subscribers'


class SubscribersDetailView(DetailView):
    model = Subscribers
    template_name = 'news/subscriber_detail.html'
    context_object_name = 'subscriber'


@login_required
def subscribe(self, pk):
    subscribe = Subscribers.objects.get(pk=pk)
    subscribe.subscribers.add(self.request.user)
    subscribe.save()


    message = 'Теперь вы подписаны на рассылку новостей этой категории.'
    return render(self.request, 'news/sub_user_message.html', {'message': message})









