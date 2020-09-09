from django.shortcuts import render, get_object_or_404, redirect
from .models import Products
from .forms import ProductCreateForm

# Create your views here.
def product_detail_view(request,id):
   # obj= Products.objects.get(id=id)
    obj= get_object_or_404(Products, id=id) #This is for validating if a certain ID is present in DB or not
    context={
        'object':obj
    }
    return render(request,"product/detail.html",context)


def product_create_view(request):
    form= ProductCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=ProductCreateForm()
  
    context={
        'form':form
    }
    return render(request,"product/product_create.html",context)


def product_update_view(request,id):
    obj= get_object_or_404(Products, id=id)
    form= ProductCreateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context={
        'form':form
    }
    return render(request,"product/product_create.html",context)

def product_delete_view(request,id):
    obj= get_object_or_404(Products, id=id)
    if request.method =='POST':
        obj.delete() 
        return redirect('../../')
    context={
        'obj':obj
    }
    return render(request,"product/product_delete.html",context)

def product_query_all_view(request):
    queryset= Products.objects.all()
    context={
        'object_list':queryset
    }
    return render(request,"product/product_list.html",context)



