# Generated by Django 5.1 on 2024-11-27 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asgns', '0018_remove_user_academic_session_delete_academic_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_reviewer',
            field=models.BooleanField(default=False),
        ),
    ]