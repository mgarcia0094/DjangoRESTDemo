from django.db import models

# Create your models here.

class House(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    more_info = models.TextField()
    m2 = models.IntegerField()
    num_bathrooms = models.IntegerField()
    num_bedrooms = models.IntegerField()
    garden = models.BooleanField(default=False, blank=False)
    owner = models.ForeignKey('auth.User', null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']