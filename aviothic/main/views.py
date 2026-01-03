from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/index-2.html')

def contact(request):
    return render(request,'core/contact.html')

def about(request):
    return render(request,'core/about.html')

def blog(request):
    return render(request,'core/blog.html')

def courses(request):
    return render(request,'core/courses.html')