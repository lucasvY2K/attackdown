# Generated by Django 3.1.7 on 2021-04-06 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pedido', '0002_auto_20210406_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='nomeFuncionario',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
