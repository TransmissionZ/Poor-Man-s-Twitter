# Generated by Django 3.2.5 on 2021-07-24 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poormans_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='dt',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
