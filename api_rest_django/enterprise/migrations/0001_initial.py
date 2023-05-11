# Generated by Django 4.2.1 on 2023-05-11 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='enterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enterprise_id', models.IntegerField(max_length=10)),
                ('name', models.CharField(default='DEFAULT VALUE', max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'enterprise',
            },
        ),
    ]