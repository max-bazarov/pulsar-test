from django.db import models


class Product(models.Model):
    class Status(models.TextChoices):
        IN_STOCK = 'in stock', 'В наличии'
        FOR_ORDER = 'for order', 'Под заказ'
        WAITING = 'waiting', 'Ожидается'
        NOT_IN_STOCK = 'not in stock', 'Нет в наличии'
        NOT_PRODUCING = 'not producing', 'Не производится'

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=255,
        choices=Status.choices,
        default=Status.IN_STOCK
    )
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name
