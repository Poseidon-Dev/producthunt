from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Product


def home(request):
    return render(request, 'products/home.html')


@login_required
def create(request):
    if request.method == 'POST':
        if (
            request.POST['title'] and 
            request.POST['body'] and
            request.POST['url'] and
            request.FILES['mainimage'] and
            request.FILES['iconimage']):
            product = Product()

            product.title = request.POST['title'] 
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']

            product.image = request.FILES['mainimage']
            product.image = request.FILES['iconimage']

            product.pub_date = timezone.datetime.now()
            product.author = request.user
            product.save()
            return redirect('home')

        else:
            return render(request, 'products/create.html', {'error':'All fields are required'})
            
    else:
        return render(request, 'products/create.html')