# Generated by Django 4.2.5 on 2023-10-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0040_news_totalview_news_viewdonelist_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicOpinions',
            fields=[
                ('OpinionID', models.AutoField(primary_key=True, serialize=False)),
                ('Opinion', models.TextField()),
            ],
        ),
    ]
