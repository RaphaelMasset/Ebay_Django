# Generated by Django 4.2.5 on 2023-10-09 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='auctions',
            fields=[
                ('auctionId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=500)),
                ('startPrice', models.IntegerField()),
                ('auctionTime', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('commentId', models.AutoField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=64)),
                ('comment', models.CharField(max_length=500)),
                ('commentTime', models.DateField()),
                ('actionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auctions')),
            ],
        ),
        migrations.CreateModel(
            name='bids',
            fields=[
                ('actionId', models.AutoField(primary_key=True, serialize=False)),
                ('bid', models.IntegerField()),
                ('bidTime', models.DateField()),
                ('bidsId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auctions')),
            ],
        ),
    ]
