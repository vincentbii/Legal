# Generated by Django 2.2.1 on 2019-05-22 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0003_casestatus_employmentterms_jobgroup_jobposition_jobtype_nationality_probationtypes_religion_requestt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='nationality',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='priority',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='religion',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
