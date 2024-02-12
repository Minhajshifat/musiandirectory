from django.urls import path, include
from . import views

urlpatterns = [
    path("add_musician/", views.add_musician, name="add_musician"),
    path("registation/", views.signup.as_view(), name="register"),
    path("login/", views.UserLogin.as_view(), name="user_login"),
    path("logout/", views.Userlogout.as_view(), name="logout"),
    path("edit/<int:id>/", views.edit_musician, name="editmusician"),
    path("/Edit/<int:id>/", views.EditMusician.as_view(), name="EditMusician"),
]
