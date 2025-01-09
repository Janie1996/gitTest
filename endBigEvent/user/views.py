import json

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest, JsonResponse

from user.models import BookInfo


def index(request):
    con={
        'name':'weijie'
    }
    # return HttpResponse('ok,success')
    return render(request,'index.html',context=con)

def createBook(request):
    book = BookInfo.objects.create(
        name='django',
        pub_date='2001-01-12',
        readcount=10,
    )
    return HttpResponse('create book success')

def goods(request,cat_id,goods_id):

    params = request.GET
    print(params)
    print(cat_id,goods_id)
    return JsonResponse({'cat_id':cat_id,'id':goods_id})

def addBook(request):
    data = request.body.decode()  # 字符串类型，str
    data = json.loads(data)  # 转为字典
    print(data['name'])
    return JsonResponse(data)
    # return HttpResponse('add book success')

from django.shortcuts import redirect

def response(request):
    return redirect('/createBook')