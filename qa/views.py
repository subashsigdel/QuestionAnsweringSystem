from django.shortcuts import render, HttpResponse
from qa.models import User

# Create your views here.
def home(request):
    
    user = User.objects.all()
    context = {"user":user}
    # context = {"first_name": user.frist_name, "last_name": user.last_name,"username":user.username,"password":user.password,"email":user.email}
    return render(request,"home.html",context)


# form display -> views
# form ko data fetch garna lai function


def form(request):

    return render(request,"form.html")


def get_from(request):
    firstname = request.first_name
    last_name = request.last_name