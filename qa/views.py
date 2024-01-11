from django.shortcuts import render, HttpResponse,get_object_or_404,HttpResponseRedirect
from qa.models import User,Books
from .forms import BookCreatefrom
from django.views import generic

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


def delete(request):
    username = request.POST.get("username")
    user = get_object_or_404(User, username=username)
    user.delete()
    return HttpResponseRedirect("/")

def get_form(request):
    frist_name = request.POST.get("frist_name")
    last_name = request.POST.get("last_name")
    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")

    context = {
        "frist_name": frist_name,
        "last_name": last_name,
        "username": username,
        "password": password,
        "email": email,
    }
    new_user = User(
            frist_name=frist_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )
    new_user.save()


    return render(request,"form_show.html",context)




def book_form(request):
    if request.method =="POST":
        form = BookCreatefrom()
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/")
    else:
        form = BookCreatefrom()
        return render(request,"book_create.html",context={"form":form})

class BooksListView(generic.ListView):
    model = Books
    template_name = "book_list.html"
