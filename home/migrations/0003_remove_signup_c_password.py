# Generated by Django 3.1.8 on 2022-01-05 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_signup_captcha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='c_password',
        ),
    ]