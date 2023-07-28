# Generated by Django 4.2 on 2023-07-28 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Abonnement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_abonnement', models.DateTimeField(auto_now_add=True)),
                ('date_debut', models.DateTimeField()),
                ('date_fin', models.DateTimeField()),
                ('isValide', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=200)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='centre_logos/')),
                ('numeros_telephone', models.CharField(max_length=200)),
                ('emails', models.EmailField(max_length=254)),
                ('numero_compte', models.CharField(max_length=100)),
                ('no_ifu', models.CharField(max_length=100)),
                ('isActif', models.BooleanField(default=True)),
                ('heure_douverture', models.CharField(max_length=200)),
                ('services_offerts', models.TextField()),
                ('abonnements', models.ManyToManyField(blank=True, null=True, related_name='centres', to='api_gestion_centres.abonnement')),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profil_type', models.CharField(choices=[('superAdmin', 'Super Admin'), ('adminLocal', 'Admin Local'), ('personnelAdmin', 'Personnel Admin'), ('personnel', 'Personnel'), ('user', 'User')], default='user', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profil_Affectation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_affectation', models.DateField(auto_now_add=True)),
                ('isValide', models.BooleanField(default=True)),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_gestion_centres.centre')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_gestion_centres.profil')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='abonnement',
            name='centre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_gestion_centres.centre'),
        ),
    ]
