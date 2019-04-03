# coding=utf-8
from django.db import models
from users.models import UsersProfile

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

    def fio(self) -> str:
        """
        Функция возврата полного ФИО
        :return: Полное ФИО
        """
        return '{} {} {}'.format(self.last_name, self.first_name, self.middle_name)

    def shortfio(self, supershort=False) -> str:
        """
        Функция возврата сокращенного ФИО
        :return: Короткое ФИО
        """
        if self.middle_name and len(self.middle_name) > 0:
            r = '{} {}.{}.'.format(self.last_name, self.first_name[0], self.middle_name[0])
        else:
            r = '{} {}.'.format(self.last_name, self.first_name[0])
        if supershort:
            r = r.replace(". ", "").replace(".", "")
        return r

    def __str__(self):
        return self.fio()


class Category(models.Model):
    """
    Категория клиента
    """
    category = models.CharField(max_length=40)  # Категория граждан

    def __str__(self):
        return self.category


class Control(models.Model):
    """
    Контроль за передвижением ЛД
    """
    check_mark = models.CharField(max_length=30) # Перемещение ЛД

    def __str__(self):
        return self.check_mark


class CardIndex(models.Model):
    """
    Личное дело
    """
    ipd = models.IntegerField(verbose_name='Индивидуальное порядковое дело')
    client = models.ForeignKey(Client, verbose_name='Клиент')
    category = models.ForeignKey(Category, verbose_name='Категория клиента')
    control = models.ForeignKey(Control, verbose_name='Статус ЛД')
    spec = models.ForeignKey(UsersProfile, default="в архиве", blank=True, verbose_name='Движение ЛД по специалистам')
    info = models.CharField(max_length=200, blank=True, verbose_name='Движение ЛД по другим УСЗН')

    def __str__(self):
        return '{} {}'.format(self.ipd, self.client)