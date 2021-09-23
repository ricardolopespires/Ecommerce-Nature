from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 100, unique = True, help_text = " Nome da categoria dos produtos ")
    slug = models.SlugField(max_length = 100, unique = True, help_text = "Slug do nome do produtos ")

    class Meta:
        ordering = ('-name',)


class Product(models.Model):
    category = models.ForeignKey(Category, related_name = "products", on_delete = models.CASCADE, help_text = "categoria do produto")
    name = models.CharField(max_length = 150, unique = True, help_text = "Nome do Produto")
    slug = models.SlugField(max_length = 150, unique = True)
    image = models.ImageField(upload_to = 'products', help_text = "image do Produto")
    description = models.TextField(help_text = "Descrição do Produto")
    shu = models.CharField(max_length = 40, )
    price = models.DecimalField(max_digits = 10, decimal_places = 2, help_text = "O Valor do Produto")
    available  = models.BooleanField(default = True)

    class Meta:
        ordering = ('shu',)
 


