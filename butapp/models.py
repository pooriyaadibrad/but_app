from django.db import models
from django_jalali.db import models as jalali_models
from django.db.models import Q

class Gender(models.TextChoices):
    male = 'پسرونه', 'پسرونه'
    female = 'دخترونه', 'دخترونه'


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

    def remaining_capacity(self):
        accepted_requests = self.requests.filter(
            status='درخواست قبول شده : وضعیت درخواست ثبت نام شما در مرحله قبول شده می‌باشد ، لطفا در زمان اعلامی از طرف دانشگاه نسبت به نهایی کردن ثبت نام خود اقدام نمایید').count()
        return self.len_member - accepted_requests


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    but = models.ForeignKey(But, on_delete=models.CASCADE, related_name='photos')


class StudentDormitory(models.Model):
    class Status(models.TextChoices):
        in_progress = 'درخواست در حال بررسی : درخواست ثبت نام شما در حال بررسی می‌باشد ، لطفا تا زمان بررسی درخواست شکیبا باشید', 'در حال بررسی'
        rejected = 'درخواست رد شده : درخواست شما از طرف کارشناس امور خوابگاه ها رد شده است ، جهت پیگیری در تایم اداری با شماره ۰۱۱۴۴۴۴۲۱۳۵ با داخلی ۱۴۹ تماس حاصل فرمایید', 'رد شده'
        confirm = 'درخواست قبول شده : وضعیت درخواست ثبت نام شما در مرحله قبول شده می‌باشد ، لطفا در زمان اعلامی از طرف دانشگاه نسبت به نهایی کردن ثبت نام خود اقدام نمایید', 'تایید شده'

    but = models.ForeignKey(But, on_delete=models.CASCADE, null=True, blank=True, verbose_name='خوابگاه',
                            related_name="requests")
    first_name = models.CharField(max_length=100, verbose_name='اسم')
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    student_code = models.CharField(max_length=20, verbose_name='شماره دانشجویی')
    mobile_number = models.CharField(max_length=20, verbose_name='شماره تلفن')
    parent_mobile_number = models.CharField(max_length=20, verbose_name='شماره تلفن والدین')
    nation_code = models.CharField(max_length=20, verbose_name='شماره ملی', unique=True)
    grade = models.IntegerField(verbose_name='سال ورودی')
    field = models.CharField(max_length=100, verbose_name='رشته')
    location = models.CharField(max_length=100, verbose_name='شهر سکونت فرد')
    gender = models.CharField(max_length=20, choices=Gender.choices, default=Gender.female, verbose_name='جنسیت')
    status = models.CharField(choices=Status.choices, default=Status.in_progress, max_length=200,
                              verbose_name='وضعیت')
    date = jalali_models.jDateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'فرم خوابگاه'
        verbose_name = 'فرم خوابگاه'

    def save(self, *args, **kwargs):
        but = But.objects.all()
        for item in but:
            student_req = StudentDormitory.objects.filter(Q(but=item)&
                                                          Q(status=StudentDormitory.Status.confirm)).all()

            capa = CapacityBut.objects.get(but=item)
            capa.number = int(item.len_member) - int(student_req.count())
            capa.save()

        super().save(*args, **kwargs)



class HomePageImage(models.Model):
    image = models.ImageField(upload_to='images/Home', verbose_name='عکس')

    def __str__(self):
        return 'عکس های صفحه اصلی خوابگاه'

    class Meta:
        verbose_name_plural = 'عکس های صفحه اصلی خوابگاه'
        verbose_name = 'عکس های صفحه اصلی خوابگاه'


class CapacityBut(models.Model):
    number = models.IntegerField(default=0, verbose_name='تعداد ظرفیت بافی مانده')
    but = models.ForeignKey(But, on_delete=models.CASCADE, related_name='capacity')

    class Meta:
        verbose_name_plural = 'ظرفیت باقی مانده هر خوابگاه'
        verbose_name = 'ظرفیت باقی مانده هر خوابگاه'
