# Django:
from django.urls import path

# Localfolder:
from . import views

app_name = "test_task"

urlpatterns = [
    path("", views.applications_list, name="applications-list"),
    path("application/<int:pk>/", views.application_detail, name="application_detail"),
]
