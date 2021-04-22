import diseases
from diseases.models import Symptom


class Disease:
    def __init__(self, diesease, symptoms):
        self.disease = diesease
        self.symptoms = symptoms

def get_diseases():
        d = []
        #----------------------
        vals = [20,10,10,30,30]
        symptoms = []
        symptoms.append(Symptom.objects.get(pk=1))
        symptoms.append(Symptom.objects.get(pk=2))
        symptoms.append(Symptom.objects.get(pk=5))
        symptoms.append(Symptom.objects.get(pk=8))
        symptoms.append(Symptom.objects.get(pk=17))
        disease = diseases.models.Disease.objects.get(pk=1)
        d.append(Disease(disease, dict(zip(symptoms, vals))))
        #----------------------
        vals = [20,20,10,20,30]
        symptoms = []
        symptoms.append(Symptom.objects.get(pk=2))
        symptoms.append(Symptom.objects.get(pk=6))
        symptoms.append(Symptom.objects.get(pk=5))
        symptoms.append(Symptom.objects.get(pk=8))
        symptoms.append(Symptom.objects.get(pk=16))
        disease = diseases.models.Disease.objects.get(pk=2)
        d.append(Disease(disease, dict(zip(symptoms, vals))))
        #----------------------
        vals = [40,10,10,10,30]
        symptoms = []
        symptoms.append(Symptom.objects.get(pk=1))
        symptoms.append(Symptom.objects.get(pk=4))
        symptoms.append(Symptom.objects.get(pk=6))
        symptoms.append(Symptom.objects.get(pk=7))
        symptoms.append(Symptom.objects.get(pk=11))
        disease = diseases.models.Disease.objects.get(pk=3)
        d.append(Disease(disease, dict(zip(symptoms, vals))))
        #----------------------
        vals = [10,40,10,10,30]
        symptoms = []
        symptoms.append(Symptom.objects.get(pk=11))
        symptoms.append(Symptom.objects.get(pk=12))
        symptoms.append(Symptom.objects.get(pk=13))
        symptoms.append(Symptom.objects.get(pk=14))
        symptoms.append(Symptom.objects.get(pk=16))
        disease = diseases.models.Disease.objects.get(pk=4)
        d.append(Disease(disease, dict(zip(symptoms, vals))))
        #----------------------
        vals = [25,25,10,15,25]
        symptoms = []
        symptoms.append(Symptom.objects.get(pk=7))
        symptoms.append(Symptom.objects.get(pk=2))
        symptoms.append(Symptom.objects.get(pk=8))
        symptoms.append(Symptom.objects.get(pk=4))
        symptoms.append(Symptom.objects.get(pk=11))
        disease = diseases.models.Disease.objects.get(pk=5)
        d.append(Disease(disease, dict(zip(symptoms, vals))))
        #----------------------
        vals = [15,15,15,15,40]
        symptoms = []
        symptoms.append(Symptom.objects.get(pk=4))
        symptoms.append(Symptom.objects.get(pk=11))
        symptoms.append(Symptom.objects.get(pk=12))
        symptoms.append(Symptom.objects.get(pk=16))
        symptoms.append(Symptom.objects.get(pk=16))
        symptoms.append(Symptom.objects.get(pk=7))
        disease = diseases.models.Disease.objects.get(pk=6)
        d.append(Disease(disease, dict(zip(symptoms, vals))))
        #----------------------
        vals = [10,10,25,20,35]
        symptoms = []
        symptoms.append(Symptom.objects.get(pk=2))
        symptoms.append(Symptom.objects.get(pk=4))
        symptoms.append(Symptom.objects.get(pk=6))
        symptoms.append(Symptom.objects.get(pk=8))
        symptoms.append(Symptom.objects.get(pk=10))
        disease = diseases.models.Disease.objects.get(pk=7)
        d.append(Disease(disease, dict(zip(symptoms, vals))))
        return d
