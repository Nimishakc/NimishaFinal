from django.contrib import admin
from. models import Onlinepayment,Offlinepayment,Onlineapproval,Offlineapproval,Send

admin.site.register(Onlinepayment)
admin.site.register(Offlinepayment)
admin.site.register(Onlineapproval)
admin.site.register(Offlineapproval)
admin.site.register(Send)
