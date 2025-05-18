from django import forms
from django.forms import ModelForm
from .models import Student, Parent

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'school_grade', 'birth_date', 'enrollment_status')


class ParentForm(ModelForm):
    class Meta:
        model = Parent
        fields = ('student', 'name', 'phone', 'email', 'profession', 'workplace', 'relationship')