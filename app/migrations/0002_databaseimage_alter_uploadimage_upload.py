# Generated by Django 5.0 on 2024-01-16 03:13

import app.utils.path_and_rename
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DatabaseImage",
            fields=[
                ("index", models.AutoField(primary_key=True, serialize=False)),
                ("url", models.URLField()),
                ("category", models.CharField(max_length=50)),
                ("gender", models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name="uploadimage",
            name="upload",
            field=models.ImageField(upload_to=app.utils.path_and_rename.generate_name),
        ),
    ]
