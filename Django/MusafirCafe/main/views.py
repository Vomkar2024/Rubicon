from django.shortcuts import render , HttpResponse
from datetime import datetime
from .models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "title": "Main"
    }
    return render(request,'index.html',context)

def Menu(request):
    context={
        "title": "Menu"
    }
    return render(request,'index.html')

def about(request):
    return render(request,'About.html')
    # return HttpResponse("This is About page")

def services(request):
    return render(request,'Services.html')
    # return HttpResponse("This is Services page")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # Save to database
        contact = Contact(name=name, email=email, phone=phone, message=message , date=datetime.today())
        contact.save()

        messages.success(request, "We have recieved your message😊")
        
        # You can add a success message here
    return render(request,'Contact.html')
    # return HttpResponse("This is Contact page")

