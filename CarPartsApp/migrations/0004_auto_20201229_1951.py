# Generated by Django 2.2.5 on 2020-12-30 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarPartsApp', '0003_auto_20201229_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycarparts',
            name='make',
            field=models.CharField(choices=[('Honda', 'Honda'), ('Subaru', 'Subaru'), ('Mercedes-benz', 'Mercedes-benz'), ('Toyota', 'Toyota'), ('Ford', 'Ford'), ('Chevy', 'Chevy')], default='', max_length=6),
        ),
    ]
