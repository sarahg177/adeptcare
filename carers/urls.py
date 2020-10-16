from django.urls import path
from carers import views

urlpatterns = [
    path('', views.carer_profile, name='carer_profile'),

]
