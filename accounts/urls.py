from django.urls import path

from .views import (
    UserLoginView,
    user_logout,
    register,
    profile,
)


app_name = "accounts"


urlpatterns = [

    path(
        "accounts/login/",
        UserLoginView.as_view(),
        name="login",
    ),

    path(
        "accounts/logout/",
        user_logout,
        name="logout",
    ),

    path(
        "accounts/register/",
        register,
        name="register",
    ),

    path(
        "accounts/profile/",
        profile,
        name="profile",
    ),
]