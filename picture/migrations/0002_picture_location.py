# Generated by Django 3.2.3 on 2021-05-15 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='picture.location'),
            preserve_default=False,
        ),
    ]
