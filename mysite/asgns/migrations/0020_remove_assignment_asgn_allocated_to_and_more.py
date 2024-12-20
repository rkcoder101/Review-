# Generated by Django 5.1 on 2024-12-08 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asgns', '0019_user_is_admin_user_is_reviewer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='asgn_allocated_to',
        ),
        migrations.CreateModel(
            name='Assignment_Allocated_to',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment', to='asgns.assignment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='asgns.user')),
            ],
        ),
    ]
