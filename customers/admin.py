from django.contrib import admin
from . models import Customer

@admin.register(Customer)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('id', 'tc_no', 'name', 'surname', 'phone', 'city', 'district')
    list_filter = ('id', 'tc_no', 'name', 'surname', 'phone', 'city', 'district')
    search_fields = ('id', 'tc_no', 'name', 'surname', 'phone', 'city', 'district')