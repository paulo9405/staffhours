# Generated by Django 4.0.2 on 2022-02-22 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_point_entrance'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='left',
            field=models.TimeField(null=True),
        ),
    ]