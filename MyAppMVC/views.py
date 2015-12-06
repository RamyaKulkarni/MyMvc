from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse
from MyAppMVC.models import Article
from django.template.loader import get_template
from PIL import Image

def listArticle(request):
    list_art = Article.objects.all()
    preview = Article.objects.get(id=1)
    sample1 = Article.objects.get(id=2)
    sample2 = Article.objects.get(id=3)
    temp = loader.get_template("template.html")
    context = RequestContext(request,{
       'list_art':list_art,
       'preview' : preview,
       'sample1':sample1,
       'sample2':sample2,
        })
    return HttpResponse(temp.render(context))


def singleArt(request,art_id):
    single_art=Article.objects.get(
        id=art_id
        )
    lists = Article.objects.all()
    tempr=loader.get_template("viewpage.html")
    ctx = RequestContext(request,{'art_id':art_id,
        'single_art':single_art,
        'lists': lists,
        })
    return HttpResponse(tempr.render(ctx))

    
