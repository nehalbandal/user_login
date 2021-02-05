from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import Registration


class HomePage(TemplateView):
    template_name = "users/index.html"


class Register(CreateView):
    form_class = Registration
    success_url = reverse_lazy("index")
    template_name = "users/register.html"
    

class UserList(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "users/user_list.html"


class UserDetail(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "users/user_detail.html"


class UpdateProfile(UpdateView):
    model = CustomUser
    fields = ["username", "fullname", "email", "age", "address"]
    success_url = reverse_lazy("index")
    template_name = "users/update.html"


class DeleteUser(DeleteView):
    model = CustomUser
    success_url = reverse_lazy("index")
    template_name = "users/delete_user.html"

