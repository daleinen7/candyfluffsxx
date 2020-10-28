# Generated by Django 3.0.8 on 2020-10-27 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_profile_signup_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=270)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='')),
                ('fandom', models.CharField(choices=[('H', 'My Hero Academia'), ('M', 'Miraculous Lady'), ('S', 'Sailor Moon'), ('V', 'Vampire Hunter D'), ('J', "JoJo's Bizarre Adventure"), ('H', 'Haikyuu'), ('K', 'Kingdom Hearts'), ('N', 'Necahual'), ('F', 'Final Fantasy'), ('C', 'Castlevania')], max_length=1)),
                ('product_type', models.CharField(choices=[('M', 'Misc'), ('B', 'Buttons')], max_length=1)),
                ('variation', models.CharField(max_length=200)),
                ('stock', models.IntegerField()),
                ('sku', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('size', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(verbose_name='Created on')),
            ],
        ),
    ]
