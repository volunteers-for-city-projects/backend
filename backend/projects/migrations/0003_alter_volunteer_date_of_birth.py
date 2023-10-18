# Generated by Django 4.2.6 on 2023-10-18 12:01

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_organization_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='date_of_birth',
            field=models.DateField(help_text='Введите дату в формате "ДД.ММ.ГГГГ", пример: "01 01 2000".', validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(1900, 1, 1)), django.core.validators.MaxValueValidator(limit_value=datetime.date(2023, 10, 18))], verbose_name='Дата рождения'),
        ),
    ]
