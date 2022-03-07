from . import views
from django.urls import path

#from .views import home

urlpatterns= [
    path('',views.topic),
    path('home/',views.retireveTopic),
    #path('home/tques/',views.detailTopic),
    path('tmques/', views.retireveTopic, name='tmques'),
    path('tsubques/(<topic_name>)/$', views.retireveSubTopic, name='tsubques'),
    path('tques/',views.retireveQTopic, name='tques'),
    path('questions/(<topic_name>)/$',views.questionDetails,name='questions'),
    
]
