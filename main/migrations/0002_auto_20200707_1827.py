# Generated by Django 3.0.4 on 2020-07-07 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='tutorial_cublished',
            new_name='tutorial_published',
        ),
    ]