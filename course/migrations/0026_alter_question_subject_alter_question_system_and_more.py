# Generated by Django 4.0.4 on 2022-08-10 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0025_alter_question_subject_alter_question_system_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='subject',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='course.subject'),
        ),
        migrations.AlterField(
            model_name='question',
            name='system',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='course.system'),
        ),
        migrations.AlterField(
            model_name='system',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='system', to='course.subject'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='course.system'),
        ),
    ]