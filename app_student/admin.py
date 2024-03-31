from django.contrib import admin
from app_student.models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','mark_1','mark_2','mark_3','mark_4','mark_5','mark_6','mark_7')
    search_fields = ('name',)
    list_filter =('age','mark_1')

admin.site.register(Student, StudentAdmin)

# Register your models here.
