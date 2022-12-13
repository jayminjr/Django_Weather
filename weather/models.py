from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_expired = models.BooleanField(default=False)

    class Meta:
        abstract = True


class City(BaseModel):
    name = models.CharField(max_length=25)
    temperature = models.CharField(max_length=25, default="")
    min_temp = models.CharField(max_length=25, default="")
    max_temp = models.CharField(max_length=25, default="")
    wind_speed = models.CharField(max_length=25, default="")
    humidity = models.CharField(max_length=25, default="")
    next_min_temp = models.CharField(max_length=25, default="")
    next_max_temp = models.CharField(max_length=25, default="")

    def __str__(self):
        return self.name
