# Generated by Django 2.2.27 on 2022-05-02 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='createdTime',
            field=models.CharField(max_length=100),
        ),
    ]