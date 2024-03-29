# Generated by Django 2.2.7 on 2020-10-03 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.RenameField(
            model_name='store',
            old_name='address',
            new_name='address1',
        ),
        migrations.RenameField(
            model_name='store',
            old_name='store_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='store',
            old_name='latitude',
            new_name='pos_x',
        ),
        migrations.RenameField(
            model_name='store',
            old_name='longitude',
            new_name='pos_y',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='store',
            name='area',
        ),
        migrations.RemoveField(
            model_name='store',
            name='branch',
        ),
        migrations.AddField(
            model_name='hotel',
            name='pos_x',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='pos_y',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='address2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='category',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
