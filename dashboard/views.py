from django.shortcuts import render, redirect
from main import models

def index(request):
    contacts = models.Contact.objects.filter(is_show=False).count()

    context = {
        'contacts':contacts
    }
    return render(request, 'dashboard/index.html', context)


# CRUD 

# Create
# Read -> List/Detail
# Update
# Delte

#Banner 
def create_banner(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        models.Banner.objects.create(
            title=title,
            body=body,
        )
    return render(request, 'dashboard/banner/create.html')


def list_banner(request):
    banners = models.Banner.objects.all()
    context = {
        'banners':banners
    }
    return render(request, 'dashboard/banner/list.html', context)


def banner_detail(request, id):
    banner = models.Banner.objects.get(id=id)
    context = {
        'banner':banner
    }
    return render(request, 'dashboard/banner/detail.html', context)


def banner_edit(request, id):
    banner = models.Banner.objects.get(id=id)
    if request.method == 'POST':
        banner.title = request.POST['title']
        banner.body = request.POST['body']
        banner.save()
        return redirect('banner_detail', banner.id)
    context = {
        'banner':banner
    }
    return render(request, 'dashboard/banner/edit.html', context)


def banner_delete(request, id):
    models.Banner.objects.get(id=id).delete()
    return redirect('list_banner')






# Service
def create_service(request):
    if request.method == "POST":
        name = request.POST['name']
        body = request.POST['body']
        models.Service.objects.create(
            name=name,
            body=body,
        )
    return render(request, 'dashboard/service/create.html')


def list_service(request):
    services = models.Service.objects.all()
    context = {
        'services':services
    }
    return render(request, 'dashboard/service/list.html', context)


def service_detail(request, id):
    service = models.Service.objects.get(id=id)
    context = {
        'service':service
    }
    return render(request, 'dashboard/service/detail.html', context)


def service_edit(request, id):
    service = models.Service.objects.get(id=id)
    if request.method == 'POST':
        service.name = request.POST['name']
        service.body = request.POST['body']
        service.save()
        return redirect('service_detail', service.id)
    context = {
        'service':service
    }
    return render(request, 'dashboard/service/edit.html', context)


def service_delete(request, id):
    models.Service.objects.get(id=id).delete()
    return redirect('list_service')






# AboutUs
def create_aboutus(request):
    if request.method == "POST":
        body = request.POST['body']
        models.AboutUs.objects.create(
            body=body,
        )
    return render(request, 'dashboard/aboutus/create.html')


def list_aboutus(request):
    abouts = models.AboutUs.objects.all()
    context = {
        'abouts':abouts
    }
    return render(request, 'dashboard/aboutus/list.html', context)


def aboutus_detail(request, id):
    aboutus = models.AboutUs.objects.get(id=id)
    context = {
        'aboutus':aboutus
    }
    return render(request, 'dashboard/aboutus/detail.html', context)


def aboutus_edit(request, id):
    aboutus = models.AboutUs.objects.get(id=id)
    if request.method == 'POST':
        aboutus.body = request.POST['body']
        aboutus.save()
        return redirect('aboutus_detail', aboutus.id)
    context = {
        'aboutus':aboutus
    }
    return render(request, 'dashboard/aboutus/edit.html', context)


def aboutus_delete(request, id):
    models.AboutUs.objects.get(id=id).delete()
    return redirect('list_aboutus')






# Price
def create_price(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        models.Price.objects.create(
            title=title,
            body=body,
        )
    return render(request, 'dashboard/price/create.html')


def list_price(request):
    prices = models.Price.objects.all()
    context = {
        'prices':prices
    }
    return render(request, 'dashboard/price/list.html', context)


def price_detail(request, id):
    price = models.Price.objects.get(id=id)
    context = {
        'price':price
    }
    return render(request, 'dashboard/price/detail.html', context)


def price_edit(request, id):
    price = models.Price.objects.get(id=id)
    if request.method == 'POST':
        price.title = request.POST['title']
        price.body = request.POST['body']
        price.save()
        return redirect('price_detail', price.id)
    context = {
        'price':price
    }
    return render(request, 'dashboard/price/edit.html', context)


def price_delete(request, id):
    models.Price.objects.get(id=id).delete()
    return redirect('list_price')




# Contact
def list_contact(request):
    contacts = models.Contact.objects.all()
    context = {
        'contacts':contacts
    }
    return render(request, 'dashboard/contact/list.html', context)


def contact_detail(request, id):
    contact = models.Contact.objects.get(id=id)
    context = {
        'contact':contact
    }
    return render(request, 'dashboard/contact/detail.html', context)


def contact_edit(request, id):
    contact = models.Contact.objects.get(id=id)
    if request.method == 'POST':
        contact.is_show = request.POST['is_show']
        contact.body = request.POST['body']
        contact.save()
        return redirect('contact_detail', contact.id)
    context = {
        'contact':contact
    }
    return render(request, 'dashboard/contact/edit.html', context)


def contact_delete(request, id):
    models.Contact.objects.get(id=id).delete()
    return redirect('list_contact')