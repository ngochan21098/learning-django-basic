# Generated by Django 4.2.16 on 2024-10-14 15:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_application_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(default=datetime.time, on_delete=django.db.models.deletion.DO_NOTHING, to='users.user'),
            preserve_default=False,
        ),
    ]
