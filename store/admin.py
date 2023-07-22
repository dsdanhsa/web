from django.contrib import admin

from .models import *

admin.site.register(Customer)
#store
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
#iphone
admin.site.register(ProductApple)
admin.site.register(OrderApple)
admin.site.register(OrderItemApple)



admin.site.register(ShippingAddress)