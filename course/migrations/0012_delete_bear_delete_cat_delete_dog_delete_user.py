# Generated by Django 4.0.4 on 2022-07-22 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_alter_user_content_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bear',
        ),
        migrations.DeleteModel(
            name='Cat',
        ),
        migrations.DeleteModel(
            name='Dog',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
