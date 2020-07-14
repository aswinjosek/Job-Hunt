from django.urls import path
from.import views
from django.contrib import admin

urlpatterns = [
    path('',views.index,name="index"),
    path('admin1',views.admin1,name='admin1'),
    path('adminreg',views.adminreg,name='adminreg'),
    path('admintable',views.admintable,name='admintable'),
    path('userdelete/<int:dataid>/', views.userdelete,name='userdelete'),
    path('adminupdate/<int:dataid>/',views.adminupdate,name='adminupdate'),
    path('updating/<int:dataid>/',views.updating,name='updating'),
    path('candidatetable',views.candidatetable,name='candidatetable'),
    path('login',views.login,name='login')
    
   
   ]

