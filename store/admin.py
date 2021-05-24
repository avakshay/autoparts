from django.contrib import admin
from .models import Customer,OrderPlaced,Cart,Product

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','address','city','zipcode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted_price','description','brand','category','sub_category']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']    

@admin.register(OrderPlaced)    
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['user','customer','product','quantity','ordered_date','status']
