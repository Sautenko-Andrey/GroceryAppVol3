from django.db import models
from django.contrib.auth.models import User

class MainPage(models.Model):
    '''Модель для контента главной страницы приложения.
    Применяется заголовок, подзаголовок,текст и брендовый значок приложения.'''

    title = models.CharField(max_length=100)
    under_title=models.CharField(max_length=100,null=True)
    text_on_page = models.TextField(blank=True)
    main_logo=models.ImageField(upload_to='media/%Y/%m/%d/',null=True)

    class Meta:
        verbose_name = 'Контент главной страницы'
        verbose_name_plural = 'Контент главной страницы'


class SitePolitics(models.Model):
    '''Модель пользовательских соглашений,
    включающая "Условия пользования", "Политику конфиденциальности" и "Поилитку cookie".'''

    terms_of_use=models.TextField()
    privacy_policy=models.TextField()
    cookie_policy=models.TextField()

    class Meta:
        verbose_name='Пользовательские соглашения'
        verbose_name_plural='Пользовательские соглашения'

class UserPhotoUpload(models.Model):
    """Модель, которая будет сохранять в базе данных
    загруженные пользователем изображения товара,
    для дальнейшей их обработки и дообучения НС"""

    user_image=models.ImageField(null=True)

    class Meta:
        verbose_name = 'Изображение пользователя'
        verbose_name_plural = 'Изображение пользователя'


class UserItemNameUpload_2(models.Model):
    """Модель, которая будет сохранять в базе данных
    загруженные пользователем названия товара,
    для дальнейшей их обработки и дообучения НС"""

    user_item_name=models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Название товара пользователя_2'
        verbose_name_plural = 'Название товара пользователя_2'


class UserPhotoUploadModel_2(models.Model):
    "Рабочая модель для пользовательских фотографий 2-я!!!"
    image=models.ImageField(null=True, upload_to='photos/user/')
    time_create=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Фото пользователя2'
        verbose_name_plural = 'Фото пользователя2'
        ordering = ['-id']


class ItemsPicsFromNet(models.Model):
    '''Модель, в которой будут храниться изображения товаров,
    которые мы сможем отображать по запросу пользователя,
    если он ищет товар в ручную,а не по фотографиям.
    Т.е. тут просто будут храниться изображения продуктов и напитков,
    которые я скачаю из сети.'''

    item_name=models.CharField(max_length=150, null=True)
    picture=models.ImageField()
    description=models.TextField(null=True)
    class Meta:
        verbose_name = 'Изображения из сети'
        verbose_name_plural = 'Изображения из сети'


class Dishes(models.Model):
    dish_name=models.CharField(max_length=100)
    count_persons=models.CharField(max_length=2)
    time_create=models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name='Поиск блюд'
        verbose_name_plural='Поиск блюд'

class SetOfProducts(models.Model):
    product_name=models.CharField(max_length=150)
    amount=models.CharField(max_length=20)
    request_time=models.DateTimeField(auto_now_add=True)
    atb_choice=models.BooleanField(null=True)
    eko_choice=models.BooleanField(null=True)
    varus_choice=models.BooleanField(null=True)
    silpo_choice=models.BooleanField(null=True)
    ashan_choice=models.BooleanField(null=True)
    novus_choice=models.BooleanField(null=True)
    metro_choice=models.BooleanField(null=True)
    nash_kray_choice=models.BooleanField(null=True)
    fozzy_choice=models.BooleanField(null=True)
    owner=models.IntegerField(blank=False)

    def __str__(self):
        return self.product_name


    class Meta:
        verbose_name='Набор продуктов'
        verbose_name_plural='Набор продуктов'

class InfoAboutDishes(models.Model):
    '''Модель дляадминистратора сайта,
     которая хранит информацию о доступных для поиска блюдах .
     Добавлять инфу можно через админ-панель.'''

    name=models.CharField(max_length=100,verbose_name='Название блюда')
    img=models.ImageField(verbose_name='Изображение блюда')


    class Meta:
        verbose_name = 'Информация о блюдах'
        verbose_name_plural = 'Информация о блюдах'


class RelevantMarkets(models.Model):
    '''Модель для добавления маркетов'''
    market_name=models.CharField(max_length=25,verbose_name='Название маркета')

    class Meta:
        verbose_name = 'Досутпные супермаркеты'
        verbose_name_plural= 'Досутпные супермаркеты'







