# Generated by Django 3.2.5 on 2021-08-02 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webkiosk', '0006_alter_orders_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webkiosk.customer'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webkiosk.food'),
        ),
    ]
