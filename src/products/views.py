from django.shortcuts import render,redirect

from .forms import ProductForm
from .models import Product

# import function to run
#from .test_external import sure


import requests

def button(request):
    return render(request,"external.html")

def output(request):
    data=requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'external.html',{'data':data})

'''
def external(request):
    import sys
    #from subprocess import run,PIPE
    #from django.http import HttpResponse
    # import function to run
    from .test_external import sure
    #inp= request.POST.get('param')
    #out= run([sys.executable,'products/test_external.py',inp],shell=False,stdout=PIPE)
    out=sure()
    #print("holy cow, let's find this bug!",out)
    #return HttpResponse("return this string")
    return render(request,'external.html',{'test_phrase':out})
'''

# I can't seem to get the output to print on the page if I import this as an External
# file... It works fine below if I declare the function here in views though.

#def external(request):
#    from .test_external import sure
#    out=sure()
#    return render(request,'external.html',{'test_phrase':out})


def external(request):
    return render(request,'external.html',{'test_phrase':sure})
def sure():
    var = "\num, seems ok to me...\n"
    #print(var)
    return var


def read_file(request):
    f = open('products/test_text.txt', 'r')
    file_content = f.read()
    f.close()
    context = {'file_content': file_content}
    return render(request, "external.html", context)


def py_tests(request):
    return render(request,'external.html',{'test_cos':testies})
def testies():
    import numpy as np
    import cartopy.crs as ccrs
    #print("wow, cartopy is installed. Let's make some maps")
    var = np.cos(0.76)
    var2 = "wow, cartopy is installed. Let's make some maps"
    #print(var)
    return var2


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
    "form": form,
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    #context = {"title":obj.title,
    #"description": obj.description,
    #"price":obj.price
    #}
    context = {
    "object": obj,
    }
    return render(request, "product/detail.html", context)
