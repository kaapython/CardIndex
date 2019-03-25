from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class UsersProfile(models.Model):
    """
    Профили сотрудников
    """

    user = models.OneToOneField(User, null=True, blank=True, help_text='Ссылка на Django-аккаунт')
    fio = models.CharField(max_length=255, help_text='ФИО')


    def get_fio(self, dots=True):
        """
        Функция формирования фамилии и инициалов (Иванов И.И.)
        :param dots:
        :return:
        """
        fio = self.fio.replace("  ", " ").strip()
        fio_split = fio.split(" ")

        if len(fio_split) == 0:
            fio_split.append("")
        if len(fio_split) == 1:
            fio_split.append("")
        if len(fio_split) == 2:
            fio_split.append("")

        if dots:
            return fio_split[0] + " " + fio_split[1][0] + "." + fio_split[2][0] + "."
        return fio_split[0] + " " + fio_split[1][0] + fio_split[2][0]


    def is_member(self, groups: list) -> bool:
        """
        Проверка вхождения пользователя в группу
        :param group: название группы
        :return: bool, входит ли в указаную группу
        """
        return self.user.groups.filter(name__in=groups).exists()

    def __str__(self):  # Получение фио при конвертации объекта UsersProfile в строку
        return self.fio