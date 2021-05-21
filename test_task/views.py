from django.shortcuts import render

# Create your views here.
from test_task.models import CreditApplication


def contracts_list(request):
    contracts = CreditApplication.objects.all()
    context = {"contracts": contracts}
    return render(request, "test_task/contracts_list.html", context)


def contract_detail(request, pk):
    contract = CreditApplication.objects.filter(contract__pk=pk).values_list("product__manufacturer__id",
                                                                             flat=True).distinct()
    context = {"contract": contract}
    # import pdb;
    # pdb.set_trace()
    return render(request, "test_task/contract_detail.html", context)
