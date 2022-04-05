
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from company.models import Problems

def index(request):
    # return HttpResponse("Hello, world. DUDE .")
    registro = Problems.objects.get(id = 1)
    print(registro)
    context = {"registro": registro}
    return render(request, "index.html", context)