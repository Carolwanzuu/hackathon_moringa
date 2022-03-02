# Generated by Django 4.0.2 on 2022-03-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0003_alter_new_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new_user',
            old_name='password1',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='new_user',
            name='password2',
        ),
        migrations.RemoveField(
            model_name='new_user',
            name='username',
        ),
        migrations.AddField(
            model_name='new_user',
            name='age',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
