from django.contrib import admin

from django.contrib import admin
from shop.models import *
admin.site.register(Country)
admin.site.register(City)
admin.site.register(DeliveryMethod)
admin.site.register(Categories)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Suppliers)
admin.site.register(Transactions)
admin.site.register(Inventory)