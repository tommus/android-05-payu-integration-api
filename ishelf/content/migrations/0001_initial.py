# Generated by Django 2.0.7 on 2018-07-19 19:35

from django.db import migrations, models
import django.db.models.deletion
import ishelf.content.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=127, verbose_name='First name')),
                ('last_name', models.CharField(max_length=127, verbose_name='Last name')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=255, verbose_name='Subtitle')),
                ('published', models.DateTimeField(verbose_name='Published')),
                ('regular_price', models.PositiveIntegerField(verbose_name='Regular price')),
                ('discount_price', models.PositiveIntegerField(verbose_name='Discount price')),
                ('description', models.TextField(max_length=1023, verbose_name='Description')),
                ('isbn', models.CharField(max_length=127, verbose_name='ISBN')),
                ('pages', models.IntegerField(default=1, verbose_name='Pages')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('cover', models.ImageField(blank=True, upload_to=ishelf.content.models.book_media_directory)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Author', verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['id'],
            },
        ),
    ]