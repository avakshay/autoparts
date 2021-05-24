from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) 





CATEGORY_CHOICES = (
    ('IN','interior'),
    ('EX','exterior'),
    ('AC','accessories')
)
SUBCATEGORY = (
    ('engine','engine'),
 ('ac','ac'),
 ('clutch','clutch'),
 ('steering','steering'),
 ('filters','filters'),
 ('seat_cover','seat_cover'),
 ('sound_system','sound_system'),
 ('perfumes','perfumes'),
 ('wheel','wheel'),
 ('buffer','buffer'),
 ('break','break'),
 ('wind_screen','wind_screen'),
 ('suspension','suspension'),
 ('body_parts','body_parts')
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField(blank=True)
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    sub_category = models.CharField(choices=SUBCATEGORY,max_length=15)
    product_image = models.ImageField(upload_to='productimg')
    product_image1 = models.ImageField(upload_to='productimg',blank=True, default='img')
    product_image2 = models.ImageField(upload_to='productimg',blank=True, default='img')
    product_image3 = models.ImageField(upload_to='productimg',blank=True, default='img')
    product_image4 = models.ImageField(upload_to='productimg',blank=True, default='img')
    

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the Way','On the Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)
class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

