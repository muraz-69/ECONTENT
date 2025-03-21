# Generated by Django 5.1.7 on 2025-03-19 12:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('econtentapp', '0005_climatechangeresource'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='online_courses/covers/')),
                ('file', models.FileField(help_text='Upload PDF or Video', upload_to='online_courses/files/')),
                ('course_type', models.CharField(choices=[('ebook', 'E-Book'), ('video', 'Video')], default='video', max_length=10)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='ebooks/covers/')),
                ('file', models.FileField(help_text='Upload PDF or Video', upload_to='ebooks/files/')),
                ('resource_type', models.CharField(choices=[('ebook', 'E-Book'), ('video', 'Video')], default='ebook', max_length=10)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HealthWellnessResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='health_wellness/images/')),
                ('description', models.TextField()),
                ('resource_type', models.CharField(choices=[('ebook', 'E-Book'), ('video', 'Video')], max_length=10)),
                ('file', models.FileField(upload_to='health_wellness/')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrendyFashionResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('resource_type', models.CharField(choices=[('ebook', 'E-Book'), ('video', 'Video')], max_length=10)),
                ('file', models.FileField(upload_to='trendy_fashion/')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='trendy_fashion/images/')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
