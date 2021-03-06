from django.contrib import admin

from .models import (
    MasterList, MasterListService, MasterListGeo,
    MasterListContact)
from ml_setup.utils import dump_to_csv


class MasterListAdmin(admin.ModelAdmin):
    search_fields = ['code', 'name']
    list_display = ['code', 'name', 'approved']
    ordering = ('-timestamp_created',)

    list_filter = ['approved', 'is_void', 'timestamp_created']

    readonly_fields = ('code',)
    actions = [dump_to_csv]


admin.site.register(MasterList, MasterListAdmin)


class MasterListServiceAdmin(admin.ModelAdmin):
    search_fields = ['master_list']
    list_display = ['master_list', 'service']
    ordering = ('-timestamp_created',)

    list_filter = ['is_void', 'timestamp_created']
    actions = [dump_to_csv]


admin.site.register(MasterListService, MasterListServiceAdmin)


class MasterListGeoAdmin(admin.ModelAdmin):
    search_fields = ['master_list']
    list_display = ['master_list', 'county']
    ordering = ('-timestamp_created',)

    list_filter = ['is_void', 'timestamp_created']
    actions = [dump_to_csv]


admin.site.register(MasterListGeo, MasterListGeoAdmin)


class MasterListContactAdmin(admin.ModelAdmin):
    search_fields = ['master_list', 'contact_detail']
    list_display = ['master_list', 'contact_type', 'contact_detail']
    ordering = ('-timestamp_created',)

    list_filter = ['is_void', 'timestamp_created']
    actions = [dump_to_csv]


admin.site.register(MasterListContact, MasterListContactAdmin)
