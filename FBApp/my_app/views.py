import os, glob

import json

from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from rest_framework import generics

from my_app.utils import MutualContext, best_price_identify
from django.views.generic import ListView, CreateView

from .forms import *

from .serializers import MainPageSerializer, SitePoliticsSerializer, ItemsFromNetSerializer

from .tester_for_groceryappNNphoto import TesterForGroceryAppPhoto as NN
from .tester_for_groceryappNN_TEXT import TesterForGroceryAppText as NN_text

from .templatetags.my_app_tags import *

from .parsers import *

from rest_framework.pagination import PageNumberPagination
from .permissions import ReadOnlyPermission

from django.shortcuts import redirect

from .utils import ContextSupervisor, UserAmountConverter

with open('/home/andrey/GroceryAppVol3/FBApp/my_app/prices_store.json') as f:
#with open('/code/prices_store.json') as f:  #for docker image
    store = json.load(f)


class my_appHome(MutualContext, ListView):
    """Класс-обработчик главной страницы приложения"""

    model = MainPage
    template_name = 'my_app/index.html'
    context_object_name = 'content'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='Самые выгодные предложения от супермаркетов')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class PhotoAnswerPage(MutualContext, ListView):
    '''Класс-обработчик для страницы сайта,
    на которой пользователь будет видеть результат ответа приложения.
    '''
    model = UserPhotoUploadModel_2
    template_name = 'my_app/photo_answer.html'
    context_object_name = 'data'

    def NN_works(self):
        '''Метод, загружающий фото пользователя и пропускающий его через НС'''

        user_image = '/home/andrey/GroceryAppVol3/FBApp/media/photos'
        pred = NN()
        result = pred.identify_item(user_image)
        return result

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        context_dict['nn_answer'] = self.NN_works()  # подключение НС:

        # подключение класса, который формирует контекст (цены + инфо о товаре)
        item_context = ContextSupervisor(context_dict['nn_answer'])
        # подключение тега для отображения информации о товаре (изображение и текст)
        context_dict['item_image_for_user'] = item_context.info
        # подключение цен товара
        context_dict['price_from_site_atb'] = item_context.atb_price
        context_dict['price_from_site_eko'] = item_context.eko_price
        context_dict['price_from_site_varus'] = item_context.varus_price
        context_dict['price_from_site_silpo'] = item_context.silpo_price
        context_dict['price_from_site_ashan'] = item_context.ashan_price
        context_dict['price_from_site_novus'] = item_context.novus_price
        context_dict['price_from_site_metro'] = item_context.metro_price
        context_dict['price_from_site_nash_kray'] = item_context.nk_price
        context_dict['price_from_site_fozzy'] = item_context.fozzy_price

        mutual_context_dict = self.get_user_context(title='Результат поиска')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))

    def get_queryset(self):
        '''На странице будем отображать только одну единственную запись,
                которая была добавлена самой последней'''

        return UserPhotoUploadModel_2.objects.latest('time_create')


class ItemNameAnswerPage(MutualContext, ListView):
    '''Класс-обработчик для страницы сайта,
    на которой пользователь будет видеть результат ответа приложения.
    '''
    model = UserItemNameUpload_2
    template_name = 'my_app/text_answer.html'
    context_object_name = 'data'

    def NN_works(self):
        pred = NN_text()
        user_text = self.get_queryset().user_item_name
        result = pred.identify_item(user_text)
        return result

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        context_dict['nn_answer'] = self.NN_works()  # работа НС

        #подключение класса, который формирует контекст (цены + инфо о товаре)
        item_context = ContextSupervisor(context_dict['nn_answer'])
        # подключение тега для отображения информации о товаре (изображение и текст)
        context_dict['item_image_for_user'] = item_context.info
        #подключение цен товара
        context_dict['price_from_site_atb'] = item_context.atb_price
        context_dict['price_from_site_eko'] = item_context.eko_price
        context_dict['price_from_site_varus'] = item_context.varus_price
        context_dict['price_from_site_silpo'] = item_context.silpo_price
        context_dict['price_from_site_ashan'] = item_context.ashan_price
        context_dict['price_from_site_novus'] = item_context.novus_price
        context_dict['price_from_site_metro'] = item_context.metro_price
        context_dict['price_from_site_nash_kray'] = item_context.nk_price
        context_dict['price_from_site_fozzy'] = item_context.fozzy_price

        mutual_context_dict = self.get_user_context(title='Результат поиска')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))

    def get_queryset(self):
        '''На странице будем отображать только одну единственную запись,
        которая была добавлена самой последней'''

        return UserItemNameUpload_2.objects.latest('time_create')


class GetItemNameFromUser(MutualContext, CreateView):
    '''Класс-обработчки в привязке с формой для получения
    изображения от пользователя, его сохранения в БД
    и последующей обработки.'''

    form_class = UploadItemNameForm
    template_name = 'my_app/upload_text_page.html'
    success_url = reverse_lazy('result_with_name')

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='Поиск товара по названию')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class Terms_of_Use(MutualContext, ListView):
    """Класс-обработчик страницы 'Условия использования'."""

    model = SitePolitics
    template_name = 'my_app/terms_of_use.html'
    context_object_name = 'info'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='Условия использования')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class PrivacyPolicy(MutualContext, ListView):
    """Класс-обработчик страницы 'Условия использования'."""

    model = SitePolitics
    template_name = 'my_app/privacy_policy.html'
    context_object_name = 'info'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='Политика конфиденциальности')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class CookiePolicy(MutualContext, ListView):
    """Класс-обработчик страницы 'Политика cookie'."""

    model = SitePolitics
    template_name = 'my_app/cookie_policy.html'
    context_object_name = 'info'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='Политика cookie')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class SearchByPhoto(MutualContext, CreateView):
    '''Класс для поиска товара по фото пользователя'''
    form_class = SearchByPhotoForm
    template_name = 'my_app/search_by_photo.html'
    success_url = reverse_lazy('result_with_photo')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='Поиск по фото')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class Thanksfull(MutualContext, ListView):
    '''Класс для удаления изображения из БД и
    по совместительству страница благодарностей.'''

    template_name = 'my_app/thanksfull.html'
    success_url = reverse_lazy('home')
    model = UserPhotoUploadModel_2

    def get_queryset(self):
        '''В данном методе будет прописана логика удаления загруженного
        пользователем изображения из БД и самого проекта.'''

        # вот тут можно удалить фото из папки
        try:
            for file in glob.glob("/home/andrey/GroceryAppVol3/FBApp/media/photos/user/*"):
                os.remove(file)
        except Exception:
            print("Can't remove users pic from, using this path:"
                  " '/home/andrey/GroceryAppVol3/FBApp/media/photos/user/*'")

        # тут удаляем загруженное фото из БД
        user_pic = UserPhotoUploadModel_2.objects.latest('time_create')
        return user_pic.delete()


class Thanksfull_DELETE_NAME(MutualContext, ListView):
    '''Класс для удаления изображения из БД и
    по совместительству страница благодарностей.'''

    template_name = 'my_app/thanksfull.html'
    success_url = reverse_lazy('home')
    model = UserItemNameUpload_2

    def get_queryset(self):
        '''В данном методе будет прописана логика удаления загруженного
        пользователем названия товара из БД'''

        # тут удаляем загруженное название из БД
        user_item_name = UserItemNameUpload_2.objects.latest('time_create')
        return user_item_name.delete()


class FindYouDishHere(MutualContext, CreateView):
    '''Класс-представление, который использует форму , с помощью
    которой пользователь может выбрать интересующее его блюдо
    и узнать его себестоимость в супермаркетах'''

    form_class = SearchDishesForm
    template_name = 'my_app/dishes.html'
    success_url = reverse_lazy('prices_for_dish')

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='Поиск блюда')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class DishesResult(MutualContext, ListView):
    '''Класс-представление, который ответчает за
     выдачу результат пользователю после поиска блюда'''

    model = Dishes
    template_name = 'my_app/dishes_result.html'
    context_object_name = 'info'

    def calculate_dish_value(self, count_people, parser):
        '''Метод для упрощения кода.Выноисм подсчет стоимости блюда в отельную функцию.'''
        self.value_atb = round(parser * int(count_people), 2)
        self.value_eko = round(parser * int(count_people), 2)
        self.value_varus = round(parser * int(count_people), 2)
        return self.value_atb, self.value_eko, self.value_varus

    def what_dish(self):
        user_dish = self.get_queryset().dish_name
        user_count = self.get_queryset().count_persons
        dish_parser = AllDishParsersVol2()
        if user_dish == "Борщ":
            self.value_atb = dish_parser.dish_red_borsh_parser()[0] * int(user_count)
            self.value_eko = dish_parser.dish_red_borsh_parser()[1] * int(user_count)
            self.value_varus = dish_parser.dish_red_borsh_parser()[2] * int(user_count)
        elif user_dish == 'Вареники с картошкой':
            self.value_atb = dish_parser.dish_vareniki_s_kartoshkoy_parser()[0] * int(user_count)
            self.value_eko = dish_parser.dish_vareniki_s_kartoshkoy_parser()[1] * int(user_count)
            self.value_varus = dish_parser.dish_vareniki_s_kartoshkoy_parser()[2] * int(user_count)
        elif user_dish == 'Вареники с капустой':
            self.value_atb = dish_parser.dish_vareniki_s_kapustoy_parser()[0] * int(user_count)
            self.value_eko = dish_parser.dish_vareniki_s_kapustoy_parser()[1] * int(user_count)
            self.value_varus = dish_parser.dish_vareniki_s_kapustoy_parser()[2] * int(user_count)

        result_atb = self.value_atb
        result_eko = self.value_eko
        result_varus = self.value_varus
        return user_dish, user_count, result_atb, result_eko, result_varus

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        context_dict['user_dish_name'] = self.what_dish()[0]
        # для украинского борща:
        if context_dict['user_dish_name'] == 'Борщ':
            context_dict['user_count_persons'] = self.what_dish()[1]
            context_dict['value_result_atb'] = self.what_dish()[2]
            context_dict['value_result_eko'] = self.what_dish()[3]
            context_dict['value_result_varus'] = self.what_dish()[4]
            context_dict['dish_pic'] = get_borsh_ukr_info
        # для вареников с картошкой
        elif context_dict['user_dish_name'] == 'Вареники с картошкой':
            context_dict['user_count_persons'] = self.what_dish()[1]
            context_dict['value_result_atb'] = self.what_dish()[2]
            context_dict['value_result_eko'] = self.what_dish()[3]
            context_dict['value_result_varus'] = self.what_dish()[4]
            context_dict['dish_pic'] = get_vareniki_s_kartoshkoy_info
        # для вареников с капустой
        elif context_dict['user_dish_name'] == 'Вареники с капустой':
            context_dict['user_count_persons'] = self.what_dish()[1]
            context_dict['value_result_atb'] = self.what_dish()[2]
            context_dict['value_result_eko'] = self.what_dish()[3]
            context_dict['value_result_varus'] = self.what_dish()[4]
            context_dict[
                'dish_pic'] = get_vareniki_s_kartoshkoy_info  # картинка одинакова для вареников с картошкой и капустой

        mutual_context_dict = self.get_user_context(title='Запрашиваемое блюдо')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))

    def get_queryset(self):
        '''На странице будем отображать только одну единственную запись,
        которая была добавлена самой последней'''

        return Dishes.objects.latest('time_create')


class DishesSet(MutualContext, CreateView):
    '''Класс, для страницы, на которой пользователь будет выбирать
    интересующее его блюдо.'''

    form_class = SearchDishesForm
    template_name = 'my_app/dishes_set.html'
    success_url = reverse_lazy('dish_info')

class DishesSetResult(MutualContext, ListView):
    '''Страница для отображения результатов по блюдам'''
    model = Dishes
    template_name = 'my_app/dishes_set_result.html'
    context_object_name = 'info'

    def what_dish(self):
        user_dish = self.get_queryset().dish_name
        user_count = self.get_queryset().count_persons
        return user_dish, user_count

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)

        context_dict['nn_answer'] = self.what_dish()[0]
        # подключение класса, который формирует контекст (цены + инфо о товаре)
        item_context = ContextSupervisor(context_dict['nn_answer'])

        # подключение класса, который формирует контекст (цены + инфо о товаре)
        context_dict['user_count_persons'] = int(self.what_dish()[1])   #количество порций

        # подключение тега для отображения информации о товаре (изображение и текст)
        context_dict['item_info_for_user'] = item_context.info

        #округление до 2 знаков после запятой
        round_num = 2

        # подключение цен товара
        context_dict['price_from_site_atb'] = round(item_context.atb_price * context_dict['user_count_persons'],round_num)
        context_dict['price_from_site_eko'] = round(item_context.eko_price * context_dict['user_count_persons'],round_num)
        context_dict['price_from_site_varus'] = round(item_context.varus_price * context_dict['user_count_persons'],round_num)
        context_dict['price_from_site_silpo'] = round(item_context.silpo_price * context_dict['user_count_persons'],round_num)
        context_dict['price_from_site_ashan'] = round(item_context.ashan_price * context_dict['user_count_persons'],round_num)
        context_dict['price_from_site_novus'] = round(item_context.novus_price * context_dict['user_count_persons'],round_num)
        context_dict['price_from_site_metro'] = round(item_context.metro_price * context_dict['user_count_persons'],round_num)
        context_dict['price_from_site_nash_kray'] = round(item_context.nk_price * context_dict['user_count_persons'],round_num)
        context_dict['price_from_site_fozzy'] = round(item_context.fozzy_price * context_dict['user_count_persons'],round_num)
        context_dict['flag_price'] = (max(
            context_dict['price_from_site_atb'],context_dict['price_from_site_eko'],context_dict['price_from_site_varus'],
            context_dict['price_from_site_silpo'],context_dict['price_from_site_ashan'],context_dict['price_from_site_novus'],
            context_dict['price_from_site_metro'],context_dict['price_from_site_nash_kray'],context_dict['price_from_site_fozzy']
        )) / 100 * 60

        mutual_context_dict = self.get_user_context(title='Цена блюда')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))

    def get_queryset(self):
        '''На странице будем отображать только одну единственную запись,
        которая была добавлена самой последней'''

        return Dishes.objects.latest('time_create')



class ProductsSet(MutualContext, CreateView):
    '''Класс-обработчик для страницы , на которой пользователь
    может собирать продуктовые наборы, вручную написав их в форме заполнения'''
    form_class = AssembleProductSet
    template_name = 'my_app/products_set_main.html'
    success_url = reverse_lazy('items_set')

    def compile_all_user_requests(self):
        """Собираем с помощбю тэга get_product_set_from_data_base
        описание и иозображения для товаров, попавших в продуктовый набор
        пользователя"""
        self.product_order_info = get_product_set_from_data_base
        return self.product_order_info

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # получаем id владельца, кто собирает продуктовый набор(зарегестрированный пользователь)
        self.object.owner = self.request.user.id
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        context_dict['user_item_info'] = self.compile_all_user_requests()
        context_dict['all_markets'] = get_all_markets
        mutual_context_dict = self.get_user_context(title='Продуктовый набор')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class SetResults(MutualContext, ListView):
    '''Класс для удаления пользовательских продуктовых наборов из БД и
    по совместительству страница для выбора маркетов для поиска выгодных цен.'''

    template_name = 'my_app/answer_sets.html'
    success_url = reverse_lazy('home')
    model = SetOfProducts
    context_object_name = 'user_orders'

    #флаг, означающий, что маркет выбран пользователем для формирования цен
    MARKER = 1

    #имена доступных супермаркетов
    __ATB_MARKET = "ATB"
    __EKO_MARKET = "EKO"
    __VARUS_MARKET = "Varus"
    __SILPO_MARKET = "Сильпо"
    __ASHAN_MARKET = "Ашан"
    __NOVUS_MARKET = "Novus"
    __METRO_MARKET = "Metro"
    __NK_MARKET = "Наш Край"
    __FOZZY_MARKET = "Fozzy"

    def NN_works(self):
        '''Подключение НС для текста, которая определяет, какой
        конкретно продукт пользователь добавил в список (название продукта)'''
        pred = NN_text()
        user_orders = self.get_queryset()
        total_product_info = []

        for order in user_orders:

            result = pred.identify_item(order.product_name)
            # добавим цены из БД цен
            # подключение класса, который формирует контекст (цены + инфо о товаре)
            item_context = ContextSupervisor(result)
            atb_price = item_context.atb_price
            eko_price = item_context.eko_price
            varus_price = item_context.varus_price
            silpo_price = item_context.silpo_price
            ashan_price = item_context.ashan_price
            novus_price = item_context.novus_price
            metro_price = item_context.metro_price
            nash_kray_price = item_context.nk_price
            fozzy_price = item_context.fozzy_price
            picture = item_context.info

            #отфильтруем цены. оставим только те цены , которые соответствуют выбранным супермаркетам!
            filtered_prices=[]

            if order.atb_choice==self.MARKER:
                filtered_prices.append((self.__ATB_MARKET,atb_price))
            if order.eko_choice==self.MARKER:
                 filtered_prices.append((self.__EKO_MARKET,eko_price))
            if order.varus_choice==self.MARKER:
                 filtered_prices.append((self.__VARUS_MARKET,varus_price))
            if order.silpo_choice==self.MARKER:
                 filtered_prices.append((self.__SILPO_MARKET,silpo_price))
            if order.ashan_choice==self.MARKER:
                 filtered_prices.append((self.__ASHAN_MARKET,ashan_price))
            if order.novus_choice==self.MARKER:
                 filtered_prices.append((self.__NOVUS_MARKET,novus_price))
            if order.metro_choice==self.MARKER:
                 filtered_prices.append((self.__METRO_MARKET,metro_price))
            if order.nash_kray_choice==self.MARKER:
                 filtered_prices.append((self.__NK_MARKET,nash_kray_price))
            if order.fozzy_choice==self.MARKER:
                 filtered_prices.append((self.__FOZZY_MARKET,fozzy_price))

            print('Отфильтрованный список цен',filtered_prices)

            #определяем лучшую цену:
            best_price=best_price_identify(filtered_prices)
            print('Best price: ',best_price)

            # new
            mul_amount = UserAmountConverter(order.amount).convert_str_to_num()
            # end

            total_product_info.append(
                {result: [
                    order.amount, order.atb_choice, order.eko_choice, order.varus_choice,
                    order.silpo_choice, order.ashan_choice, order.novus_choice, order.metro_choice,
                    order.nash_kray_choice, order.fozzy_choice, round(atb_price * mul_amount,2),
                    round(eko_price * mul_amount,2),round(varus_price * mul_amount,2),
                    round(silpo_price * mul_amount,2),round(ashan_price * mul_amount,2),
                    round(novus_price * mul_amount,2),round(metro_price * mul_amount,2),
                    round(nash_kray_price * mul_amount,2),round(fozzy_price * mul_amount,2),
                    picture, best_price
                ]}
            )

        return total_product_info

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        context_dict['all_relevant_markets'] = get_all_markets
        # отображение списка кортежей с полной информацией по заказу
        context_dict['products_set']  = self.NN_works()
        mutual_context_dict = self.get_user_context(title='Результаты по наборам')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))

    def get_queryset(self):
        '''На странице будем отображать только те записи из БД,
         которые принадлежат текущему пользователю'''

        return super().get_queryset().filter(owner=self.request.user.id)

#delete order from set
def delete_product(request, order_id):
    '''Метод для удаления заказов в списке покупок'''
    order = SetOfProducts.objects.get(pk = order_id)
    order.delete()
    return redirect("items_set")


class Thanksfull_DELETE_SET(MutualContext, ListView):
    '''Класс для удаления продуктовых наборов из БД и
    по совместительству страница благодарностей.'''

    template_name = 'my_app/thanksfull.html'
    success_url = reverse_lazy('home')
    model = SetOfProducts

    def get_queryset(self):
        '''В данном методе будет прописана логика удаления загруженного
        пользователем названия товара из БД'''

        # тут удаляем загруженное название из БД айдишнюку текущего пользователя
        user_id = super().get_queryset().filter(owner=self.request.user.id)
        return user_id.delete()


class UserRegistration(MutualContext, CreateView):
    '''Класс для регистрации пользователей на сайте'''
    form_class = UserRegisterForm
    template_name = 'my_app/user_registration.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        context_dict['all_relevant_markets'] = get_all_markets
        mutual_context_dict = self.get_user_context(title='Регистрация')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))

    def form_valid(self, form):
        '''Автоматическая авторизация пользователя
         при его успешной регистрации'''
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    '''Класс для авторизации пользователя'''
    form_class = LoginForm
    template_name = 'my_app/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def pageNotFound(request, exception):
    '''Функция-обработчик для запросов несуществующих страниц приложения'''
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# Далее идут обработчики для REST API!!!
class MainPageAPI(generics.ListAPIView):
    '''Обработчик для предоставления данных из БД по главной странице приложения.
    Работает только для GET-запросов со стороны клиента.'''

    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer


class SitePoliticsAPI(generics.ListAPIView):
    '''Обработчик для предоставления данных из БД по
    условиям пользовательских соглашений.
    Работает только для get-запросов со стороны клиента.'''

    queryset = SitePolitics.objects.all()
    serializer_class = SitePoliticsSerializer


class ItemsInfoAPIPagination(PageNumberPagination):
    '''Класс пагинации для представления ItemsInfoAPI'''

    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 50


class ItemsInfoAPI(generics.ListAPIView):
    """Обработчик для предоставлений из БД
    информации о продуктах, которые может обрабатывать
    приложение(название товара, фото и описание)"""

    queryset = ItemsPicsFromNet.objects.all()
    serializer_class = ItemsFromNetSerializer

    pagination_class = ItemsInfoAPIPagination
    permission_classes = (ReadOnlyPermission,)


