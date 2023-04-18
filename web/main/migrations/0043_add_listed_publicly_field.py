# Generated by Django 3.2.18 on 2023-04-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_legaldocument_indexes'),
    ]

    operations = [
        migrations.AddField(
            model_name='casebook',
            name='listed_publicly',
            field=models.BooleanField(db_index=True, default=True, help_text='Whether the casebook, when published, is available in public listings such as H2O search or search engine indexes.'),
        ),
        migrations.AddField(
            model_name='historicalcasebook',
            name='listed_publicly',
            field=models.BooleanField(db_index=True, default=True, help_text='Whether the casebook, when published, is available in public listings such as H2O search or search engine indexes.'),
        ),
    ]
