from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import item
from django.template import loader
from .forms import ItemForm
from django.urls import reverse


# Create your views here.
def index(request):
    # url = reverse('food:index')
    item_list = item.objects.all()
    # template = loader.get_template('food/index.html')
    context = {
        'item_list':item_list,

    }
    return render(request,'food/index.html',context)

def detail(request,id):
    items = item.objects.get(pk=id)
    context = {
        'items':items,
    }
    return render(request,'food/detail.html',context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')
    
    return render(request,'food/item-form.html',{'form':form})

def update_item(request,id):
    items = item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=items)

    if form.is_valid():
        form.save()
        return redirect('index')
    
    return render(request,'food/item-form.html',{'form':form,'items':items})

def delete_item(request,id):
    Item = item.objects.get(id=id)

    if request.method == 'POST':
        Item.delete()
        return redirect('index')
    
    return render(request,'food/delete-item.html',{'Item':Item})



    



