# Generated by Django 2.2.27 on 2022-05-02 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('dob', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BrandCompany',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('foundationYear', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ElectroProducer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('foundationYear', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('discriminator', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('foundationYear', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MobileType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('totalPrice', models.FloatField()),
                ('createdTime', models.IntegerField()),
                ('cartId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Cart')),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('foundationYear', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('foundationYear', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fromAddress', models.CharField(max_length=200)),
                ('toAddress', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
                ('status', models.BinaryField()),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('screen', models.CharField(max_length=200)),
                ('impPrice', models.FloatField()),
                ('image', models.ImageField(default='images/mobile/default.jpg', upload_to='images/mobile/')),
                ('os', models.CharField(max_length=200)),
                ('BrandCompanyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.BrandCompany')),
                ('mobileType', models.ManyToManyField(to='ecommerce.MobileType')),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cpu', models.CharField(max_length=200)),
                ('ram', models.CharField(max_length=200)),
                ('screen', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(default='images/laptop/default.jpg', upload_to='images/laptop/')),
                ('impPrice', models.FloatField()),
                ('producerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Producer')),
                ('type', models.ManyToManyField(to='ecommerce.Type')),
            ],
        ),
        migrations.CreateModel(
            name='FullName',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Electronics',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(default='images/electronics/default.jpg', upload_to='images/electronics/')),
                ('name', models.CharField(max_length=200)),
                ('powerConsume', models.FloatField()),
                ('impPrice', models.FloatField()),
                ('usage', models.CharField(max_length=200)),
                ('electroProducerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.ElectroProducer')),
                ('kind', models.ManyToManyField(to='ecommerce.Kind')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=200)),
                ('time', models.IntegerField()),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Customer')),
                ('itemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(default='images/clothes/default.jpg', upload_to='images/clothes/')),
                ('impPrice', models.FloatField()),
                ('manufactureId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.Manufacture')),
                ('style', models.ManyToManyField(to='ecommerce.Style')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('type', models.CharField(max_length=200)),
                ('cartId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Cart')),
                ('itemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Item')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='customerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Customer'),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('page', models.IntegerField()),
                ('impPrice', models.FloatField()),
                ('image', models.ImageField(default='images/book/default.jpg', upload_to='images/book/')),
                ('name', models.CharField(max_length=200)),
                ('author', models.ManyToManyField(to='ecommerce.Author')),
                ('category', models.ManyToManyField(to='ecommerce.Category')),
                ('publisher', models.ManyToManyField(to='ecommerce.Publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('district', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('descrip', models.CharField(max_length=200)),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='ItemMobile',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ecommerce.Item')),
                ('yearEdition', models.IntegerField()),
                ('maintainTime', models.FloatField()),
                ('memorySize', models.IntegerField()),
                ('color', models.CharField(max_length=200)),
                ('mobileId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Mobile')),
            ],
            bases=('ecommerce.item',),
        ),
        migrations.CreateModel(
            name='ItemLaptop',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ecommerce.Item')),
                ('yearEdition', models.IntegerField()),
                ('color', models.CharField(max_length=200)),
                ('maintainTime', models.FloatField()),
                ('laptopId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Laptop')),
            ],
            bases=('ecommerce.item',),
        ),
        migrations.CreateModel(
            name='ItemElectronics',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ecommerce.Item')),
                ('maintainTime', models.FloatField()),
                ('electronicsId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Electronics')),
            ],
            bases=('ecommerce.item',),
        ),
        migrations.CreateModel(
            name='ItemClothes',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ecommerce.Item')),
                ('color', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=200)),
                ('clothesId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Clothes')),
            ],
            bases=('ecommerce.item',),
        ),
        migrations.CreateModel(
            name='ItemBook',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ecommerce.Item')),
                ('edition', models.IntegerField()),
                ('bookId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Book')),
            ],
            bases=('ecommerce.item',),
        ),
    ]
