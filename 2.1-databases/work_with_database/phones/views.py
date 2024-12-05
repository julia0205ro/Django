from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request, **kwargs):
    template = 'catalog.html'
    my_sort = request.GET.get('sort')
    if my_sort == 'min_price':
        context = {'phones': Phone.objects.order_by('price')}
    elif my_sort == 'max_price':
        context = {'phones': Phone.objects.order_by('-price')}
    elif my_sort == 'name':
        context = {'phones': Phone.objects.order_by('name')}
    else:
        context = {'phones': Phone.objects.all()}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
