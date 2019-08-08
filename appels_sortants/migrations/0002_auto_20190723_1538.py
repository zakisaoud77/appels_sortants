# Generated by Django 2.2.3 on 2019-07-23 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appels_sortants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adresse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rue', models.CharField(max_length=30)),
                ('ville', models.CharField(max_length=30)),
                ('pays', models.CharField(max_length=30)),
                ('codezip', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='published_date',
            new_name='cible_date',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='author',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='text',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='title',
        ),
        migrations.RemoveField(
            model_name='historique',
            name='author',
        ),
        migrations.RemoveField(
            model_name='historique',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='historique',
            name='text',
        ),
        migrations.RemoveField(
            model_name='historique',
            name='title',
        ),
        migrations.AddField(
            model_name='contact',
            name='dernier_appel_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='nom',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='prenom',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='statut',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historique',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historique',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appels_sortants.Contact'),
        ),
        migrations.AddField(
            model_name='historique',
            name='id_action',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='adresse_postal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appels_sortants.Adresse'),
        ),
    ]
