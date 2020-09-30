from django.shortcuts import render
from mainApp.models import Article,Cametn,Category,Mark,Slider_image,Slider_info
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
# Create your views here.
def index(request, articl_id): 
    try:
        article= Article.objects.get(id=articl_id)
    except:
        raise Http404("a")        
    coments=article.com.order_by('-id')[:10]
    return render(request,'articl/index.html',{'article':article, 'coments':coments})    


def leave_coment(request, articl_id): 
    try:
        article= Article.objects.get(id=articl_id)
    except:
        raise Http404("a")    


    article.com.create(autor_name=request.POST['name'],text=request.POST['text'])

    return HttpResponseRedirect(reverse('articl:index',args=(article.id,)))