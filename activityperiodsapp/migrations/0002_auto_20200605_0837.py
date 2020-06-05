# Generated by Django 3.0.4 on 2020-06-05 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activityperiodsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activityperiod',
            name='activity_periods',
        ),
        migrations.AddField(
            model_name='activityperiod',
            name='activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='activityperiodsapp.User'),
        ),
    ]