from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from . import models
from .forms import registations
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, View
from django.urls import reverse_lazy


# Create your views here.
def add_musician(request):
    if request.method == "POST":
        musician_form = forms.add_musician(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect("add_album")
    else:
        musician_form = forms.add_musician()
        return render(request, "add_musician.html", {"form": musician_form})


class Addmusician(CreateView):
    model = models.musician
    form_class = forms.add_musician
    template_name = "add_musician.html"
    success_url = reverse_lazy("home")


def edit_musician(request, id):
    post = models.musician.objects.get(pk=id)
    musician_form = forms.add_musician(instance=post)
    if request.method == "POST":
        musician_form = forms.add_musician(request.POST, instance=post)
        if musician_form.is_valid():
            musician_form.save()
            return redirect("home")
    return render(request, "add_musician.html", {"form": musician_form})


class EditMusician(UpdateView):
    model = models.musician
    form_class = forms.add_musician
    template_name = "add_musician.html"
    success_url = reverse_lazy("home")
    pk_url_kwarg = "id"


def userlogin(request):
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
        user_name = form.cleaned_data["username"]
        user_pass = form.cleaned_data["password"]
        user = authenticate(username=user_name, password=user_pass)
        if user is not None:
            messages.success(request, "log in successfully")
            return redirect("user_login")
        else:
            messages.warning(request, "incorrect log in information")
            return redirect("register")
    else:
        form = AuthenticationForm()
        return render(request, "./registation.html", {"form": form, "type": "Log IN"})


class signup(CreateView):
    form_class = forms.registations
    template_name = "registation.html"
    success_url = reverse_lazy("user_login")


class UserLogin(LoginView):
    template_name = "registation.html"

    def get_success_url(self):
        return reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, "Logged in successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Logged in information incorrect")
        return super().form_invalid(form)


class Userlogout(View):
    def get(self, request):
        messages.success(self.request, "Logged out successfully")
        logout(request)
        return redirect("home")


def register(request):
    if request.method == "POST":
        form = registations(request.POST)
        if form.is_valid():
            messages.success(request, "Account created succcessfully")
            form.save()
            return redirect("home")
    else:
        form = registations()
    return render(request, "./registation.html", {"form": form, "type": "register"})
