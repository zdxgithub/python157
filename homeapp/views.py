from django.shortcuts import render, redirect,HttpResponse
from homeapp.models import BookClassT,BooksT


# Create your views here.

def home(request):
    cls = BookClassT.objects.filter(pid=1)
    cls2 = BookClassT.objects.filter(pid=4)
    cls3 = BookClassT.objects.filter(pid=6)
    books = BooksT.objects.filter(id__in=range(1,14))
    books2 = BooksT.objects.filter(id__in=range(14,27))
    books3 = BooksT.objects.filter(id__in=range(27,40))
    books4 = books[:3]
    books5 = books[3:10]
    res =render(request,'homeapp/index.html',{'t_cate':cls,'t_cate2':cls2,'t_cate3':cls3,'books':books,'books2':books2,'books3':books3,'books4':books4,'books5':books5})
    return res

def h_login(request):
    return redirect('lrapp:login')

def h_regist(request):
    return redirect('lrapp:regist')
def h_bookdetails(request):
    num = request.GET.get('myid')
    books = BooksT.objects.filter(id=num)[0]
    ca2 = books.pid
    ids1 = ca2.pid
    ca1 = BookClassT.objects.filter(id=ids1)[0]
    discoun = (books.dd_price/books.price)*10
    res = render(request,'categoryapp/Book details.html',{'books':books,'discoun':int(discoun),'ca2':ca2,'ca1':ca1})
    return res

