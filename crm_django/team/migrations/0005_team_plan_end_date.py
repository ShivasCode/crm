# Generated by Django 3.2 on 2022-08-27 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20220825_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='plan_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
