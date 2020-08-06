from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.

PRODUCT_CHOICES = [('Men', 'Men'), ('Women', 'Women'), ('Kids', 'Kids')]

class Product(models.Model):
    title = models.CharField(max_length=50)
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=10, choices=PRODUCT_CHOICES)
    slug = models.SlugField(max_length=75, unique=True)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='products/cover_images')
    image1 = models.ImageField(upload_to='products/images', null=True, blank=True)
    image2 = models.ImageField(upload_to='products/images', null=True, blank=True)
    rating = models.DecimalField(max_digits=2, default=4.5, decimal_places=1)
    ratings_quantity = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    # Creating a unique slug for each product
    def _create_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    # Overriding save method to save the unique slug for the product
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._create_unique_slug()
        super().save(*args, **kwargs)
