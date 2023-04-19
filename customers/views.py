from django.shortcuts import render , get_object_or_404 , redirect
from . models import Customer
from . forms import CustomerForm
from django.views.generic.list import ListView
import uuid
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class CustomerListView(ListView):
    model = Customer
    template_name = 'pages/index.html'
    context_object_name = 'customers'
    ordering = '-created_at'
    paginate_by = 25

    def get_paginate_by(self, queryset):
        page_size = self.request.GET.get('page_size')
        if page_size:
            return int(page_size)
        return self.paginate_by
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_size'] = self.request.GET.get('page_size')
        return context


@login_required
def edit_customer(request, id):
    if not request.user.groups.filter(name='yetkili').exists():
        messages.error(request, 'Bu sayfaya erişim yetkiniz bulunmamaktadır.')
        return redirect('index')

    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
    else:
        form = CustomerForm(instance=customer)

    context = {
        'form': form,
        'customer': customer,
    }
    return render(request, 'pages/edit_customers.html', context)

def search(request):
    query = request.GET.get('search')
    if query:
        customers = Customer.objects.filter(id__icontains=query) | \
                    Customer.objects.filter(name__icontains=query) | \
                    Customer.objects.filter(surname__icontains=query) | \
                    Customer.objects.filter(tc_no__icontains=query) | \
                    Customer.objects.filter(phone__icontains=query) | \
                    Customer.objects.filter(city__icontains=query) | \
                    Customer.objects.filter(district__icontains=query)
    else:
        customers = Customer.objects.all()

    return render(request, 'pages/index.html', {'customers': customers, 'search': query})

@login_required
def create_customer(request):
    if not request.user.groups.filter(name='yetkili').exists():
        messages.error(request, 'Bu sayfaya erişim yetkiniz bulunmamaktadır.')
        return redirect('index')
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['id'] = uuid.uuid4()
            customer = Customer(**cleaned_data)
            customer.save()
            return redirect('index')
        else:
            messages.error(request, 'Lütfen formu doğru şekilde doldurunuz.')
    else:
        form = CustomerForm()
    context = {
        'form': form
    }
    return render(request, 'pages/form.html', context)

def delete_customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == 'POST':
        customer.delete()
        messages.success(request, 'Müşteri başarıyla silindi.')
        return redirect('index')
    return render(request, 'pages/delete_customer.html', {'customer': customer})