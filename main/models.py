# coding=utf-8
from django.db import models
from users.models import UsersProfile

# Create your models here.

class Client(models.Model):
    """
    Личное дело клиента
    """
    last_name = models.CharField(max_length=30, help_text='Фамилия') # Фамилия
    first_name = models.CharField(max_length=30, help_text='Имя') # Имя
    middle_name = models.CharField(max_length=30, help_text='Отчество') # Отчество
    bday = models.DateField(auto_now=False, auto_now_add=False, help_text='Дата рождения') # Дата рождения
    address = models.CharField(max_length=100, help_text='Адрес проживания') # Адрес проживания

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
    category = models.CharField(max_length=40, help_text='Категория клиента')  # Категория граждан

    def __str__(self):
        return self.category


class Control(models.Model):
    """
    Контроль за передвижением ЛД
    """
    check_mark = models.CharField(max_length=30, help_text='Движение ЛД') # Перемещение ЛД

    def __str__(self):
        return self.check_mark


class CardIndex(models.Model):
    """
    Личное дело
    """
    ipd = models.IntegerField(verbose_name='Индивидуальное порядковое дело', help_text='ИПД')
    client = models.ForeignKey(Client, verbose_name='Клиент', help_text='Клиент')
    category = models.ForeignKey(Category, verbose_name='Категория клиента', help_text='Категория клиента')
    control = models.ForeignKey(Control, verbose_name='Статус ЛД', help_text='Статус ЛД')
    spec = models.ForeignKey(UsersProfile, default="в архиве", blank=True, null=True,
                             verbose_name='Движение ЛД по специалистам', help_text='Движение ЛД')
    info = models.CharField(max_length=200, blank=True, verbose_name='Движение ЛД по другим УСЗН',
                            help_text='Движение по др. УСЗН.')

    def __str__(self):
        return '{} {}'.format(self.ipd, self.client)

class Query(models.Model):
    """
    Запрос специалиста на работу с ЛД
    """
    query_client = models.ForeignKey(CardIndex, null=True, help_text='* Личное дело')
    query_spec = models.ForeignKey(UsersProfile, null=True, help_text='* Специалист')
    query_ld = models.BooleanField(default=False, blank=False, help_text='* Статус запроса')
    query_date = models.DateField(default=None, null=True, help_text='* Дата запроса (01.01.2019)')