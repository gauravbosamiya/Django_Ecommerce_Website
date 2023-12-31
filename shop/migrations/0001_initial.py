# Generated by Django 4.2 on 2023-07-24 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='products/')),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
