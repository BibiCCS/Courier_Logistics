from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        context['first_name'] = self.request.user.first_name
        context['last_name'] = self.request.user.last_name
        user = self.request.user


class SubmittableLoginView(LoginView):
    template_name = 'login.html'


class SubmittablePasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = '/'

