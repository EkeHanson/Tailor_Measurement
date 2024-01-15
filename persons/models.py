from django.db import models

class Customer(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Measurement(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    
    favorite_style = models.CharField(max_length=100)
    
    # Top Measurements
    round_neck = models.FloatField()
    shoulder = models.FloatField()
    top_length = models.FloatField()
    long_sleeve = models.FloatField()
    short_sleeve = models.FloatField()
    round_sleeve = models.FloatField()
    chest = models.FloatField()
    
    # Down Measurements
    down_length = models.FloatField()
    knee = models.FloatField()
    round_knee = models.FloatField()
    bottom = models.FloatField()
    hip = models.FloatField()
    waist = models.FloatField()
    thigh = models.FloatField()

    def __str__(self):
        return f"Measurements for {self.customer.first_name} {self.customer.last_name}"
