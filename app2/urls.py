from django.urls import path
from app2.views import *

app_name='pawan'

urlpatterns=[
    path('pawankalyan/',pawankalyan,name='pawankalyan'),
]