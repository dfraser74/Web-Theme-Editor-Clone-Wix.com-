# Generated by Django 2.2.1 on 2019-05-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20190514_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumedb',
            name='Type',
            field=models.CharField(default='Resume', max_length=50),
        ),
    ]