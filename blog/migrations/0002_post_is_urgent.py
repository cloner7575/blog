# Generated by Django 5.1.3 on 2024-11-18 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_urgent',
            field=models.BooleanField(default=False, verbose_name='فوری'),
        ),
    ]
