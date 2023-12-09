# Generated by Django 4.2.6 on 2023-11-01 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0048_applicant'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeatAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=255)),
                ('due_time', models.DateTimeField()),
                ('available_seats', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Applicant',
        ),
        migrations.DeleteModel(
            name='ImportantNotice',
        ),
    ]
