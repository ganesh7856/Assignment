from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    view_count = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name




class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products',null=True)
    #category = models.ManyToManyField(Category, related_name='Cate', null=True)
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200)
    description = models.TextField(max_length=500, default="Empty description.")
    picture = models.ImageField(upload_to="products/images", null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    quantity = models.IntegerField(default=10)
    view_count = models.IntegerField(default=None,null=True)


    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
