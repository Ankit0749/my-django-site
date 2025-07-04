from django.shortcuts import  render,HttpResponse
from .models import BusinessInfo, Cuisine, OpeningHour
# Create your views here.
def index(request):
    context= {
        'variable': "this is sent "
    }
    return render(request, 'home/index.html',context)
    # return HttpResponse("this is home page ")

def about(request):
    return render(request, 'home/about.html')


def services(request):
    return render(request, 'home/services.html')


# app/views.py
def contact(request):
    business = BusinessInfo.objects.first()
    cuisines = Cuisine.objects.all()
    hours = OpeningHour.objects.all()
    is_open = True  # Optional: implement your own logic here
    return render(request, 'home/contact.html', {
        'business': business,
        'cuisines': cuisines,
        'hours': hours,
        'is_open': is_open,
    })
