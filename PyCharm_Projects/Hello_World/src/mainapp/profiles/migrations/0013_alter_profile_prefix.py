# Generated by Django 4.1 on 2022-08-19 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_alter_profile_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Prefix',
            field=models.CharField(choices=[('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Mr', 'Mr')], default='', max_length=10),
        ),
    ]
