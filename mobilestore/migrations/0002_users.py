# Generated by Django 3.1.7 on 2021-08-13 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobilestore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=20)),
                ('u_pass', models.CharField(max_length=20)),
                ('u_email', models.EmailField(max_length=254)),
            ],
        ),
    ]