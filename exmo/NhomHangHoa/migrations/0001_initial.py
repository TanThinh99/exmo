# Generated by Django 3.0.8 on 2020-11-30 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nhomhanghoa',
            fields=[
                ('manhom', models.AutoField(db_column='MaNhom', primary_key=True, serialize=False)),
                ('ten', models.CharField(blank=True, db_column='Ten', max_length=100, null=True)),
            ],
            options={
                'db_table': 'nhomhanghoa',
                'managed': False,
            },
        ),
    ]
