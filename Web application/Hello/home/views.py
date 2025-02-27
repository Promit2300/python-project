from django.shortcuts import render, HttpResponse

# Create your views here.
#def index(request):
    #return HttpResponse("This is Homepage")
def index(request):
    context = {
        "variable1":"this is sent",
        "variable2":"I am great"
    }
    return render(request, 'index.html')    

def about(request):
    return render(request, 'about.html')    
    #return HttpResponse("This is About")

def sevices(request):
    return render(request, 'services.html')    
    #return HttpResponse("This is service page")

def contact(request):
    return render(request, 'contact.html')    
   # return HttpResponse("This is contact page")