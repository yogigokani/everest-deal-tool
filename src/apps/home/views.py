from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from apps.deal_tool.models import Deal


@login_required(login_url=reverse_lazy('user:login'))
def home(request):
    context = {
        "data": Deal.list_deals_in_json()
    }
    return render(request, "home/home.html", context)
