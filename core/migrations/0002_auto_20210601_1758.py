# Generated by Django 3.1.1 on 2021-06-01 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='create_user',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='update_user',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='create_user',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='update_user',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='create_user',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='update_user',
            field=models.UUIDField(editable=False, null=True),
        ),
    ]
