from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required


@login_required(login_url=reverse_lazy('user:login'))
def home(request):
    context = {}
    return render(request, "home/home.html", context)
