# Generated by Django 4.1.3 on 2022-11-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0004_alter_course_id_alter_matriculation_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="image",
            field=models.ImageField(blank=True, upload_to=""),
        ),
    ]