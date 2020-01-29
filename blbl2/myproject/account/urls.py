from django.conf.urls import url

from .import views

app_name = "account"
urlpatterns = [
    url(r"^login/$", views.user_login, name="login"),
    url(r"^user-register/$", views.user_register, name="user_register"),
    url(r"^reg/$", views.reg, name="reg"),
    url(r"^login-for-medal/$", views.login_for_medal, name="login_for_medal"),
    url(r"^logout/$", views.logout, name="logout"),
    url(r"user-info/$", views.user_info, name="user_info"),
    url(r"^change-nickname/$", views.change_nickname, name="change_nickname"),
    url(r"^bind-email/$", views.bind_email, name="bind_email"),
    url(r"^change-password/$", views.change_password, name="change_password"),
    url(r"^forgot-password/$", views.forgot_password, name="forgot_password"),
    url(r"^send-verification-code/$", views.send_verification_code, name="send_verification_code"),
]