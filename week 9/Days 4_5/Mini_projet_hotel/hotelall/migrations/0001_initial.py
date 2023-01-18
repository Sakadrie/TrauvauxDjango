# Generated by Django 4.1.5 on 2023-01-18 20:45

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
                ('prenom', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('address', models.CharField(max_length=200, null=True)),
                ('ville', models.CharField(max_length=200, null=True)),
                ('pays', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeChambre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typecharmbre', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ari', models.DateField()),
                ('date_sorti', models.DateField()),
                ('number_person', models.IntegerField()),
                ('number_chambre', models.IntegerField()),
                ('cout', models.IntegerField()),
                ('statu', models.BooleanField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelall.customer')),
                ('typechambre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelall.typechambre')),
            ],
        ),
        migrations.CreateModel(
            name='Chambre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cout', models.IntegerField()),
                ('taille', models.IntegerField()),
                ('photo', models.ImageField(default='img_chambre/default.jpg', upload_to='img_chambre', verbose_name='photo de chambre')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelall.typechambre')),
            ],
        ),
        migrations.CreateModel(
            name='Avis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avis', models.CharField(max_length=70, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelall.customer')),
            ],
        ),
    ]