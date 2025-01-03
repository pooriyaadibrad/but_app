from django.shortcuts import render, redirect
from .forms import StudentDormitoryForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = StudentDormitoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'ثبت موفق بود')
            return redirect('register')
        messages.success(request, 'در ثبت درخواست مشکلی پیش آمده لطفا فیلد های ورودی بررسی کنید')
        return redirect('register')
    form = StudentDormitoryForm()
    return render(request, 'registration.html', {'form': form})
