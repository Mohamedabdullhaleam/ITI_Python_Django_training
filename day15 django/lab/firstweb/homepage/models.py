from django.db import models
from django.shortcuts import reverse
# Create your models here.

class category (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)  ## blank = for admin panel || null for db
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_all_categorys(cls):
        return cls.objects.all()

    @classmethod
    def get_specific_category(cls, id):
        return cls.objects.get(id=id)
class Course (models.Model):
    name = models.CharField(max_length=100)
    price =models.IntegerField(default=0)
    # image =models.CharField(max_length=100)
    image = models.ImageField(upload_to='web/images/', null=True, blank=True)
    categ = models.ForeignKey(category, null=True, blank=True, on_delete=models.CASCADE,related_name='categories')
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    no_items = models.IntegerField(default=0)


    def __str__(self):
        return self.name

    @classmethod
    def get_all_products(cls):
        return  cls.objects.all()

    @classmethod
    def get_specific_student(cls, id):
        return cls.objects.get(id=id)

    def get_image_url(self):
        return f'/media/{self.image}'

    def get_show_url(self):
        return reverse('products.details', args=[self.id])

    def get_delete_url(self):
        return reverse('products.delete', args=[self.id])

    def get_edit_url(self):
        return reverse('products.edit', args=[self.id])
