# Generated by Django 4.2.3 on 2023-07-22 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_aboutmephoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_future', models.TextField(verbose_name='Напишите блог об вашем ближайшем будущем')),
                ('target_personal_live', models.TextField(verbose_name='Напишите блог об личной жизни')),
                ('target_soul', models.TextField(verbose_name='Напишите блог об состоянии души')),
            ],
        ),
    ]