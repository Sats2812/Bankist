from unicodedata import name
from django.contrib.admin.decorators import register
from  django.urls  import path
from . import views

urlpatterns =  [
    path('',views.index,name='index'),
    path('account',views.account,name='account'),
    path('form',views.form,name='form'),
    path('contacts',views.contacts,name='contacts'),
    path('getloan',views.getloan,name='getloan'),
    path('maketransaction',views.maketransaction,name='maketransaction'),
    path('getdebitcard',views.getdebitcard,name='getdebitcard')
]