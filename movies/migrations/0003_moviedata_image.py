# Generated by Django 4.1.7 on 2023-03-02 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_moviedata_genre"),
    ]

    operations = [
        migrations.AddField(
            model_name="moviedata",
            name="image",
            field=models.ImageField(
                default="Images/None/Noimg.jpg", upload_to="Images/"
            ),
        ),
    ]
