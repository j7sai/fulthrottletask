# Generated by Django 3.0.4 on 2020-06-05 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activityperiodsapp', '0003_auto_20200605_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
