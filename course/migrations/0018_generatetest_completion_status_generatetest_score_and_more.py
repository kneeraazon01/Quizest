# Generated by Django 4.0.4 on 2022-07-27 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0017_question_explaination_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='generatetest',
            name='completion_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='generatetest',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='generatetest',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='UserQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField(default=False)),
                ('is_incorrect', models.BooleanField(default=False)),
                ('is_unused', models.BooleanField(default=True)),
                ('is_marked', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='course.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TempUserQuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='course.answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='course.question')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='course.generatetest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]