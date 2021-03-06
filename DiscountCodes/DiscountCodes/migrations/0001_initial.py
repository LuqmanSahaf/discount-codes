# Generated by Django 4.0 on 2021-12-21 09:06

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('short_hand', models.CharField(max_length=4, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_short_hand', message='Short hand not valid', regex='[A-Z]{1,4}')])),
                ('create_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'brands',
            },
        ),
        migrations.CreateModel(
            name='DiscountCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, null=True, validators=[django.core.validators.RegexValidator(code='invalid_discount_code', message='Discount code not valid', regex='[A-Z0-9]{10}')])),
                ('description', models.CharField(max_length=256)),
                ('fineprint', models.CharField(max_length=256)),
                ('create_date', models.DateTimeField(default=datetime.datetime.now)),
                ('update_date', models.DateTimeField(default=datetime.datetime.now)),
                ('expiry_date', models.DateTimeField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DiscountCodes.brand')),
            ],
            options={
                'db_table': 'discount_codes',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=256, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_email', message='Email not valid', regex='(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$)')])),
                ('phone', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(code='invalid_phone', message='Phone number not valid', regex='\\+{0,1}[0-9]{5,14}')])),
                ('create_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='DiscountCodeUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_fetched', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DiscountCodes.discountcode')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DiscountCodes.user')),
            ],
            options={
                'db_table': 'discount_code_users',
            },
        ),
        migrations.AddField(
            model_name='discountcode',
            name='users',
            field=models.ManyToManyField(through='DiscountCodes.DiscountCodeUser', to='DiscountCodes.User'),
        ),
    ]
