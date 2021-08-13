from django.urls import path
from . import views

urlpatterns = [
    path('signUp',views.signUp,name='signUp'),
    path('login',views.login,name='login'),
    path('',views.homepage,name='home'),
    path('detail/<int:id>',views.productDetail,name='productdetail'),
    path('addcart',views.addcart,name='addcart'),
    path('cart',views.showcart,name='cart'),
]