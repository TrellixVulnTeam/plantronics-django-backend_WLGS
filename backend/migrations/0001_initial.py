# Generated by Django 4.0.3 on 2022-05-05 02:15

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
            name='Family',
            fields=[
                ('family', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('family_description', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Family',
                'verbose_name_plural': 'Families',
            },
        ),
        migrations.CreateModel(
            name='Genus',
            fields=[
                ('genus', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('genus_description', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'genus',
                'verbose_name_plural': 'genus',
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_name', models.CharField(max_length=255)),
                ('plant_latin_name', models.CharField(max_length=255)),
                ('plant_image', models.ImageField(blank=True, upload_to='images/')),
                ('plant_description', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='backend.family')),
                ('genus', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='backend.genus')),
            ],
            options={
                'verbose_name': 'Plant',
            },
        ),
        migrations.CreateModel(
            name='UserPlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, null=True)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.plant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'verbose_name': 'User Plant',
                'verbose_name_plural': 'Users Plants',
            },
        ),
        migrations.CreateModel(
            name='SoilPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preference', models.CharField(choices=[(None, '(Unknown)'), ('AN', 'Any Soil'), ('CL', 'Clay'), ('SA', 'Sandy'), ('SI', 'Silty'), ('PE', 'Peaty'), ('CH', 'Chalky'), ('LO', 'Loamy')], default='(Unknown)', max_length=3)),
                ('soil_description', models.CharField(max_length=500, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('plants', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.plant')),
            ],
            options={
                'verbose_name': 'Soil Preference',
                'verbose_name_plural': 'Soil Preferences',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sun_preference', models.CharField(choices=[(None, '(Unknown)'), ('FS', 'Full Sun'), ('LS', 'Light Shade\n                             (Between 3 and 5 hours of direct sun)'), ('PS', 'Partial Shade (Receives 2 hours of sun a day)'), ('FSH', 'Full Shade (Less then an hour of sunlight a day)'), ('DS', 'Dense Shade (No direct sun light and little\n                             indirect sun light')], default='FS', max_length=3)),
                ('climate', models.CharField(choices=[('A', 'All'), ('A2', 'All Expect Polar'), ('T', 'Tropical'), ('ST', 'Sub-Tropical'), ('TE', 'Temperate'), ('P', 'Polar or SubPolar')], default='T', max_length=3, verbose_name='Climate Zones')),
                ('season', models.CharField(choices=[(None, '(Unknown)'), ('W', 'Winter'), ('SP', 'Spring'), ('SU', 'Summer'), ('AU', 'Autumn')], default='SU', max_length=3, verbose_name='Planting Season')),
                ('time_frame', models.CharField(choices=[(None, '(Unknown)'), ('D', 'Daily'), ('AD', 'Alternating Days (Every Other Day)'), ('W', 'Weekly'), ('F', 'Fort Nightly'), ('M', 'Monthly')], default='D', max_length=3, verbose_name='Watering Schedule')),
                ('info_description', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('plant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.plant')),
            ],
            options={
                'verbose_name': 'Info',
                'verbose_name_plural': 'Info',
            },
        ),
        migrations.CreateModel(
            name='Edible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_fruit_edible', models.CharField(choices=[(None, '(Unknown)'), ('Y', 'Yes'), ('N', 'No'), ('P', 'Partially Edible'), ('RP', 'Requires Preperation'), ('PRP', 'Partially Edible But Requires Preperation')], default='(Unknown)', max_length=3)),
                ('fruit_image', models.ImageField(blank=True, upload_to='images/')),
                ('are_leaves_edible', models.CharField(choices=[(None, '(Unknown)'), ('Y', 'Yes'), ('N', 'No'), ('P', 'Partially Edible'), ('RP', 'Requires Preperation'), ('PRP', 'Partially Edible But Requires Preperation')], default='(Unknown)', max_length=3)),
                ('leaf_image', models.ImageField(blank=True, upload_to='images/')),
                ('are_roots_edible', models.CharField(choices=[(None, '(Unknown)'), ('Y', 'Yes'), ('N', 'No'), ('P', 'Partially Edible'), ('RP', 'Requires Preperation'), ('PRP', 'Partially Edible But Requires Preperation')], default='(Unknown)', max_length=3)),
                ('root_image', models.ImageField(blank=True, upload_to='images/')),
                ('are_flowers_edible', models.CharField(choices=[(None, '(Unknown)'), ('Y', 'Yes'), ('N', 'No'), ('P', 'Partially Edible'), ('RP', 'Requires Preperation'), ('PRP', 'Partially Edible But Requires Preperation')], default='(Unknown)', max_length=3)),
                ('flower_image', models.ImageField(blank=True, upload_to='images/')),
                ('are_seeds_edible', models.CharField(choices=[(None, '(Unknown)'), ('Y', 'Yes'), ('N', 'No'), ('P', 'Partially Edible'), ('RP', 'Requires Preperation'), ('PRP', 'Partially Edible But Requires Preperation')], default='(Unknown)', max_length=3)),
                ('seed_image', models.ImageField(blank=True, upload_to='images/')),
                ('edible_description', models.CharField(max_length=1000)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.plant')),
            ],
            options={
                'verbose_name': 'Edible',
            },
        ),
    ]
