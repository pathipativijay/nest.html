from urllib import request
from django.shortcuts import render

# Create your views here.
def nesthtml(request):
    d={'a':34,'b':44,'c':55}
    return render(request,'nest.html',d)