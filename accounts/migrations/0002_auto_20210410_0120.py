# Generated by Django 3.1.5 on 2021-04-09 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='galleryPicFour',
            field=models.ImageField(default='default.jpg', upload_to='gallerypics'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='galleryPicOne',
            field=models.ImageField(default='default.jpg', upload_to='gallerypics'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='galleryPicThree',
            field=models.ImageField(default='default.jpg', upload_to='gallerypics'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='galleryPicTwo',
            field=models.ImageField(default='default.jpg', upload_to='gallerypics'),
        ),
    ]
