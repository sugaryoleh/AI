from django.contrib import admin

from diseases.models import *

admin.site.register(Customer)
admin.site.register(Doctor)
admin.site.register(Disease)
admin.site.register(DiseaseHistory)
admin.site.register(Symptom)
admin.site.register(Speciality)