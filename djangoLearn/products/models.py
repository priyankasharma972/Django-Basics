from django.db import models
from django.urls import reverse

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=100)
    description= models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2,max_digits=1000)
    summary= models.TextField(default='Add your product summary here')

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id":self.id}) #Namespace and URL Name(products:product-detail)