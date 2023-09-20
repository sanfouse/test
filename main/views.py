from django.shortcuts import render
from .main_service import generate_random_code
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        logout()
        return render(request, 'main/index.html', {"code": generate_random_code()})