# Generated by Django 4.2.4 on 2023-09-04 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=50)),
                ('event_description', models.TextField()),
                ('pic', models.FileField(blank=True, null=True, upload_to='media/images')),
                ('video', models.FileField(blank=True, null=True, upload_to='media/video')),
            ],
        ),
    ]