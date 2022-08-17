# Generated by Django 4.1 on 2022-08-15 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(blank=True, default='', max_length=20)),
                ('Last_name', models.CharField(blank=True, default='', max_length=20)),
                ('Email', models.CharField(blank=True, default='', max_length=50)),
                ('Username', models.CharField(blank=True, default='', max_length=50)),
            ],
        ),
    ]
