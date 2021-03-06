# Generated by Django 2.2.5 on 2020-08-03 10:22

import datetime
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
            name='BankXlsx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=20, verbose_name='题库名称')),
                ('bank_type', models.CharField(max_length=10, verbose_name='题库所属分类')),
                ('bank_xlsx', models.CharField(max_length=50, verbose_name='上传文件名称')),
                ('bank_nums', models.IntegerField(verbose_name='题库总数')),
                ('bank_chio', models.IntegerField(verbose_name='单选题数')),
                ('bank_chios', models.IntegerField(verbose_name='多选题数')),
                ('bank_judge', models.IntegerField(verbose_name='判断题数')),
                ('bank_gap', models.IntegerField(verbose_name='填空题数')),
                ('bank_person', models.IntegerField(verbose_name='参与人数')),
                ('bank_bs', models.IntegerField(verbose_name='已出考试')),
            ],
            options={
                'verbose_name': '存储题库xlsx',
                'verbose_name_plural': '存储题库xlsx',
            },
        ),
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=10, verbose_name='类型名')),
                ('class_head', models.ImageField(default='default_class.png', upload_to='', verbose_name='类型头像')),
                ('class_desc', models.TextField(verbose_name='类型描述')),
            ],
            options={
                'verbose_name': '考试分类',
                'verbose_name_plural': '考试分类',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=50, verbose_name='考试名称')),
                ('game_nums', models.IntegerField(verbose_name='出题数量')),
                ('game_score', models.IntegerField(verbose_name='总分数')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='开始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
                ('time_bar', models.IntegerField(verbose_name='答题时间限制')),
                ('game_rule', models.TextField(verbose_name='考试规则')),
                ('bank_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.BankXlsx', verbose_name='关联题库表')),
                ('class_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.Classify', verbose_name='关联分类表')),
            ],
            options={
                'verbose_name': '考试配置',
                'verbose_name_plural': '考试配置',
            },
        ),
        migrations.CreateModel(
            name='Ques_judge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques_type', models.CharField(default='判断题', max_length=5, verbose_name='题类型')),
                ('question', models.TextField(verbose_name='判断题目')),
                ('answer', models.TextField(verbose_name='答案')),
                ('score', models.IntegerField(verbose_name='分值')),
                ('judge_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.BankXlsx', verbose_name='关联题库表')),
            ],
            options={
                'verbose_name': '判断题',
                'verbose_name_plural': '判断题',
            },
        ),
        migrations.CreateModel(
            name='Ques_gap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques_type', models.CharField(default='填空题', max_length=5, verbose_name='题类型')),
                ('question', models.TextField(verbose_name='填空题目')),
                ('answer', models.TextField(verbose_name='答案')),
                ('score', models.IntegerField(verbose_name='分值')),
                ('gap_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.BankXlsx', verbose_name='关联题库表')),
            ],
            options={
                'verbose_name': '填空题',
                'verbose_name_plural': '填空题',
            },
        ),
        migrations.CreateModel(
            name='Ques_choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques_type', models.CharField(default='多选题', max_length=5, verbose_name='题类型')),
                ('question', models.TextField(verbose_name='多选题目')),
                ('answer', models.TextField(verbose_name='答案')),
                ('choiceA', models.TextField(verbose_name='选项A')),
                ('choiceB', models.TextField(verbose_name='选项B')),
                ('choiceC', models.TextField(verbose_name='选项C')),
                ('choiceD', models.TextField(verbose_name='选项D')),
                ('score', models.IntegerField(verbose_name='分值')),
                ('chois_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.BankXlsx', verbose_name='关联题库表')),
            ],
            options={
                'verbose_name': '多选题',
                'verbose_name_plural': '多选题',
            },
        ),
        migrations.CreateModel(
            name='Ques_choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques_type', models.CharField(default='单选题', max_length=5, verbose_name='题类型')),
                ('question', models.TextField(verbose_name='单选题目')),
                ('answer', models.TextField(verbose_name='答案')),
                ('choiceA', models.TextField(verbose_name='选项A')),
                ('choiceB', models.TextField(verbose_name='选项B')),
                ('choiceC', models.TextField(verbose_name='选项C')),
                ('choiceD', models.TextField(verbose_name='选项D')),
                ('score', models.IntegerField(verbose_name='分值')),
                ('choi_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.BankXlsx', verbose_name='关联题库表')),
            ],
            options={
                'verbose_name': '单选题',
                'verbose_name_plural': '单选题',
            },
        ),
        migrations.CreateModel(
            name='GameInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(verbose_name='得分')),
                ('times', models.CharField(max_length=20, verbose_name='用时')),
                ('ginfo_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.Game', verbose_name='关联考试配置表')),
                ('ginfo_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='关联用户表')),
            ],
            options={
                'verbose_name': '考试记录',
                'verbose_name_plural': '考试记录',
            },
        ),
    ]
