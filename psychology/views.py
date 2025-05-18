from .forms import CaseForm, DiagnosticForm, FollowUpForm
from .models import Case, Diagnostic, FollowUp
from directory.models import Student
from django.shortcuts import render, redirect, get_object_or_404


def psychology(request):
    return render(request, 'psychology.html')


def create_case(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('psychology:create_case:home') # Assuming 'home' URL in psychology app
    else:
        form = CaseForm()
    return render(request, 'create_case.html', {'form': form}) # Changed template path


def create_diagnostic(request, case_id):
    case = get_object_or_404(Case, pk=case_id)
    if request.method == 'POST':
        form = DiagnosticForm(request.POST)
        if form.is_valid():
            diagnostic = form.save(commit=False)
            diagnostic.case = case
            diagnostic.save()
            return redirect('psychology:case_detail', case_id=case.id)
    else:
        form = DiagnosticForm(initial={'case': case})
    return render(request, 'create_diagnostic.html', {'form': form, 'case': case})


def create_followup(request, case_id):
    case = get_object_or_404(Case, pk=case_id)
    if request.method == 'POST':
        form = FollowUpForm(request.POST)
        if form.is_valid():
            followup = form.save(commit=False)
            followup.case = case
            followup.save()
            return redirect('psychology:case_detail', case_id=case.id)
    else:
        form = FollowUpForm(initial={'case': case})
    return render(request, 'create_followup.html', {'form': form, 'case': case})


def create_case_for_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            case = form.save(commit=False)
            case.student = student
            case.save()
            return redirect('psychology:student_cases', student_id=student.id)
    else:
        form = CaseForm(initial={'student': student})
    return render(request, 'create_case.html', {'form': form, 'student': student})