from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import OpenFireUser
from django.contrib.auth import get_user


class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        current_user = get_user(request)
        users = current_user.openfireuser_set.all()
        return render(request, 'website/index.html', context={'open_fire_users': users})


class WebSiteLoginView(LoginView):
    template_name = 'website/registration/login.html'
    redirect_authenticated_user = 'index'


class WebSiteLogoutView(LogoutView):
    template_name = 'website/registration/logged_out.html'
    next_page = 'index'


class second_index(View):
    def delete(self, request, *args, **kwargs):
        return HttpResponse("done!")
