from django.shortcuts import render,redirect
from django.views import View
from .models import Customer,Product,OrderPlaced,Cart
from .forms import CustomerRegistrationForm, CustomerProfileView
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
# def home(request):
#     return render(request,'index.html')
class Home(View):
     def get(self,request):
         interior = Product.objects.filter(category='IN')
         exterior = Product.objects.filter(category='EX')
         accessories = Product.objects.filter(category='AC')
         inter = Product.objects.filter(category='IN')[:4]
         exter = Product.objects.filter(category='EX')[:4]
         acces = Product.objects.filter(category='AC')[:4]
         wheel = Product.objects.filter(sub_category='wheel')
         return render(request,'index.html',{'interior':interior,'exterior':exterior,'accessories':accessories,'wheel':wheel,'inter':inter,'exter':exter,'acces':acces})

def search(request):
    qur = request.GET.get('search')
    product = Product.objects.filter(title__contains= qur)
    return render(request,'search.html',{'qur':qur,'product':product})   

def report(request):
    return render(request,'dashboard.html')


def category(request):
    return render(request,'category.html')     

def sub_category(request):
    return render(request,'category_part.html')

class Product_Details(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        already_in_cart = False
        if request.user.is_authenticated:

            already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()

        return render(request,'product_details.html',{'product':product,'already':already_in_cart})

@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')   


@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)    
        amount =0.0
        shipping_amount = 50.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]

        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount = amount + shipping_amount
           

            return render(request,'add_to_cart.html',{'carts':cart,'totalamount':totalamount,'amount':amount})
        else:
            return render(request,'emptycart.html')


def plus_cart(request):
    if request.method =='GET':
        prod_id = request.GET['prod_id']            
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 50.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data= {
                'quantity':c.quantity,
                'amount':amount,
                'totalamount':amount + shipping_amount
            }
            
        return JsonResponse(data)

def minus_cart(request):
    if request.method =='GET':
        prod_id = request.GET['prod_id']            
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 50.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data= {
                'quantity':c.quantity,
                'amount':amount,
                'totalamount': amount + shipping_amount
            }
            
        return JsonResponse(data)
def remove_cart(request):
    if request.method =='GET':
        prod_id = request.GET['prod_id']            
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 50.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data= {
                'amount':amount,
                'totalamount': amount + shipping_amount
            }
            
        return JsonResponse(data)
@login_required
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 50.0
    totalamount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]       
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        totalamount = amount +shipping_amount    


    return render(request,'checkout2.html',{'add':add,'amount':amount,'totalamount':totalamount,'cart_items':cart_items})     


def Interior(request, data=None):
    if data==None:
        interior = Product.objects.filter(category='IN')[:12]
    elif data == 'engine' or data =='filters' or data =='ac' or data =='clutch' or data =='steering':    
        interior = Product.objects.filter(sub_category=data)[:6]
        

    return render(request,'interior.html',{'interior':interior}) 


def Exterior(request, data=None):
    if data==None:
        exterior = Product.objects.filter(category='EX')[:12]
    elif data == 'wheel' or data =='buffer' or data =='break' or data =='wind_screen' or data =='suspension' or data =='body_parts':    
        exterior = Product.objects.filter(sub_category=data)[:6]

    return render(request,'exterior.html',{'exterior':exterior})    


def Accessories(request, data=None):
    if data==None:
        accessories = Product.objects.filter(category='AC')[:12]
    elif data == 'perfumes' or data =='sound_system' or data =='seat_cover':    
        accessories = Product.objects.filter(sub_category=data)[:6]

    return render(request,'accessories.html',{'accessories':accessories})    


class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()    
        return render(request,'sign_up.html',{'form':form})

    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Congratulations!! Registration Successfully')
            return redirect('/accounts/login/')
        return render(request,'sign_up.html',{'form':form})    



@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileView()
        return render(request,'profile.html',{'form':form,'active':'active'})
        
    def post(self,request):
        form = CustomerProfileView(request.POST)    
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=usr,name=name,address=address,city=city,state=state,zipcode=zipcode )
            reg.save()
            messages .success(request, 'Congratulations !!! Profile Update Successfully')
        return render(request,'profile.html',{'form':form,'active':'active'})    

@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,'address.html',{'add':add,'active':'active'})




@login_required
def paymentdone(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect("/orders")    

@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user= request.user)
    return render(request,"orders.html",{'order_placed':op})