from django.urls import path
from django.conf import urls
from . import views

urlpatterns = [
    path('', views.home, name='f1.html'),
    path('tv',views.tv,name='tv.html'),
    path('mobile',views.mobile,name='mobile.html'),
    path('theatre',views.theatre,name='hometheatre.html'),
    path('air',views.air,name="airconditioner.html"),
    path('buy',views.buy,name='otpver.html'),
    path('offpay',views.offpay,name='offlinepayment.html'),
    path('onpay',views.onpay,name='onlinepayment.html'),
    path('staff',views.staff,name='staff.html'),
    path('app',views.app,name='approval.html'),
    path('onlineok',views.onlineok,name='onlinepayment.html'),
    path('offlineok',views.offlineok,name='offlinepayment.html'),
    path('onappro',views.onappro,name='onlineapproval.html'),
    path('offapro',views.offapro,name='offlineapproval.html'),
    path('onpays',views.onpays,name='onlinestatus.html'),
    path('offpays',views.offpays,name='offlinestatus.html'),
    path('send',views.send,name='otpver.html'),
    path('verify',views.verify,name='registration.html'),
    path('homea',views.homea,name='dashboard.html'),
    path('logout',views.logout,name='staff.html'),
]