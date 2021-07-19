from django.db import models

# Create your models here.
class Product(models.Model):
    #title = models.TextField()
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10000,decimal_places=2)
    summary = models.TextField(max_length=120)

    upload = models.FileField(blank=True,upload_to='uploads/')
    # or...
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    #upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
