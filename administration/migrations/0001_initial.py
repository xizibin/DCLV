# Generated by Django 3.2 on 2021-12-15 17:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalDepartment',
            fields=[
                ('department_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('department_category', models.CharField(max_length=100)),
                ('department_type', models.CharField(choices=[('lâm sàng', 'Lâm sàng'), ('cận lâm sàng', 'Cận lâm sàng')], default='lâm sàng', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PractitionerModel',
            fields=[
                ('identifier', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('birthdate', models.DateField(default=datetime.datetime.now)),
                ('gender', models.CharField(choices=[('Nam', 'Nam'), ('Nữ', 'Nữ')], max_length=3)),
                ('home_address', models.CharField(max_length=255)),
                ('telecom', models.CharField(max_length=10)),
                ('practitioner_role', models.CharField(choices=[('doctor', 'Bác sĩ'), ('surgeon', 'Bác sĩ phẫu thuật'), ('medical assistant', 'Trợ lý y tế'), ('medical laboratory technician', 'Kỹ thuật viên phòng thí nghiệm y tế'), ('diagnostic imaging technican', 'Kỹ thuật viên chẩn đoán hình ảnh'), ('nurse', 'Y tá')], default='doctor', max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.clinicaldepartment')),
            ],
        ),
    ]