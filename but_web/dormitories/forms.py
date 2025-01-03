from django import forms
from .models import StudentDormitory


class StudentDormitoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentDormitoryForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = StudentDormitory
        fields = '__all__'
