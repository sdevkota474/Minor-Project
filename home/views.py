from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate , login
from django.core.files.storage import FileSystemStorage
#$cooty1234
#ilovenepal
#deve$h1234
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'index.html')
    
    

def loginUser(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
         
        if user is not None:
            login(request, user)
            return redirect("/")
    # A backend authenticated the credentials
        else:
                  return render(request, 'login.html')
    # No backend authenticated the credentials
   
   
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")


