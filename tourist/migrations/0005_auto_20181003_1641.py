# Generated by Django 2.1.2 on 2018-10-03 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0004_auto_20181003_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotmark',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
