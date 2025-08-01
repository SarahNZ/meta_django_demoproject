from django.urls import path
from . import views
from .views import (
    IndexView, 
    EmployeeCreate, 
    EmployeeList, 
    EmployeeDetail, 
    EmployeeUpdate, 
    EmployeeDelete,
    success)

app_name = "myapp"

urlpatterns = [
    path('delete/<int:pk>', EmployeeDelete.as_view(), name = "EmployeeDelete"),
    path('success/', views.success, name = 'success'),
    path('update/<int:pk>', EmployeeUpdate.as_view(), name = "EmployeeUpdate"),
    path('show/<int:pk>', EmployeeDetail.as_view(), name = "EmployeeDetail"),
    path('create/', EmployeeCreate.as_view(), name = "EmployeeCreate"),
    path('list/', EmployeeList.as_view(), name = "EmployeeList"),
    path('index/', IndexView.as_view(), name = 'index'),
    path('home/', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('menu/', views.menu, name = 'menu'),
    path('', views.index, name = 'index'),
    # path('home/', views.form_view, name = "input_form"),
    path('menu_card/', views.menu_by_id),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
]