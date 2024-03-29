# Generated by Django 5.0 on 2024-01-03 14:38

import django.db.models.deletion
import phone_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_status', models.CharField(max_length=100)),
                ('patient_code', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Patient_Details',
                'ordering': ['-patient_status'],
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('patient_surname', models.CharField(max_length=100)),
                ('patient_address', models.CharField(max_length=100)),
                ('patient_number', phone_field.models.PhoneField(help_text='Contact phone number', max_length=31, unique=True)),
                ('patient_description', models.CharField(max_length=100)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Patients.patient_status')),
            ],
            options={
                'db_table': 'Patient_list',
                'ordering': ['-patient_name'],
            },
        ),
    ]
