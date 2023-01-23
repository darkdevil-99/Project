from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Table
from .serializers import Table_serializers
from django.contrib.auth import get_user


# Create your views here.


def login(request):
    if request.method == "POST":
        if request.POST["user"] and request.POST["psw"]:
            x = Table.objects.all()
            c = 0
            while c < len(x):
                y = x[c]
                if y.username == request.POST["user"] and y.password == request.POST["psw"]:
                    return render(request, 'library.html')
                c += 1
            else:
                messages.error(request, 'Invalid Username or Password')
                return render(request, 'login.html')

        else:
            messages.error(request, 'Fill all the columns')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        data = Table()
        if request.POST["username"] and request.POST["email"] and request.POST["psd"] and request.POST["confirm"]:
            if len(request.POST["psd"]) >= 8:
                data.username = request.POST["username"]
                data.email = request.POST["email"]
                try:
                    if request.POST["psd"] == request.POST["confirm"]:
                        data.password = request.POST["psd"]
                        data.save()
                        messages.success(request, 'Username and Password updated')
                        return redirect('/')
                    else:
                        messages.error(request, 'Check password')
                        return render(request, 'signup.html')
                except:
                    messages.error(request, 'Username or email already exists')
                    return render(request, 'signup.html')
            else:
                messages.error(request, 'Password is too short')
                return render(request, 'signup.html')
        else:
            messages.error(request, 'Fill all the columns')
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')


def password(request):
    if request.method == "POST":
        if request.POST["user1"] and request.POST["email"] and request.POST["new-psd"] and request.POST["new-con-psd"]:
            if request.POST["new-psd"] == request.POST["new-con-psd"]:
                c = 0
                x = Table.objects.all()
                while c < len(x):
                    y = x[c]
                    if y.username == request.POST["user1"] and y.email == request.POST["email"]:
                        y.password = request.POST["new-psd"]
                        y.save()
                        messages.success(request, 'Password updated')
                        return redirect('/')
                    c += 1
            else:
                messages.error(request, 'Check your password')
                return render(request, 'password.html')
        else:
            messages.error(request, 'Fill all the columns')
            return render(request, 'password.html')
    else:
        return render(request, 'password.html')


def logout(request):
    messages.success(request, 'Logged out Successfully')
    return redirect('/')













