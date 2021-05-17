# Django:
from django.urls import path

# Localfolder:
from . import views

app_name = "test_task"

urlpatterns = [
    path("", views.contracts_list, name="contracts-list"),
    path("<int:pk>/", views.contract_detail, name="contract-detail"),
]
