# Generated by Django 4.2.17 on 2024-12-23 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cart', '0004_alter_donhang_ma_don_hang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khuyenmai',
            name='ma_khuyen_mai',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='khuyenmai',
            name='ti_le_khuyen_mai',
            field=models.BigIntegerField(default=0),
        ),
    ]
