# Generated by Django 2.2.3 on 2019-08-01 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appels_sortants', '0016_auto_20190729_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='historique',
            name='operateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
