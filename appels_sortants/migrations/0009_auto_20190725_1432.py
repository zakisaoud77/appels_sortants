# Generated by Django 2.2.3 on 2019-07-25 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appels_sortants', '0008_historique_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historique',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appels_sortants.Contact'),
        ),
    ]