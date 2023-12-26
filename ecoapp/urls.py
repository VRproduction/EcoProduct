from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='home'),
 
    path('shop',shop,name='shop'),
    path('about',about,name='about'),
    path('blog',blog,name='blog'),
    path('contact',contact,name='contact'),
    path('message',message,name='message'),
    path('wish',wish,name='wish'),
 
    

]
urlpatterns += [
]