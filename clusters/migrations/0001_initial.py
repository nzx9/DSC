# Generated by Django 3.2.5 on 2021-07-17 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('timestamp', models.TextField()),
                ('createdby', models.TextField()),
                ('availableat', models.TextField()),
            ],
        ),
    ]
