# Generated by Django 4.2.6 on 2023-11-01 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0046_applicant_course_importantnotice_university_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationdeadline',
            name='course',
        ),
        migrations.RemoveField(
            model_name='applicationdeadline',
            name='university',
        ),
        migrations.DeleteModel(
            name='AdmissionDecision',
        ),
        migrations.DeleteModel(
            name='Applicant',
        ),
        migrations.DeleteModel(
            name='ApplicationDeadline',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='University',
        ),
    ]
