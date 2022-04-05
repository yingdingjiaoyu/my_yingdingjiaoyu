# Generated by Django 4.0.3 on 2022-04-03 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admissions_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major_group_code', models.IntegerField(default='', verbose_name='专业组代码')),
                ('major_group_name', models.CharField(default='', max_length=200, verbose_name='专业组名称')),
                ('preferred_subject', models.CharField(default='', max_length=2, verbose_name='首选科目')),
                ('recleaning_subject', models.CharField(default='', max_length=20, verbose_name='再选科目')),
                ('annual_target', models.IntegerField(null=True, verbose_name='计划数')),
                ('plan_change', models.IntegerField(null=True, verbose_name='计划增减')),
                ('provinces', models.CharField(default='', max_length=10, verbose_name='所在省份')),
                ('region', models.CharField(default='', max_length=10, verbose_name='所在地区')),
                ('college_property', models.CharField(default='', max_length=4, verbose_name='院校性质')),
                ('college_state', models.CharField(blank=True, max_length=20, null=True, verbose_name='院校说明')),
                ('line_2019', models.IntegerField(blank=True, null=True, verbose_name='2019录取线')),
                ('line_2020', models.IntegerField(blank=True, null=True, verbose_name='2020录取线')),
                ('line_2021', models.IntegerField(blank=True, null=True, verbose_name='2021录取线')),
                ('ranking_2019', models.IntegerField(blank=True, null=True, verbose_name='2019位次')),
                ('ranking_2020', models.IntegerField(blank=True, null=True, verbose_name='2020位次')),
                ('ranking_2021', models.IntegerField(blank=True, null=True, verbose_name='2021位次')),
            ],
        ),
    ]