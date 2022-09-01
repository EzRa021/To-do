from email import message
from multiprocessing import context
from tkinter import Image
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Contact
from .models import Images
from django.contrib.auth.decorators import login_required



# quCreate your views here.
# def index(request):
#   comp = "school"
#   wel='welcome'

#   context ={
#     'get':comp,
#     'wel':"welcome"

#   }
#   return render(request, "cordarapp/index.html",context)

  
# def index(request):
#   counter=request.POST['count']
#   text_number= len(counter.split())
#   context={
#     'amount': text_number,
#   }

#   return render(request, "cordarapp/index.html",context)

  
def about(request):
  return render(request, 'cordarapp/about.html')

@login_required
def home(request):
  if request.method=='POST':
    name=request.POST.get('name')
    email=request.POST.get('email')
    phone=request.POST.get('phone')
    message=request.POST.get('message')
    image = request.FILES['upload']

    info = Contact(name=name,email=email,phone=phone,message=message)
    info.save()
    pix = Images(image=image)
    pix.save()
  
  return render(request, 'cordarapp/home.html')

def dash(request):
  cmd=Contact.objects.all()
  context={
    'all':cmd
  }
  return render(request, 'cordarapp/admin.html',context)

def edit(request, id):
  tel=Contact.objects.get(id=id)
  if request.method=='POST':
    tel.name=request.POST.get("name")
    tel.email=request.POST.get("email")
    tel.phone=request.POST.get("phone")
    tel.message=request.POST.get("message")
    tel.save()
    return redirect('cordarapp/admin.html')
  context={
    'call':tel
  }

  return render(request, 'cordarapp/update.html',context)

def delete(request, id):
  dels=Contact.objects.get(id=id)
  dels.delete()
  return redirect('cordarapp/admin.html')

def pricing(request):
  return render(request, 'cordarapp/pricing.html')

def services(request):
  return render(request, 'cordarapp/services.html')