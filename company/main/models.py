from django.db import models

class Worker(models.Model):
    id = models.IntegerField('№', primary_key=True)
    name = models.CharField('Ім’я', max_length=20)
    surname = models.CharField('Прізвище', max_length=20)
    position = models.CharField('Посада', max_length=50)
    salary = models.DecimalField('Зарплата', max_digits=10, decimal_places=2)
    phone = models.CharField('Телефон', max_length=20)
    date_hired = models.DateField('Дата найму')
    is_active = models.BooleanField('Активний', default=False)

    def __str__(self):
        return f"{self.name} {self.surname}"

    def get_absolute_url(self):
        return f'/moderator/workers/{self.id}'

class Project(models.Model):
    id = models.IntegerField('№', primary_key=True)
    name = models.CharField('Назва проекту', max_length=200)
    clients = models.ManyToManyField('Client', related_name='projects', verbose_name='Клієнти')
    workers = models.ManyToManyField('Worker', related_name='projects', verbose_name='Співробітники')
    description = models.TextField('Опис проекту')
    price = models.DecimalField('Ціна', max_digits=10, decimal_places=2)
    status = models.CharField('Статус', choices=[
        ('planned', 'План'),
        ('in_progress', 'В процесі'),
        ('completed', 'Завершено')
    ], default='planned')
    date_created = models.DateField('Дата створення')
    deadline = models.DateField('Термін завершення')

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField('Ім’я', max_length=20)
    surname = models.CharField('Прізвище', max_length=20)
    phone = models.CharField('Телефон', max_length=20)
    date_registered = models.DateField('Дата реєстрації')

    def __str__(self):
        return f"{self.name} {self.surname}"
