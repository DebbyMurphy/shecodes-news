from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class ProfileView(LoginRequiredMixin, generic.DetailView):
    model = CustomUser
    context_object_name = 'profile'
    template_name = 'users/profile.html'

# Create your views here.
