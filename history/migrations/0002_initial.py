# Generated by Django 4.2.13 on 2024-08-03 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('history', '0001_initial'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tags.tag'),
        ),
    ]
