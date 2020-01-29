from django.contrib import admin
from .models import BlogType, Blog, ReadNum


# Register your models here.

class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "type_name")


admin.site.register(BlogType, BlogTypeAdmin)

# get_read_num是Blog models里返回值的方法
class BlogAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "created_time", "content", "blog_type", "get_read_num")


admin.site.register(Blog, BlogAdmin)


class ReadNumAdmin(admin.ModelAdmin):
    list_display = ("blog", "read_num")


admin.site.register(ReadNum, ReadNumAdmin)
