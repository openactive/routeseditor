# Generated by Django 3.1 on 2020-10-08 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protoroute', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routeguide',
            name='author',
            field=models.ManyToManyField(blank=True, to='protoroute.PersonAndOrganization', verbose_name='Author'),
        ),
    ]