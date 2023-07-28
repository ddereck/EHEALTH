# Generated by Django 4.2 on 2023-07-28 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceReimbursement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compagnie_assurance', models.CharField(max_length=100)),
                ('montant_remboursement', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_remboursement', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_facture', models.CharField(max_length=100)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_facture', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode_paiement', models.CharField(max_length=100)),
                ('montant_paye', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_paiement', models.DateField()),
            ],
        ),
    ]