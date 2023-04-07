# Generated by Django 4.1.6 on 2023-02-03 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=225)),
                ('position', models.CharField(max_length=225)),
                ('avatar', models.ImageField(upload_to='feedbacks/')),
                ('message', models.TextField()),
            ],
        ),
    ]