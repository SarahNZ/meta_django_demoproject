from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import InputForm
from .models import Menu

def home(request):
    return render(request, "home.html", {})

def register(request):
    return render(request, "register.html", {})

def login(request):
    return render(request, "login.html", {})

def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict ={'menu': newmenu}
    return render(request, 'menu_card.html', newmenu_dict)

# Create your views here.
# def menu(request):
#     newmenu = { 'pricechart': [
#         {'name': "falafel", 'price': "12"},
#         {'name': "shawarma", 'price': "15"},
#         {'name': "gyro", 'price': "10"},
#         {'name': "hummus", 'price': "5"},
#     ]}
#     return render(request, 'menu.html', newmenu)

def about(request):
    about_content = {"about": "Based in Auckland, New Zealand, Little Lemon is about great food at moderate prices, making it a popular place for a meal any time of the day."}
    return render(request, "about.html", about_content)

def form_view(request):
    form = InputForm()
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}    # context dictionary
    return render(request, "home.html", context)

def index(request):
    return HttpResponse("Myapp works!")