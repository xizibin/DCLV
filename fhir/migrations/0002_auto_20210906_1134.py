# Generated by Django 3.2 on 2021-09-06 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fhir', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication_medication', models.CharField(max_length=100)),
                ('medication_reasonCode', models.CharField(max_length=100)),
                ('medication_effective', models.CharField(max_length=100)),
                ('medication_dosage', models.CharField(max_length=100)),
                ('encounter_identifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fhir.encountermodel')),
            ],
        ),
        migrations.RenameField(
            model_name='allergymodel',
            old_name='allergy_status',
            new_name='allergy_clinical_status',
        ),
        migrations.RenameField(
            model_name='allergymodel',
            old_name='patient_id',
            new_name='patient_identifier',
        ),
        migrations.AddField(
            model_name='allergymodel',
            name='allergy_last_occurrence',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='allergymodel',
            name='allergy_onset',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='allergymodel',
            name='allergy_reaction',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='proceduremodel',
            name='procecure_identifier',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='proceduremodel',
            name='procedure_bodySite',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='proceduremodel',
            name='procedure_complication',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='proceduremodel',
            name='procedure_focalDevice',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='proceduremodel',
            name='procedure_followUp',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='proceduremodel',
            name='procedure_note',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proceduremodel',
            name='procedure_category',
            field=models.CharField(choices=[('22642003', 'Phương pháp hoặc dịch vụ tâm thần'), ('409063005', 'Tư vấn'), ('409073007', 'Giáo dục'), ('387713003', 'Phẫu thuật'), ('103693007', 'Chuẩn đoán'), ('46947000', 'Phương pháp chỉnh hình'), ('410606002', 'Phương pháp dịch vụ xã hội')], max_length=100),
        ),
        migrations.DeleteModel(
            name='MedicineModel',
        ),
    ]