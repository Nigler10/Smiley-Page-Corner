from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "base_price",
        "is_available",
        "created_at",
    )
    list_filter = ("category", "is_available")
    search_fields = ("name", "description")
    list_editable = ("is_available",)
    readonly_fields = ("created_at",)

    fieldsets = (
        ("Basic Info", {
            "fields": ("name", "description", "category")
        }),
        ("Pricing & Availability", {
            "fields": ("base_price", "is_available")
        }),
        ("Media", {
            "fields": ("image",)
        }),
        ("Metadata", {
            "fields": ("created_at",)
        }),
    )
