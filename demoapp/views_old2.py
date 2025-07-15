from django.http import HttpResponse
from datetime import datetime

def homepage(request):
    path = request.path
    method = request.method
    content = ''' 
        <center><h2>Testing Django Request Response Objects</h2>
        <p>Request path: {}</p>
        <p>Request method : {}</p>
        '''.format(path, method)
    return HttpResponse(content)

def say_hello(request):
    return HttpResponse("Hello world")

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = '''<h1 style="color: #F4CE14;">This is Little Lemon again!</h1>'''
    return HttpResponse(text)