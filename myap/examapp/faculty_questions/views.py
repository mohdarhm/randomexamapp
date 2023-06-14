from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Concept, Subject
from django.http import JsonResponse

# Create your views here.

def login_view(request):
    # Logic for rendering the login page
    return render(request, 'facultylogin.html')


# @login_required
#uncomment this line when login page is ready.

def portal_view(request):
    subjects = Subject.objects.all()
    selected_subject_id = request.POST.get('subject', None)
    selected_subject = None
    concepts = []

    if selected_subject_id:
        selected_subject = Subject.objects.get(id=selected_subject_id)
        concepts = Concept.objects.filter(subject=selected_subject)

    context = {
        'subjects': subjects,
        'selected_subject': selected_subject,
        'concepts': concepts,
    }
    return render(request, 'facultyportal.html', context)


