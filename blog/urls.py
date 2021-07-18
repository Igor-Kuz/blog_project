from django.urls import path
from .views import HomeView, PostDetailView, PostListView, AddPostView, AddCommentView, DeletePostView, UpdatePostView,    AddCategoryView, CategoryView, CategoryListView

urlpatterns = [
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('post_list/', PostListView.as_view(), name="post_list"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('new_comment/<int:pk>/comment', AddCommentView.as_view(), name="new_comment"),
    path('delete_post/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('update_post/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('category/<slug:cats>', CategoryView, name="category"),  # <str:cats>/
    path('category_list/', CategoryListView, name="category_list"),
    path('<slug:slug>/<slug:post_slug>/', PostDetailView.as_view(), name="post_single"),
    path('', HomeView.as_view(), name="home"),   # home
]
