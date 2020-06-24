# Generated by Django 3.0.7 on 2020-06-24 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0003_car_vin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='to_history',
            old_name='car',
            new_name='car_to_history',
        ),
        migrations.AddField(
            model_name='car',
            name='certificate',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='car',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='taxi.Car', to_field='grz'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='to_type',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='to_history',
            unique_together={('car_to_history', 'to_type')},
        ),
    ]
