from django.contrib import admin
from .models import Product,Category,Order,Register,Contact
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Register) 
admin.site.register(Contact)