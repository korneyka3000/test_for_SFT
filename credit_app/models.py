from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class CreditRequest(TimeStampMixin, models.Model):
    contract = models.OneToOneField(
        'Contract',
        on_delete=models.PROTECT,
        null=True,
        related_name='credit_request',
    )

    class Meta:
        db_table = 'credit_request'


class Contract(TimeStampMixin, models.Model):
    number = models.CharField(
        'Номер контракта',
        max_length=150,
        unique=True
    )

    class Meta:
        db_table = 'contract'


class Product(TimeStampMixin, models.Model):
    name = models.CharField('Название', max_length=250, null=False)
    price = models.DecimalField(
        'Цена',
        max_digits=8,
        decimal_places=2,
        null=False
    )
    producer = models.ForeignKey(
        'Producer',
        on_delete=models.PROTECT,
        related_name='products'
    )
    credit_request = models.ForeignKey(
        CreditRequest,
        on_delete=models.PROTECT,
        null=True,
        related_name='products'
    )

    class Meta:
        db_table = 'product'


class Producer(TimeStampMixin, models.Model):
    name = models.CharField('Название', max_length=250, null=False)

    class Meta:
        db_table = 'producer'
