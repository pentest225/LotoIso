from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from  django.contrib.auth import  authenticate ,login ,logout
# Create your views here.

def index(request):

    return render(request,'MyApp/index.html')
