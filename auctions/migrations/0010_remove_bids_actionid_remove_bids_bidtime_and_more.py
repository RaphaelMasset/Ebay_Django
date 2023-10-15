# Generated by Django 4.2.5 on 2023-10-15 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_rename_auctionid_auctions_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bids',
            name='actionId',
        ),
        migrations.RemoveField(
            model_name='bids',
            name='bidTime',
        ),
        migrations.AddField(
            model_name='auctions',
            name='userName',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auction_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bids',
            name='auctionId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auctions.auctions'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bids',
            name='userName',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bid_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bids',
            name='bidsId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comments',
            name='userName',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to=settings.AUTH_USER_MODEL),
        ),
    ]
