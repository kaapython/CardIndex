from django.db import models

# Create your models here.

class Client(models.Model):
    """
    Личное дело клиента
    """
    last_name = models.CharField(max_length=30) # Фамилия
    first_name = models.CharField(max_length=30) # Имя
    middle_name = models.CharField(max_length=30) # Отчество
    bday = models.DateField(auto_now=False, auto_now_add=False) # Дата рождения
    address = models.CharField(max_length=100) # Адресс проживания

    def __str__(self):
       return self.last_name + ' ' + self.first_name + ' ' + self.middle_name + ' | ' + self.address


class Category(models.Model):
    """
    Категория клиента
    """
    category = models.CharField(max_length=40)  # Категория

    def __str__(self):
        return self.category


class Control(models.Model):
    """
    Контроль за передвижением ЛД
    """
    check_mark = models.CharField(max_length=30) # Статус ЛД

    def __str__(self):
        return self.check_mark


class CardIndex(models.Model):
    """
    Личное дело
    """
    client = models.ForeignKey(Client, verbose_name='Клиент')
    category = models.ForeignKey(Category, verbose_name='Категория клиента')
    control = models.ForeignKey(Control, verbose_name='Движение ЛД')

    def __str__(self):
        return '{}, категория: {}'.format(str(self.client), str(self.category))
