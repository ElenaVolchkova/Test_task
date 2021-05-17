from django.shortcuts import render

# Create your views here.
from test_task.models import CreditApplication

def contracts_list(request):
    contracts = CreditApplication.objects.all()
    context = {"contracts": contracts}
    return render(request, "test_task/contracts_list.html", context)

#
def contract_detail(request, pk):
    contract = CreditApplication.objects.get(pk=pk)
    context = {"contract": contract}
    return render(request, "test_task/contract_detail.html", context)

