from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


def status_validator(order_status):
    if order_status not in ["open", "closed", "in progress", "need info"]:
        raise ValidationError(
            gettext_lazy('%(order_status)s is wrong order status'),
            params={'order_status': order_status},
        )


class Pictures(models.Model):
    """Картины"""

    class Meta:
        db_table = 'pictures'
        verbose_name = 'Доступные картины'
        verbose_name_plural = 'Доступные картины'

    title = models.TextField(verbose_name='Название картины')
    cost = models.TextField(verbose_name='Стоимость')

    def __str__(self):
        return f'{self.title} {self.cost}'


class Customer(models.Model):
    """Покупатели"""

    class Meta:
        db_table = 'customers'
        verbose_name = 'Описание покупателя'
        verbose_name_plural = 'Описание покупателей'

    customer_name = models.TextField(verbose_name='ФИО покупателя')
    customer_address = models.TextField(verbose_name='Адрес')
    customer_city = models.TextField(verbose_name='Город')

    def __str__(self):
        return self.customer_name


class SoldPictures(models.Model):
    """Проданные картины"""

    class Meta:
        db_table = 'sold_pictures'
        verbose_name = 'Проданные картины'
        verbose_name_plural = 'Проданные картины'

    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, verbose_name='Идентификатор покупателя')
    picture = models.ForeignKey(Pictures, on_delete=models.RESTRICT, verbose_name='Идентификатор картины')

    def __str__(self):
        return f'{self.customer} {self.picture}'


class Order(models.Model):
    """Заказы"""

    class Meta:
        db_table = 'orders'
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'

    picture = models.ForeignKey(SoldPictures, verbose_name='Картина', on_delete=models.RESTRICT)
    customer = models.ForeignKey(Customer, verbose_name='Покупатель', on_delete=models.RESTRICT)
    order_description = models.TextField(verbose_name='Описание заказа')
    created_date = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    last_updated_date = models.DateTimeField(verbose_name='Последнее изменение', blank=True, null=True)
    order_status = models.TextField(verbose_name='Статус заказа', validators=[status_validator])

    def save(self, *args, **kwargs):
        self.last_updated_dt = datetime.now()
        super().save(*args, **kwargs)
