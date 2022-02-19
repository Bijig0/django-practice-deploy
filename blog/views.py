from django.shortcuts import render
from .models import Tutorial
def home(request):
    context = {
        'otherposts': Tutorial.objects.all()
    }
    return render(request, 'blogs/home.html',context)

def about(request):
    return render(request, 'blogs/about.html',{'title':'Django'})