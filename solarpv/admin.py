from django.contrib import admin
from .models import Profile, Product, Certificate, Service, Location, Client, PerformanceData, TestSequence, TestStandard


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'frame_type')
    ordering = ('product_name',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_number', 'issue_date')
    ordering = ('certificate_number',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name',)
    ordering = ('service_name',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'address1', 'state', 'phone_number')
    ordering = ('client_id',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_type')
    ordering = ('client_name',)

@admin.register(PerformanceData)
class PerformanceDataAdmin(admin.ModelAdmin):
    list_display = ('model_number', 'sequence_id')
    ordering = ('model_number',)

@admin.register(TestSequence)
class TestSequenceAdmin(admin.ModelAdmin):
    list_display = ('sequence_name',)
    ordering = ('sequence_name',)

@admin.register(TestStandard)
class TestStandardAdmin(admin.ModelAdmin):
    list_display = ('standard_name', 'published_date')
    ordering = ('standard_name',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
