# Generated by Django 4.2.5 on 2023-10-11 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_rename_startprice_auctions_sprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='actionId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Avis', to='auctions.auctions'),
        ),
    ]
