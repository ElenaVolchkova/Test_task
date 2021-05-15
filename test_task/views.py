from django.shortcuts import render

# Create your views here.
from test_task.models import CreditApplication


# def manufacturers_list(request, id):
#     manufacturers = CreditApplication.objects.get(pk=id)
#     context = {"manufacturers": manufacturers}

def manufacturers_list(request):
    manufacturers = CreditApplication.objects.all()
    context = {"manufacturers": manufacturers}
    return render(request, "test_task/manufacturers_list.html", context)