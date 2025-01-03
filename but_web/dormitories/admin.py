from django.contrib import admin
from .models import StudentDormitory
from django.contrib.auth.models import User, Group


class StudentDormitoryAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'student_code', 'mobile_number', 'parent_mobile_number', 'nation_code', 'grade',
        'field',
        'location')
    search_fields = (
        'first_name', 'last_name', 'student_code', 'mobile_number', 'parent_mobile_number', 'nation_code', 'grade',
        'field',
        'location')
    list_display_links = (
        'first_name', 'last_name', 'student_code', 'mobile_number', 'parent_mobile_number', 'nation_code', 'grade',
        'field',
        'location')

admin.site.register(StudentDormitory, StudentDormitoryAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)