# Generated by Django 5.0.3 on 2024-04-01 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_requisition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisition',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
