# Generated by Django 4.2.4 on 2023-08-23 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_chairman_pic_socity_member_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_title', models.CharField(max_length=50)),
                ('notice_description', models.TextField()),
                ('pic', models.FileField(blank=True, null=True, upload_to='media/images')),
                ('video', models.FileField(blank=True, null=True, upload_to='media/video')),
            ],
        ),
    ]
