from django.urls import path
from . import views
from members.views import *

urlpatterns = [
    path('', views.home,name='josaa-home'),
    path('contact/', views.contact1,name='josaa-contact'),
   
    path('about/', views.about,name='josaa-about'),
     path('input/', views.input1,name='josaa-input'),
    path('iitList/', views.iitList,name='iit-list'),
    # path('iitb/',views.iitb,name='iitb'),
    path('iitb/<str:college>/', views.iitb, name='iitb'),
    path('iitbranch', views.iitbranch, name='iitbranch'),
    path('iitmech/<str:college>/', views.iitmech, name='iitmech'),
    
    path('insti_cutoff/', views.insti_cutoff, name='insti_cutoff'),
    # path('iitb/',AdmissionChartView.as_view(),name='iitb'),
]
