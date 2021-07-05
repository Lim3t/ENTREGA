from django.urls import path
from .views import index,test,form_cliente,Form_del_cliente,form_mod_cliente
from django.conf import settings
urlpatterns =[
    path('',index,name="index"),
    path('test',test,name="test"),
    path('form_cliente',form_cliente,name="form_cliente"),
    path('form_mod_cliente/<id>',form_mod_cliente,name="form_mod_cliente"),
    path('form_del_cliente/<id>',Form_del_cliente,name="form_del_cliente"),
]