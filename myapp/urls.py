from django.urls import path
from . import views
from .views import IndexView, EmployeeCreate, EmployeeList, EmployeeDetail

app_name = "myapp"

urlpatterns = [
    path('show/<int:pk>', EmployeeDetail.as_view(), name = "EmployeeDetail"),
    path('create/', EmployeeCreate.as_view(), name = "EmployeeCreate"),
    path('list/', EmployeeList.as_view(), name = "EmployeeList"),
    path('home/', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('menu/', views.menu, name = 'menu'),
    path('index/', IndexView.as_view(), name = 'index'),
    path('', views.index, name = 'index'),
    # path('home/', views.form_view, name = "input_form"),
    path('menu_card/', views.menu_by_id),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
]