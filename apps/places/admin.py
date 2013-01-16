# coding: utf-8
from django.contrib import admin
from django import forms

from models import City, Clinic, Branch, Drugstore, Lab
from apps.utils.widgets import MapCity, MapObject


class CityAdminForm(forms.ModelForm):
    coordinates_center = forms.CharField(widget=MapCity(attrs={}),
                                         initial='37.619405,55.751173', label='центр координат')
    zoom = forms.CharField(initial='10', label='зум')

    class Meta:
        model = City

class CityAdmin(admin.ModelAdmin):
    form = CityAdminForm


class ClinicAdminForm(forms.ModelForm):
    coordinates = forms.CharField(widget=MapObject(attrs={}),
                                         initial='37.619405,55.751173', label='координаты')
    
    class Meta:
        model = Clinic

class ClinicAdmin(admin.ModelAdmin):
    form = ClinicAdminForm


class BranchAdminForm(forms.ModelForm):
    coordinates = forms.CharField(widget=MapObject(attrs={}),
                                         initial='37.619405,55.751173', label='координаты')
    
    class Meta:
        model = Branch

class BranchAdmin(admin.ModelAdmin):
    form = BranchAdminForm


class DrugstoreAdminForm(forms.ModelForm):
    coordinates = forms.CharField(widget=MapObject(attrs={}),
                                         initial='37.619405,55.751173', label='координаты')
    
    class Meta:
        model = Drugstore

class DrugstoreAdmin(admin.ModelAdmin):
    form = DrugstoreAdminForm


class LabAdminForm(forms.ModelForm):
    coordinates = forms.CharField(widget=MapObject(attrs={}),
                                         initial='37.619405,55.751173', label='координаты')
    
    class Meta:
        model = Lab

class LabAdmin(admin.ModelAdmin):
    form = LabAdminForm


admin.site.register(City, CityAdmin)
admin.site.register(Clinic, ClinicAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Drugstore, DrugstoreAdmin)
admin.site.register(Lab, LabAdmin)