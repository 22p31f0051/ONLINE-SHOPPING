from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import ProductList
from .forms import add_product

# Create your views here.

def ProductListView(request):

    data = ProductList.objects.all()
    print('data from products table',data)

    content={
        'data':data
    }
    return render(request,'products.html',context=content)


def add_products(request):
    if request.method == 'POST':
        form = add_product(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products/')
    else:
        form = add_product()

    return render(request, 'add_products.html', {'form': form})
    

        


