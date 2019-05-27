from django.core.paginator import Paginator
from django.shortcuts import render, redirect


# Create your views here.
from carapp.models import BookClassT, BooksT


def booklist(request):
    cls = BookClassT.objects.filter(pid=1)
    cls2 = BookClassT.objects.filter(pid=4)
    cls3 = BookClassT.objects.filter(pid=6)
    oid = request.GET.get('oid')
    tid = request.GET.get('tid')
    num = request.GET.get('page')
    num1 = request.GET.get('num1')
    if not num:
        num = 1
    elif num1:
        num = num1
    us = BookClassT.objects.filter(pid=oid)
    uu = BooksT.objects.filter(pid__id=tid)
    if uu :
        gps2 = BookClassT.objects.get(id=tid)
        othergps1 = BookClassT.objects.get(id=BookClassT.objects.get(id=tid).pid)
        pagtor = Paginator(uu, per_page=2)
        page = pagtor.page(num)
        res = render(request, 'categoryapp/booklist.html',{'uu':uu,'t_cate':cls,'t_cate2':cls2,'t_cate3':cls3,'page':page,'id':tid,'stu':2,'othergps1':othergps1,'gps2':gps2,'pagtor':pagtor})
        return res
    elif us:
        books = BooksT.objects.filter(pid__pid=oid)
        # l = []
        # for j in us:
        #     u = BooksT.objects.filter(pid__id=j.id)
        #     l+=u
        gps1 = BookClassT.objects.get(id=oid)
        pagtor = Paginator(books, per_page=2)
        page = pagtor.page(num)
        res = render(request, 'categoryapp/booklist.html',{'t_cate': cls, 't_cate2': cls2, 't_cate3': cls3,'page':page,'id':oid,'stu':1,'gps1':gps1,'pagtor':pagtor})
        return res
    else:
        return redirect('categoryapp:booklist')
