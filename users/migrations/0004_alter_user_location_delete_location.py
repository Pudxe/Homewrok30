# Generated by Django 4.1.6 on 2023-02-16 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('users', '0003_alter_location_options_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.location'),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]