from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import InputForm

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

