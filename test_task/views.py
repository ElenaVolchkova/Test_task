from django.shortcuts import render

# Create your views here.
from test_task.models import Product

def applications_list(request):
    applications = Product.objects.all()
    context = {"applications": applications}
    return render(request, "test_task/applications_list.html", context)


def application_detail(request, id):
    application = Product.objects.get(pk=id)
    context = {"application": application}
    return render(request, "test_task/application_detail.html", context)

