from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import orders_list
from .forms import orderhere


# Create your views here.

def orders(request):
    data=orders_list.objects.all()
    print('Data from Products Table',data)

    prd={
        'data':data
    }
    return render(request,'orders.html',context=prd)

def add_orders(request):
    if request.method == 'POST':
        form = orderhere(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders/')
    else:
        form = orderhere()

    return render(request, 'add_orders.html', {'form': form})
    

        