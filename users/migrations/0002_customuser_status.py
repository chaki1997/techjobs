# Generated by Django 2.0.3 on 2019-10-03 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('freelancer', 'Work As A Freelancer'), ('company', 'Hire of Project')], default='freelancer', max_length=255),
        ),
    ]
