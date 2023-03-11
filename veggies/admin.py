from django.contrib import admin
from .models import Veggie, Offer

# Register your models here.
class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class VeggieAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

admin.site.register(Offer, OfferAdmin)
admin.site.register(Veggie, VeggieAdmin)
