# Generated by Django 3.2.9 on 2022-02-13 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20220206_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='profile/default.png', upload_to='profile/'),
        ),
    ]
