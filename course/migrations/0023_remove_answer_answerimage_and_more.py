# Generated by Django 4.0.4 on 2022-08-10 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0022_remove_question_is_correct_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answerImage',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='answer_explaination',
        ),
    ]