# Generated by Django 3.2.5 on 2021-08-02 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webkiosk', '0005_auto_20210802_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webkiosk.food'),
        ),
    ]
