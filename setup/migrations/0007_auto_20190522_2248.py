# Generated by Django 2.2.1 on 2019-05-22 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0006_auto_20190522_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employmentterms',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='jobgroup',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='jobposition',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='probationtypes',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
