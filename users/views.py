from django.views.generic import CreateView
from .forms import Customusercreation
from django.urls import reverse_lazy
# Create your views here.
class Signup(CreateView):
    form_class=Customusercreation
    template_name="signup.html"
    success_url=reverse_lazy("login")