# Generated by Django 2.2.3 on 2019-07-25 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appels_sortants', '0009_auto_20190725_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='statut',
            field=models.IntegerField(default=0),
        ),
    ]
