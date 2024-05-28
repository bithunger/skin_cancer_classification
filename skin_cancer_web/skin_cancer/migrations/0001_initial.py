# Generated by Django 4.2.7 on 2023-11-14 06:05

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
            name='PredictiveModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=200)),
                ('accuracy', models.FloatField()),
                ('precision', models.FloatField()),
                ('recall', models.FloatField()),
                ('f1_score', models.FloatField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkinUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20, verbose_name='Gender')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='users_profile/', verbose_name='Profile image')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='Address')),
                ('country', models.CharField(blank=True, max_length=200, verbose_name='Country')),
                ('city', models.CharField(blank=True, max_length=200, verbose_name='City')),
                ('contact', models.CharField(max_length=20, verbose_name='Contact')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SkinData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skin_image', models.ImageField(blank=True, null=True, upload_to='skin_images/', verbose_name='Skin image')),
                ('is_benign', models.BooleanField(default=False)),
                ('is_malignant', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]