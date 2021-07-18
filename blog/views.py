from django.shortcuts import render, get_object_or_404
from django.template.context_processors import request
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm, EditForm
from django.http import HttpResponseRedirect
# from mysite.user.models import User


class HomeView(ListView):
    model = Post
    template_name = "blog/home.html"
    cats = Category.objects.all()
    ordering = ['-published']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'blog/category_list.html', {'cat_menu_list': cat_menu_list})


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__url =self.kwargs.get("slug")).select_related('category')
# sdelat pod title


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    slug_url_kwarg = 'post_slug'
    # template_name = "blog/post_detail.html"
    template_name = "blog/detail_post.html"
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/new_comment.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    template_name = 'blog/add_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category__name=cats.replace('-', ''))
    return render(request, 'blog/categories.html', {'cats': cats.replace('-', '').title(), 'category_posts': category_posts})
