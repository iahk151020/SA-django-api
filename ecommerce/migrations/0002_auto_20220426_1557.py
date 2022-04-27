# Generated by Django 2.2.27 on 2022-04-26 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='electronics',
            name='image',
            field=models.ImageField(default='images/electronics/default.jpg', upload_to='images/electronics/'),
        ),
        migrations.AddField(
            model_name='mobile',
            name='image',
            field=models.ImageField(default='images/mobile/default.jpg', upload_to='images/mobile/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='images/book/default.jpg', upload_to='images/book/'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='image',
            field=models.ImageField(default='images/clothes/default.jpg', upload_to='images/clothes/'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='image',
            field=models.ImageField(default='images/laptop/default.jpg', upload_to='images/laptop/'),
        ),
    ]