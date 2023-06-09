# Generated by Django 3.2.18 on 2023-05-08 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prescriptions', '0007_auto_20230508_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutPrescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thurday'), ('FR', 'Friday'), ('SA', 'Saturday'), ('SU', 'Sunday')], max_length=2)),
                ('set', models.IntegerField()),
                ('rep', models.IntegerField()),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prescriptions.workout')),
                ('workout_sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prescriptions.workoutsheet')),
            ],
        ),
    ]
