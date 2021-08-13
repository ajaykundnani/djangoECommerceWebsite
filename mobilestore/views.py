from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from . models import Product,Users
from .forms import ProductForm,UsersForm

# Create your views here.

def homepage(request):
    if request.session.has_key('yes'):
        myproducts = Product.objects.all()
        return render(request,'home.html',{'myproducts':myproducts})
    else:
        return redirect(login)
    
       

def productDetail(request,id):
    if request.method == 'POST':
        myid = Product.objects.get(id = id)
        frm = ProductForm(request.POST,instance=myid)
        if frm.is_valid():
            frm.save()
    else:
        myid = Product.objects.get(id = id)
        frm = ProductForm()
        return render(request,'productDetail.html',{'form':frm,'myid':myid})

def addcart(request):
    #myproduct = Product.objects.get(id = id)
    #name = myproduct.p_name
    #print('ProductName',name)
    qty = request.POST.get('qty')
    product = request.POST.get('p')
    cart = request.session.get('cart')
    if cart:
        cart[product] = qty               
    else:
        cart = {}
        cart[product] = qty

    request.session['cart'] = cart
    print('Cart',request.session['cart'])
    return HttpResponseRedirect('/')

def showcart(request):
    c = request.session.get('cart')
    if c:
        cart = list(request.session.get('cart').values())
        ids = list(request.session.get('cart').keys())
        mycart = Product.getProductsByIds(ids)
        return render(request,'cart.html',{'mycart':mycart,'c':c})
    else:
        return HttpResponse('No Item In Cart')


def signUp(request):
    if request.method == "POST":
        uname = request.POST['myuser']
        passw = request.POST['password']
        ema = request.POST['email']
        myusers = Users.objects.filter(u_name = uname)
        if myusers:
            return render(request,'signUp.html',{'error':'Already Exists '})
        else:
            newUser = Users.objects.create(u_name = uname , u_pass = passw , u_email = ema)
            newUser.save()
            return render(request,'signUp.html',{'error':'Successfully Register '})     
    else:
        return render(request,'signUp.html')

def login(request):
    if request.session.has_key('yes'):
        return redirect('/')

    if request.method == 'POST':
        nm = request.POST['myuser']
        passw = request.POST['password']
        loginuser = Users.objects.filter(u_name = nm , u_pass = passw)
        if  not loginuser:
            return redirect(login)
        else:
            request.session['yes']=True
            return redirect('/')
    else:
        return render(request,'login.html')