from .models import Student
from collections import defaultdict
from .constants import DESIRED_GRADE_ORDER
from django.db.models import When, Value, IntegerField, Case
from collections import OrderedDict
from .forms import StudentForm, ParentForm
from django.shortcuts import render, redirect, get_object_or_404


order_cases = [
    When(school_grade=grade, then=Value(i)) for i, grade in enumerate(DESIRED_GRADE_ORDER)
]


def index(request):
    students_list_dict = defaultdict(list)
    all_students = Student.objects.all().annotate(
        grade_order=Case(*order_cases, default=Value(len(DESIRED_GRADE_ORDER)), output_field=IntegerField())
    ).order_by('grade_order')
    for student in all_students:
        students_list_dict[student.school_grade].append(student)
    # Order the dictionary keys based on DESIRED_GRADE_ORDER
    ordered_students_list = OrderedDict()
    for grade in DESIRED_GRADE_ORDER:
        if grade in students_list_dict:
            ordered_students_list[grade] = students_list_dict[grade]
    # Add any remaining grades not in the desired order (optional)
    for grade, students in students_list_dict.items():
        if grade not in ordered_students_list:
            ordered_students_list[grade] = students

    context = {'students_list': ordered_students_list}
    return render(request, 'index.html', context)


def students_parents(request):
    students_with_parents = Student.objects.all().annotate(
        grade_order=Case(*order_cases, default=Value(len(DESIRED_GRADE_ORDER)), output_field=IntegerField())
    ).order_by('grade_order').prefetch_related('parents')
    context = {'students_with_parents': students_with_parents}
    return render(request, 'student_parent.html', context)


def add_students(request):
    submitted = False
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/directory/add_students/?submitted=True')
        else:
            print("Form is NOT valid")
            print(form.errors)
    else:
        form = StudentForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_students.html', {'form': form, 'submitted': submitted})


def add_parent(request):
    submitted = False
    if request.method == "POST":
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            # Assuming your Parent model has a ForeignKey to Student named 'student'
            return redirect(f'/directory/student/{form.cleaned_data["student"].id}/parents/?added=True')
        else:
            print("Parent form is NOT valid")
            print(form.errors)
    else:
        form = ParentForm()
    return render(request, 'add_parent.html', {'form': form, 'submitted': submitted})
