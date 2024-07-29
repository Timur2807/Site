from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView
from myauth.models import Profile
from django.views import View
from django.utils.translation import gettext_lazy as _, ngettext


class HelloView(View):
    welcome_message = _("welcome hello world!")

    def get(self, request: HttpRequest) -> HttpResponse:
        item_str = request.GET.get("items") or 0
        items = int(item_str)
        products_line = ngettext(
            "one product",
            "{count} products",
            items,
        )
        products_line = products_line.format(count=items)
        return HttpResponse(
            f"<h1>{self.welcome_message}</h1>"
            f"<h2>{products_line}</h2>"
        )


def login_view(request: HttpRequest):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/admin/')
        return render(request, 'myauth/login.html')
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/admin/')
    return render(request, 'myauth/login.html', {"error": "Invalid Login"})


@user_passes_test(lambda u: u.is_superuser)
def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("<h1>Cookie set</h1>")
    response.set_cookie("fizz", "buzz", max_age=3600)
    return response


def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get("fizz", "default value")
    return HttpResponse(f"<h1>Cookie value: {value!r}</h1>")


@permission_required("myauth.view_profile", raise_exception=True)
def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session['foobar'] = 'spameggs'
    return HttpResponse("Session set!")


@login_required
def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get("foobar", "default")
    return HttpResponse(f"<h1>Session value: {value!r}</h1>")


def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse("myauth:login"))


class My_Logout_View(LogoutView):
    next_page = reverse_lazy("myauth:login")


class AboutMeView(TemplateView):
    template_name = "myauth/about-me.html"


class RegistorView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy("myauth:about-me")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password,

        )
        login(request=self.request, user=user)
        return response


class FooBarView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({"foo": "bar", "spam": "eggs"})


