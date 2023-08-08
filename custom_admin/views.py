from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from shop. models import Category,Product,Contact,Order,Register
from django.contrib import messages
# Create your views here.
def adminLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password=request.POST.get('pass')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('Dashboard')
        else:
           messages.info(request,"username and password is incorrect")
    return render(request,'adminTemplates/adminLogin.html')

def Dashboard(request):
    register_user = Register.objects.all()
    return render(request,'adminTemplates/dashboard.html',{'register_user':register_user})

def category(request):
    categories = Category.objects.all()
    return render(request,'adminTemplates/prodCategory.html',{'categories':categories})

def add_category(request):
    if request.method == "POST":
        img = request.POST.get('img')
        name = request.POST.get('name')
        
        specific_folder = 'uploads/products/'
    
        add = Category(category_img=specific_folder + img,name=name)
        add.save()
        return redirect('category') 
    return render(request,'adminTemplates/add_category.html')

def update_category(request,myid):
    category = Category.objects.get(id=myid)
    if request.method == 'POST':
        cat_img = request.POST.get('image')
        cat_name = request.POST.get('name')
        
        specific_folder = 'uploads/products/'
        
        update_cat = Category(id=myid,category_img=specific_folder+cat_img,name=cat_name)
        update_cat.save()
        return redirect('category')
    return render(request,'adminTemplates/update_category.html',{'obj':category})

def delete_category(request,id):
    category_name = Category.objects.get(id=id)
    if category_name.delete():
        return redirect('category')
    else:
        pass
    return render(request,'adminTemplates/update_category.html')

def orders(request):
    order = Order.objects.all()
    return render(request,'adminTemplates/order_details.html',{'order':order})

def delete_order(request,id):
    del_order = Order.objects.get(order_id =id)
    if del_order.delete():
        return redirect('orders')
    else:
        pass
    return render(request,'adminTemplates/order_details.html')


def searchProduct(request):
    query = request.GET.get('searchmenu')
    if query:
        products = Product.objects.filter(name__icontains = query)
    return render(request,'adminTemplates/productSearch.html',{'query': query, 'product_list': products})

def productList(request):
    product_list = Product.objects.all()
    return render(request,'adminTemplates/product_list.html',{'product_list':product_list})

def add_product(request):
    category_name = Category.objects.all()
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        category_id = request.POST.get('category')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        pub_date = request.POST.get('pub_date')
        images = request.POST.get('image')
        
        specific_folder = 'uploads/products/'
        
        category = Category.objects.get(pk=category_id)
        product = Product(name=product_name, category=category, price=price, desc=desc, pub_date=pub_date, image=specific_folder + images)
        product.save()
        return redirect('productList')         
    return render(request,'adminTemplates/add_product.html',{'category_name':category_name})

def delete_product(request,id):
    del_product = Product.objects.get(id=id)
    if del_product.delete():
        return redirect('productList')
    else:
        pass
    return render(request,'adminTemplates/product_list.html')

def update_product(request,id):
    data = Product.objects.get(id=id)
    if request.method == 'POST':
        product_name = request.POST.get('nm')
        price = request.POST.get('pr')
        description = request.POST.get('desc')
        pub_date = request.POST.get('date')
        img = request.POST.get('img')
        
        if img is not None:
            specific_folder = 'uploads/products/'
            data.name=product_name
            data.price=price
            data.desc=description
            data.pub_date=pub_date
            data.image=specific_folder + img
            data.save()
            return redirect('productList')
    return render(request,'adminTemplates/update_product.html',{'obj':data})

def contactList(request):
    contact = Contact.objects.all()
    return render(request,'adminTemplates/contact.html',{'contact':contact})
    
def adminLogout(request):
    return redirect('adminLogin')
    
