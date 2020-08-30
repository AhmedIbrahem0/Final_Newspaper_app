from django.views.generic import TemplateView

# Create your views here.
class Homepageview(TemplateView):
    template_name="home.html"
    