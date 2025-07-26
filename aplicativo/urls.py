from django.urls import path,re_path
from .views import create_item,get_item,delete_item,update_item
from . import views

urlpatterns= [
    path('create/item/',create_item,name='create'),
    path('get/item/<int:pk>',get_item,name='get'),
    path('delete/item/<int:pk>',delete_item,name='delete'),
    path('update/item/<int:pk>',update_item,name='update'),
    re_path('login',views.login),
    re_path('signup',views.signup),
    re_path('login',views.test_token)
    
    
    #ok
]