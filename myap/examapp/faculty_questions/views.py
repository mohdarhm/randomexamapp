from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def login_view(request):
    # Logic for rendering the login page
    return render(request, 'facultylogin.html')

@login_required
def portal_view(request):
    # Logic for rendering the main portal
    return render(request, 'facultyportal.html')
