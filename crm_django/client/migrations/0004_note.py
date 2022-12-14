# Generated by Django 3.2 on 2022-08-23 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_initial'),
        ('client', '0003_client_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField(blank=True, null=True)),
                ('associated_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='team.team')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='client.client')),
            ],
        ),
    ]
