# Generated by Django 4.2.2 on 2023-06-21 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_questions', '0009_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('options', models.TextField()),
                ('correct_answer', models.CharField(max_length=255)),
                ('concept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty_questions.concept')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty_questions.subject')),
            ],
            options={
                'db_table': 'question',
            },
        ),
    ]
