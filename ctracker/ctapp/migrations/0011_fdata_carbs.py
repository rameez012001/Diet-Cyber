# Generated by Django 4.0.5 on 2022-10-31 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctapp', '0010_alter_rcal_rcal'),
    ]

    operations = [
        migrations.AddField(
            model_name='fdata',
            name='carbs',
            field=models.FloatField(blank=True, default=None),
            preserve_default=False,
        ),
    ]
