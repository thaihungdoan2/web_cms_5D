# Generated by Django 3.0.7 on 2020-06-15 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('home', '0007_blogpagegalleryimage_productsindexpage_productspage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductsIndexPage',
        ),
    ]
