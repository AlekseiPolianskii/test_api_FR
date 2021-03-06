# Generated by Django 2.2.10 on 2021-12-21 10:04

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('surveyapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerquestion',
            name='question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='surveyapp.Question', verbose_name='Вопрос'),
        ),
        migrations.AddField(
            model_name='answeruser',
            name='survey',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='surveyapp.Survey', verbose_name='Опрос'),
        ),
        migrations.AlterField(
            model_name='answeruser',
            name='answer',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='surveyapp.AnswerQuestion', verbose_name='Вариант ответа'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='date_to_finish',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 24, 10, 4, 18, 19284, tzinfo=utc), verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='date_to_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 21, 10, 4, 18, 19270, tzinfo=utc), verbose_name='Дата старта'),
        ),
    ]
