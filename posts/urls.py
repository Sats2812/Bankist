from django.contrib.admin.decorators import register
from  django.urls  import path
from . import views

urlpatterns =  [
    path('',views.index,name='index'),
    path('account',views.account,name='account'),
    path('form',views.form,name='form'),
    path('contact',views.contact,name='contact')
]