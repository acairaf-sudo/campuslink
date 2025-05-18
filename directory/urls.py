from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index_directory'),  # Lista principal de estudiantes
    path('add_students/', views.add_students, name='add_students'),
    path('add_parent/', views.add_parent, name='add_parent'),
    path('students-parents/', views.students_parents, name='student_parent_list'),  # Nueva URL para la lista de todos los estudiantes con padres
    path('student/<int:student_id>/parents/', views.students_parents, name='student_parents'),  # Lista de padres para un estudiante específico
]