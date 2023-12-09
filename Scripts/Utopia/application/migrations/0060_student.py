# Generated by Django 4.2.6 on 2023-11-01 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0059_rename_userimagefile_usersprimarydetails_userimagefilename'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]