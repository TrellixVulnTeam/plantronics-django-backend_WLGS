# Generated by Django 4.0.3 on 2022-05-11 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_edible_are_flowers_edible_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='climate',
            field=models.CharField(choices=[('A', 'All'), ('A2', 'All Expect Polar'), ('TTST', 'Sub Tropical to Tropical'), ('STAT', 'Temperate to Subtropical'), ('PTT', 'Polar to Temperate'), ('T', 'Tropical'), ('ST', 'Sub-Tropical'), ('TE', 'Temperate'), ('P', 'Polar or SubPolar')], default='T', max_length=5, verbose_name='Climate Zones'),
        ),
    ]
