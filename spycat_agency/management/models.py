from django.db import models
from django.core.validators import (
    MinValueValidator, 
    MinLengthValidator,
    MaxLengthValidator
)

class Cat(models.Model):
    name = models.CharField(max_length=100, validators=[
        MinLengthValidator(3),
        MaxLengthValidator(100)
    ])
    years_of_experience = models.IntegerField(validators=[MinValueValidator(0)])
    breed = models.CharField(max_length=60, validators=[
        MinLengthValidator(3),
        MaxLengthValidator(60)
    ])
    salary = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00,
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return self.name

class Mission(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"Mission for {self.cat.name if self.cat else 'Unassigned Cat'}"

class Target(models.Model):
    mission = models.ForeignKey(Mission, related_name='targets', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, validators=[
        MinLengthValidator(3),
        MaxLengthValidator(100)
    ])
    country = models.CharField(max_length=100, validators=[
        MinLengthValidator(3),
        MaxLengthValidator(100)
    ])
    notes = models.TextField(blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name