from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    info={"name":"Subash",
          "title":"mysite",
          "address":"thali"}
    return render(request, 'home.html',info)