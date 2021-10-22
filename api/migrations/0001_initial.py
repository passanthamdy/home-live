# Generated by Django 3.2.8 on 2021-10-21 11:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('body_en', models.TextField(blank=True, null=True)),
                ('title_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('body_ar', models.TextField(blank=True, null=True)),
                ('number_of_project', models.IntegerField(blank=True, null=True)),
                ('number_of_Awards', models.IntegerField(blank=True, null=True)),
                ('Years_of_experience', models.IntegerField(blank=True, null=True)),
                ('number_of_client', models.IntegerField(blank=True, null=True)),
                ('about_image', models.ImageField(blank=True, max_length=254, null=True, upload_to='Home/')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name_en', models.CharField(max_length=255)),
                ('client_name_ar', models.CharField(max_length=255)),
                ('review_message_en', models.TextField(blank=True, null=True)),
                ('review_message_ar', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, max_length=254, null=True, upload_to='Home/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('title_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('videofile', models.FileField(null=True, upload_to='videos/', verbose_name='')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin_url', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=255, null=True)),
                ('slider_img1', models.ImageField(blank=True, null=True, upload_to='')),
                ('slider_img2', models.ImageField(blank=True, null=True, upload_to='')),
                ('slider_img3', models.ImageField(blank=True, null=True, upload_to='')),
                ('slider_text_en', models.CharField(blank=True, max_length=255, null=True)),
                ('slider_text_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('slider_header_en', models.CharField(blank=True, max_length=255, null=True)),
                ('slider_header_ar', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='mision_vision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=255)),
                ('title_ar', models.CharField(max_length=255)),
                ('body_en', models.TextField(blank=True, null=True)),
                ('body_ar', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='product_video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_1', models.FileField(null=True, upload_to='videos/', verbose_name='')),
                ('video_2', models.FileField(null=True, upload_to='videos/', verbose_name='')),
                ('video_3', models.FileField(null=True, upload_to='videos/', verbose_name='')),
                ('video_4', models.FileField(null=True, upload_to='videos/', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, max_length=254, null=True, upload_to='Home/')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=255)),
                ('title_ar', models.CharField(max_length=255)),
                ('body_en', models.TextField(blank=True, null=True)),
                ('body_ar', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=150)),
                ('name_ar', models.CharField(max_length=150)),
                ('img', models.ImageField(upload_to='product/')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=150)),
                ('name_ar', models.CharField(max_length=150)),
                ('description_en', models.TextField(blank=True)),
                ('description_ar', models.TextField(blank=True)),
                ('img_slider', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('img_description', models.ImageField(blank=True, null=True, upload_to='product/')),
            ],
        ),
        migrations.CreateModel(
            name='why_home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=255)),
                ('title_ar', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductTuya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=300)),
                ('name_ar', models.CharField(max_length=300)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_ar', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=300)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('videofile', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('SubCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subcategory')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tag')),
            ],
        ),
        migrations.CreateModel(
            name='ProductHdl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=300)),
                ('name_ar', models.CharField(max_length=300)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_ar', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=150)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('videofile', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('SubCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subcategory')),
            ],
        ),
    ]