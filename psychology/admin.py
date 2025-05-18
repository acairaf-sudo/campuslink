from django.contrib import admin
from .models import Case, Diagnostic, FollowUp

admin.site.register(Case)
admin.site.register(Diagnostic) # Added report_date
admin.site.register(FollowUp) # Modified FollowUp