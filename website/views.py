from django.shortcuts import render, Http404, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user
from .models import OpenFireUser
from .forms import OpenFireUserForm
from django.contrib import messages


class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        users = request.user.openfireuser_set.all()
        return render(request, 'website/index.html', context={'open_fire_users': users})


class WebSiteLoginView(LoginView):
    template_name = 'website/registration/login.html'
    redirect_authenticated_user = 'index'


class WebSiteLogoutView(LogoutView):
    template_name = 'website/registration/logged_out.html'
    next_page = 'index'


class OpenFireUserView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        method = self.get_method_type(request)
        if method == "POST":
            return self.post(request, *args, **kwargs)
        elif method == "DELETE":
            return self.delete(request, *args, **kwargs)
        else:
            raise Http404

    def get_method_type(self, request):
        if request.method == "GET":
            return "GET"
        elif "_method" in request.POST:
            return request.POST["_method"].upper()
        else:
            return "POST"

    def post(self, request, *args, **kwargs):
        # create new user using form
        new_openfire = OpenFireUserForm(request.POST)
        if new_openfire.is_valid():
            new_openfire.save()
        else:
            if new_openfire.has_error("username"):
                messages.add_message(request, messages.WARNING, new_openfire.errors["username"][0])
            if new_openfire.has_error("password"):
                messages.add_message(request, messages.WARNING, new_openfire.errors["password"][0])
        return redirect('index')

    def delete(self, request, *args, **kwargs):
        # delete user using request
        if "user_pk" in request.POST:
            old_open_fire = get_object_or_404(OpenFireUser, pk=request.POST["user_pk"])
            old_open_fire.delete()
        return redirect('index')
