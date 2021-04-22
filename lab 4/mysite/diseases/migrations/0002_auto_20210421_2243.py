# Generated by Django 3.1.7 on 2021-04-22 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diseasehistory',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='diseasehistory',
            name='disease',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='speciality',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='user',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='DiseaseHistory',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]
