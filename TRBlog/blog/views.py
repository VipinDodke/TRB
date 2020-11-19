from lib2to3.fixer_util import Call

from django.shortcuts import render
from .models import page, Contect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')
def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        call = request.POST.get('call', '')
        desc = request.POST.get('desc','')
        contect = Contect(Name=name, Email=email, Call=call, desc=desc)
        contect.save()
    return render(request, 'blog/contact.html')
def video(request):
    total_page = page.objects.all()
    n=len(total_page)
    params={'range': range(-n), 't_blog':total_page}
    return render(request, 'blog/video.html',params)
def hinglish(request):
    total_page = page.objects.all()
    n = len(total_page)
    params={'range': range(-n), 't_blog':total_page}
    return render(request, 'blog/hinglish.html',params)
