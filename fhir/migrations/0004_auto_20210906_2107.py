# Generated by Django 3.2 on 2021-09-06 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fhir', '0003_auto_20210906_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceduremodel',
            name='procedure_asserter',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='proceduremodel',
            name='procedure_performder',
            field=models.CharField(max_length=100, null=True),
        ),
    ]