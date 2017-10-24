from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.shortcuts import render, Http404, redirect, get_object_or_404
from django.views import View
from .forms import OpenFireUserForm, UserTokenForm, UserToken
from .models import OpenFireUser, Action
from .openfire import rest_api
import datetime
import hashlib
from random import random


# TODO: use toastjs for error
# TODO: add option for upload custom bot class and modules
class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        users = request.user.openfireuser_set.all()
        tokens = request.user.usertoken_set.all()
        return render(request, 'website/index.html', context={'user_tokens': tokens, 'open_fire_users': users})


class WebSiteLoginView(LoginView):
    template_name = 'website/registration/login.html'
    redirect_authenticated_user = 'openfire-admin:index'


class WebSiteLogoutView(LogoutView):
    template_name = 'website/registration/logged_out.html'
    next_page = 'openfire-admin:index'


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
        new_open_fire = OpenFireUserForm(request.POST)
        if new_open_fire.is_valid():
            ret = rest_api.create_new_user(request.POST["username"], request.POST["password"])
            if ret:
                new_open_fire.save()
                action = Action()
                action.user = request.user
                action.action_text = 'create openfire user: {} on {}'.format(request.POST["username"],
                                                                             datetime.datetime.now())
                action.save()
            else:
                raise Http404()
        else:
            if new_open_fire.has_error("username"):
                messages.add_message(request, messages.WARNING, new_open_fire.errors["username"][0])
            if new_open_fire.has_error("password"):
                messages.add_message(request, messages.WARNING, new_open_fire.errors["password"][0])
        return redirect('openfire-admin:index')

    def delete(self, request, *args, **kwargs):
        # delete user using request
        if "user_pk" in request.POST:
            old_open_fire = get_object_or_404(OpenFireUser, pk=request.POST["user_pk"])
            ret = rest_api.delete_user(old_open_fire.username)
            if ret:
                action = Action()
                action.user = request.user
                action.action_text = 'delete openfire user: {} on {}'.format(old_open_fire.username,
                                                                             datetime.datetime.now())
                action.save()
                old_open_fire.delete()
            else:
                raise Http404()
        return redirect('openfire-admin:index')


class UserTokenView(LoginRequiredMixin, View):
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
        new_token_form = UserTokenForm(request.POST)
        if new_token_form.is_valid():
            hsh_token_str = "hash string for:{} date:{} pk:{} rand number:{}".format(
                request.user.username, datetime.datetime.now(),
                request.user.pk, random())
            hashed = hashlib.md5(hsh_token_str.encode())
            # TODO: make use of form instead model
            # TODO: check for token existence upon generation (?)
            new_token = UserToken()
            new_token.token = hashed.hexdigest()
            new_token.bot_class_name = request.POST["bot_class_name"]
            new_token.bot_module_name = request.POST["bot_module_name"]
            new_token.user = request.user
            new_token.save()
        else:
            if new_token_form.has_error("bot_module_name"):
                messages.add_message(request, messages.ERROR, new_token_form.errors["bot_module_name"][0])
            if new_token_form.has_error("bot_class_name"):
                messages.add_message(request, messages.ERROR, new_token_form.errors["bot_class_name"][0])
        return redirect('openfire-admin:index')

    def delete(self, request, *args, **kwargs):
        if "token_pk" in request.POST:
            object = get_object_or_404(UserToken, pk=request.POST["token_pk"])
            object.delete()
            return redirect("openfire-admin:index")
