# Generated by Django 5.1.4 on 2025-01-05 02:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('pub_date', models.DateField(null=True, verbose_name='发布日期')),
                ('readcount', models.IntegerField(default=0, verbose_name='阅读量')),
                ('commentcount', models.IntegerField(default=0, verbose_name='评论量')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
            ],
            options={
                'verbose_name': '图书',
                'db_table': 'bookinfo',
            },
        ),
        migrations.CreateModel(
            name='PeopleInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('gender', models.SmallIntegerField(choices=[(0, 'male'), (1, 'female')], default=0, verbose_name='性别')),
                ('description', models.CharField(max_length=200, null=True, verbose_name='描述信息')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.bookinfo', verbose_name='图书')),
            ],
            options={
                'verbose_name': '人物信息',
                'db_table': 'peopleinfo',
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]