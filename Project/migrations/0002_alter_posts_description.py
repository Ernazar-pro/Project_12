# Generated by Django 4.2.7 on 2023-11-18 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]