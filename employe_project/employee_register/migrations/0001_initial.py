# Generated by Django 4.2.3 on 2023-07-12 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('emp_code', models.CharField(max_length=5)),
                ('mobile', models.CharField(max_length=15)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_register.position')),
            ],
        ),
    ]
