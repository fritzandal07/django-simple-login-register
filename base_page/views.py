from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from base_page.forms import RegisterUserForm
# Create your views here.

@login_required(login_url='/login/')
def dashboard(request):
    return render(request, "dashboard.html", {})

def register_view(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST or None)
        if form.is_valid():
            # form.save()
            login(request, form.save())
            # return redirect("base_page:login_view")
        
    else:
        form = RegisterUserForm()
    if request.user.is_authenticated:
        return redirect("base_page:dashboard")
    else:
        return render(request, "registration/register.html", {"form": form})
    
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST) 
        if form.is_valid():
            login(request, form.get_user())
            return redirect("base_page:dashboard")
    else: 
        form = AuthenticationForm() 

    if request.user.is_authenticated:
        return redirect("base_page:dashboard")
    
    return render(request, "registration/login.html", {"form": form})

@login_required(login_url='/login/')
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("base_page:login_view")
    
    return redirect("base_page:dashboard")