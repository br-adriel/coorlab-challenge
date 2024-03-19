from django.db import models

# Create your models here.
class Travel(models.Model):
    name = models.CharField(max_length=60)
    price_confort = models.DecimalField(max_digits=8, decimal_places=2)
    price_econ = models.DecimalField(max_digits=8, decimal_places=2)
    city = models.CharField(max_length=100)
    duration = models.DurationField()
    seat = models.CharField(max_length=10)
    bed = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.city} - {self.name}"
