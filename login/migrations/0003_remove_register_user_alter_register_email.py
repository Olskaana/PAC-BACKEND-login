# Generated by Django 5.0.6 on 2024-06-28 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_register_email_alter_register_municipio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='user',
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]