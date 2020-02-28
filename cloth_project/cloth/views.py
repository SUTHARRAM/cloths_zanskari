from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):

    data = clothModel.objects.all()
    cloths = []
    for i in data:
        print(i.cloth_img)
        cloths.append(i)
    context={
        'cloths':cloths,
    }

    return render(request, "cloth/base.html",context)
def purchase(request):

    return render(request, "cloth/purchase.html")
