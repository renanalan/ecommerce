#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
from django.db import models

WIDTH = 720
HEIGHT = 480

def upload_to_photo(instance, name):
    type = os.path.splitext(name)[-1]
    date = datetime.datetime.now()
    information = str(date.day) + '_' + str(date.month) + '_' + str(date.year) + '_' + str(date.hour) + '_' + str(
        date.minute) + '_' + str(date.second)
    return os.path.join('product', 'photo', '%s%s' % (information, type))

class Product(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    quantity = models.IntegerField(verbose_name='Quantidade')
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Preço')
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Desconto')
    photo = models.ImageField(upload_to=upload_to_photo, max_length=255, verbose_name=u'Foto', blank=False, null=False)
    date = models.DateTimeField(auto_now_add= True, editable= False, verbose_name= 'Data')

    def __unicode__(self):
        return self.title
# def photo_post_save(signal, instance, sender, **kwargs):
#     arq = Product.objects.get(photo=instance.foto)
#     image = Image.open(arq.foto.path)
#     image_resize = image.resize((WIDTH,HEIGHT), Image.ANTIALIAS)
#     image_resize.save(arq.foto.path, 'JPEG', quality=100)

# def photo_pre_delete(signal, instance, sender, **kwargs):
#     arq = Product.objects.get(photo=instance.foto)
#     if os.path.exists(arq.photo.path):
#         os.remove(arq.photo.path)