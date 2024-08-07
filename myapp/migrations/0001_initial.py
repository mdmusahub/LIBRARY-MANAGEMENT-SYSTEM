# Generated by Django 5.0.1 on 2024-03-01 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('B_id', models.IntegerField(primary_key=True, serialize=False)),
                ('B_name', models.CharField(max_length=300)),
                ('Subject', models.CharField(max_length=300)),
                ('Description', models.CharField(max_length=300)),
                ('Semester', models.IntegerField()),
                ('Quantity', models.IntegerField()),
                ('Price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('M_id', models.IntegerField(primary_key=True, serialize=False)),
                ('M_name', models.CharField(max_length=300)),
                ('Mobile_number', models.IntegerField()),
                ('Semester', models.IntegerField()),
                ('Branch', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('R_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Member_Name', models.CharField(max_length=300)),
                ('Book_name', models.CharField(max_length=300)),
                ('B_issue_date', models.DateField()),
                ('B_return_date', models.DateField()),
                ('Status', models.CharField(max_length=300)),
                ('Book_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.book')),
                ('Member_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.members')),
            ],
        ),
    ]
