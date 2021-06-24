from django.contrib import admin
from django.db.models import F

from .models import Patient, PatientCureHistory


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'mobile', 'father_name', 'date_of_birth')

@admin.register(PatientCureHistory)
class PatientCureHistoryAdmin(admin.ModelAdmin):
    list_display=('id', 'disease', 'cure', 'cure_date','patient', 'age')


    readonly_fields = ('age',)



# Register your models here.
