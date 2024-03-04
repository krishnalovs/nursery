from django.contrib import admin
from .models import *


class AdminNavbar(admin.ModelAdmin):
    list_display = ('name', 'slug')
    readonly_fields = ('slug',)
    verbose_name = "Navbar"


class AdminCategory(admin.ModelAdmin):
    list_display = ('navbar', 'name', 'slug')
    readonly_fields = ('slug',)
    verbose_name = "Category"


class AdminSubCategory(admin.ModelAdmin):
    list_display = ('category', 'name', 'slug')
    verbose_name = "SubCategory"
    readonly_fields = ('slug',)


class AdminItem(admin.ModelAdmin):
    list_display = ('navbar', 'category', 'subcategory', 'name', 'slug')
    readonly_fields = ('slug',)
    verbose_name = "Items"


# Register your models here.
admin.site.register(Navbar, AdminNavbar)
admin.site.register(Category, AdminCategory)
admin.site.register(SubCategory, AdminSubCategory)
admin.site.register(Items, AdminItem)
admin.site.register(UserProfile)
admin.site.register(Cart)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(Subscribe)