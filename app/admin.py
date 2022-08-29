from django.contrib import admin
from .models import Pictures, Customer, SoldPictures, Order


class PicturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cost')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_address', 'customer_city')


class SoldPicturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_id', 'picture_id')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'picture', 'customer', 'order_description',
                    'created_date', 'last_updated_date', 'order_status')


admin.site.register(Pictures, PicturesAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(SoldPictures, SoldPicturesAdmin)
admin.site.register(Order, OrderAdmin)
