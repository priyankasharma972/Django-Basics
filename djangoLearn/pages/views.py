from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args,**kwargs):
    my_context={
        "my_id":"Priyanka",
        "my_num":23,
        "my_list":[123,345,45656],
        "new_html":"<h1>Hello World!!</h1>"
    }
    return render(request,"home.html",my_context)
