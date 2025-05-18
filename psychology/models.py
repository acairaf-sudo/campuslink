from django.db import models
from directory.models import Student # Importa el modelo Student de tu otra app

class Case(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='psychology_cases')  # Conecta un caso a un estudiante
    start_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True, null=True) # General notes about the case

    def __str__(self):
        return f"Case for {self.student.name} - {self.start_date}"

class Diagnostic(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='diagnostics')
    diagnostic_date = models.DateField()
    report_date = models.DateField(blank=True, null=True)
    diagnosis = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Diagnostic: {self.diagnosis} - {self.diagnostic_date}"


class FollowUp(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='followups')
    followup_date = models.DateField()
    summary = models.TextField()
    observations = models.TextField(blank=True, null=True)
    # Agregando campos de Strategy a FollowUp
    strategy_date = models.DateField(auto_now_add=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Follow-up: {self.followup_date}"