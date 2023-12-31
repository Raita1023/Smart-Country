# Generated by Django 4.2.5 on 2023-10-06 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0029_countryministries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ministerprimarydetails',
            name='MinisterID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='application.politiciansprimarydetails'),
        ),
        migrations.AlterField(
            model_name='ministerprimarydetails',
            name='MinistryName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.countryministries'),
        ),
    ]
