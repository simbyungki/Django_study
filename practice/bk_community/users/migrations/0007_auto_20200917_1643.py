# Generated by Django 3.1.1 on 2020-09-17 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200917_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bkuser',
            name='email',
            field=models.EmailField(max_length=128, null=True, verbose_name='이메일'),
        ),
    ]
