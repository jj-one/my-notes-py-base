from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
  path("", views.getRoutes, name="routes"),
  path("notes/", views.getNotes, name="notes"),
  path("notes/<int:id>/", views.getNote, name="note"),
]