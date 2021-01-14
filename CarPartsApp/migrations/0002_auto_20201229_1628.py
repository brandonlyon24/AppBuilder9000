# Generated by Django 2.2.5 on 2020-12-30 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarPartsApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycarparts',
            name='type',
        ),
        migrations.AddField(
            model_name='mycarparts',
            name='make',
            field=models.CharField(choices=[('Chevy', 'Chevy'), ('Honda', 'Honda'), ('Toyota', 'Toyota'), ('Mercedes-benz', 'Mercedes-benz'), ('Subaru', 'Subaru'), ('Ford', 'Ford')], default='', max_length=6),
        ),
    ]