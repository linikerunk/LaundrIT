# Generated by Django 2.2.7 on 2019-11-10 03:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Pedido', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roupa',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome_peca', models.CharField(max_length=50, verbose_name='Nome da Peça')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço')),
            ],
            options={
                'verbose_name': 'Roupa',
                'verbose_name_plural': 'Roupas',
                'ordering': ('-nome_peca',),
            },
        ),
        migrations.AddField(
            model_name='item',
            name='roupa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='roupa_items', to='Pedido.Roupa', verbose_name='Roupa'),
            preserve_default=False,
        ),
    ]
