from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def all_rooms(request):
    # print(dir(request))
    now = datetime.now()
    return HttpResponse(content=f"<h1>hello {now} </h1>")