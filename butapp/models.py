from django.db import models
from django_jalali.db import models as jalali_models


class Gender(models.TextChoices):
    male = 'male', 'پسرونه'
    female = 'female', 'دخترونه'


class But(models.Model):
    name = models.CharField(max_length=100, verbose_name='اسم')
    address = models.TextField(verbose_name='آدرس')
    len_member = models.IntegerField(verbose_name='ظرفیت')
    gender_type = models.CharField(max_length=20, choices=Gender.choices, default=Gender.female, verbose_name='جنسیت')
    description = models.TextField(default='', verbose_name='توضیحات')

    class Meta:
        verbose_name_plural = 'خوابگاه ها'
        verbose_name = 'خوابگاه'

    def __str__(self):
        if self.gender_type == Gender.female:
            return f'{self.name}----- دخترونه'
        elif self.gender_type == Gender.male:
            return f'{self.name}----- پسرونه'
        return f'{self.name}----- نامشخص'


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    but = models.ForeignKey(But, on_delete=models.CASCADE)


class StudentDormitory(models.Model):
    class Status(models.TextChoices):
        in_progress = 'در حال بررسی', 'در حال بررسی'
        rejected = 'رد شده', 'رد شده'
        confirm = 'تایید شده', 'تایید شده'

    but = models.ForeignKey(But, on_delete=models.CASCADE, null=True, blank=True , verbose_name='خوابگاه')
    first_name = models.CharField(max_length=100, verbose_name='اسم')
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    student_code = models.CharField(max_length=20, verbose_name='شماره دانشجویی')
    mobile_number = models.CharField(max_length=20, verbose_name='شماره تلفن')
    parent_mobile_number = models.CharField(max_length=20, verbose_name='شماره تلفن والدین')
    nation_code = models.CharField(max_length=20, verbose_name='شماره ملی', unique=True)
    grade = models.IntegerField(verbose_name='سال ورودی')
    field = models.CharField(max_length=100, verbose_name='رشته')
    location = models.CharField(max_length=100, verbose_name='شهر سکونت فرد')
    gender = models.CharField(max_length=20, choices=Gender.choices, default=Gender.female)
    status = models.CharField(choices=Status.choices, default=Status.in_progress, max_length=20,
                              verbose_name='وضعیت')
    date = jalali_models.jDateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'فرم خوابگاه'
        verbose_name = 'فرم خوابگاه'
