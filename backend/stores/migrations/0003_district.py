# Generated by Django 2.2.7 on 2020-10-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_auto_20201003_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sido', models.CharField(default=False, max_length=20)),
                ('gugun', models.CharField(default=False, max_length=20)),
                ('dong', models.CharField(default=False, max_length=20)),
            ],
        ),
    ]