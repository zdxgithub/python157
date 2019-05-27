import random

from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
# from alipay import AliPay
import time

from django.urls import reverse

from lrapp.models import AdrssInfo,OrderItem,Orders

# Create your views here.

app_private_key_string = open("D:\\Users\Administrator\PycharmProjects\DD\orderapp\keys\应用私钥2048.txt").read()
alipay_public_key_string = open("D:\\Users\Administrator\PycharmProjects\DD\orderapp\keys\应用公钥2048.txt").read()
app_private_key_string == """
    -----BEGIN PUBLIC KEY-----
    MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCwgksE59TpUWPS2MoGnwLdSV28+XyvUMdlPSOlPuvxp+z58UxXh6SapSjMMB5e99dqSolIyg0RjhLXAf3kAHgrg4KL4zZbtJS/zLDlDzZ8lM7nIcgyatAj/NaY4XkJlP8miodvVBgUkAjxZ5dE/ZquvE3+/V/VbCjsyqpC3q/3WrLS/rvXm6plmEMi9RR4wiwoXZpkSqswg70RxwgBv03pFBsO83yIcybmUPVT855XQca7QLvfO3xiYXc0BcEyKdgBce71TZ70QS2aKEufjYGhIJJjP3MYl4Gjhq7FUO5OKBmgyNRe0/rR2FmkreuOd9qQXYV4ZMtdF4PzKvd0hBHlAgMBAAECggEAVUj/WoVx+LJc21noc76NMcLrSg36UvNjBOW/vW5jrsYG2NXgn0JpJFe9GLv/UL/MFA2ju8n0+pB9ReoudOZNKilHALRuZW0hmnMa3fK1zwhP2JoYE1RM8baPMhtv0lNt3X995Srq37SgvZPiIXGwNdHClfxzO7ohJBjgn6Ldv1QAxDEusUrNNsug1yCaXjNHF2goGjHRzEJVtCIWNqa1rKcP7sa9lnDb4z2jJJxEnXyQBGxBjrGZbEUv/1Ujcqz9oJ1thu3iKWQfh2+JyHZYXiPFr4ZRiTAAWARU3Ehn61wH5qiuC7C4F2RzyFKESB6ENz9LHCljlU9iZwb3l5EdwQKBgQD/YG9ob598XOwemAsDlQKz2V5XR+pxSCylyTuf5RNyckMjm0m36943+xPCDNaDHc09hkGO2AISPI9OmuTeBflpn69l+Z9beTSB/4WA5y+zCKkPBZDPoFP8OrO+RsQeGsZ8B0sg3eeY2fZ26OgOujfdsRy14bwgZbXxWSLahkc4iQKBgQCw8JRhJVNLAvVCxajxOYaswSeXTHqERF8o0px+iDfstIbHk9E/yrlLTnAxh5EwKjsbyPiYadgomcMeleKyLsnvWNvKH8pS4RJziMsK0CpyxO4IFbcJqQx0QReFLWOIZaqjxT0uoDAEtLqmmHldAojftJ6/nkEPe1viMnnSqcX/fQKBgACXoKqFV8FaFdIcWCox9kekgWuCZzDMEg5wYQsF5P2m9jDm80zR5zoKAwm4Lecv8oHqBcznA1o3eb2c7lr1eJaeIDIEWjJEHbMPfKfH4Xxw0LOQN73DiW5UVIZkc5/+P+eZvLreyOK53rB36dHe7LI+7uodE+qfUcS1iDcpiJDBAoGAAcQE1wtWT3NSGz55tx6J14N976aVumgsQu4HHcQiOrx6c9dnySkuvC+mMvhVXJOvT1GsGWlE/PK73bxFLN4GqdrLJrM2g6k3U+vTiuIU6lxIu8/rqa8ELszPfUa8rYnGMCgxuhtjH0jma+8tlt4Fm6Xjx6m+oHbsrc8vJAkJrskCgYEAtVLSODWoeCOh6Qr6rqgNyBCveYDtEuced0INS2R6JYq6Mi63IcLFVyo8esQHNyEKOBmC8IlVYQyLQVWlBChWcFeSX8MUZqhzk4LelU89u+4Abs/Qs6286sVzOXrvze5DISJ+Efl4dPhi8CaJJXgeYeO/pA0+C87noWBkggFr9U0=
    -----END PUBLIC KEY-----

"""

alipay_public_key_string == """
    -----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsIJLBOfU6VFj0tjKBp8C3UldvPl8r1DHZT0jpT7r8afs+fFMV4ekmqUozDAeXvfXakqJSMoNEY4S1wH95AB4K4OCi+M2W7SUv8yw5Q82fJTO5yHIMmrQI/zWmOF5CZT/JoqHb1QYFJAI8WeXRP2arrxN/v1f1Wwo7MqqQt6v91qy0v6715uqZZhDIvUUeMIsKF2aZEqrMIO9EccIAb9N6RQbDvN8iHMm5lD1U/OeV0HGu0C73zt8YmF3NAXBMinYAXHu9U2e9EEtmihLn42BoSCSYz9zGJeBo4auxVDuTigZoMjUXtP60dhZpK3rjnfakF2FeGTLXReD8yr3dIQR5QIDAQAB
    -----END PUBLIC KEY-----

"""

# alipay1 = AliPay(
#     appid="2016092700608436",
#     app_notify_url=None,
#     app_private_key_string=app_private_key_string,
#
#     alipay_public_key_string=alipay_public_key_string,
#     sign_type="RSA" ,
#     debug=False
# )


def order_indent(request):
    uid = request.session.get('login')
    if uid:
        cart = request.session.get('cart')
        ad = AdrssInfo.objects.filter(pid=uid)
        res = render(request,'orderapp/indent.html',{'cart':cart,'ad':ad})
        return res
    else:
        return redirect('lrapp:login')


def checkname(request):
    username = request.POST.get('input_user')
    if not username:
        return HttpResponse('em')
    else:
        # a = AdrssInfo(recipient=username)
        # a.save()
        return HttpResponse('ok')


def checkadress(request):
    useradress = request.POST.get('input_adress')
    if not useradress:
        return HttpResponse('em')
    else:
        # a = AdrssInfo(adress=useradress)
        # a.save()
        return HttpResponse('ok')


def checkcode(request):
    usercode = request.POST.get('input_code')
    if not usercode:
        return HttpResponse('em')
    else:
        # a = AdrssInfo(zip_code=usercode)
        # a.save()
        return HttpResponse('ok')


def checkphone(request):
    userphone = request.POST.get('input_phone')
    if not userphone:
        return HttpResponse('em')
    else:
        # a = AdrssInfo(phone=userphone)
        # a.save()
        return HttpResponse('ok')


def order_indentlogic(request):
    cart = request.session.get('cart')
    uid = request.session.get('login')
    if uid:
        for i in cart.items:
            oic = OrderItem.objects.filter(pid__id=1)[0]
            pid = oic.pid
            oi = OrderItem(book_name=i.book_name,price=i.allprice,pid=pid)
            oi.save()
        l = '1234567890'
        or_num = ''.join(random.sample(l, 9))
        o = Orders(or_num=or_num,recipient=cart.allprice)
        o.save()
        ship_man = request.POST.get('ship_man')
        ship_man2 = request.POST.get('ship_man2')
        ship_man3 = request.POST.get('ship_man3')
        ship_man4 = request.POST.get('ship_man4')
        a = AdrssInfo(recipient=ship_man,adress=ship_man2,zip_code=ship_man3,phone=ship_man4)
        if a:
            pass
        else:
            a.save()
        url=reverse('orderapp:indentok')
        return redirect(url)
    else:
        return redirect('lrapp:login')


def checkad(request):
    adid = request.POST.get('adid')
    a = AdrssInfo.objects.filter(id=adid)[0]
    jstr = {'gna':a.recipient,'gad':a.adress,'gco':str(a.zip_code),'gph':str(a.phone)}
    return JsonResponse(jstr)


def index(request):
    return render(request, 'orderapp/index.html')
def indentok(request):
    # uid = request.GET.get('uid')
    # a = AdrssInfo.objects.get(pid=uid)
        # cart = request.GET.get('cart')
        # name = request.GET.get('name')
    cart = request.session.get('cart')
    # for i in cart.items:
    #     oi = OrderItem.objects.filter(pid__id=1)[0]
        # for j in oi:
        #     x = j.pid
        # pid = oi.pid
        # oi = OrderItem.objects.filter(id=i.bid)
    uid = request.GET.get('uid')
    ord = Orders.objects.filter(id=1)[0]

        # print(ord)
    return render(request,'orderapp/indent ok.html',{'ord':ord,'cart':cart})
def page1(request):
    if request.method == "GET":
        return render(request, 'orderapp/index.html')
    else:
        money = float(request.POST.get('money'))
        alipay =alipay1
        # 生成支付的url
        query_params = alipay.api_alipay_trade_page_pay(

            subject="百知饮水机",  # 商品简单描述
            out_trade_no="x2" + str(time.time()),  # 商户订单号
            total_amount=money,  # 交易金额(单位: 元 保留俩位小数)
            return_url='http://127.0.0.1:8000/orderapp/indentok/'
        )


        pay_url = "https://openapi.alipaydev.com/gateway.do?{0}".format(query_params)

        return redirect(pay_url)


def page2(request):
    alipay = alipay1
    if request.method == "POST":
        # 检测是否支付成功
        # 去请求体中获取所有返回的数据：状态/订单号
        from urllib.parse import parse_qs
        body_str = request.body.decode('utf-8')
        post_data = parse_qs(body_str)

        post_dict = {}
        for k, v in post_data.items():
            post_dict[k] = v[0]
        print(post_dict)

        sign = post_dict.pop('sign', None)
        status = alipay.verify(post_dict, sign)
        print('POST验证', status)
        return HttpResponse('POST返回')

    else:
        params = request.GET.dict()
        sign = params.pop('sign', None)
        status = alipay.verify(params, sign)
        print('GET验证', status)
        return HttpResponse('支付成功')

