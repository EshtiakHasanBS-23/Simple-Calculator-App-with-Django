from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index(request):
    return render(request,'index.html')
def submitquery(request):
    q=request.GET['query']
    try:
        ans=eval(q)
        mydict={
            "ans":ans,
            "q":q,
            "error":False,
            "result":True
        }
        return render(request,'index.html',context=mydict)
    except:
        mydict={
            "error":True,
            "result":False
        }
        return render(request,'index.html',context=mydict)

 