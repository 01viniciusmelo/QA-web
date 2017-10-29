from django.shortcuts import render
from django.views import View
from django.shortcuts import Http404


class BaseChat(View):
    def get(self, request, *args, **kwargs):
        request
