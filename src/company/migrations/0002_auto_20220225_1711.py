# Generated by Django 3.2.9 on 2022-02-25 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='company_type',
        ),
        migrations.AlterField(
            model_name='company',
            name='business_type',
            field=models.CharField(choices=[('per', 'Personal'), ('pre', 'Premium'), ('ent', 'Enterprise')], max_length=255),
        ),
    ]
