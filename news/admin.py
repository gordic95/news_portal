from django.contrib import admin
from . models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'post_type','author')
    list_display_links = ('title', 'author')
    search_fields = ('title', 'author__username')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


class SubscribersAdmin(admin.ModelAdmin):
    list_display = ('user', 'category')
    list_display_links = ('user', 'category')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PostCategory)
admin.site.register(Subscribers, SubscribersAdmin)