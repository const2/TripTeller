# Generated by Django 2.1.2 on 2018-10-03 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0005_auto_20181003_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewlike',
            old_name='ts',
            new_name='review',
        ),
    ]