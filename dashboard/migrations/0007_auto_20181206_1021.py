# Generated by Django 2.1.3 on 2018-12-06 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20181206_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz_enrollments',
            name='quiz_name',
            field=models.CharField(max_length=50),
        ),
    ]
