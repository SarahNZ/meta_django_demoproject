from django.urls import path
from . import views

app_name='demoapp'    # define the app_name variable (in the app's url.py file)

urlpatterns = [
    # path('', views.home, name='home'),
    # path('getuser/<name>/<id>', views.pathview, name='pathview'),
    # path('getuser/', views.qryview, name='qryview'),
    path("showform/", views.showform, name="showform"),
    path("getform/", views.getform, name="getform"),
    path('dishes/<str:dish>', views.menuitems),
    path('', views.index, name="index"),
]