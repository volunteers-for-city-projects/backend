# Generated by Django 4.2.6 on 2023-11-05 01:31

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_projectparticipants_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='date_of_birth',
            field=models.DateField(help_text='Введите дату в формате "ГГГГ-ММ-ДД", пример: "2000-01-01".', validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(1900, 1, 1)), django.core.validators.MaxValueValidator(limit_value=datetime.date(2023, 11, 5))], verbose_name='Дата рождения'),
        ),
    ]
