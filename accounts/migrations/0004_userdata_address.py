# Generated by Django 4.0.2 on 2022-02-09 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_pins'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='address',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]