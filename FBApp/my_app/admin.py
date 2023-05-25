from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class MainPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'under_title','text_on_page','main_logo')
    list_display_links = ('title',)

class SitePoliticsAdmin(admin.ModelAdmin):
    list_display = ('terms_of_use','privacy_policy','cookie_policy')
    list_display_links = ('terms_of_use',)


class UserPhotoUploadModel_2Admin(admin.ModelAdmin):
    list_display = ('image','time_create')
    list_display_links = ('image',)

class UserItemNameUpload_2Admin(admin.ModelAdmin):
    list_display = ('user_item_name','time_create')
    list_display_links = ('user_item_name',)

class ItemsPicsFromNetAdmin(admin.ModelAdmin):
    list_display = ('item_name','get_html_photo','description')
    list_display_links = ('item_name',)

    def get_html_photo(self,object):
        return mark_safe(f'<img src="{object.picture.url}" width=50>')

    get_html_photo.short_description='Изображение'

class DishesAdmin(admin.ModelAdmin):
    list_display = ('dish_name', 'count_persons')
    list_display_links = ('dish_name',)

class InfoAboutDishesAdmin(admin.ModelAdmin):
    list_display = ('name','get_html_photo')
    list_display_links = ('name',)

    def get_html_photo(self,object):
        return mark_safe(f'<img src="{object.img.url}" width=50>')


class SetOfProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'amount','request_time')
    list_display_links = ('product_name',)


class RelevantMarketsAdmin(admin.ModelAdmin):
    list_display = ('market_name',)
    list_display_links = ('market_name',)



admin.site.register(MainPage, MainPageAdmin)
admin.site.register(SitePolitics,SitePoliticsAdmin)
admin.site.register(UserPhotoUploadModel_2,UserPhotoUploadModel_2Admin)
admin.site.register(UserItemNameUpload_2,UserItemNameUpload_2Admin)
admin.site.register(ItemsPicsFromNet,ItemsPicsFromNetAdmin)
admin.site.register(Dishes,DishesAdmin)
admin.site.register(InfoAboutDishes,InfoAboutDishesAdmin)
admin.site.register(SetOfProducts,SetOfProductsAdmin)
admin.site.register(RelevantMarkets,RelevantMarketsAdmin)