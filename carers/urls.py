from django.urls import path
from carers import views

urlpatterns = [
    path('', views.carer_profile, name='carer_profile'),
    path('thanks/', views.thanks, name='thanks'),
    path('carer_list/', views.get_carer_list, name='carer_list')

]
