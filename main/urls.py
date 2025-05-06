from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/python-automation/', views.python_automation, name='python_automation'),
    path('services/rpa/', views.rpa, name='rpa'),
    path('services/intelligent-document-processing/', views.intelligent_document_processing, name='intelligent_document_processing'),
    path('services/chatbot/', views.chatbot, name='chatbot'),

    path('industries/', views.industries, name='industries'),
    path('industries/manufacturing/', views.manufacturing, name='manufacturing'),
    path('industries/healthcare/', views.healthcare, name='healthcare'),
    path('industries/finance/', views.finance, name='finance'),
    path('industries/retail/', views.retail, name='retail'),

    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('blog/', views.blog, name='blog'),
]
