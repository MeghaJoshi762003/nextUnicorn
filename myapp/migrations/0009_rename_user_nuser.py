# Generated by Django 4.1.2 on 2022-10-30 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_user_bio_alter_user_facebook_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='nuser',
        ),
    ]