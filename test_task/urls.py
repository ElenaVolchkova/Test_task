# Django:
from django.urls import path

# Localfolder:
from . import views

app_name = "test_task"

urlpatterns = [
    path("", views.manufacturers_list, name="manufacturers-list"),
]