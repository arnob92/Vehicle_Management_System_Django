# Generated by Django 5.0.3 on 2024-03-30 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_department_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('vehicle_type', models.CharField(max_length=100)),
                ('cause', models.IntegerField(default=0)),
                ('reason', models.TextField()),
                ('req_status', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('driver_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.driver')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.teacher')),
                ('vehicle_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.vehicle')),
            ],
        ),
    ]
