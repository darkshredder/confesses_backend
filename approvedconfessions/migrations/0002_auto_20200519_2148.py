# Generated by Django 3.0.6 on 2020-05-19 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('approvedconfessions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='approvedconfessions',
            old_name='your_confession',
            new_name='confession',
        ),
    ]
