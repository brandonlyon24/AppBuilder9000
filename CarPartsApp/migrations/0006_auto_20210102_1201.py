# Generated by Django 2.2.5 on 2021-01-02 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarPartsApp', '0005_auto_20201230_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycarparts',
            name='make',
            field=models.CharField(choices=[('Honda', 'Honda'), ('Mercedes-benz', 'Mercedes-benz'), ('Chevy', 'Chevy'), ('Ford', 'Ford'), ('Toyota', 'Toyota'), ('Subaru', 'Subaru')], default='', max_length=6),
        ),
        migrations.AlterField(
            model_name='mycarparts',
            name='user_name',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='mycarparts',
            name='year',
            field=models.CharField(choices=[('2005', '2005'), ('1995', '1995'), ('1990', '1990'), ('2020', '2020'), ('2010', '2010'), ('2000', '2000'), ('2015', '2015')], default='', max_length=6),
        ),
    ]
