# coding: utf-8
from datetime import datetime

from apps.products.models import Product
from django.db import models

class MailingAddress(models.Model):
    email = models.CharField(
        verbose_name = 'e-mail',
        max_length = 300,
    )
    initials = models.CharField(
        verbose_name = u'инициалы',
        max_length = 300,
    )
    is_active = models.BooleanField(
        verbose_name = 'активен',
        default = True,
    )
    # timestamps
    created_at = models.DateTimeField(
        verbose_name = u'дата создания',
        default = datetime.now(),
        editable = False,
    )
    updated_at = models.DateTimeField(
        verbose_name = u'дата изменения',
        auto_now = True,
    )

    class Meta:
        ordering = ['-created_at', '-id',]
        verbose_name = u'адрес рассылки'
        verbose_name_plural = u'адреса рассылок'

    def __unicode__(self):
        return self.email


class Order(models.Model):
    PAYMENT_TYPE_CHOICES = (
        ('cash', 'наличными'),
        ('credit_card', 'кредиткой'),
    )
    MESSAGE_STATE_CHOICES = (
        ('new', 'новый'),
    )

    product = models.ForeignKey(
        'products.Product',
        verbose_name = 'тип товара',
    )
    product_quantity = models.IntegerField(
        verbose_name = u'количество',
    )
    initials = models.CharField(
        verbose_name = u'инициалы',
        max_length = 300,
    )
    email = models.CharField(
        verbose_name = u'e-mail',
        max_length = 200,
    )
    allow_mailings = models.BooleanField(
        verbose_name = u'разрешение на рассылку',
    )
    city = models.CharField(
        verbose_name = u'город',
        max_length = 200,
    )
    address = models.TextField(
        verbose_name = u'адрес',
    )
    phone = models.CharField(
        verbose_name = u'номер телефона',
        max_length = 200,
    )
    payment_type = models.CharField(
        verbose_name = u'тип платежа',
        max_length = 200,
        choices = PAYMENT_TYPE_CHOICES,
    )
    # пояснение для оплаты наличными
    cash_pay_sum = models.CharField(
        verbose_name = u'сумма наличных для оплаты',
        max_length = 100,
        help_text = 'с какой суммы готовить сдачу',
        blank=True,
    )
    state = models.CharField(
        verbose_name = u'статус обращения',
        max_length = 200,
        choices = MESSAGE_STATE_CHOICES,
        default = 'new',
    )
    # timestamps
    created_at = models.DateTimeField(
        verbose_name = u'дата создания',
        default = datetime.now(),
        editable = False,
    )
    updated_at = models.DateTimeField(
        verbose_name = u'дата изменения',
        auto_now = True,
    )

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super(Order, self).save()
        if is_new:
            if self.allow_mailings:
                self.create_mailing_address(is_active=True)
            else:
                self.create_mailing_address(is_active=False)

    def create_mailing_address(self, is_active):
        MailingAddress.objects.create(email=self.email, is_active=is_active)

    def total(self):
        return self.product.price*self.product_quantity

    class Meta:
        ordering = ['-created_at', '-id',]
        verbose_name = u'заказ'
        verbose_name_plural = u'заказы'

    def __unicode__(self):
        return self.product.title + ' ' + self.initials


class PartnershipOffer(models.Model):
    OFFER_AUTHOR_TYPE_CHOICES = (
        ('doctor', 'врач'),
        ('drugstore', 'аптека'),
    )
    MESSAGE_STATE_CHOICES = (
        ('new', 'новый'),
    )

    title = models.CharField(
        verbose_name = u'ФИО или название',
        max_length = 300,
    )
    offer_author_type = models.CharField(
        verbose_name = u'тип автора предложения',
        max_length = 100,
    )
    email = models.CharField(
        verbose_name = 'e-mail',
        max_length = 200,
    )
    allow_mailings = models.BooleanField(
        verbose_name = u'разрешение на рассылку',
    )
    phone = models.CharField(
        verbose_name = 'телефон',
        max_length = 200,
    )
    message = models.TextField(
        verbose_name = 'текст сообщения'
    )
    state = models.CharField(
        verbose_name = u'статус обращения',
        max_length = 200,
        choices = MESSAGE_STATE_CHOICES,
        default = 'new',
    )
    # timestamps
    created_at = models.DateTimeField(
        verbose_name = u'дата создания',
        default = datetime.now(),
        editable = False,
    )
    updated_at = models.DateTimeField(
        verbose_name = u'дата изменения',
        auto_now = True,
    )

    class Meta:
        ordering = ['-created_at', '-id',]
        verbose_name = u'предложение о сотрудничестве'
        verbose_name_plural = u'предложения о сотрудничестве'

    def __unicode__(self):
        return self.initials


class EntryInSchool(models.Model):
    MESSAGE_STATE_CHOICES = (
        ('new', 'новый'),
    )

    initials = models.CharField(
        verbose_name = u'ФИО',
        max_length = 300,
    )
    email = models.CharField(
        verbose_name = 'e-mail',
        max_length = 200,
    )
    allow_mailings = models.BooleanField(
        verbose_name = u'разрешение на рассылку',
    )
    phone = models.CharField(
        verbose_name = 'телефон',
        max_length = 200,
    )
    message = models.TextField(
        verbose_name = 'цель записи'
    )
    state = models.CharField(
        verbose_name = u'статус обращения',
        max_length = 200,
        choices = MESSAGE_STATE_CHOICES,
        default = 'new',
    )
    # timestamps
    created_at = models.DateTimeField(
        verbose_name = u'дата создания',
        default = datetime.now(),
        editable = False,
    )
    updated_at = models.DateTimeField(
        verbose_name = u'дата изменения',
        auto_now = True,
    )

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super(EntryInSchool, self).save()
        if is_new:
            if self.allow_mailings:
                self.create_mailing_address(is_active=True)
            else:
                self.create_mailing_address(is_active=False)

    def create_mailing_address(self, is_active):
        MailingAddress.objects.create(email=self.email, is_active=is_active)

    class Meta:
        ordering = ['-created_at', '-id',]
        verbose_name = u'обращение для записи в школу'
        verbose_name_plural = u'обращения для записи в школу'

    def __unicode__(self):
        return self.initials


class Question(models.Model):
    MESSAGE_STATE_CHOICES = (
        ('new', 'новый'),
        ('saved', 'сохранен'),
        ('sent', 'отправлен'),
    )

    initials = models.CharField(
        verbose_name = u'ФИО',
        max_length = 300,
    )
    email = models.CharField(
        verbose_name = 'e-mail',
        max_length = 200,
    )
    allow_mailings = models.BooleanField(
        verbose_name = u'разрешение на рассылку',
    )
    question = models.TextField(
        verbose_name = u'вопрос',
    )
    answer = models.TextField(
        verbose_name = u'ответ',
        blank = True,
    )
    send_answer = models.BooleanField(
        verbose_name = u'отправить ответ?',
        default = False,
    )
    state = models.CharField(
        verbose_name = u'статус обращения',
        max_length = 200,
        choices = MESSAGE_STATE_CHOICES,
        default = 'new',
    )
    # timestamps
    created_at = models.DateTimeField(
        verbose_name = u'дата создания',
        default = datetime.now(),
        editable = False,
    )
    updated_at = models.DateTimeField(
        verbose_name = u'дата изменения',
        auto_now = True,
    )

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        if self.send_answer:
            self.send_answer_to()
            self.send_answer = False
            self.state = 'sent'
        else:
            if not is_new:
                self.state = 'saved'
        super(Question, self).save()
        if is_new:
            if self.allow_mailings:
                self.create_mailing_address(is_active=True)
            else:
                self.create_mailing_address(is_active=False)

    def send_answer_to(self):
        pass

    def create_mailing_address(self, is_active):
        MailingAddress.objects.create(email=self.email, is_active=is_active)

    class Meta:
        ordering = ['-created_at', '-id',]
        verbose_name = u'вопрос'
        verbose_name_plural = u'вопросы'

    def __unicode__(self):
        return self.initials
