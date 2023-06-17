from django.contrib import admin
from main.models import Category, Contact, Order, OrderItem, Parameter, Product, ProductInfo, ProductParameter, Shop, User

# Register your models here.
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ProductParameter)
admin.site.register(User)
admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(ProductInfo)
admin.site.register(Parameter)