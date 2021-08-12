from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from . models import Product
from .forms import ProductForm

# Create your views here.

def homepage(request):
    #request.session.clear()
    myproducts = Product.objects.all()
    return render(request,'home.html',{'myproducts':myproducts})

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


    