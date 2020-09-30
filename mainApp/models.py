from django.db import models

# Create your models here.
class Articlesnew(models.Model):
    title=models.CharField(max_length=120)
    text=models.TextField()
    category=models.TextField()
    views=models.IntegerField()
    img=models.ImageField()
    date=models.DateTimeField()

    def __str__(self):
        return self.title

class Slider_info(models.Model):
    title=models.CharField(max_length=120, verbose_name="Текст заголовка")
    btn_text=models.CharField(max_length=120, verbose_name="Текст кнопки")
    def __str__(self):
        return self.title

class Slider_image(models.Model):
    image = models.ImageField()
    slider_info = models.ForeignKey('Slider_info', on_delete=models.CASCADE)


class Category(models.Model):
    title=models.CharField(max_length=120,verbose_name="Назва категорії")
    slug=models.SlugField(unique=True)
    image = models.ImageField()
    text=models.TextField( verbose_name="Текст статі")
    def __str__(self):
        return self.title

class Mark(models.Model):
    name=models.CharField(max_length=120, verbose_name="Назва мітки")
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title=models.CharField(max_length=120, verbose_name="Заголовок статі")
    text=models.TextField( verbose_name="Текст статі")
    image = models.ImageField()
    slug=models.SlugField()
    category=models.ForeignKey('Category', on_delete=models.CASCADE ,verbose_name="Категорія")
    mark=models.ForeignKey('Mark', on_delete=models.CASCADE, verbose_name="Мітка")
    views=models.IntegerField()
    date=models.DateTimeField()
    def __str__(self):
        return self.title

class Cametn(models.Model):
    autor_name=models.CharField(max_length=120, verbose_name="Імя автора")
    text=models.TextField( verbose_name="Текст")
    articl=models.ForeignKey('Article', on_delete=models.CASCADE,related_name="com")
    


class Email(models.Model):
    name=models.CharField(max_length=120, verbose_name="Імя автора") 
    surname=models.CharField(max_length=120, verbose_name="Прізвище автора") 
    email=models.CharField(max_length=120, verbose_name="Email автора") 