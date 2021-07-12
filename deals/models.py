from django.db import models

# Create your models here.

class Deal(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    agency = models.CharField(max_length=100)
    dt_created = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    no_bedrm = models.IntegerField()
    no_bathrm = models.IntegerField()
    size = models.DecimalField(max_digits=10, decimal_places=2)
    img1 = models.URLField(blank=True)
    img2 = models.URLField(blank=True)
    img3 = models.URLField(blank=True)

    def __str__(self):
        return self.title