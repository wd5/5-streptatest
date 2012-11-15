# -*- coding: utf-8 -*-
import datetime
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User, UserManager

class CustomUserManager(UserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given username, e-mail and password.
        """
        now = datetime.datetime.now()

        # Normalize the address by lowercasing the domain part of the email
        # address.
        if email:
            try:
                email_name, domain_part = email.strip().split('@', 1)
            except ValueError:
                pass
            else:
                email = '@'.join([email_name, domain_part.lower()])
        else:
            email = ''

        user = self.model(username=username, email=email, is_staff=False,
                         is_active=True, is_superuser=False, last_login=now,
                         date_joined=now)

        user.set_password(password)
        user.save(using=self._db)
        return user

sex_choices = (
    (u'male', u'Мужской'),
    (u'female', u'Женский'),
)

class CustomUser(User):
    """User with app settings."""
    third_name = models.CharField(max_length=20, verbose_name=u'отчество', blank=True)
    phone = models.CharField(max_length=20, verbose_name=u'телефон', blank=True)
    b_day = models.DateField(verbose_name=u'дата рождения', default=datetime.date.today)
    sex = models.CharField(max_length=30, verbose_name=u'Пол', choices=sex_choices, default='female' )

    # Use UserManager to get the create_user method, etc.
    objects = CustomUserManager()

    class Meta:
        verbose_name = u'пользователь'
        verbose_name_plural = u'пользователи'

    def get_addresses(self):
        return self.customuseraddress_set.order_by('city')

    def get_orders(self):
        return self.order_set.all()

    def get_name(self):
        if self.get_name:
            return '%s %s %s' %(self.first_name, self.last_name, self.third_name)
        else:
            return '%s %s' %(self.first_name, self.last_name)

class CustomUserAddress(models.Model):
    user =  models.ForeignKey(User, verbose_name=u'пользователь')
    city = models.CharField(max_length=255, verbose_name=u'Адрес')
    street = models.CharField(max_length=255, verbose_name=u'Улица, Дом, Квартира')

    class Meta:
        verbose_name =_(u'profile_addres')
        verbose_name_plural =_(u'profile_addreses')

    def __unicode__(self):
        return u'%s %s' % (self.city, self.street)



