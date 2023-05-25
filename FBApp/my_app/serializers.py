from rest_framework import serializers

from .models import MainPage, SitePolitics, ItemsPicsFromNet

class MainPageSerializer(serializers.ModelSerializer):
    '''Сериализатор для главной страницы.
    Трансформирует данные в JSON-строку.
    Предоставляем данные о заголовке, подзаголовке и тексте.'''

    class Meta:
        model = MainPage
        fields = ('title', 'under_title', 'text_on_page')

class SitePoliticsSerializer(serializers.ModelSerializer):
    '''Сериализатор для страниц пользовательских соглашений,
    предоставляет данные об "Условиях пользования",
    "Политики конфиденциальности" и "Политики cookie".'''

    class Meta:
        model=SitePolitics
        fields=('terms_of_use','privacy_policy','cookie_policy')

class ItemsFromNetSerializer(serializers.ModelSerializer):
    '''Сериализатор для информации о продуктах'''

    class Meta:
        model=ItemsPicsFromNet
        fields=('item_name','picture','description')
