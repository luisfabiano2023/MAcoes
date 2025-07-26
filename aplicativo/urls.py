from django.urls import path
from .views import create_item,get_item,delete_item,update_item,signup
urlpatterns= [
    path('create/item/',create_item,name='create'),
    path('get/item/<int:pk>',get_item,name='get'),
    path('delete/item/<int:pk>',delete_item,name='delete'),
    path('update/item/<int:pk>',update_item,name='update'),
    path('signup',signup)
    #ok
]