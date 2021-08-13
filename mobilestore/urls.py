from django.urls import path
from . import views
from .api import UserList,UserModify

urlpatterns = [
    path('signUp',views.signUp,name='signUp'),
    path('login',views.login,name='login'),
    path('',views.homepage,name='home'),
    path('detail/<int:id>',views.productDetail,name='productdetail'),
    path('addcart',views.addcart,name='addcart'),
    path('cart',views.showcart,name='cart'),

    path('api',UserList.as_view(),name='user_list'),
    path('api/<int:id>/',UserModify.as_view(),name='user_list')
]