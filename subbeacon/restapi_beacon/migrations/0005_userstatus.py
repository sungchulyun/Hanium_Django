# Generated by Django 3.2.5 on 2021-09-07 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi_beacon', '0004_subwayim'),
    ]

    operations = [
        migrations.CreateModel(
            name='userstatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usersta', models.CharField(max_length=50)),
                ('usertrain', models.IntegerField()),
            ],
        ),
    ]
