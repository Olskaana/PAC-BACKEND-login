# Generated by Django 5.0.6 on 2024-06-28 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_remove_register_user_alter_register_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='municipio',
        ),
    ]