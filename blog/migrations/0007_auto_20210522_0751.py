# Generated by Django 3.1.7 on 2021-05-22 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210520_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=models.TextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.category'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title_tag',
            field=models.CharField(max_length=255, verbose_name='title tag'),
        ),
    ]