# Generated by Django 3.0.6 on 2020-05-29 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20200528_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_image',
            field=models.FileField(blank=True, default='default-avatar.png', null=True, upload_to='pics/'),
        ),
    ]
