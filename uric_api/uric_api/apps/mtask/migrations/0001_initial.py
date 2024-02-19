# Generated by Django 3.0 on 2024-02-07 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CmdTemplateCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='名称/标题')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='描述信息')),
            ],
            options={
                'verbose_name': '模板分类',
                'verbose_name_plural': '模板分类',
                'db_table': 'cmd_template_category',
            },
        ),
        migrations.CreateModel(
            name='CmdTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='名称/标题')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='描述信息')),
                ('cmd', models.TextField(verbose_name='模板内容')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtask.CmdTemplateCategory', verbose_name='模板类别')),
            ],
            options={
                'verbose_name': '指令模板',
                'verbose_name_plural': '指令模板',
                'db_table': 'cmd_template',
            },
        ),
    ]
