from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ['owner']


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['owner', 'town', 'address']
    readonly_fields = ['id', 'created_at']
    list_display = [
        'address', 'price', 'new_building', 'construction_year', 'town',
    ]
    list_editable = ['new_building']
    list_filter = ['rooms_number', 'has_balcony', 'new_building']
    raw_id_fields = ['liked_by']
    inlines = [OwnerInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats_owned']
