from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from .models import New, Teacher

# Create your views here.


def index_page_render(request):
    return render_to_response('index.html', {'news': New.objects.all()})


def about_page_render(request):
    return render_to_response('about.html', {'news': New.objects.all()})


def teacherstaff_page_render(request):
    return render_to_response('teacherstaff.html', {'news': New.objects.all(), 'teachers': Teacher.objects.all()})


def person_detail(request, id = None):
    person = get_object_or_404(Teacher, id)
    context = {
        'person': person
    }

    return render_to_response("personabout.html", context)


