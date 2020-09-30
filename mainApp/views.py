from django.shortcuts import render
from django.template import loader
from mainApp.models import Article,Cametn,Category,Mark,Slider_image,Slider_info,Email
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
# Create your views here.

def index(request):
    articl = Article.objects.all().order_by('-views')[:10]
    category = Category.objects.all()
    
    context = {
        'articl': articl,
        'category': category,
    }
    return render(request,'mainApp/index.html',context)

def leave_email(request): 
    try:
        email= Email.objects.create(name=request.POST['name'],surname=request.POST['surname'],email=request.POST['email'])
    except:
        raise Http404("a")    


    return HttpResponseRedirect(reverse('mainApp:index'))