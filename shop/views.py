from django.shortcuts import render,redirect
from . models import Product,Category,Order,Register,Contact
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def collections(request):
    category = Category.objects.all()
    context = {'category':category}
    return render(request,'category.html',context)

def collectionsviews(request,myid):
    if (Category.objects.filter(id=myid)):
        products = Product.objects.filter(category = myid)
        context = {'products':products}
        return render(request,'products.html',context)
    else:
        messages.warning(request,"No such ctaegory found")
        return redirect('collections')
    
def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson')
        name=request.POST.get('name')
        amount=request.POST.get('amount')
        email=request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        phone=request.POST.get('phone')

        order = Order(items_json=items_json,name=name,amount=amount,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request,'checkout.html',{'thank':thank, 'id':id})
    return render(request,'checkout.html')


def contact(request):
    if request.method == "POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact= Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        thank = True
        return render(request,'contact.html',{'thank':thank})
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def signIn(request):
    if request.method =="POST":
        username=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        con_password=request.POST.get('con_password')
        
        if password != con_password:
            messages.info(request,"password and confirm password are not same")
        elif Register.objects.filter(email=email).exists():
            messages.info(request,"Email Already exists")
        elif username != "" and email != "" and password !="" and con_password != "":
            register = Register(username=username,email=email,password=password,con_password=con_password)
            register.save()
            return redirect('loginUser/') 
        else:
            messages.info(request,"All fields are required!")
    return render(request,'register.html')
    

def loginUser(request):
    if request.method == "POST":
        user_name = request.POST.get('username')
        pass1=request.POST.get('pass')
        
        loginUser = Register.objects.filter(username = user_name,password=pass1)
        if loginUser.exists():
            return redirect('home')
        else:
            messages.info(request, "Please enter valid username or password.")
    return render(request,'login.html')

def search(request):
    query = request.GET.get('search')
    if query:
        products = Product.objects.filter(name__icontains = query)
    return render(request,'search.html',{'query': query, 'products': products})

def prodView(request,id): 
    product = Product.objects.filter(id=id)
    return render(request,'prodView.html',{'product':product[0]})
