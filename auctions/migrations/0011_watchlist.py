# Generated by Django 4.2.5 on 2023-10-15 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_remove_bids_actionid_remove_bids_bidtime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auctionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auctions')),
                ('userName', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='waList_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
