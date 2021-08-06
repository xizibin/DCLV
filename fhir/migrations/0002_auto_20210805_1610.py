# Generated by Django 3.2 on 2021-08-05 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fhir', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conditionmodel',
            name='condition_severity',
            field=models.CharField(choices=[('Nặng', 'Nặng'), ('Vừa', 'Vừa'), ('Nhẹ', 'Nhẹ')], max_length=100),
        ),
        migrations.AlterField(
            model_name='encountermodel',
            name='encounter_class',
            field=models.CharField(choices=[('Nội trú', 'Nội trú'), ('Ambulatory', 'Ambulatory'), ('Khám tại địa điểm ngoài', 'Khám tại địa điểm ngoài'), ('Khẩn cấp', 'Khẩn cấp'), ('Khám tại nhà', 'Khám tại nhà'), ('Nội trú khẩn cấp', 'Nội trú khẩn cấp'), ('Nội trú không khẩn cấp', 'Nội trú không khẩn cấp'), ('Thăm khám quan sát', 'Thăm khám quan sát'), ('Ngoại trú', 'Ngoại trú'), ('Trực tuyến', 'Trực tuyến'), ('Tái khám', 'Tái khám')], default='AMB', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='encountermodel',
            name='encounter_location',
            field=models.CharField(choices=[('1', 'Khoa Khám bệnh'), ('2', 'Khoa Hồi sức cấp cứu'), ('3', 'Khoa Nội tổng hợp'), ('4', 'Khoa Nội tổng hợp'), ('5', 'Khoa Nội tiêu hóa'), ('6', 'Khoa Nội - tiết niệu'), ('7', 'Khoa Nội tiết'), ('8', 'Khoa Nội cơ - xương - khớp'), ('9', 'Khoa Nội tiết'), ('10', 'Khoa Dị ứng'), ('11', 'Khoa Huyết học lâm sàng'), ('12', 'Khoa Truyền nhiễm'), ('13', 'Khoa Lao'), ('14', 'Khoa Tâm thần'), ('15', 'Khoa Thần kinh')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='encountermodel',
            name='encounter_priority',
            field=models.CharField(choices=[('A', 'ASAP'), ('EL', 'Tự chọn'), ('EM', 'Khẩn cấp'), ('P', 'Trước'), ('R', 'Bình thường'), ('S', 'Star')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='encountermodel',
            name='encounter_reason',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='encountermodel',
            name='encounter_service',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='encountermodel',
            name='encounter_type',
            field=models.CharField(choices=[('1', 'Bệnh án nội khoa'), ('2', 'Bệnh án ngoại khoa'), ('3', 'Bệnh án phụ khoa'), ('4', 'Bệnh án sản khoa')], default='', max_length=100, null=True),
        ),
    ]