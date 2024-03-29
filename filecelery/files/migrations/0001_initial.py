# Generated by Django 4.2.6 on 2023-10-22 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(help_text='Загрузите файл', upload_to='files', verbose_name='Файл')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время загрузки файла')),
                ('processed', models.BooleanField(default=False, verbose_name='Обработан ли файл')),
            ],
        ),
    ]
