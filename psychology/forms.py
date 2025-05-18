from django import forms
from .models import Case, Diagnostic, FollowUp

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['student', 'is_active', 'notes']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}), # Optional widget customization
        }

class DiagnosticForm(forms.ModelForm):
    class Meta:
        model = Diagnostic
        fields = ['case', 'diagnostic_date', 'report_date', 'diagnosis', 'notes']
        widgets = {
            'diagnostic_date': forms.DateInput(attrs={'type': 'date'}),
            'report_date': forms.DateInput(attrs={'type': 'date'}),
        }

class FollowUpForm(forms.ModelForm):
    class Meta:
        model = FollowUp
        fields = ['case', 'followup_date', 'summary', 'observations', 'description']
        widgets = {
            'followup_date': forms.DateInput(attrs={'type': 'date'}),
        }