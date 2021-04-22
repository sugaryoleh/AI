from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, CharField, OneToOneField, CASCADE, ForeignKey, DateField


class Customer(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)

class Speciality(Model):
    name = CharField(max_length=30)

class Doctor(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    speciality = ForeignKey(Speciality, on_delete=CASCADE)

class Disease(Model):
    name = CharField(max_length=30)

class Symptom(Model):
    name = CharField(max_length=30)

class DiseaseHistory(Model):
    disease = ForeignKey(Disease, on_delete=CASCADE)
    customer = ForeignKey(Customer, on_delete=CASCADE)
    date = DateField()