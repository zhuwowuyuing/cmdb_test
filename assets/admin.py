from django.contrib import admin
from assets.models import Status, Servers

# Register your models here.
# class DeviceAdmin(admin.ModelAdmin):
#     list_display = ('asset', 'asset_old', 'district', 'company', 'type', 'subtype', 'manufacturer', 'model', 'serialno')
#     list_filter = ('asset',)
#     search_fields = ('asset',)
#
# class ServerAdmin(admin.ModelAdmin):
#     list_display = ('asset', 'size', 'cpu', 'harddisk', 'ram', 'os')
#     list_filter = ('asset',)
#     search_fields = ('asset',)
#
# class UsingInfoAdmin(admin.ModelAdmin):
#     list_display = ('asset', 'status', 'building', 'location', 'consignee', 'hostname', 'dept', 'business', 'ownername')
#     list_filter = ('asset',)
#     search_fields = ('asset',)
#
# class FinanceAdmin(admin.ModelAdmin):
#     list_display = ('asset', 'purchase_date', 'purchase_cost', 'accounting_date', 'account_cost', 'vendor')
#     list_filter = ('asset',)
#     search_fields = ('asset',)
#
# class ManInfoAdmin(admin.ModelAdmin):
#     list_display = ('asset', 'administrator')
#     list_filter = ('asset',)
#     search_fields = ('asset',)

# admin.site.register(Device, DeviceAdmin)
# admin.site.register(Server, ServerAdmin)
# admin.site.register(UsingInfo, UsingInfoAdmin)
# admin.site.register(Finance, FinanceAdmin)
# admin.site.register(ManInfo, ManInfoAdmin)
admin.site.register(Status)
admin.site.register(Servers)








