# Generated by Django 3.1.7 on 2021-04-21 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulting_system', '0002_profession'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profession',
        ),
        migrations.RemoveField(
            model_name='value',
            name='ability',
        ),
        migrations.RemoveField(
            model_name='value',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Ability',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Value',
        ),
    ]
