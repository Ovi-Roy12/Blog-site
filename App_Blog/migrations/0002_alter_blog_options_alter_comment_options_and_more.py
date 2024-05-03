# Generated by Django 4.2.4 on 2023-11-17 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-publish_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-comment_date',)},
        ),
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
        migrations.AlterField(
            model_name='blog',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
