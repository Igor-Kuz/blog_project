from django.contrib import admin

from .models import Post, Comment, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'status')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'author', 'category', 'tags')
    search_fields = ('title', 'category')


@admin.register(Comment)
class PostComment(admin.ModelAdmin):
    list_display = ('text', 'author')
    list_filter = ('published', 'author')
    search_fields = ('published', 'author')


admin.site.register(Category)

 
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)