# Generated by Django 2.2.7 on 2019-11-17 16:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Pedido', '0037_auto_20191117_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suporte',
            name='data_mensagem',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
