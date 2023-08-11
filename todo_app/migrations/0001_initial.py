# Generated by Django 4.2.3 on 2023-08-11 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=150)),
                ('task_description', models.CharField(max_length=300)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
