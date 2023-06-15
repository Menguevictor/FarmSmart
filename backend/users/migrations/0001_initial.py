# Generated by Django 4.2.2 on 2023-06-12 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='Email adress')),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=10, null=True)),
                ('first_name', models.CharField(max_length=10, null=True)),
                ('last_name', models.CharField(max_length=10, null=True)),
                ('photoProfil', models.ImageField(null=True, upload_to='images/pp')),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Admin',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthDay', models.DateField(max_length=60, null=True, verbose_name='Birth Day')),
                ('nationality', models.CharField(max_length=60, null=True)),
                ('phone_mother', models.IntegerField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('registration', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('adress', models.CharField(max_length=200)),
                ('birthDay', models.DateField(max_length=60, null=True, verbose_name='Birth Day')),
                ('nationality', models.CharField(max_length=60, null=True)),
                ('phone', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]