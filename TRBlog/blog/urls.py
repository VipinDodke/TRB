from django.urls import path
from . import views
app_name ='video'
urlpatterns = [
    path('',views.index,name="BlogHome" ),
    path('blog/about/',views.about,name="AboutUS" ),
    path('blog/contact/',views.contact,name="Contact" ),
    path('blog/video/',views.video,name="Video"),
    path('blog/like_post/',views.like_post,name="like-post" ),
    path('blog/hinglish/',views.hinglish,name="hinglish" ),
]
