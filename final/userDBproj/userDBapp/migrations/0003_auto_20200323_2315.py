# Generated by Django 3.0.4 on 2020-03-24 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userDBapp', '0002_auto_20200323_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodtype',
            old_name='typeDscription',
            new_name='typeDescription',
        ),
    ]