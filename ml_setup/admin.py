from django.contrib import admin
from .models import (
    Listing, Regulator, ListGeneral, ServiceCategory, Service,
    TypeCategory, FacilityType, OwnerCategory, OwnerType,
    ListGeoCounty, ListGeoConstituency, ListGeoWard)
from .utils import dump_to_csv


class ListingAdmin(admin.ModelAdmin):
    search_fields = ['listing_name']
    list_display = ['listing_code', 'listing_name']
    ordering = ('-timestamp_created',)

    list_filter = ['is_void', 'timestamp_created']
    actions = [dump_to_csv]


admin.site.register(Listing, ListingAdmin)


class ServiceCategoryAdmin(admin.ModelAdmin):
    search_fields = ['category_abbr', 'category_name']
    list_display = ['id', 'category_name', 'category_abbr']
    ordering = ('-timestamp_created',)

    list_filter = ['is_void', 'timestamp_created']
    actions = [dump_to_csv]


admin.site.register(ServiceCategory, ServiceCategoryAdmin)


class ServiceAdmin(admin.ModelAdmin):
    search_fields = ['service_code', 'service_name']
    list_display = ['service_code', 'category', 'service_name', 'service_abbr']
    ordering = ('-timestamp_created', )

    list_filter = ['is_void', 'timestamp_created']
    actions = [dump_to_csv]


admin.site.register(Service, ServiceAdmin)


class TypeCategoryAdmin(admin.ModelAdmin):
    search_fields = ['type_category_abbr', 'type_category_name']
    list_display = ['id', 'type_category_abbr', 'type_category_name']
    ordering = ('-timestamp_created',)

    list_filter = ['is_void', 'timestamp_created']
    actions = [dump_to_csv]


admin.site.register(TypeCategory, TypeCategoryAdmin)


class FacilityTypeAdmin(admin.ModelAdmin):
    search_fields = ['facility_type_code', 'facility_type_name']
    list_display = ['facility_type_code', 'facility_type',
                    'facility_type_name', 'facility_type_abbr']
    ordering = ('-timestamp_created', )

    list_filter = ['is_void', 'timestamp_created']
    actions = [dump_to_csv]


admin.site.register(FacilityType, FacilityTypeAdmin)


class OwnerCategoryAdmin(admin.ModelAdmin):
    search_fields = ['owner_category_abbr', 'owner_category_name']
    list_display = ['id', 'owner_category_abbr', 'owner_category_name']
    ordering = ('-timestamp_created',)

    list_filter = ['is_void', 'timestamp_created']
    actions = [dump_to_csv]


admin.site.register(OwnerCategory, OwnerCategoryAdmin)


class OwnerTypeAdmin(admin.ModelAdmin):
    search_fields = ['owner_type_code', 'owner_type_name']
    list_display = ['owner_type_code', 'owner_type',
                    'owner_type_name', 'owner_type_abbr']
    ordering = ('-timestamp_created', )

    list_filter = ['is_void', 'timestamp_created']
    actions = [dump_to_csv]


admin.site.register(OwnerType, OwnerTypeAdmin)


class RegulatorAdmin(admin.ModelAdmin):
    search_fields = ['regulator_abbr', 'regulator_name']
    list_display = ['regulator_abbr', 'regulator_name', 'regulation_verb']
    ordering = ('-timestamp_created',)

    list_filter = ['is_void', 'timestamp_created']
    actions = [dump_to_csv]


admin.site.register(Regulator, RegulatorAdmin)


class ListGeneralAdmin(admin.ModelAdmin):
    """Register persons admin."""

    search_fields = ['item_id', 'item_category', 'item_description']
    list_display = ['item_id', 'item_category', 'item_description',
                    'the_order', 'timestamp_created', 'is_active']
    # readonly_fields = ['id']
    list_filter = ['is_active', 'timestamp_created', 'field_name']
    actions = [dump_to_csv]


admin.site.register(ListGeneral, ListGeneralAdmin)


class ListGeoCountyAdmin(admin.ModelAdmin):
    search_fields = ['county_code', 'county_name']
    list_display = ['id', 'county_name', 'county_code']
    ordering = ('-timestamp_created',)

    list_filter = ['is_void', 'timestamp_created']
    actions = [dump_to_csv]


admin.site.register(ListGeoCounty, ListGeoCountyAdmin)


class ListGeoConstituencyAdmin(admin.ModelAdmin):
    search_fields = ['constituency_code', 'constituency_name']
    list_display = ['id', 'constituency_name', 'constituency_code']
    ordering = ('-timestamp_created',)

    list_filter = ['is_void', 'timestamp_created']
    actions = [dump_to_csv]


admin.site.register(ListGeoConstituency, ListGeoConstituencyAdmin)


class ListGeoWardAdmin(admin.ModelAdmin):
    search_fields = ['ward_code', 'ward_name']
    list_display = ['id', 'ward_name', 'ward_code',
                    'constituency_name', 'county_name']
    ordering = ('-timestamp_created',)

    list_filter = ['is_void', 'timestamp_created']
    actions = [dump_to_csv]


admin.site.register(ListGeoWard, ListGeoWardAdmin)
