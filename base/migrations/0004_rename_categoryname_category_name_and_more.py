# Generated by Django 4.0.3 on 2022-04-03 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_subcategory_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='categoryName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='subCategoryName',
            new_name='name',
        ),
    ]