# Generated by Django 4.2.6 on 2023-11-02 14:52

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import projects.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line', models.CharField(max_length=100, verbose_name='Адрес в одну строчку')),
                ('street', models.CharField(max_length=75, verbose_name='Улица')),
                ('house', models.CharField(max_length=5, verbose_name='Дом')),
                ('block', models.CharField(max_length=5, verbose_name='Корпус')),
                ('building', models.CharField(max_length=5, verbose_name='Строение')),
            ],
            options={
                'verbose_name': 'Адрес проекта',
                'verbose_name_plural': 'Адреса проектов',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, validators=[projects.validators.validate_title], verbose_name='Название')),
                ('ogrn', models.CharField(max_length=13, unique=True, validators=[projects.validators.validate_ogrn], verbose_name='ОГРН')),
                ('phone', models.CharField(max_length=12, validators=[projects.validators.validate_phone_number], verbose_name='Телефон')),
                ('about', models.TextField(blank=True, verbose_name='Об организации')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='Фото')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization', to='content.city', verbose_name='Город')),
                ('contact_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка')),
                ('start_datetime', models.DateTimeField(verbose_name='Дата и время, начало мероприятия')),
                ('end_datetime', models.DateTimeField(verbose_name='Дата и время, окончания мероприятия')),
                ('start_date_application', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время, начало подачи заявок')),
                ('end_date_application', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время, окончания подачи заявок')),
                ('event_purpose', models.TextField(verbose_name='Цель мероприятия')),
                ('project_tasks', models.TextField(verbose_name='Задачи проекта')),
                ('project_events', models.TextField(blank=True, verbose_name='Мероприятия на проекте')),
                ('organizer_provides', models.TextField(blank=True, verbose_name='Организатор предоставляет')),
                ('status_project', models.CharField(choices=[('open', 'Открыт'), ('ready_for_feedback', 'Готов к откликам'), ('reception_of_responses_closed', 'Прием откликов окончен'), ('project_completed', 'Проект завершен')], default='editing', max_length=100, verbose_name='Статус проекта')),
                ('photo_previous_event', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото с мероприятия')),
                ('status_approve', models.CharField(choices=[('approved', 'Одобрено'), ('editing', 'Черновик'), ('pending', 'На рассмотрении'), ('rejected', 'Отклонено'), ('canceled_by_organizer', 'Отменено организатором')], default='pending', max_length=50, verbose_name='Статус проверки')),
                ('categories', models.ManyToManyField(related_name='projects', to='projects.category', verbose_name='Категории')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='content.city', verbose_name='Город')),
                ('event_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.address', verbose_name='Адрес проведения проекта')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='projects.organization', verbose_name='Организация')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram', models.CharField(max_length=32, validators=[projects.validators.validate_telegram])),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='Фото')),
                ('date_of_birth', models.DateField(help_text='Введите дату в формате "ГГГГ.ММ.ДД", пример: "2000 01 01".', validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(1900, 1, 1)), django.core.validators.MaxValueValidator(limit_value=datetime.date(2023, 11, 2))], verbose_name='Дата рождения')),
                ('phone', models.CharField(blank=True, max_length=12, validators=[projects.validators.validate_phone_number], verbose_name='Телефон')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteers', to='content.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Волонтер',
                'verbose_name_plural': 'Волонтеры',
                'ordering': ['user__last_name'],
            },
        ),
        migrations.CreateModel(
            name='VolunteerSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.skills')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.volunteer')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.volunteer')),
            ],
        ),
        migrations.AddField(
            model_name='volunteer',
            name='skills',
            field=models.ManyToManyField(related_name='volunteers', through='projects.VolunteerSkills', to='content.skills', verbose_name='Навыки'),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='volunteers', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.CreateModel(
            name='ProjectSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.skills')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectParticipants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.volunteer')),
            ],
            options={
                'verbose_name': 'Участник проекта',
                'verbose_name_plural': 'Участники проекта',
                'default_related_name': 'projects_volunteers',
            },
        ),
        migrations.CreateModel(
            name='ProjectIncomes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_incomes', models.CharField(choices=[('application_submitted', 'Заявка подана'), ('rejected', 'Отклонена'), ('accepted', 'Принята')], default='application_submitted', max_length=100, verbose_name='Статус заявки волонтера')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Статус заявки волонтера')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_incomes', to='projects.project', verbose_name='Проект')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_incomes', to='projects.volunteer', verbose_name='Волонтер')),
            ],
            options={
                'verbose_name': 'Заявки волонтеров',
                'verbose_name_plural': 'Заявки волонтеров',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='participants',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='projects.projectparticipants', verbose_name='Участники'),
        ),
        migrations.AddField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='projects', through='projects.ProjectSkills', to='content.skills', verbose_name='Навыки'),
        ),
        migrations.AddConstraint(
            model_name='volunteerskills',
            constraint=models.UniqueConstraint(fields=('volunteer', 'skill'), name='unique_volunteer_skills'),
        ),
        migrations.AddConstraint(
            model_name='volunteerfavorite',
            constraint=models.UniqueConstraint(fields=('volunteer', 'project'), name='unique_volunteer_favorites'),
        ),
        migrations.AddConstraint(
            model_name='projectparticipants',
            constraint=models.UniqueConstraint(fields=('project', 'volunteer'), name='projectsprojectparticipants_unique_project_volunteer'),
        ),
        migrations.AddConstraint(
            model_name='projectincomes',
            constraint=models.UniqueConstraint(fields=('project', 'volunteer', 'status_incomes'), name='projectsprojectincomes_unique_project_volunteer'),
        ),
    ]
