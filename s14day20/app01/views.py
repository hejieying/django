from django.shortcuts import render,HttpResponse,redirect
from app01 import models
import json
# Create your views here.


def business(request):
    v1 = models.Business.objects.all()
    #queryset

    v2 = models.Business.objects.all().values('id','caption')
    #例如：select id,caption from business
    #返回的是字典[{}]

    v3 = models.Business.objects.all().values_list('id', 'caption')
    # 例如：select id,caption from business
    #返回的是元组[()]


    #查询也可以使用values  和  values_list方法
    # v4 = models.Business.objects.values('id','caption')
    # v4 = models.Business.objects.filter(id=1).first()
    # print(v4)
    return render(request,'business.html',{'v1':v1,'v2':v2,'v3':v3})


# def host(request):
#     v1 = models.Host.objects.filter(nid__gt=0)   #filter(nid__gt=0)  相当于all()
#     for i in v1:
#         print(i.nid,i.hostname,i.ip,i.port,i.b_id,i.b,i.b.id,i.b.caption,i.b.code)
#         #i.b是一个objects   可实现不跨表查询
#
#         # print(i.b.fk.name)
#         #可以使用嵌套表查询
#
#     # return HttpResponse('host')
#
#     v2 = models.Host.objects.filter(nid__gt=0).values('nid','hostname','b_id','b__caption')
#     #跨表取值要用__双下划綫       'b__caption'
#     print(v2)
#
#     v3 = models.Host.objects.filter(nid__gt=0).values_list('nid','hostname','b_id','b__caption')
#     #跨表取值要用__双下划綫       'b__caption'     并且要按照顺序取，以坐标取0123……
#     print(v3)
#
#     return render(request, 'host.html', {'v1': v1,'v2': v2,'v3': v3})







def host(request):
    if request.method == "GET":
        v1 = models.Host.objects.filter(nid__gt=0)   #filter(nid__gt=0)  相当于all()
        v2 = models.Host.objects.filter(nid__gt=0).values('nid','hostname','b_id','b__caption')
        #跨表取值要用__双下划綫       'b__caption'

        v3 = models.Host.objects.filter(nid__gt=0).values_list('nid','hostname','b_id','b__caption')

        b_list = models.Business.objects.all()

        return render(request, 'host.html', {'v1': v1,'v2': v2,'v3': v3,'b_list':b_list})

    elif request.method == "POST":
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        models.Host.objects.create(hostname=h,
                                   ip=i,
                                   port=p,
                                   b_id=b,)

        return redirect('/host')



def test_ajax(request):
    # print(request.method,request.POST,sep='\t')
    # return HttpResponse('我把门观赏了')


    ret = {'status':True,'error':None,'data':None}
    try:
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        if h and len(h) > 5:
            models.Host.objects.create(hostname=h,
                                       ip=i,
                                       port=p,
                                       b_id=b, )
        else:
            ret['status'] = False
            ret['error'] = "太短了"
    except Exception as  e:
        ret['status'] = False
        ret['error'] = "请求错误"
    return HttpResponse(json.dumps(ret))



def app(request):
    if request.method == "GET":
        app_list=models.Application.objects.all()
        # for row in app_list:
        #     print(row.name,row.r.all())

        host_list = models.Host.objects.all()
        return render(request,'app.html',{'app_list':app_list,'host_list':host_list})
    elif request.method == "POST":
        app_name = request.POST.get('app_name')
        host_list = request.POST.getlist('host_list')
        print(app_name,host_list)

        obj = models.Application.objects.create(name=app_name)
        obj.r.add(*host_list)

        return redirect('/app')


def ajax_add_app(request):
    ret = {'status':True,'error':None,'data':None}
    app_name = request.POST.get('app_name')
    host_list = request.POST.getlist('host_list')
    obj = models.Application.objects.create(name=app_name)
    obj.r.add(*host_list)
    return HttpResponse(json.dumps(ret))
