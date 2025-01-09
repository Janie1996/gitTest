from django.urls import path
from user.views import index, createBook, goods, addBook, response

urlpatterns = [
    path('index',index),
    path('createBook',createBook),
    # path('<cat_id>/<goods_id>/',goods),
    path('add',addBook),
    path('res',response)
]