# Generated by Django 4.2.6 on 2023-11-04 19:47

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import projects.validators


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_merge_20231104_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectparticipants',
            name='project',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='projects.project',
            ),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='date_of_birth',
            field=models.DateField(
                help_text='Введите дату в формате "ГГГГ-ММ-ДД", пример: "2000-01-01".',
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=datetime.date(1900, 1, 1)
                    ),
                    django.core.validators.MaxValueValidator(
                        limit_value=datetime.date(2023, 11, 4)
                    ),
                ],
                verbose_name='Дата рождения',
            ),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='telegram',
            field=models.CharField(
                blank=True,
                max_length=32,
                validators=[projects.validators.validate_telegram],
            ),
        ),
    ]
