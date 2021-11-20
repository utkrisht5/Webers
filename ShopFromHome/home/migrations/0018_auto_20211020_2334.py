# Generated by Django 3.2.8 on 2021-10-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_recordforshopkeeper'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordforshopkeeper',
            name='response',
        ),
        migrations.AddField(
            model_name='recordforshopkeeper',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='recordforshopkeeper',
            name='item',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='recordforshopkeeper',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='recordforshopkeeper',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='recordforshopkeeper',
            name='shop',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='recordforshopkeeper',
            name='shopkeeper',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]