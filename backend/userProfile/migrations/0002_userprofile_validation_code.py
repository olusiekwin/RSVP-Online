# Generated by Django 5.0.4 on 2024-04-18 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='validation_code',
            field=models.CharField(default='hftrg&dhdywezvxddjdd', editable=False, max_length=50),
        ),
    ]
