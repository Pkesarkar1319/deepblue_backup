# Generated by Django 3.1.8 on 2022-01-18 05:36

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220105_1537'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='signup',
            managers=[
                ('empAuth_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='signup',
            name='role',
            field=models.CharField(default='Candidate', max_length=10),
        ),
    ]