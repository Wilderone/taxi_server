# Generated by Django 3.0.7 on 2020-06-24 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_auto_20200624_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='vin',
            field=models.CharField(max_length=20, null=True),
        ),
    ]