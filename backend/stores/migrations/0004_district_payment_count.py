# Generated by Django 2.2.7 on 2020-10-05 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='payment_count',
            field=models.BigIntegerField(default=False, max_length=20),
        ),
    ]
