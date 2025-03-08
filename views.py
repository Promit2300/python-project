from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(username=username, password=password)  # Fixed the hardcoded values

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})  # Show error message

    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect('/login')

