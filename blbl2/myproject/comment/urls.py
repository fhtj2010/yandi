from django.conf.urls import url
from . import views

app_name = "comment"
urlpatterns = [
    url(r"^update-comment/$", views.update_comment, name="update_comment"),

]