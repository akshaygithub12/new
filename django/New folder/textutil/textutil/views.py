
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"home.html")


#def about(request):
 #   return HttpResponse("<h1>HELLO</h1>")


def analysis(request):
    data=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    caps=request.GET.get('caps','off')
    if removepunc=="on":
        punct='''!@#$%^&(*)_+}{":><?'''
        analysis=""
        for i in data:
            if i not in punct:
                analysis=analysis + i
        param={"purpose":"user yor data wisely","analyzed_text": analysis}
        return render(request,"analysis.html",param)

    elif caps=="on":
        analysis=""
        for i in data:
                analysis=analysis+i.upper()
        param={"purpose":"capital","analyzed_text": analysis}
        return render(request,"analysis.html",param)
        
    else:
        return HttpResponse("error")
