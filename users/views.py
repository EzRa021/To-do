from email import message
from email.errors import MessageParseError
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login



# Create your views here.
  
def register(request):
    if request.method =='POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        comfirmpassword = request.POST.get('password2')

        if password != comfirmpassword:
           messages.error(request, "Your password does not match")
           return redirect('/register')

        if User.objects.filter(username=username):
           messages.error(request, "This username is already exist")
           return redirect('/register')

        if User.objects.filter(email=email):
           messages.error(request, "This username is already exist")
           return redirect('/register')

        if len(username)>15:
           messages.error(request, "the username should be lesser than 15")
           return redirect('/register')

        user = User.objects.create_user(username,email,password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        messages.success(request, "you details has been successfully register")
    return render(request, 'users/register.html')
  



def login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username,password=password)
    if user is not None:
        auth_login(request,user)
        messages.success(request, "you have successfully logged in")
        return redirect("cordarapp:home")
    else:
        messages.success(request, "wrong password or username")
        return redirect('/login')
  
  return render(request, 'users/login.html')


def exits(request):
  logout(request)
  return redirect('/login')

