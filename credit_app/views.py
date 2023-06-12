from django.shortcuts import render
from .db_query import get_producers_by_contract
from .forms import FormByPk


def index(request):
    form = FormByPk()
    context = {"form": form}

    if request.method == 'POST':
        form_data = FormByPk(request.POST)

        if form_data.is_valid():

            if producers_id := get_producers_by_contract(
                    form_data.cleaned_data
            ):
                context.update({"producers_id": producers_id})
            else:
                context.update({"error": "No such contract"})
    return render(request, 'index.html', context)
