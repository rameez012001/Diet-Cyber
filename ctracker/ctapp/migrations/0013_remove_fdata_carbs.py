# Generated by Django 4.0.5 on 2022-10-31 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctapp', '0012_alter_fdata_carbs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fdata',
            name='carbs',
        ),
    ]
