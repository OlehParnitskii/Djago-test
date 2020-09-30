from django.shortcuts import render
from mainApp.models import Article,Cametn,Category,Mark,Slider_image,Slider_info
from django.http import HttpResponseRedirect,Http404
# Create your views here.
def index(request):
    category= Category.objects.all()
    articl= Article.objects.all()
    return render(request,'category/index.html',{'category':category,'articl':articl})

def category_detal(request,category_id):
    try:
        category= Category.objects.get(id=category_id)
        
    except:
        raise Http404("cta")    
    try:
        
        article= Article.objects.all().filter(category=category_id)
    except:
        raise Http404("a")   
    return render(request,'category/category.html',{'category':category,'article':article})    


