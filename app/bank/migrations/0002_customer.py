# Generated by Django 2.2.7 on 2019-11-25 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_first_name', models.CharField(max_length=200)),
                ('customer_last_name', models.CharField(max_length=200)),
                ('customer_email', models.EmailField(max_length=300)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.Branch')),
            ],
        ),
    ]
