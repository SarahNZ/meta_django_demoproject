from django.urls import path
from . import views

app_name="myapp"

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.form_view, name = "input_form"),
    path('about/', views.about)
]