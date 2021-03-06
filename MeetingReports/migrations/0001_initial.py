# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-08-29 17:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='My Company', max_length=30, unique=True, verbose_name='名称')),
                ('name_ext', models.CharField(default='better Co.,Ltd.', max_length=30, verbose_name='名称补充')),
                ('mission', models.CharField(default='Try everything', max_length=20, verbose_name='使命')),
                ('url', models.URLField(default='http://www.test.com', max_length=50, verbose_name='多点商城')),
                ('mobile', models.CharField(default='11111111', max_length=11, verbose_name='服务热线')),
                ('address', models.CharField(default='company address', max_length=50, verbose_name='公司地址')),
            ],
            options={
                'indexes': [],
            },
        ),
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='组邮件')),
                ('contain_menber', models.BooleanField(default=True, verbose_name='收件人是否包含全部组员（存在群邮箱时，此设置忽略）')),
                ('cclist', models.ManyToManyField(related_name='cclist', to=settings.AUTH_USER_MODEL, verbose_name='抄送用户')),
            ],
            options={
                'indexes': [],
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50, unique=True, verbose_name='主题')),
                ('menber', models.CharField(max_length=100, verbose_name='参会人员')),
                ('position', models.CharField(default='工位', max_length=20, verbose_name='会议地点')),
                ('milestone1', models.CharField(max_length=50, verbose_name='里程碑')),
                ('milestonedate1', models.DateTimeField(verbose_name='里程碑时间')),
                ('milestone2', models.CharField(max_length=50, verbose_name='下一里程碑')),
                ('milestonedate2', models.DateTimeField(verbose_name='下一里程碑时间')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'indexes': [],
            },
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave', models.BooleanField(default=False, verbose_name='是否请假')),
                ('content', models.CharField(max_length=200, verbose_name='早会条目')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MeetingReports.Meeting', verbose_name='早会')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='成员')),
            ],
            options={
                'indexes': [],
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='小组名')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('master', models.ManyToManyField(blank=True, related_name='groupmaster', to=settings.AUTH_USER_MODEL, verbose_name='管理员')),
                ('ower', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'indexes': [],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, default='SoftwareEngineer', max_length=20, verbose_name='职位')),
                ('departments', models.CharField(blank=True, default='BusinessDepartment', max_length=20, verbose_name='部门')),
                ('mobile', models.CharField(blank=True, max_length=11, unique=True, verbose_name='手机')),
                ('duty', models.BooleanField(default=False, verbose_name='值日')),
                ('sorts', models.PositiveIntegerField(blank=True, default=0, verbose_name='排序')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MeetingReports.Company', verbose_name='公司')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usergroup', to='MeetingReports.UserGroup', verbose_name='小组')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'indexes': [],
                'ordering': ('sorts', 'user__date_joined'),
            },
        ),
        migrations.AddField(
            model_name='meeting',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MeetingReports.UserGroup', verbose_name='所属小组'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='master', to=settings.AUTH_USER_MODEL, verbose_name='主持人'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='noter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noter', to=settings.AUTH_USER_MODEL, verbose_name='记录人'),
        ),
        migrations.AddField(
            model_name='emails',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MeetingReports.UserGroup', verbose_name='小组'),
        ),
        migrations.AddField(
            model_name='emails',
            name='relist',
            field=models.ManyToManyField(related_name='relist', to=settings.AUTH_USER_MODEL, verbose_name='附加收件人'),
        ),
    ]
