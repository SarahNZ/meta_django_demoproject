from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import InputForm

def about(request):
    about_content = {"about": "Based in Chicago, Illinois, Little Lemon is about great food at moderate prices, making it a popular place for a meal any time of the day."}
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