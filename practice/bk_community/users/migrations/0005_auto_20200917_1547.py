# Generated by Django 3.1.1 on 2020-09-17 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200916_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='BKUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='사용자명')),
                ('email', models.EmailField(max_length=128, verbose_name='이메일')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록일시')),
            ],
            options={
                'verbose_name': 'BK 커뮤니티 사용자',
                'verbose_name_plural': 'BK 커뮤니티 사용자',
                'db_table': 'bk_users',
            },
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
