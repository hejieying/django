# Generated by Django 2.2.7 on 2020-05-14 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20200513_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='r',
            field=models.ManyToManyField(to='app01.Host'),
        ),
        migrations.DeleteModel(
            name='HostToApp',
        ),
    ]
