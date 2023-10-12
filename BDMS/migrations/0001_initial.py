# Generated by Django 4.0.1 on 2022-01-26 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IFSC', models.CharField(blank=True, max_length=10, null=True)),
                ('Bname', models.CharField(blank=True, max_length=200, null=True)),
                ('Bpin', models.CharField(blank=True, max_length=6, null=True)),
                ('Address', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cname', models.CharField(blank=True, max_length=200, null=True)),
                ('AccNumber', models.CharField(blank=True, max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CName', models.CharField(blank=True, max_length=200, null=True)),
                ('CardNo', models.CharField(blank=True, max_length=16, null=True)),
                ('Expiry', models.CharField(blank=True, max_length=8, null=True)),
                ('AccNumber', models.CharField(blank=True, max_length=16, null=True)),
                ('CVV', models.CharField(blank=True, max_length=3, null=True)),
                ('IFSC', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cname', models.CharField(blank=True, max_length=200, null=True)),
                ('IFSC', models.CharField(blank=True, max_length=10, null=True)),
                ('AccNumber', models.CharField(blank=True, max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccType', models.CharField(blank=True, max_length=200, null=True)),
                ('Balance', models.CharField(blank=True, max_length=200, null=True)),
                ('AccNo', models.CharField(blank=True, max_length=200, null=True)),
                ('CName', models.CharField(blank=True, max_length=200, null=True)),
                ('IFSC', models.CharField(blank=True, max_length=200, null=True)),
                ('PhoneNo', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Loanid', models.CharField(blank=True, max_length=15, null=True)),
                ('Loantype', models.CharField(blank=True, max_length=200, null=True)),
                ('Lamount', models.CharField(blank=True, max_length=20, null=True)),
                ('AccNumber', models.CharField(blank=True, max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aadhar', models.CharField(blank=True, max_length=12, null=True)),
                ('Cname', models.CharField(blank=True, max_length=200, null=True)),
                ('Cid', models.CharField(blank=True, max_length=5, null=True)),
                ('Phone', models.CharField(blank=True, max_length=10, null=True)),
                ('Caddress', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
