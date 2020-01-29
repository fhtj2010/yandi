from django.contrib import admin
from .models import Comment


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id","content_object", "content_type", "user", "text", "comment_time")


admin.site.register(Comment, CommentAdmin)
