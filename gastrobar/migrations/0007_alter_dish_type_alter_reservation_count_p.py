# Generated by Django 4.0 on 2022-03-31 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gastrobar', '0006_alter_dish_id_alter_reservation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='type',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='count_p',
            field=models.IntegerField(default=None),
        ),
    ]
