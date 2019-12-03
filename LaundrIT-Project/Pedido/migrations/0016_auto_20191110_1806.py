# Generated by Django 2.2.7 on 2019-11-10 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pedido', '0015_auto_20191110_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='status',
        ),
        migrations.AddField(
            model_name='status',
            name='pedido',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='pedido', to='Pedido.Pedido', verbose_name='Pedido'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='status',
            name='status_pedido',
            field=models.CharField(choices=[('Pedido Ativo', 'Pedido Ativo'), ('Pedido Finalizado', 'Pedido Finalizado'), ('Pedido Cancelado', 'Pedido Cancelado')], default='Pedido Ativo', max_length=50, verbose_name='Situação'),
        ),
    ]