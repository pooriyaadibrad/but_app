from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from butapp.models import But, StudentDormitory, HomePageImage, CapacityBut, Image
from django.contrib import messages


def index(request):
    buts = But.objects.prefetch_related('photos').all()

    home = HomePageImage.objects.all().order_by('-id')[0:3]
    if len(list(home)) != 3:
        return HttpResponse(
            '<h1>برای لود شدن صفحه اصلی حداقل ۳ عکس برای خوابگاه های صفحه اصلی اضافه کنید از پنل ادمین</h1>')
    return render(request, 'homepage.html', {'buts': buts, 'home': home})


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        nation_code = request.POST.get('nation_code')
        phone = request.POST.get('phone')
        grade = request.POST.get('grade')
        field = request.POST.get('field')
        but = request.POST.get('but')
        parent = request.POST.get('parent')
        location = request.POST.get('location')
        student_code = request.POST.get('student_code')
        but = But.objects.get(name=but)

        StudentDormitory.objects.create(first_name=first_name, last_name=last_name,
                                        nation_code=nation_code, mobile_number=phone,
                                        grade=grade, but=but, parent_mobile_number=parent, location=location,
                                        field=field, student_code=student_code, gender=but.gender_type)
        messages.success(request, 'درخواست شما با موفقیت ثبت شد')
        return redirect('register_')
    buts = But.objects.values_list('name', 'gender_type')
    return render(request, 'request-khabgah.html', {'buts': buts})


def follow(request):
    if request.method == 'POST':
        nation_code = request.POST.get('nation_code')
        student_code = request.POST.get('student_code')
        student = StudentDormitory.objects.filter(
            Q(student_code=student_code) | Q(nation_code=nation_code)).values_list('status').all()
        return render(request, 'follow_request.html', {'student': student})
    return render(request, 'follow_request.html')


def detail(request, but_id):
    but = But.objects.get(id=but_id)
    images = Image.objects.filter(but=but)
    print(images)
    remaining_capacity = CapacityBut.objects.get(id=but.id)
    return render(request, 'detail.html', {'but': but, 'remaining_capacity': remaining_capacity, 'images': images})
