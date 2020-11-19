from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="BlogHome" ),
    path('blog/about/',views.about,name="AboutUS" ),
    path('blog/contact/',views.contact,name="Contact" ),
    path('blog/video/',views.video,name="Video" ),
    path('blog/hinglish/',views.hinglish,name="hinglish" ),
]
