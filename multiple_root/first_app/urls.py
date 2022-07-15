from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login_page/',views.login_page,name='login_page'),
    path('register_page/',views.register_page,name='register_page'),
    path('home/',views.home,name='home'),
    path('admin/',views.Is_admin,name = 'admin'),
    path('staff/',views.Is_staff,name = 'staff'),
    path('customer/',views.Is_customer,name = 'customer'),
]