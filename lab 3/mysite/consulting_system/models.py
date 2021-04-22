from django.db.models import FloatField, CharField, Model

class Candidate(Model):
    name = CharField(max_length=30)
    a1 = FloatField()
    a2 = FloatField()
    a3 = FloatField()
    a4 = FloatField()
    a5 = FloatField()
    a6 = FloatField()
    a7 = FloatField()
    a8 = FloatField()
    a9 = FloatField()
    a10 = FloatField()