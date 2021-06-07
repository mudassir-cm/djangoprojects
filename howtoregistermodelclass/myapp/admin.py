from django.contrib import admin
from .models import Student

@admin.register(Student)                  #### ye use kro ya ye   admin.site.register(Student, StudentAdmin)
class StudentAdmin(admin.ModelAdmin):
  list_display=('id',)                          ##### single fields representation
  list_display=('id', 'phone', 'name', 'city')  ##### multiple fields representaions


# Register your models here.
