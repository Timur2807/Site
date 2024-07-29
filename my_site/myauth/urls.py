from django.contrib.auth.views import LoginView
from django.urls import path
from .views import (
    set_cookie_view,
    get_cookie_view,
    get_session_view,
    set_session_view,
    logout_view,
    My_Logout_View,
    AboutMeView,
    RegistorView,
    FooBarView,
    HelloView,
)

app_name = "myauth"

urlpatterns = [
    path(
        "login/", LoginView.as_view(
            template_name="myauth/login.html",
            redirect_authenticated_user=True,
        ), name="login"
    ),
    path("cookie/get/", get_cookie_view, name="cookie-get"),
    path("session/get/", get_session_view, name="session_get"),
    path("cookie/set/", set_cookie_view, name="cookie_set"),
    path("session/set/", set_session_view, name="session_set"),
    path("logout/", logout_view, name="logout"),
    path("about-me/", AboutMeView.as_view(), name="about-me"),
    path("register/", RegistorView.as_view(), name="register"),
    path("foo-bar/", FooBarView.as_view(), name="foo-bar"),
    path("hello/", HelloView.as_view(), name="hello-world"),

]
