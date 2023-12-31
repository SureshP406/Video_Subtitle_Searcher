# Generated by Django 4.1 on 2023-12-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_file', models.FileField(upload_to='videos/')),
                ('subtitles', models.TextField(blank=True, null=True)),
                ('processed_file', models.FileField(blank=True, null=True, upload_to='processed_videos/')),
                ('start_time', models.CharField(max_length=10)),
                ('end_time', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
                'db_table': 'video_video',
            },
        ),
    ]
