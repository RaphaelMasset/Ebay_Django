# Generated by Django 4.2.5 on 2023-10-11 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_comments_actionid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctions',
            name='auctionTime',
        ),
    ]
