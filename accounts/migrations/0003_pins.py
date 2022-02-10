# Generated by Django 4.0.2 on 2022-02-07 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_userdata_mobile_number_alter_userdata_account_bank_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_pin', models.CharField(default=None, max_length=6, null=True)),
                ('mobile_pin', models.CharField(default=None, max_length=6, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='u', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]