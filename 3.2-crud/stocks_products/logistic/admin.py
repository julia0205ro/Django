from django.contrib import admin

from logistic.models import Product, Stock, StockProduct
# Register your models here.


class StockProductInline(admin.TabularInline):
    model = StockProduct
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # inlines = (StockProductInline,)
    pass


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    inlines = (StockProductInline,)
