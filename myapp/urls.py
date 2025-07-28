from django.urls import path
from . import views

app_name="myapp"

urlpatterns = [
    path('', views.index, name="index"),
    # path('home/', views.form_view, name = "input_form"),
    path('about/', views.about),
    # path('menu/', views.menu),
    path('menu_card/', views.menu_by_id),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]