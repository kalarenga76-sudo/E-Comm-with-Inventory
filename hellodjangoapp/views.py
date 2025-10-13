from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone
from .models import Student # add this import


def welcome(request):
    today = timezone.localtime().strftime("%B %d, %Y")
    return HttpResponse(f"Hello Django welcomes you — {today}")

def homePageView(request):
    return HttpResponse("Hello, Django!")

def welcomeView(request):
    return HttpResponse("My Learning of creating micro services!")

def numbers_show(request):
    x = []
    for i in range(10):
        x.append(i)
    return HttpResponse("<h1> List of numbers </h1>    The Digits are {0}".format(x))

def student_show(request):
    students = Student.objects.all()
    return render(request, "show.html",{'student':students})
                
