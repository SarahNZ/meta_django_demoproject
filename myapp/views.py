from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import InputForm
from .models import Menu, Employee
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

def success(request):
    return HttpResponse("The operation was completed successfully.")

class EmployeeDelete(DeleteView):
    model = Employee
    template_name = "employee_confirm_delete.html"
    success_url = "/success"

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = "employee_form.html"
    success_url = "/success"

class EmployeeDetail(DetailView):
    model = Employee
    template_name = "employee_detail.html"
    success_url = "/success"

class EmployeeList(ListView):
    model = Employee
    template_name = "employee_list.html"

class IndexView(TemplateView):
    template_name = 'index.html'

class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'
    template_name = "employee_form.html"
    success_url = "/success"

def home(request):
    return render(request, "index.html")
#     return render(request, "home.html", {})

def about(request):
    return render(request, "about.html")
    # about_content = {"about": "Based in Auckland, New Zealand, Little Lemon is about great food at moderate prices, making it a popular place for a meal any time of the day."}
    # return render(request, "about.html", about_content)

def menu(request):
    return render(request, "menu.html")
#     newmenu = { 'pricechart': [
#         {'name': "falafel", 'price': "12"},
#         {'name': "shawarma", 'price': "15"},
#         {'name': "gyro", 'price': "10"},
#         {'name': "hummus", 'price': "5"},
#     ]}
#     return render(request, 'menu.html', newmenu)

def register(request):
    return render(request, "register.html", {})

def login(request):
    return render(request, "login.html", {})

def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict ={'menu': newmenu}
    return render(request, 'menu_card.html', newmenu_dict)

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