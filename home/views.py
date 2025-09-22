from django.conf import settings
from django.shortcuts import render

# Create your views here.
def home_view(request):
    context = {
        "restaurant_name": getattr(settings, "RESTAURANT_NAME", "My Restaurant"),
    }
    return render(request, "home.html", context)

def about_view(request):
    context = {
        "restaurant_name": getattr(settings, "RESTAURANT_NAME", "My Restaurant"),
        "description" : "We serve the best dishes with fresh ingredients, warm hospitality, and a cozy atmosphere."
    }
    return render(request, "about.html", context)
