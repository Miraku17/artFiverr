# Generated by Django 4.2.10 on 2024-02-17 03:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='appUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.IntegerField(blank=True, choices=[(0, 'Customer'), (1, 'Artist'), (2, 'Admin')], default=0, null=True)),
                ('instagram', models.CharField(blank=True, max_length=25)),
                ('facebook', models.CharField(blank=True, max_length=25)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]