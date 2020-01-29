from django.conf.urls import url
from .import views

app_name = "likes"
urlpatterns = [
    url(r"^like-change/$", views.like_change, name="like_change")
]


