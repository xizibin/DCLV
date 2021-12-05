# Generated by Django 3.2 on 2021-11-17 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fhir', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosticreportmodel',
            name='service_identifier',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fhir.servicerequestmodel'),
        ),
        migrations.AlterField(
            model_name='proceduremodel',
            name='service_identifier',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fhir.servicerequestmodel'),
        ),
        migrations.AlterField(
            model_name='servicerequestmodel',
            name='service_status',
            field=models.CharField(choices=[('draft', 'Nháp'), ('active', 'Đang hoạt động'), ('on-hold', 'Tạm giữ'), ('revoked', 'Đã thu hồi'), ('completed', 'Hoàn tất'), ('entered-in-error', 'Nhập sai'), ('unknown', 'Không xác định')], default='active', max_length=100),
        ),
    ]