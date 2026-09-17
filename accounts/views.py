from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import RegisterForm, ProfileForm


class UserLoginView(LoginView):

    template_name = "accounts/login.html"

    authentication_form = AuthenticationForm

    redirect_authenticated_user = True


def user_logout(request):

    logout(request)

    return redirect("blog:home")


def register(request):

    if request.user.is_authenticated:
        return redirect("blog:home")

    form = RegisterForm(
        request.POST or None
    )

    if request.method == "POST":

        if form.is_valid():

            user = form.save()

            login(
                request,
                user,
            )

            messages.success(
                request,
                "Account created successfully.",
            )

            return redirect("blog:home")

    return render(
        request,
        "accounts/register.html",
        {
            "form": form,
        },
    )


@login_required
def profile(request):

    form = ProfileForm(
        request.POST or None,
        instance=request.user,
    )

    if request.method == "POST":

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Profile updated successfully.",
            )

            return redirect(
                "accounts:profile"
            )

    return render(
        request,
        "accounts/profile.html",
        {
            "form": form,
        },
    )