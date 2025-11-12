from django.db import models

# Create your models here.

class Settings(models.Model):
    title = models.CharField(max_length=50,verbose_name = "Название")
    description = models.TextField(verbose_name = "Описание")
    logo = models.ImageField(upload_to="logo",verbose_name = "Логотип")
    phone_number = models.CharField(max_length=15,verbose_name = "Номер телефона")
    email = models.EmailField(verbose_name = "Почта")
    address = models.CharField(max_length=100,verbose_name = "Адрес")
    work_time = models.CharField(max_length=30,verbose_name = "Рабочее время")
    facebook = models.URLField(verbose_name = "Facebook",blank=True,null =True)
    instagram = models.URLField(verbose_name = "Instagram",blank=True,null =True)
    linkedin = models.URLField(verbose_name = "Linkedin",blank=True,null =True)   
    
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"