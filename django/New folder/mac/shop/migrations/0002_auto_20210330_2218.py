# Generated by Django 3.1.7 on 2021-03-30 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='msg_id',
            new_name='msg',
        ),
    ]
