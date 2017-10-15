from django.shortcuts import render, Http404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
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
        return HttpResponse("POST")

    def delete(self, request, *args, **kwargs):
        # delete user using request
        return HttpResponse("POST")
