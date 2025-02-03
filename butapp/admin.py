from django.contrib import admin
from .models import StudentDormitory, Image
from django.contrib.auth.models import Group, User
from . import models


class ImageAdmin(admin.TabularInline):
    model = Image
    extra = 1



class StudentDormitoryAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'student_code',
        'nation_code',
        'status',
        'grade',
        'field',
        'gender',
        'but__name',
        'date',
    )
    search_fields = (
        'first_name',
        'last_name',
        'student_code',
        'nation_code',
        'nation_code',
        'mobile_number',
        'parent_mobile_number',
    )
    list_filter = (
        'status',
        'gender',
        'grade',
        'field',
        'date',
    )
    list_display_links = (
         'first_name',
        'last_name',
        'student_code',
        'nation_code',
        'status',
        'grade',
        'field',
        'gender',
        'but__name',
        'date',
    )
    ordering = ('-date',)  # Orders by most recent date first




class ButAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'len_member', 'gender_type')
    search_fields = ('name', 'len_member', 'gender_type')
    list_display_links = ('name', 'len_member', 'gender_type')
    inlines = [ImageAdmin]

class CapacityAdmin(admin.ModelAdmin):
    list_display = ('number','but__name')
    list_display_links = ('number','but__name')



admin.site.register(models.But, ButAdmin)
admin.site.register(models.HomePageImage)
admin.site.register(models.CapacityBut, CapacityAdmin)
admin.site.register(StudentDormitory, StudentDormitoryAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)