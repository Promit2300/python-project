from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
#def index(request):
    #return HttpResponse("This is Homepage")
def index(request):
    return render(request, 'index.html')    

def about(request):
    return render(request, 'about.html')    
    #return HttpResponse("This is About")

def sevices(request):
    return render(request, 'services.html')    
    #return HttpResponse("This is service page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, "Your message has been save.")

    
    return render(request, 'contact.html')    
   # return HttpResponse("This is contact page")