# Generated by Django 2.0.3 on 2019-10-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(default='empty', max_length=64),
        ),
    ]
