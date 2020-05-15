# Generated by Django 3.0.5 on 2020-05-13 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Network.Customer')),
                ('title', models.CharField(max_length=20)),
                ('url', models.URLField(default=' ')),
                ('Source_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerBookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Network.Bookmark')),
            ],
        ),
    ]