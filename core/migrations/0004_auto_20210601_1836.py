# Generated by Django 3.1.1 on 2021-06-01 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210601_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
