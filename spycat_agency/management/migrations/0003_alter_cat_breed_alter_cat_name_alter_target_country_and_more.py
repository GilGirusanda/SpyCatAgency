# Generated by Django 5.1.3 on 2024-11-28 11:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0002_cat_salary_alter_cat_years_of_experience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cat",
            name="breed",
            field=models.CharField(
                max_length=60,
                validators=[
                    django.core.validators.MinLengthValidator(3),
                    django.core.validators.MaxLengthValidator(60),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="cat",
            name="name",
            field=models.CharField(
                max_length=100,
                validators=[
                    django.core.validators.MinLengthValidator(3),
                    django.core.validators.MaxLengthValidator(100),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="target",
            name="country",
            field=models.CharField(
                max_length=100,
                validators=[
                    django.core.validators.MinLengthValidator(3),
                    django.core.validators.MaxLengthValidator(100),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="target",
            name="name",
            field=models.CharField(
                max_length=100,
                validators=[
                    django.core.validators.MinLengthValidator(3),
                    django.core.validators.MaxLengthValidator(100),
                ],
            ),
        ),
    ]