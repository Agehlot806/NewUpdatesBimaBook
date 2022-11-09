# Generated by Django 4.0.6 on 2022-11-09 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bima_policy', '0002_rtotables_statertos_alter_agents_login_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agents',
            name='login_id',
            field=models.CharField(default='85D1002DCA', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bankdetail',
            name='id',
            field=models.CharField(default='C3BE9E', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='brokercode',
            name='id',
            field=models.CharField(default='557BE7', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='insurancecompany',
            name='id',
            field=models.CharField(default='9FF156', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='payout',
            name='payoutid',
            field=models.CharField(default='CE2F729', editable=False, max_length=7, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='policy',
            name='policyid',
            field=models.CharField(default='1C4B915', editable=False, max_length=7, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='id',
            field=models.CharField(default='1C00F58111AA415', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='rtoconversionmodel',
            name='id',
            field=models.CharField(default='759E44', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='rtotables',
            name='rto_id',
            field=models.CharField(default='4021A', editable=False, max_length=5, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='id',
            field=models.CharField(default='BE8A8F', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='login_id',
            field=models.CharField(default='6A77FD9E32', editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='statertos',
            name='stateid',
            field=models.CharField(default='7D6F5D60B3', editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='user_id',
            field=models.CharField(default='CA6C71A6AF104F3', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='vehiclecategory',
            name='id',
            field=models.CharField(default='8BB415', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='vehiclemakeby',
            name='id',
            field=models.CharField(default='4567CC', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='vehiclemodelname',
            name='id',
            field=models.CharField(default='973C39', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
