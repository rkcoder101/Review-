# Generated by Django 5.1 on 2024-09-28 15:31

import django.contrib.postgres.fields
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asgns', '0005_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('date_of_assigning', models.DateField()),
                ('due_date', models.DateField()),
                ('asgn_allocated_to', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), size=None)),
            ],
        ),
        migrations.RemoveField(
            model_name='team',
            name='user_and_team',
        ),
        migrations.RemoveField(
            model_name='team',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='session_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_and_academic_session',
        ),
        migrations.AddField(
            model_name='team',
            name='user',
            field=models.ManyToManyField(related_name='teams', to='asgns.user'),
        ),
        migrations.AddField(
            model_name='user',
            name='academic_session',
            field=models.ManyToManyField(related_name='acad_session_of_user', to='asgns.academic_session'),
        ),
        migrations.AlterField(
            model_name='user',
            name='branch',
            field=models.CharField(choices=[('CSE', 'Computer Science'), ('DSAI', 'Data Science and Artificial Intelligence'), ('MNC', 'Mathematics and Computing'), ('ECE', 'Electronics and Communication'), ('EE', 'Electrical'), ('ME', 'Mechanical'), ('EPH', 'Engineering Physics'), ('CH', 'Chemical'), ('CE', 'Civil'), ('PNI', 'Production and Industrial'), ('MT', 'Metallurgy'), ('BSBE', 'Biosciences and Biotechnology'), ('BSMSCY', 'Chemical Sciences'), ('BSMSPY', 'Physics'), ('GPT', 'Geophysical Technology'), ('GT', 'Geological Technology')], default='CSE', max_length=6),
        ),
        migrations.AlterField(
            model_name='user',
            name='enrollment_number',
            field=models.CharField(max_length=8, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(8)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.CreateModel(
            name='Completed_Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_completion', models.DateTimeField()),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completed_assignments', to='asgns.assignment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completed_assignments', to='asgns.user')),
            ],
        ),
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewers', to='asgns.user')),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentReviewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewers', to='asgns.assignment')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='asgns.reviewer')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='assigner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asgns.reviewer'),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_date', models.DateTimeField()),
                ('comments', models.TextField(blank=True, null=True)),
                ('iteration_no', models.PositiveIntegerField()),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='asgns.assignment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='asgns.user')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_history', to='asgns.reviewer')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_history', to='asgns.submission')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('comments', models.TextField()),
                ('iteration_no', models.IntegerField()),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='asgns.assignment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_received', to='asgns.user')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_given', to='asgns.reviewer')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission_reviews', to='asgns.submission')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment_for_submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='attachments/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='asgns.submission')),
            ],
        ),
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('text', models.TextField()),
                ('asgn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_assignment', to='asgns.assignment')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='attachments/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('subtask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asgns.subtask')),
            ],
        ),
    ]