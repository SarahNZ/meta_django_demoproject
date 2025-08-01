# Generated by Django 5.2.3 on 2025-07-18 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_person_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('time_log', models.TimeField(help_text='Enter the exact time')),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
