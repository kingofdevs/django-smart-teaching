# Generated by Django 2.1.3 on 2018-12-08 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_auto_20181208_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_exams',
            name='avg_marks',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='marks',
            name='q_name',
            field=models.CharField(max_length=50),
        ),
    ]
