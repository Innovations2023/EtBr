# Generated by Django 3.2.11 on 2022-04-01 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BDMS', '0005_auto_20220331_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='mac_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='MAC',
        ),
    ]