# Generated by Django 4.0.3 on 2022-04-03 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_subcategory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.category'),
        ),
    ]
