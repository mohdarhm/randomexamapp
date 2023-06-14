from django.shortcuts import render, HttpResponse
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
# uncomment this line when login page is ready.

def portal_view(request):
    subjects = Subject.objects.all()

    context = {
        'subjects': subjects,
    }
    return render(request, 'facultyportal.html', context)


def get_concepts(request):
    subject_id = request.GET.get('subject')

    if subject_id:
        try:
            # Retrieve the subject object based on the subject_id
            subject = Subject.objects.get(id=subject_id)

            # Fetch the concepts related to the subject
            concepts = Concept.objects.filter(subject=subject).values('name', 'subject__name')

        except Subject.DoesNotExist:
            concepts = []
    else:
        concepts = []

    # Return the concepts as a JSON response
    return JsonResponse(list(concepts), safe=False)