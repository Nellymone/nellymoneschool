from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('5-10/', views.about5_10, name='page2'),
    path('11-17/', views.about11_17, name='page3'),
    path('branches/', views.branches, name='branches'),
    path('group/', views.group, name='group'),
    path('pictures/', views.gallery, name='pictures'),
    path('training/', views.training, name='training'),

]