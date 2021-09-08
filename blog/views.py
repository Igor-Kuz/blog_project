from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import PostForm, CommentForm, EditForm
from django.db.models import Q
from .models import *


def like_view(request, slug):
    post = Post.objects.get(slug=slug)
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse(
        'post_single', kwargs={"slug": post.category.url, 'post_slug': slug})
    )


class Year:

    def get_category(self):
        return Category.objects.all()

    def get_author(self):
        return Post.objects.filter(draft=False).select_related('author').values("author__id", "author__username")


class HomeView(Year, ListView):
    model = Post
    template_name = "blog/home.html"
    cats = Category.objects.all()
    ordering = ['-published']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def categorylistview(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'blog/category_list.html', {'cat_menu_list': cat_menu_list})


class PostListView(Year, ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__url=self.kwargs.get("slug")).select_related('category')
# sdelat pod title


class SearchView(Year, ListView):
    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = f'q={self.request.GET.get("q")}&'
        return context


class PostDetailView(Year, DetailView):
    model = Post
    context_object_name = "post"
    slug_url_kwarg = 'post_slug'
    # template_name = "blog/post_detail.html"
    template_name = "blog/detail_post.html"
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        #staff = get_object_or_404(Post, id=self.kwargs['pk'])
        #total_likes = staff.total_likes()
        context['cat_menu'] = cat_menu
        #context['total_likes'] = total_likes
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


class PostByTag(Year, ListView):
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__url=self.kwargs['slug'])  # url - >slug!

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Записи по тэгу: ' + str(Tag.objects.get(url=self.kwargs['slug']))  # url - >slug!
        return context


class FilterAuthorView(Year, ListView):
    """Фильтр постов"""

    def get_queryset(self):
        queryset = Post.objects.filter(
            Q(author__in=self.request.GET.getlist("author")),
            Q(category__in=self.request.GET.getlist("category"))
        ).distinct()
        print(self.request.GET.getlist("category"))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["author"] = ''.join([f"author={x}&" for x in self.request.GET.getlist("author")])
        context["category"] = ''.join([f"category={x}&" for x in self.request.GET.getlist("category")])
        print('############', context["category"])
        return context


def category_view(request, cats):
    category_posts = Post.objects.filter(category__name=cats.replace('-', ''))
    return render(request, 'blog/categories.html', {'cats': cats.replace('-', '').title(),
                                                    'category_posts': category_posts})
