# Generated by Django 3.2.4 on 2021-06-24 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_login_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='name',
            field=models.CharField(max_length=123),
        ),
    ]
