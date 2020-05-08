from django.shortcuts import render,HttpResponse
from home.models import Product,Contact,Order,Track
from math import ceil
from django.contrib import messages
# Create your views here.
def index(request):
    products=Product.objects.all()
    print(products)
    n=len(products)
    l=[]
    allinfo=[]
    nslides=n//4 + ceil(n/4 - n//4)
    for i in range(n):
        l.append(Product.objects.all()[i].category)
    l=list(set(l))
    for cat in l:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nslides=n//4 + ceil(n/4 - n//4)
        allinfo.append([prod,range(1,nslides),nslides])    
    # params={"product":products,'range':range(1,nslides)}
    # allinfo=[[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]
    params={"product":allinfo}
    return render(request,"index.htm",params)
def about(request):
    return render(request,"about.htm")

def contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        query=request.POST.get("query")
        con=Contact(name=name,email=email,query=query)
        con.save()
        messages.success(request, 'Query has been submitted')
    return render(request,"contact.htm")

def tracker(request):
    
    return render(request,"tracker.htm")
def search(request):
    return render(request,"search.htm")
def pview(request,id):
    product=Product.objects.filter(id=id)
    
    return render(request,"pview.htm",{'product':product})
def checkout(request):
    if request.method=='POST':
        itemjson=request.POST.get("itemjson")
        name=request.POST.get("name")
        email=request.POST.get("email")
        address=request.POST.get("add1") + " " + request.POST.get("add2")
        city=request.POST.get("city")
        state=request.POST.get("state")
        zipcode=request.POST.get("zipcode")
        check=Order(itemjson=itemjson,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode)
        check.save()
        orderid=check.id
        id=orderid
        order_update=Track(id=id,update="order is placed")
        order_update.save()
        messages.success(request, 'Order has been placed with id ' + str(orderid))
    return render(request,"checkout.htm")
    
