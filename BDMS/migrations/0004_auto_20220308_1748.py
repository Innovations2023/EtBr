# Generated by Django 3.1.8 on 2022-03-08 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BDMS', '0003_auto_20220207_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='project',
            name='Username',
        ),
        migrations.RemoveField(
            model_name='test',
            name='MAC_ID',
        ),
        migrations.AddField(
            model_name='project',
            name='Age',
            field=models.CharField(default=20, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='MAC_ID',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='PhoneNo',
            field=models.CharField(default=7639748329, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='Profile_Pic',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='MAC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MAC_ID', models.CharField(blank=True, max_length=17, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='test',
            name='mac_id',
            field=models.ForeignKey(default=1212122112, on_delete=django.db.models.deletion.CASCADE, to='BDMS.mac'),
            preserve_default=False,
        ),
    ]
