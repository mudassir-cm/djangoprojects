from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .forms import CustomerForm, LoginForm
from .models import Product, Category, Customer, Order
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            print(quantity)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('index')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
        products = None
        # request.session.get('cart').clear()
        categories = Category.objects.all()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.objects.filter(category__id=categoryID)
        else:
            products = Product.objects.all()
        return render(request, 'store/index.html', {'products': products, 'categories': categories})


# def index(request):


def signup(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            messages.success(request, 'hhhhhhhhh')
            customer = form.save(commit=False)  #### it return model object. in this case customer object
            customer.password = make_password(form.cleaned_data['password'])
            form.save()
            return redirect('index')

    else:
        form = CustomerForm()
    return render(request, 'store/signup.html', {'form': form})


# def user_login(request):
#     if request.method == 'POST':
#         pass
#     else:
#         pass


class Login(View):
    returnurl = None
    def get(self, request):
        form = LoginForm()
        Login.returnurl = request.GET.get('return_url')
        return render(request, 'store/user_login.html', {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            customer = None
            try:
                customer = Customer.objects.get(email=email)
            except Customer.DoesNotExist:
                messages.error(request, 'email or passwor is invalid try')
            if customer:
                flag = check_password(password, customer.password)
                if flag:
                    request.session['customer'] = customer.id
                    messages.success(request, 'Login Successfully')
                    if Login.returnurl:
                        return HttpResponseRedirect(Login.returnurl)
                    else:
                        return redirect('index')
                else:
                    messages.error(request, 'email or passwor is invalid')
        return render(request, 'store/user_login.html', {'form': form})

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.objects.filter(id__in=ids)
        print(products)
        return render(request, 'store/cart.html', {'products': products})

class CheckOut(View):
    def post(self, request):
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        customer = request.session.get('customer')
        cart =  request.session.get('cart')
        products = Product.objects.filter(id__in=list(cart.keys()))
        print(phone, address, customer, cart, products)

        for product in products:
            order = Order(customer = Customer(id = customer),
                              phone = phone,
                              address = address,
                              product = product,
                              price = product.price,
                              quantity = cart.get(str(product.id))
                              )

            order.save()
        request.session['cart'] = {}

        return redirect('cart')

class OrderView(View):
    @method_decorator(auth_middleware)
    def get(self, request):
        customer_id = request.session.get('customer')
        orders = Order.objects.filter(customer = customer_id)
        return render(request, 'store/order.html', {'orders': orders})

def logout(request):
    request.session.clear()
    return redirect('user_login')
# Create your views here.
