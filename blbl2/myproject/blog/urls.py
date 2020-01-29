from django.conf.urls import url
from .import views
from django.urls import path


app_name = "blog"
urlpatterns = [
    url(r"^all-blogs/$", views.blog_list, name="all_blogs"),
    # url(r"^blog-detail/(?P<blog_id>\d+)/$", views.blog_detail, name="blog_detail"),
    path('<int:blog_pk>', views.blog_detail, name="blog_detail"),
    path('type/<int:blog_type_pk>', views.blog_with_type, name="blog_with_type"),

]


