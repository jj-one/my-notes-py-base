from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
  path("", views.getRoutes, name="routes"),
  path("notes/", views.getNotes, name="notes"),
  path("notes/create/", views.createNote, name="create"),
  path("notes/<int:id>/update/", views.updateNote, name="update"),
  path("notes/<int:id>/delete/", views.deleteNote, name="delete"),
  path("notes/<int:id>/", views.getNote, name="note"),
]