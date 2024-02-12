from django.urls import path, include
from . import views

urlpatterns = [
    path("add_album/", views.add_album, name="add_album"),
    path("AddAlbum/", views.Addalbum.as_view(), name="addalbum"),
    path("edit/<int:id>", views.edit_post, name="edit_post"),
    path("Edit/<int:id>", views.EditPost.as_view(), name="editpost"),
    path("delete/<int:id>", views.delete_post, name="delete_post"),
    path("Delete/<int:id>", views.DeletePost.as_view(), name="deletepost"),
]
