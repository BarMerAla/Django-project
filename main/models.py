from django.db import models
from user_auth.forms import User

# Create your models here.

class Catalog(models.Model):
    name = models.CharField(verbose_name = "Название товара", max_length = 70)
    price = models.IntegerField(verbose_name = "Цена")
    photo = models.ImageField(verbose_name = "Фото товара", upload_to = "photo/%Y/%m/%d/", default= "photo/2023/12/05/empty.jpg")
    description = models.TextField(verbose_name = "Описание товара", default = '')
    category = models.ForeignKey('Category', on_delete = models.PROTECT, verbose_name = "Категория", null = True)
    subcategory = models.ForeignKey('SubCategory', on_delete = models.PROTECT, verbose_name = "Субкатегория", null = True)
    brand = models.ForeignKey('Brand', on_delete = models.PROTECT, verbose_name = "Бренд", null = True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['name']

class Category(models.Model):
    name = models.CharField(verbose_name = "Название категории", max_length = 70)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']

class SubCategory(models.Model):
    name = models.CharField(verbose_name = "Название категории", max_length = 70)
        
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Субкатегория"
        verbose_name_plural = "Субкатегории"
        ordering = ['name']    

class Brand(models.Model):
    name = models.CharField(verbose_name = "Название бренда", max_length = 70)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"
        ordering = ['name']    


class Client(models.Model):
    username = models.CharField(verbose_name = "ник клиента", max_length = 70)
    email = models.EmailField(verbose_name = "email клиента", max_length = 70)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"
        ordering = ['username']            

