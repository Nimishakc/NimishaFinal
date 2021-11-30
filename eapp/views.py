from django.contrib import messages
from django.shortcuts import render
import random
import smtplib
from.models import Onlinepayment,Offlinepayment,Onlineapproval,Offlineapproval,Send



def home(request):
    return render(request,'f1.html')
def tv(request):
    return render(request,'tv.html')
def mobile(request):
    return render(request,'mobile.html')
def theatre(request):
    return render(request,'hometheatre.html')
def air(request):
    return render(request,'airconditioner.html')
def buy(request):
    if request.method == 'POST':
        return render(request,'otpver.html')
    else:
        return render(request,'otpver.html')

def offpay(request):
    if request.method == 'POST':
        return render(request, 'offlinepayment.html')
    else:
        return render(request,'offlinepayment.html')

def onpay(request) :
    if request.method == 'POST':
        return render(request,'onlinepayment.html')
    else:
        return render(request,'onlinepyment.html')
def onlineok(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        city = request.POST['city']
        ph = request.POST['ph']
        mail = request.POST['mail']
        item = request.POST['item']
        imo = request.POST['imo']
        credit = request.POST['credit']
        Onlineapproval(name=name, address=address, city=city, ph=ph, mail=mail, item=item,
                       imo=imo, credit=credit).save()
        msg = name + ", your order has been registered you will get your product within " \
                     "one week. Your payment has been received. for any quiries contact-xxxx "
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("nimishachandran98@gmail.com", "Nimishakc@98")
        s.sendmail("nimishachandran98@gmail.com",mail, msg)
        s.quit()
        messages.success(request, 'SUCCESSFULLY ORDERED YOU WILL RECIEVE AN EMAIL SHORTLY')
        return render(request,'onlinepayment.html')
    else:
        messages.success(request, 'REGISTRATION FAILED TRY AGAIN LATER')
        return render(request,'onlinepayment.html')

def offlineok(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        city = request.POST['city']
        ph = request.POST['ph']
        mail = request.POST['mail']
        item = request.POST['item']
        imo = request.POST['imo']
        Offlineapproval(name=name, address=address, city=city, ph=ph, mail=mail, item=item,
                       imo=imo).save()
        msg = name + ", your order has been registered you will get your product within " \
                     "one week. Your have opted offline payment system. for any quiries contact-xxxx "
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("nimishachandran98@gmail.com", "Nimishakc@98")
        s.sendmail("nimishachandran98@gmail.com", mail, msg)
        s.quit()
        messages.success(request, 'SUCCESSFULLY ORDERED YOU WILL RECIEVE AN EMAIL SHORTLY')
        return render(request,'offlinepayment.html')
    else:
        messages.success(request, 'REGISTRATION FAILED TRY AGAIN LATER')
        return render(request,'offlinepayment.html')

def staff(request):
    return render(request,'staff.html')

def app(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'app' and password == 'app':
            return render(request, 'dashboard.html')
        else:
            return render(request, 'staff.html')

def onappro(request):
    x = Onlineapproval.objects.all()
    return render(request, 'onlineapproval.html', {'all': x})

def offapro(request):
    x = Offlineapproval.objects.all()
    return render(request, 'offlineapproval.html', {'all': x})

def onpays(request):
    if request.method == 'POST':
        return render(request,'onlinestatus.html')
    else:
        return render(request, 'onlinestatus.html')

def offpays(request):
    if request.method == 'POST':
        return render(request,'offlinestatus.html')
    else:
        return render(request, 'offlinestatus.html')

val=None

def send(request):
    if request.method == 'POST':
        email = request.POST['email']
        x = str(random.randint(1000,9999))
        c=x
        global val
        def val():
            return c
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("nimishachandran98@gmail.com", "Nimishakc@98")
        s.sendmail("nimishachandran98@gmail.com",email, x)
        s.quit()
        messages.success(request, 'OTP SENT CHECK YOUR MAIL')
        return render(request,'otpver.html')

    else:
        return render(request,'otpver.html')

def verify(request):
    if request.method == 'POST':
        otpcheck = request.POST['otpcheck']
        ok=val()
        if otpcheck == ok:
            messages.success(request, 'LOGGED IN')
            return render(request,'registration.html')
        else:
            messages.success(request, 'FAILED TO VERIFY OTP')
            return render(request,'otpver.html')

def homea(request):
    return render(request,'dashboard.html')
def logout(request):
    return render(request,'staff.html')
