from django.db import models


class StudentDormitory(models.Model):
    first_name = models.CharField(max_length=100,verbose_name='اسم')
    last_name = models.CharField(max_length=100,verbose_name='نام خانوادگی')
    student_code = models.CharField(max_length=20,verbose_name='شماره دانشجویی')
    mobile_number = models.CharField(max_length=20,verbose_name='شماره تلفن')
    parent_mobile_number = models.CharField(max_length=20,verbose_name='شماره تلفن والدین')
    nation_code = models.CharField(max_length=20,verbose_name='شماره ملی')
    grade = models.IntegerField(verbose_name='سال ورودی')
    field = models.CharField(max_length=100,verbose_name='رشته')
    location = models.CharField(max_length=100,verbose_name='شهر سکونت فرد')

    class Meta:
        verbose_name_plural = 'فرم خوابگاه'
        verbose_name = 'فرم خوابگاه'
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


