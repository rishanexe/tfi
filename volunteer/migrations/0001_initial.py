# Generated by Django 2.1.7 on 2019-03-20 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('volunteeremail', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField(default=0)),
                ('commitment', models.IntegerField(default=1)),
                ('note', models.CharField(max_length=500)),
                ('experience', models.IntegerField(default=0)),
            ],
        ),
    ]