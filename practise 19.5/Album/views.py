from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.views.generic import CreateView, UpdateView, DeleteView


# Create your views here.
def add_album(request):
    if request.method == "POST":
        album_form = forms.add_album(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect("add_album")

    else:
        album_form = forms.add_album()
    return render(request, "add_album.html", {"form": album_form})


class Addalbum(CreateView):
    model = models.album
    form_class = forms.add_album
    template_name = "add_album.html"
    success_url = reverse_lazy("addalbum")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def edit_post(request, id):
    post = models.album.objects.get(pk=id)
    album_form = forms.add_album(instance=post)
    if request.method == "POST":
        album_form = forms.add_album(request.POST, instance=post)
        if album_form.is_valid():
            album_form.save()
            return redirect("home")

    return render(request, "add_album.html", {"form": album_form})


class EditPost(UpdateView):
    model = models.album
    form_class = forms.add_album
    template_name = "add_album.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")


def delete_post(request, id):
    post = models.album.objects.get(pk=id)
    post.delete()
    return redirect("home")


class DeletePost(DeleteView):
    model = models.album
    success_url = reverse_lazy("home")
    template_name = "delete.html"
    pk_url_kwarg = "id"
