from django.contrib import admin
from . models import Post, Comment, Category, Reply

admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'category', 'published_on')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(active=True)

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'comment', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_reply']

    def approve_reply(self, request, queryset):
        queryset.update(active=True)



