# Generated by Django 4.2.6 on 2023-11-04 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_alter_skills_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valuation',
            name='title',
            field=models.CharField(max_length=250, unique=True, verbose_name='Заголовок'),
        ),
    ]
