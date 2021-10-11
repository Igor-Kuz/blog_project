from django.urls import path
from .views import HomeView, PostDetailView, PostListView, AddPostView, AddCommentView, DeletePostView, UpdatePostView,\
                 AddCategoryView, category_view, category_list_view, SearchView, PostByTag, FilterAuthorView, like_view

urlpatterns = [
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path("filter/", FilterAuthorView.as_view(), name='filter'),
    path('post_list/', PostListView.as_view(), name="post_list"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('search/', SearchView.as_view(), name="search"),
    path('new_comment/<int:pk>/comment', AddCommentView.as_view(), name="new_comment"),
    path('delete_post/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('update_post/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('category/<slug:cats>', category_view, name="category"),
    path('category_list/', category_list_view, name="category_list"),
    path('tag/<str:slug>/',  PostByTag.as_view(), name='tag'),
    path('like-post/<slug:slug>/', like_view, name='like_post'),
    path('<slug:slug>/<slug:post_slug>/', PostDetailView.as_view(), name="post_single"),
    path('', HomeView.as_view(), name="home"),
    ]
