# Generated by Django 2.2.3 on 2022-03-29 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gastroblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
