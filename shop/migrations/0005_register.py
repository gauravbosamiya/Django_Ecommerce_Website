# Generated by Django 4.2 on 2023-07-24 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=500)),
                ('con_password', models.CharField(max_length=500)),
            ],
        ),
    ]
