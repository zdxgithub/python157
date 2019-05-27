# import datetime
from django.http import JsonResponse
from django.urls import reverse

from carapp.Buycar import Buycar,Item
from django.shortcuts import render,redirect,HttpResponse
# from . import models

# Create your views here.
# from DD import settings
from carapp.models import BooksT


def carlist(request):
    cart = request.session.get('cart')
    res = render(request,'carapp/car.html',{'cart':cart})
    # return HttpResponse('ok')
    return res


def addcar(request):
    bid = request.POST.get('books_id')
    bobj = BooksT.objects.filter(id=bid)[0]
    cart = request.session.get('cart')
    if not cart:
        cart = Buycar()
    item = Item(bobj,1)
    cart.add(item)
    request.session['cart'] = cart
    return HttpResponse('ok')


def upcar(request):
    iid = request.POST.get('item_id')
    new_count = int(request.POST.get('new_count'))
    cart = request.session.get('cart')
    cart.upc(iid,new_count)
    request.session['cart'] = cart
    ialp = cart.upc(iid,new_count)
    alp = cart.allprice
    acount = cart.count
    asave = cart.save
    jstr = {'alp': alp,'ialp':ialp,'acount':acount,'asave':asave}
    return JsonResponse(jstr)

    # return HttpResponse('ok')


def car_remove(request):
    info_id = request.GET.get('info_id')
    cart = request.session.get('cart')
    cart.remove(info_id)
    request.session['cart'] = cart
    alp = cart.allprice
    acount = cart.count
    asave = cart.save
    jstr = {'alp':alp,'acount':acount,'asave':asave}
    return JsonResponse(jstr)

def car_recover(request):
    info_id = request.POST.get('info_id')
    cart = request.session.get('cart')
    cart.recover(info_id)
    request.session['cart'] = cart
    alp = cart.allprice
    acount = cart.count
    asave = cart.save
    jstr = {'alp': alp, 'acount': acount, 'asave': asave}
    return JsonResponse(jstr)



def carlistlogic(request):
    lo = request.session.get('login')
    if lo:
        return redirect('orderapp:order_indent')
    else:
        url = reverse("lrapp:login")+"?flag=1"
        return redirect(url)



