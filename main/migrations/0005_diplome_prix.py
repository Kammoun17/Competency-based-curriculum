# Generated by Django 4.2 on 2023-05-11 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_diplome_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='diplome',
            name='prix',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]