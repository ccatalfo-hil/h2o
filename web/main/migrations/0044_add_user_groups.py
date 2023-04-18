# Generated by Django 3.2.18 on 2023-04-18 18:17

from django.db import migrations
from django.contrib.auth.models import Group

from main.models import User


def create_user_groups(apps, schema_editor):
    Group.objects.get_or_create(name='Professor')
    Group.objects.get_or_create(name='Student')
    Group.objects.get_or_create(name='Librarian')
    Group.objects.get_or_create(name='Other')

def populate_professor_group(apps, schema_editor):
    professor = Group.objects.get(name='Professor')
    
    for prof in User.objects.filter(verified_professor=True):
        prof.groups.add(professor)

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_add_listed_publicly_field'),
    ]

    operations = [
        migrations.RunPython(create_user_groups),
        migrations.RunPython(populate_professor_group),
    ]
