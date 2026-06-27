from django.shortcuts import render

from bio.models import Bio
from education.models import Education
from experience.models import Experience
from projects.models import Project
from skills.models import Skill


def index(request):
    """Show the portfolio homepage with all sections."""
    return render(request, 'index.html', {
        'bio': Bio.objects.first(),
        'educations': Education.objects.all(),
        'skills': Skill.objects.all(),
        'experiences': Experience.objects.all(),
        'projects': Project.objects.all(),
    })
