# Generated by Django 3.0.5 on 2021-11-24 14:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PractitionerModel',
            fields=[
                ('identifier', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('birthdate', models.DateField(default=datetime.datetime.now)),
                ('gender', models.CharField(choices=[('Nam', 'Nam'), ('Nữ', 'Nữ')], max_length=3)),
                ('home_address', models.CharField(max_length=255)),
                ('telecom', models.CharField(max_length=10)),
                ('practitioner_role', models.CharField(choices=[('doctor', 'Bác sĩ'), ('surgeon', 'Bác sĩ phẫu thuật'), ('medical assistant', 'Trợ lý y tế'), ('medical laboratory technician', 'Kỹ thuật viên phòng thí nghiệm y tế'), ('X-ray technician', 'Kỹ thuật viên X-quang'), ('ultrasound technician', 'Kỹ thuật viên siêu âm'), ('nurse', 'Y tá')], default='doctor', max_length=100)),
                ('qualification', models.CharField(max_length=100)),
            ],
        ),
    ]
