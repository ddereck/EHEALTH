# Generated by Django 4.2 on 2023-07-28 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_gestion_hospitalisations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('symptoms', models.TextField()),
                ('notes', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_gestion_hospitalisations.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('diagnosis_text', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_gestion_hospitalisations.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', models.CharField(max_length=200)),
                ('exam_requests', models.CharField(max_length=200)),
                ('exam_results', models.CharField(max_length=200)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_gestion_hospitalisations.patient')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taille', models.CharField(max_length=200)),
                ('tension_arterielle', models.CharField(max_length=200)),
                ('poids', models.CharField(max_length=200)),
                ('temperature', models.CharField(max_length=200)),
                ('electrophorese', models.CharField(max_length=200)),
                ('antecedents_medicaux', models.CharField(max_length=200)),
                ('allergies', models.CharField(max_length=200)),
                ('isDiabetic', models.BooleanField(default=False)),
                ('isAsthmatic', models.BooleanField(default=False)),
                ('isTensionnaire', models.BooleanField(default=False)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('dernier_rdv', models.DateTimeField(blank=True, null=True)),
                ('prochain_rdv', models.DateTimeField(blank=True, null=True)),
                ('medicaments_en_cours', models.TextField(blank=True)),
                ('resultat_examens', models.TextField(blank=True)),
                ('notes_medicales', models.TextField(blank=True)),
                ('recommandations', models.TextField(blank=True)),
                ('autres_informations', models.TextField(blank=True)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_gestion_dossiers_medicaux.consultation')),
                ('diagnosis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_gestion_dossiers_medicaux.diagnosis')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_gestion_hospitalisations.patient')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_gestion_dossiers_medicaux.treatment')),
            ],
        ),
    ]