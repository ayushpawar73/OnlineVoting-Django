from django.shortcuts import render
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"voting/ehome.html")
def News(request):
    return render(request,"voting/News.html")
def Feedback(request):
    return render(request,"voting/Feedback.html")
def partail(request):
    return render(request,"voting/partail.html")
