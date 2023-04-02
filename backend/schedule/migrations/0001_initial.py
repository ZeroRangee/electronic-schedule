# Generated by Django 4.1.7 on 2023-03-27 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=70, verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='LessonSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.CharField(max_length=70, verbose_name='Название предмета')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='TimeSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=30, verbose_name='Время')),
            ],
            options={
                'verbose_name': 'Время',
                'verbose_name_plural': 'Время',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='schedule.groupschedule')),
                ('lessons', models.ManyToManyField(to='schedule.lessonschedule')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='schedule.timeschedule')),
            ],
            options={
                'verbose_name': 'Раписание группы',
                'verbose_name_plural': 'Раписание групп',
            },
        ),
    ]
