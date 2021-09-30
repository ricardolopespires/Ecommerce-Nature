from django.core import validators
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 100, unique = True, help_text = " Nome da categoria dos produtos ")
    slug = models.SlugField(max_length = 100, unique = True, help_text = "Slug do nome do produtos ")

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name
 


class Product(models.Model):
    category = models.ForeignKey(Category, related_name = "products", on_delete = models.CASCADE, help_text = "categoria do produto")
    name = models.CharField(max_length = 150, unique = True, help_text = "Nome do Produto")
    slug = models.SlugField(max_length = 150, unique = True)
    image = models.ImageField(upload_to = 'products', help_text = "image do Produto")
    description = models.TextField(help_text = "Descrição do Produto")
    shu = models.CharField(max_length = 40, )
    price = models.DecimalField(max_digits = 10, decimal_places = 2, help_text = "O Valor do Produto")
    available  = models.BooleanField(default = True)

    def get_absolute_url(self):
        return reverse ("produtos:produtos_list_da_categoria", args = [self.slug])

    def get_absolute_url(self):
        return reverse('produtos:details', args=[self.category.slug, self.slug])

    class Meta:
        ordering = ('shu',)


    def __str__(self):
        return self.name
 


class Review(models.Model):
    produto = models.ForeignKey(Product, related_name = 'reviews', on_delete  = CASCADE)
    username = models.CharField(max_length = 150)
    rating = models.IntegerField(

        validators = [
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    texto = models.TextField(blank = True, help_text = "Digite seu comentário")
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-created',]
