# Generated by Django 4.2.7 on 2023-12-04 14:23

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=200)),
                ('aktif', models.BooleanField(default=True)),
                ('banner_satu', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, scale=None, size=[575, 200], upload_to='gambar/banner', verbose_name='Gambar (575 x 200 pixel)')),
                ('banner_dua', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, scale=None, size=[575, 200], upload_to='gambar/banner', verbose_name='Gambar (575 x 200 pixel)')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Data Kategori',
            },
        ),
        migrations.CreateModel(
            name='Kontak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
                ('no_whatsup', models.PositiveBigIntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('isi', models.TextField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Kontak',
            },
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
                ('keterangan', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('gambar', models.ImageField(null=True, upload_to='gambar/profil', verbose_name='Gambar (1920 x 1200 pixel)')),
                ('tanggal_upload', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Profil',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teks_awal', models.CharField(blank=True, max_length=200, null=True)),
                ('teks_dua', models.CharField(blank=True, max_length=200, null=True)),
                ('teks_tiga', models.CharField(blank=True, max_length=200, null=True)),
                ('gambar_slide', models.ImageField(null=True, upload_to='gambar/slide', verbose_name='Gambar (475 x 880 pixel)')),
                ('aktif', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Slide',
            },
        ),
        migrations.CreateModel(
            name='Statis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alamat_kami', models.TextField(max_length=200, null=True)),
                ('telpon', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Statis',
            },
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_produk', models.CharField(blank=True, max_length=200, null=True)),
                ('gambar', models.ImageField(null=True, upload_to='gambar/banner', verbose_name='Gambar (270 x 250 pixel)')),
                ('gambar_satu', models.ImageField(null=True, upload_to='gambar/banner', verbose_name='Gambar (270 x 250 pixel)')),
                ('gambar_dua', models.ImageField(null=True, upload_to='gambar/banner', verbose_name='Gambar (270 x 250 pixel)')),
                ('gambar_tiga', models.ImageField(null=True, upload_to='gambar/banner', verbose_name='Gambar (270 x 250 pixel)')),
                ('gambar_empat', models.ImageField(null=True, upload_to='gambar/banner', verbose_name='Gambar (270 x 250 pixel)')),
                ('gambar_lima', models.ImageField(null=True, upload_to='gambar/banner', verbose_name='Gambar (270 x 250 pixel)')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('keterangan', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('harga', models.PositiveIntegerField(blank=True, null=True)),
                ('no_whatsup', models.PositiveBigIntegerField(blank=True, null=True)),
                ('tanggal_upload', models.DateTimeField(auto_now_add=True, null=True)),
                ('diskon', models.IntegerField(blank=True, default=0, null=True)),
                ('dibeli', models.IntegerField(blank=True, default=0, null=True)),
                ('aktif', models.BooleanField(blank=True, default=False, null=True)),
                ('keterangan_barang', models.CharField(choices=[('Baru', 'Baru'), ('Lama', 'Lama')], max_length=200, null=True)),
                ('kategori', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='produks', to='nisa.kategori')),
            ],
            options={
                'verbose_name_plural': 'Produk',
            },
        ),
    ]
