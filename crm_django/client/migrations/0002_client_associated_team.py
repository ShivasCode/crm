# Generated by Django 3.2 on 2022-08-23 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='associated_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='team.team'),
        ),
    ]
