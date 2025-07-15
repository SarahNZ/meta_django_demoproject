from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def menuitems(request, dish):
    items = {
        'pasta': 'Pasta is a type of noodle made from a combination of flour and water',
        'falafel': 'Falafels are deep fried patties or balls made from chickpea flour',
        'cheesecake': 'Cheesecake is a type of dessert made from cream',
    }

    description = items[dish]

    return HttpResponse(f"<h2> {dish} </h2>" + description)

def showform(request):
    return render(request, "form.html")

def getform(request):
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
    return HttpResponse(f"Name:{name} UserID: {id}")

def index(request):
    # path = request.path
    # response = HttpResponse("Demoapp works!")
    # return response
    return HttpResponseNotFound(" Little Lemon ") # Should use error http responses in the project-level view.py file. I was just being lazy.

# Using path parameters for URL http://localhost:8000/getuser/John/1
# def pathview(request, name, id):
#     # return HttpResponse("Name:{} UserID:{}".format(name, id))
#     return HttpResponse(f"Name:{name} UserID:{id}".format(name, id))

# Using query parameters/strings URL is http://localhost:8000/getuser/?name=John&id=1
# def qryview(request):
#     name = request.GET['name']
#     id = request.GET['id']
#     return HttpResponse(f"Name:{name} UserID: {id}")

# def example_view(request):
#     return render(request, 'demoapp/form.html')
