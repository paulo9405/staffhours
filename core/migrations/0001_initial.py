# Generated by Django 4.0.2 on 2022-02-21 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=100)),
            ],
        ),
    ]
