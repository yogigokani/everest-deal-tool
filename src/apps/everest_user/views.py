import random
from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import get_user_model

User = get_user_model()


def everest_login(request):
    if request.method == "GET":
        login_form = LoginForm()
    elif request.method == "POST":
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get("email_id", None)
            password = login_form.cleaned_data.get("password", None)
            user_from_db = User.objects.get(username__iexact=username)
            user = authenticate(username=user_from_db.username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy('home:index'))
        return HttpResponseRedirect(reverse_lazy('user:login'))

    context = {
        "image_pick": random.choice([x for x in range(1, 7)]),
        "login_form": login_form,
    }
    return render(request, "everest_user/login.html", context)


def everest_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('user:login'))
