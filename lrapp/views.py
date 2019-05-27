from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from DD import settings
from lrapp.captcha.image import ImageCaptcha
from lrapp.models import User, BookClassT, BooksT,Check_user
import re,random,string,hashlib,datetime

# Create your views here.


def login(request):
    flag = request.GET.get('flag')
    res = render(request,'lrapp/login.html',{'flag':flag})
    return res


def regist(request):
    flag = request.GET.get('flag')
    res = render(request,'lrapp/register.html',{'flag':flag})
    return res


def get_sault():
    l = '1234567890-=qwertyuiop[]asdfghjklzxcvbnm,./'
    salt = ''.join(random.sample(l, 6))
    return salt

def has_code(name,now):
    h = hashlib.md5()
    name += now
    h.update(name.encode())
    return h.hexdigest()

def make_check_user(new_user):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    code = has_code(new_user.name,now)
    Check_user.objects.create(code=code,user=new_user)
    return code


def send_email(email,code):
    subject='来自DD的邮件'
    from_email = 'zdx_email@sina.com'
    text_content = '欢迎访问http://127.0.0.1:8000/lrapp/email_check/，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册<a href="http://{}/confirm/?code={}"target=blank>http://172.20.10.10:8000/lrapp/email_check/</a>，\欢迎你来验证你的邮箱，验证结束你就可以登录了！</p>'.format('127.0.0.1',code)
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def registlogic(request):
    name = request.POST.get('txt_username')
    pwd1 = request.POST.get('txt_password')
    pwd2 = request.POST.get('txt_repassword')
    code = request.session.get('code')
    c = request.POST.get('txt_vcode')
    nickname = request.POST.get('nick')
    x = get_sault()
    sault = pwd1+x
    h = hashlib.md5()
    h.update(sault.encode())
    t_pwd = h.hexdigest()
    u = User.objects.filter(name=name)
    res = re.findall('\w+@[0-9a-zA-Z]{2,3}\.com|^138\d{8}$|^159\d{8}$|^136\d{8}$|^171\d{8}$|^177\d{8}$|^149\d{8}$|^183\d{8}$',name)
    pwds = re.findall('[0-9a-zA-Z]{6,}',pwd1)
    # print(u,res,pwds)
    if u:
        return redirect('lrapp:regist')
    else:
        flag = request.GET.get('flag')
        if res and pwds and pwd1==pwd2 and code.lower()==c.lower():
            new_user = User.objects.create(name=name,salt=x,two_pwd=t_pwd,nickname=nickname)
            code = make_check_user(new_user)
            send_email(name,code)
            user = User.objects.get(name=name)
            url = reverse('lrapp:email_check_ok')+'?userid='+str(user.id)+'&usernick='+user.name+'&flag='+flag
            # return render(request,'lrapp/email_check_ok.html',{'userid':user.id,'usernick':user.name,'flag':flag})
            return redirect(url)
        else:
            return redirect('lrapp:regist')


def email_check_ok(request):
    flag = request.GET.get('flag')
    userid = request.GET.get('userid')
    usernick = request.GET.get('usernick')
    return render(request,'lrapp/email_check_ok.html',{'userid':userid,'usernick':usernick,'flag':flag})


def emaillogic(request):
    flag = request.GET.get('flag')
    userid = request.GET.get('userid')
    usernick = request.GET.get('usernick')
    print(userid,usernick)
    if request.POST.get('input_email_check') == request.session.get('co'):
        return render(request,'lrapp/register ok.html',{'userid':userid,'usernick':usernick,'flag':flag})
    return redirect('lrapp:regist')



def registjump(request):
    user_id = request.GET.get('name1')
    flag = request.GET.get('flag')
    u = User.objects.filter(id=user_id)[0].nickname
    cls = BookClassT.objects.filter(pid=1)
    cls2 = BookClassT.objects.filter(pid=4)
    cls3 = BookClassT.objects.filter(pid=6)
    books = BooksT.objects.filter(id__in=range(1, 14))
    books2 = BooksT.objects.filter(id__in=range(14, 27))
    books3 = BooksT.objects.filter(id__in=range(27, 40))
    books4 = books[:3]
    books5 = books[3:10]
    request.session['login'] = user_id
    stus = 1
    if flag=='1':
        request.session['login']=user_id
        return redirect('orderapp:order_indent')
    else:
        return render(request,'homeapp/index.html',{'user':u,'t_cate': cls, 't_cate2': cls2, 't_cate3': cls3, 'books': books, 'books2': books2, 'books3': books3,
                 'books4': books4, 'books5': books5,'stus':stus})


def loginlogic(request):
    name = request.POST.get('txtUsername')
    pwd = request.POST.get('txtPassword')
    us = User.objects.filter(name=name)
    if us:
        flag =  request.GET.get('flag')
        s = User.objects.filter(name=name)[0].salt
        sault = pwd + s
        h = hashlib.md5()
        h.update(sault.encode())
        t_pwd = h.hexdigest()
        u = User.objects.filter(name=name, two_pwd=t_pwd)
        if u and flag=='1':
            user_id = us[0].id
            request.session['login'] = user_id
            return redirect('orderapp:order_indent')
        elif u:
            cls = BookClassT.objects.filter(pid=1)
            cls2 = BookClassT.objects.filter(pid=4)
            cls3 = BookClassT.objects.filter(pid=6)
            books = BooksT.objects.filter(id__in=range(1, 14))
            books2 = BooksT.objects.filter(id__in=range(14, 27))
            books3 = BooksT.objects.filter(id__in=range(27, 40))
            books4 = books[:3]
            books5 = books[3:10]
            user_id = us[0].id
            request.session['login']=user_id
            stus = 1
            return render(request,'homeapp/index.html',{'user':u[0].nickname,'t_cate': cls, 't_cate2': cls2, 't_cate3': cls3, 'books': books, 'books2': books2, 'books3': books3,
             'books4': books4, 'books5': books5,'stus':stus})
        else:
            return redirect('lrapp:login')
    else:
        return redirect('lrapp:login')


def checkname(request):
    username = request.POST.get('txt_username')
    u = User.objects.filter(name=username)
    if not username:
        return HttpResponse('em')
    elif not re.findall('\w+@[0-9a-zA-Z]{2,3}\.com|^138\d{8}$|^159\d{8}$|^136\d{8}$|^171\d{8}$|^177\d{8}$|^149\d{8}$|^183\d{8}$',username):
        return HttpResponse('txterorr')
    elif u:
        return HttpResponse('no')
    else:
        return HttpResponse('yes')


def checkpwd(request):
    userpwd = request.POST.get('txt_password')
    if not userpwd:
        return HttpResponse('em')
    elif not re.findall('[0-9a-zA-Z]{6,}',userpwd):
        return HttpResponse('txterorr')
    else:
        return HttpResponse('yes')


def checklpwd(request):
    userpwd = request.POST.get('txtPassword')
    if not userpwd:
        return HttpResponse('em')
    else:
        return HttpResponse('ok')


def checklname(request):
    username = request.POST.get('txtUsername')
    if not username:
        return HttpResponse('em')
    else:
        return HttpResponse(' ')



def checkrepwd(request):
    pwd = request.POST.get('txt_password')
    repwd = request.POST.get('txt_repassword')
    if repwd != pwd:
        return HttpResponse('no')
    else:
        return HttpResponse('yes')


def getcaptcha(request):
    image = ImageCaptcha()
    code = random.sample(string.ascii_letters+string.digits,4)
    random_code = ''.join(code)
    request.session['code'] = random_code
    data = image.generate(random_code)
    return HttpResponse(data,'image/png')


def code(request):
    code = request.session.get('code')
    # print(code,request.POST.get('cname').lower())
    if code.lower() == request.POST.get('cname').lower():
        return HttpResponse('验证码相同')
    else:
        return HttpResponse('验证码不一致')

def email_check(request):
    co = random.sample(string.digits, 6)
    return render(request,'lrapp/email_check.html',{'co':co})
