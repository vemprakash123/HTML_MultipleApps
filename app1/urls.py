from app1.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('sample/',sample,name='sample')
]