# Generated by Django 4.1.2 on 2022-10-25 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0006_remove_course_date_upload_remove_course_upload_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='cover_image',
            field=models.ImageField(null=True, upload_to='file/covers'),
        ),
    ]
