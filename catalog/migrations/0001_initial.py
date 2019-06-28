# Generated by Django 2.2.2 on 2019-06-24 17:45

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(help_text='Enter name of book', max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('author', models.CharField(help_text='Enter name of author', max_length=25)),
                ('url', models.URLField()),
                ('description', models.CharField(help_text='Enter brief description for book', max_length=144)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
