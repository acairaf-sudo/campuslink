import csv
from django.core.management.base import BaseCommand
from directory.models import Parents, Students

class Command(BaseCommand):
    help = 'Imports parent data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file containing parent data')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        try:
            with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        student_id_str = row.get('student_id')

                        if student_id_str and student_id_str.lower() != 'none':
                            try:
                                student_id = int(student_id_str)
                                student = Students.objects.get(pk=student_id)
                                parent_data = {
                                    'student': student,
                                    'relationship': row.get('Relationship'),
                                    'name': row.get('name'),
                                    'phone': row.get('phone'),
                                    'email': row.get('email'),
                                    'profession': row.get('profession'),
                                    'workplace': row.get('workplace'),
                                }
                                parent = Parents.objects.create(**{k: v for k, v in parent_data.items() if v is not None})
                                self.stdout.write(self.style.SUCCESS(f"Successfully imported parent for student ID {student_id}: {parent.name} ({parent.relationship})"))
                            except ValueError:
                                self.stdout.write(self.style.ERROR(f"Invalid student_id format: '{student_id_str}'. Skipping parent row: {row}"))
                            except Students.DoesNotExist:
                                self.stdout.write(self.style.ERROR(f"Student with ID '{student_id_str}' not found. Skipping parent row: {row}"))
                        else:
                            self.stdout.write(self.style.ERROR(f"Missing or invalid student_id: '{student_id_str}'. Skipping parent row: {row}"))

                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"Error importing parent row: {row} - {e}"))

                self.stdout.write(self.style.SUCCESS('Parent data import completed successfully!'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Error: CSV file not found at {csv_file_path}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An unexpected error occurred: {e}"))