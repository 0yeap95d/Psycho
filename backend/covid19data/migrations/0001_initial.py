# Generated by Django 2.2.7 on 2020-10-05 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Covid19GenAgeInfo',
            fields=[
                ('seq', models.IntegerField(primary_key=True, serialize=False)),
                ('createDt', models.DateTimeField(null=True)),
                ('gubun', models.CharField(max_length=200, null=True)),
                ('confCase', models.CharField(max_length=200, null=True)),
                ('confCaseRate', models.CharField(max_length=200, null=True)),
                ('death', models.CharField(max_length=200, null=True)),
                ('criticalRate', models.CharField(max_length=200, null=True)),
                ('deathRate', models.CharField(max_length=200, null=True)),
                ('updateDt', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Covid19Info',
            fields=[
                ('seq', models.IntegerField(primary_key=True, serialize=False)),
                ('stateDt', models.CharField(max_length=200, null=True)),
                ('stateTime', models.CharField(max_length=200, null=True)),
                ('createDt', models.DateTimeField(null=True)),
                ('accExamCnt', models.CharField(max_length=200, null=True)),
                ('examCnt', models.CharField(max_length=200, null=True)),
                ('accExamCompCnt', models.CharField(max_length=200, null=True)),
                ('resutlNegCnt', models.CharField(max_length=200, null=True)),
                ('decideCnt', models.CharField(max_length=200, null=True)),
                ('careCnt', models.CharField(max_length=200, null=True)),
                ('clearCnt', models.CharField(max_length=200, null=True)),
                ('accDefRate', models.CharField(max_length=200, null=True)),
                ('deathCnt', models.CharField(max_length=200, null=True)),
                ('updateDt', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Covid19SidoInfo',
            fields=[
                ('seq', models.IntegerField(primary_key=True, serialize=False)),
                ('stdDay', models.CharField(max_length=200, null=True)),
                ('createDt', models.DateTimeField(null=True)),
                ('gubun', models.CharField(max_length=200, null=True)),
                ('gubunCn', models.CharField(max_length=200, null=True)),
                ('gubunEn', models.CharField(max_length=200, null=True)),
                ('defCnt', models.CharField(max_length=200, null=True)),
                ('isolIngCnt', models.CharField(max_length=200, null=True)),
                ('isolClearCnt', models.CharField(max_length=200, null=True)),
                ('incDec', models.CharField(max_length=200, null=True)),
                ('deathCnt', models.CharField(max_length=200, null=True)),
                ('localOccCnt', models.CharField(max_length=200, null=True)),
                ('overFlowCnt', models.CharField(max_length=200, null=True)),
                ('qurRate', models.CharField(max_length=200, null=True)),
                ('updateDt', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
