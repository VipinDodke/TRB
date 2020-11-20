from lib2to3.fixer_util import Call

from django.shortcuts import render, redirect
from .models import page, Contect, Like
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
    user = request.user
    n=len(total_page)
    params={'range': range(-n), 't_blog':total_page,'user':user}
    return render(request,'blog/video.html',params)

def like_post(request):
    user = request.user
    if request.method=='POST':
        post_id=request.POST.get('post_id')
        post_obj=page.objects.get(id=post_id)
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like, created= Like.objects.get_or_create(user=user, post_id=post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like';
        like.save()
    return redirect('video:Video')

def hinglish(request):
    total_page = page.objects.all()
    n = len(total_page)
    params={'range': range(-n), 't_blog':total_page}
    return render(request, 'blog/hinglish.html',params)
