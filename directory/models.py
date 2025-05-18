from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    school_grade = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    enrollment_status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Parent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='parents')
    parent_id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True, null=True)
    workplace = models.CharField(max_length=100, blank=True, null=True)
    relationship = models.CharField(max_length=50, blank=True, null=True, help_text="e.g., Mother, Father, Guardian")

    def __str__(self):
        return f"{self.relationship}: {self.name} (for {self.student.name})"

# class alergies(models.Model):