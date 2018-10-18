# Generated by Django 2.1.2 on 2018-10-03 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tourist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='댓글')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourist.ReView', verbose_name='후기')),
            ],
        ),
        migrations.CreateModel(
            name='SpotMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='spotvisit',
            name='ts',
        ),
        migrations.RemoveField(
            model_name='spotvisit',
            name='user',
        ),
        migrations.RemoveField(
            model_name='touristspot',
            name='visit_user_set',
        ),
        migrations.DeleteModel(
            name='SpotVisit',
        ),
        migrations.AddField(
            model_name='spotmark',
            name='ts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mark_set', to='tourist.TouristSpot'),
        ),
        migrations.AddField(
            model_name='spotmark',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='touristspot',
            name='mark_user_set',
            field=models.ManyToManyField(blank=True, related_name='ts_mark_user_set', through='tourist.SpotMark', to=settings.AUTH_USER_MODEL),
        ),
    ]