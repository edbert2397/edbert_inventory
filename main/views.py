import json
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, JsonResponse
from main.forms import ItemForm
from django.urls import reverse
from .models import Item
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import datetime
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user = request.user)
    cnt = len(items)
    context={
        'name_app' : 'Inventory',
        'name' : request.user.username,
        'class' : 'PBP D',
        'items' : items,
        'cnt': cnt,
        'last_login':request.COOKIES['last_login'],
    }
    return render(request,"main.html",context)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        item = form.save(commit = False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form':form}
    return render(request,"create_item.html",context)

def get_item_json(request):
    item = Item.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize('json',item))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        user = request.user
    
    new_item = Item(name = name,amount = amount,description = description, user = user)
    new_item.save()

    return HttpResponse(b"CREATED",status = 201)

@csrf_exempt
def delete_item_ajax(request, item_id):
    if request.method == 'DELETE':
        item = Item.objects.get(id=item_id)
        item.delete()
        return HttpResponse({'status': 'DELETED'}, status=200)
    
def delete_item(request,item_id):
    item = Item.objects.get(pk = item_id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def increase_item(request,item_id):
    item = Item.objects.get(pk = item_id)
    item.amount += 1 
    item.save()
    return HttpResponseRedirect(reverse('main:show_main'))
def decrease_item(request,item_id):
    item = Item.objects.get(pk = item_id)
    if(item.amount >= 1):
        item.amount -= 1
    item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml",data),content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json",data),content_type = "application/json")

def show_xml_by_id(request,id):
    data = Item.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("xml",data),content_type = "application/xml")

def show_json_by_id(request,id):
    data = Item.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("json",data),content_type = "application/json")

@csrf_exempt
def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request,'register.html',context)
    
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if(user is not None):
            login(request,user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login',str(datetime.datetime.now()))
            return response
        else:
            messages.info(request,'Sorry,incorrect username or password. Please try again.')
    context = {}
    return render(request,'login.html',context)

@csrf_exempt
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

