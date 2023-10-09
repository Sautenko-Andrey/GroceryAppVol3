import json
from .templatetags.my_app_tags import *

from .items_full_names import *

#for local
# try:
#     with open('/home/andrey/GroceryAppVol3/FBApp/my_app/prices_store.json') as f:
#         store = json.load(f)
# except Exception:
#     print("I can't open data base with prices. Check path:"
#           " '/home/andrey/GroceryAppVol3/FBApp/my_app/prices_store.json'")

#for docker
# try:
#     with open('prices_store.json') as f:
#         store = json.load(f)
# except Exception:
#     print("I can't open data base with prices. Change or check path:"
#           " '../prices_store.json'")

#new prices storage
try:
    with open('./overall_prices.json') as f:
        store = json.load(f)
except Exception:
    print("I can't open data base with prices. Change or check path:"
          " './overall_prices.json'")

#new prices storage for docker image
# try:
#     with open('overall_prices.json') as f:
#         store = json.load(f)
# except Exception:
#     print("I can't open data base with prices. Change or check path:"
#           " './overall_prices.json'")


class MutualContext:
    def get_user_context(self, **kwargs) -> dict:
        context = kwargs
        return context


def make_list(count: int, pos: int) -> list:
    '''Метод для создания вложенного списка для обучающей выборки в тестовой НС'''
    # проверяем аргументы на принадлежность к типу int:
    if type(count) != int or type(pos) != int:
        raise TypeError("Arguments count and pos for function 'make_list' must be int!")
    # создаем вложенный список:
    res = [[0 for x in range(count)]]
    res[0][pos] = 1
    return res


def price_updating_data(price: float) -> float:
    '''Функция для корректировки отображения нестандартных записей цен на сайтах'''

    # делаем проверку, что аргумент price является вещественным числом
    # if type(price) != float:
    # raise TypeError("Argument price for function 'price_updating_data' must be float")

    price = price[:5]
    try:
        price = float(price.replace(',', '.'))
    except Exception:
        print('Короткая цена!')
        price = float(price[:2])
    return price


def best_price_identify(prices_array: list) -> str:
    '''В prices_array нам поступают все цены из БД.А нам надо определить
    минимальную из тех маркетов, которые выбрал пользователь.'''

    # проверяем, что на вход функция получает список:
    if type(prices_array) != list:
        raise TypeError("Argument for function 'best_price_identify' must be list!")

    # очищаем от цен, которых нет в магазине
    clear_list = tuple(x for x in prices_array if type(x[1]) == float)
    # определяем лучшую цену
    # проверяем пуст списо с ценами или нет
    value_only = []
    for i in clear_list:
        value_only.append(i[1])

    if len(value_only) > 0:
        best_price = min(value_only)
    else:
        best_price = 0

    respond = '---'
    for index, value in enumerate(prices_array):

        if value[1] == best_price:
            respond = f'{value[0]} {best_price} грн'

    return respond


class ContextSupervisor:
    '''Класс, благодаря которму убирается дублирование кода в context_dict
    для отвтеов по фото и тексту.'''

    __slots__ = ("atb_price", "eko_price", "varus_price",
        "silpo_price", "ashan_price", "novus_price",
        "metro_price", "nk_price", "fozzy_price","info")

    # сообщения об отсутствии цены в БД.
    ATB_WARNING_MESSAGE = 'Цена в АТБ отсутствует в БД.'
    EKO_WARNING_MESSAGE = 'Цена в EKO отсутствует в БД.'
    VARUS_WARNING_MESSAGE = 'Цена в Varus отсутствует в БД.'
    SILPO_WARNING_MESSAGE = 'Цена в Сильпо отсутствует в БД.'
    ASHAN_WARNING_MESSAGE = 'Цена в Ашане отсутствует в БД.'
    NOVUS_WARNING_MESSAGE = 'Цена в Novus отсутствует в БД.'
    METRO_WARNING_MESSAGE = 'Цена в Metro отсутствует в БД.'
    NK_WARNING_MESSAGE = 'Цена в Наш Край отсутствует в БД.'
    FOZZY_WARNING_MESSAGE = 'Цена в Fozzy отсутствует в БД.'

    # переменные-ключи для маркетов
    __ATB_KEY = 'atb'
    __EKO_KEY = 'eko'
    __VARUS_KEY = 'varus'
    __SILPO_KEY = 'silpo'
    __ASHAN_KEY = 'ashan'
    __NOVUS_KEY = 'novus'
    __METRO_KEY = 'metro'
    __NK_KEY = 'nash_kray'
    __FOZZY_KEY = 'fozzy'

    # флаг, означающий, что для товара нет парсеров и цен в БД
    NO_PRICES = 'absent'

    # минимальная длина строки метки из БД
    __MIN_SAMPLE_LENGTH = 3

    # флаг для проверки существования тэга
    __NO_TAG = True

    @classmethod
    def __verify_sample(cls, sample):
        """Метод, выполняющий проверку корректности метки продукта в БД."""
        if type(sample) != str:
            raise TypeError("Sample has to be str type!")
        if len(sample) < cls.__MIN_SAMPLE_LENGTH:
            raise TypeError("Product's sample length is suspicious short!")

    @classmethod
    def __verify_tag(cls, tag):
        '''Метод проверяющий корректность тэга (его существование)'''
        if not cls.__NO_TAG:
            raise AttributeError("Tag absents!")

    def getting_prices(self, item_sample_DB, item_tag):
        '''Метод, который пытается взять цену из БД.
        Также подключается тег продукта (тег , который берет изображение и текст описания товара из БД).
        Возвращаемые значения уже передаются в метод
        products_context_maker для дальнейшей обработки.'''

        # совершаем проверку метки из БД как аргумента
        self.__verify_sample(item_sample_DB)

        # сделаем проверку существования тэга
        self.__verify_tag(item_tag)

        # делаем проверку, что если цены отсутствуют(не имееются парсеры на цены),то мы возвращаем нули
        if item_sample_DB == self.NO_PRICES:
            # инициализируем переменные с ценами
            atb_price, eko_price, varus_price, silpo_price, ashan_price, novus_price, \
                metro_price, nk_price, fozzy_price = 0, 0, 0, 0, 0, 0, 0, 0, 0

        else:
            atb_price, eko_price, varus_price, silpo_price, ashan_price, novus_price, \
                metro_price, nk_price, fozzy_price = 0, 0, 0, 0, 0, 0, 0, 0, 0
            # пробуем вытянуть цену в АТБ из БД
            try:
                atb_price = store[0][item_sample_DB][self.__ATB_KEY]
            except Exception:
                print(self.ATB_WARNING_MESSAGE)

            # пробуем вытянуть цену в ЭКО из БД
            try:
                eko_price = store[0][item_sample_DB][self.__EKO_KEY]   #добавил [0], тк у нас изменилась форма БД
            except Exception:
                print(self.EKO_WARNING_MESSAGE)

            # пробуем вытянуть цену в Варусе из БД
            try:
                varus_price = store[0][item_sample_DB][self.__VARUS_KEY]
            except Exception:
                print(self.VARUS_WARNING_MESSAGE)

            # пробуем вытянуть цену в Сильпо из БД
            try:
                silpo_price = store[0][item_sample_DB][self.__SILPO_KEY]
            except Exception:
                print(self.SILPO_WARNING_MESSAGE)

            # пробуем вытянуть цену в Ашане из БД
            try:
                ashan_price = store[0][item_sample_DB][self.__ASHAN_KEY]
            except Exception:
                print(self.ASHAN_WARNING_MESSAGE)

            # пробуем вытянуть цену в Novus из БД
            try:
                novus_price = store[0][item_sample_DB][self.__NOVUS_KEY]
            except Exception:
                print(self.NOVUS_WARNING_MESSAGE)

            # пробуем вытянуть цену в Metro из БД
            try:
                metro_price = store[0][item_sample_DB][self.__METRO_KEY]
            except Exception:
                print(self.METRO_WARNING_MESSAGE)

            # пробуем вытянуть цену в Нашем Крае из БД
            try:
                nk_price = store[0][item_sample_DB][self.__NK_KEY]
            except Exception:
                print(self.NK_WARNING_MESSAGE)

            # пробуем вытянуть цену в Fozzy из БД
            try:
                fozzy_price = store[0][item_sample_DB][self.__FOZZY_KEY]
            except Exception:
                print(self.FOZZY_WARNING_MESSAGE)

        # подключение тега для продукта
        info = item_tag

        return atb_price, eko_price, varus_price, silpo_price, ashan_price, \
            novus_price, metro_price, nk_price, fozzy_price, info

    def __init__(self, nn_respond):
        '''Сразу же формируем цены и инфо продукта при инициализации объекта класса'''
        self.atb_price, self.eko_price, self.varus_price, \
            self.silpo_price, self.ashan_price, self.novus_price, \
            self.metro_price, self.nk_price, self.fozzy_price, self.info = self.products_context_maker(nn_respond)

    def products_context_maker(self, nn_respond):
        '''Функия, в которой для каждого продукта собираются цены из БД,
        в зависимости от ответа НС(ответ НС является аргументом этого метода).
        Для продуктов, у которых пока что нет цены, результат возвращается
        в виде кортежа с нулями для всех магазинов.'''

        # проверяем на корректность ответ НС
        self.__verify_sample(nn_respond)

        if nn_respond == BEER_OBOLON_PREMIUM_EXTRA_1_1_L:
            result = self.getting_prices('obolon_premium_1.1_l', get_obolon_premium)
        elif nn_respond == VODKA_HETMAN_ICE_07_L:
            result = self.getting_prices('vodka_hetman_ice_07', get_hetman_ICE)
        elif nn_respond == COFFEE_AROMA_GOLD_CLASSIC_100_GR:
            result = self.getting_prices('coffee_aroma_gold', coffe_aroma_gold_classic_100gr)
        elif nn_respond == COCA_COLA_2_L:
            result = self.getting_prices('coca_cola_2l', get_coca_cola_2l)
        elif nn_respond == SIROK_PLAVLENIY_KOMO_PAPRIKASH:
            result = self.getting_prices('sir_plavlenniy_komo_paprikash', get_KOMO_paprikash)
        elif nn_respond == GARLIK:
            result = self.getting_prices('garlik', get_garlik)
        elif nn_respond == KENT_8:
            result = self.getting_prices('sigarets_kent_8', get_sigarets_kent_8)
        elif nn_respond == TEA_MINUTKA_40_BAGS:
            result = self.getting_prices('tea_minutka', get_tea_minutka_black_40_b)
        elif nn_respond == SUN_OIL_SHEDRIY_DAR_RAFINIR_580_GR:
            result = self.getting_prices('oil_shedriy_dar_raf_850', get_oil_shedriy_dar_085l)
        elif nn_respond == ONION:
            result = self.getting_prices('onion', get_onion)
        elif nn_respond == FAIRY_LIMON_500_GR:
            result = self.getting_prices('fairy_limon_500', get_fairy_500_lime)
        elif nn_respond == APPLE_BLACK_PRINCE:
            result = self.getting_prices('apple_black_prince', get_apple_black_prince)
        elif nn_respond == MUSTARD_KOLOS:
            result = self.getting_prices(self.NO_PRICES, get_gorchica_kolos)
        elif nn_respond == SMETANA_STOLICA_SMAKY_20PER_400_GR:
            result = self.getting_prices('smetana_stol_smaky_20%', get_smetana_stolica_smaky_20_400gr)
        elif nn_respond == LEMON:
            result = self.getting_prices('limon', get_limon)
        elif nn_respond == SUN_OIL_OLEYNA_NERAF_850_GR:
            result = self.getting_prices('oil_oleyna_neraf_850', get_oil_oleyna_neraf_850)
        elif nn_respond == BEER_LVIVSKE_SVITLE_2_4_L:
            result = self.getting_prices('beer_lvivske_svetl_2.4 l', get_pivo_lvivske_svitle)
        elif nn_respond == SHAVING_FOAM_ARKO_COOL_200_MLG:
            result = self.getting_prices('arko_cool_200', get_arko_cool_300_100)
        elif nn_respond == SHAVING_FOAM_ARKO_SENSITIVE_200_MLG:
            result = self.getting_prices('arko_sensitive_200', get_arko_sensitive_300_100)
        elif nn_respond == CARROT:
            result = self.getting_prices('carrot', get_carrot)
        elif nn_respond == DROJJI_HARKOV_100_GR:
            result = self.getting_prices(self.NO_PRICES, get_drojji_hark)
        elif nn_respond == EGGS:
            result = self.getting_prices('eggs', get_chicken_eggs)
        elif nn_respond == DESODORANT_GARNIER_MAGNIY_MEN:
            result = self.getting_prices('desodorant_garnier_man', get_dezodorant_garnier_magniy_m)
        elif nn_respond == CABBAGE:
            result = self.getting_prices('cabbage', get_cabbage)
        elif nn_respond == MARLBORO_RED:
            result = self.getting_prices('marlboro_red', get_marlboro_red)
        elif nn_respond == MAYONES_DETSKIY_SHEDRO_67:
            result = self.getting_prices('mayonez_detsk_shedro_67%', get_mayonez_dom_detsk_shedro_67)
        elif nn_respond == DESODORANT_REXONA_ALOE_VERA_WOMEN:
            result = self.getting_prices('rexona_aloe_vera', get_reksona_aloe_vera_w)
        elif nn_respond == SMETANA_STOLICA_SMAKY_15_400_GR:
            result = self.getting_prices('smetana_stol_smaky_15%', get_smetana_stol_smaku_400_15)
        elif nn_respond == TEA_MONOMAH_KENYA_BLACK_90_GR:
            result = self.getting_prices('tea_monomah_kenya_90', get_tea_monomah_kenya)
        elif nn_respond == TOILET_PAPER_KIEV_63_M:
            result = self.getting_prices(self.NO_PRICES, get_toilet_papir_kiev_63m)
        elif nn_respond == TEA_MONOMAH_CEYLON_BLACK:
            result = self.getting_prices(self.NO_PRICES, get_tea_monomah_ceylon_black)
        elif nn_respond == COFFEE_AROMA_GOLD_FREEZE_FRIED_70_GR:
            result = self.getting_prices('cofee_aroma_gold_freeze_dried_70g', get_coffee_aroma_gold_freeze_dried_70)
        elif nn_respond == MUSTARD_VERES_UKRAINSKA_MICNA_120_GR:
            result = self.getting_prices('gorchica_veres_ukrainska_micna_120g', get_gorchica_veres_micna_ukr_120g)
        elif nn_respond == TEA_MONOMAH_100_CEYLON_ORIGINAL_BLACK_KRUPNOLIST:
            result = self.getting_prices(self.NO_PRICES, get_tea_monomah_original_ceylon_90g)
        elif nn_respond == DESODORANT_GARNIER_VESENNYA_SVEJEST:
            result = self.getting_prices('desodorant_garnier_spring_spirit', get_desodorant_garnier_spring_spirit)
        elif nn_respond == APPLE_GALA:
            result = self.getting_prices('apple_gala', get_apple_gala)
        elif nn_respond == SMETANA_GALICHANSKAYA_15_370_GR:
            result = self.getting_prices('smetana_galichanska_15_370gr', get_smetana_galichanska_15_370gr)
        elif nn_respond == CHIPS_SALT_BIG_PACK_30_GR:
            result = self.getting_prices('chips_lays_with_salt_big_pack', get_chips_lays_salt_big_pack_30g)
        elif nn_respond == SPRITE_2L:
            result = self.getting_prices('sprite_2l', get_sprite_2l)
        elif nn_respond == FANTA_2L:
            result = self.getting_prices('fanta_2l', get_fanta_2l)
        elif nn_respond == BOND_STREET_BLUE_SELECTION:
            result = self.getting_prices('bond_street_blue_selection', get_bond_street_blue_selection)
        elif nn_respond == CAMEL_BLUE:
            result = self.getting_prices('camel_blue', get_camel_blue)
        elif nn_respond == LD_RED:
            result = self.getting_prices('ld_red', get_ld_red)
        elif nn_respond == MARLBORO_GOLD:
            result = self.getting_prices('marlboro_gold', get_marlboro_gold)
        elif nn_respond == ROTHMANS_DEMI_BLUE_EXCLUSIVE:
            result = self.getting_prices('rothmans_demi_blue_exclusive', get_rothmans_demi_blue_exclusive)
        elif nn_respond == ROTHMANS_DEMI_CLICK_PURPLE:
            result = self.getting_prices('rothmans_demi_click_purple', get_rothmans_demi_click_purple)
        elif nn_respond == WINSTON_CASTER:
            result = self.getting_prices('winston_caster', get_winston_caster)
        elif nn_respond == PARLAMENT_AQUA_BLUE:
            result = self.getting_prices('parlament_aqua_blue', get_parlament_aqua_blue)
        elif nn_respond == WINSTON_BLUE:
            result = self.getting_prices('winston_blue', get_winston_blue)
        elif nn_respond == BOND_STREET_RED_SELECTION:
            result = self.getting_prices('bond_street_red_selection', get_bond_street_red_selection)
        elif nn_respond == LD_BLUE:
            result = self.getting_prices('ld_blue', get_ld_blue)
        elif nn_respond == KENT_SILVER:
            result = self.getting_prices('kent_silver', get_kent_silver)
        elif nn_respond == KENT_NAVY_BLUE_NEW:
            result = self.getting_prices('kent_navy_blue', get_kent_navi_blue_new)
        elif nn_respond == BEER_CHERNIGOVSKOE_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_chernigivske_svitle_05_l_glass', get_beer_chernigivske_svitle_05_l_glass)
        elif nn_respond == BEER_STELLA_ARTOIS_05_L_GLASS:
            result = self.getting_prices('beer_stella_artois_05_l_glass', get_beer_stella_artois_05_l_glass)
        elif nn_respond == BEER_OBOLON_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_obolon_svitle_05_l_glass', get_beer_obolon_svitle_05_l_glass)
        elif nn_respond == BEER_JIGULIVSKE_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_jugulivske_svitle_05_l_glass', get_beer_jigulivsle_svitle_05_l_glass)
        elif nn_respond == BEER_ROGAN_TRADICIYNE_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_rogan_tradicionnoe_svitle_05_l_glass',
                                         get_beer_rogan_tradiciyne_svitle_05_l_glass)
        elif nn_respond == BEER_CORONA_EXTRA_SVITLE_033_L_GLASS:
            result = self.getting_prices('beer_corona_extra_svitle_033_l_glass',
                                         get_beer_corona_extra_svitle_033_l_glass)
        elif nn_respond == BEER_CHERNIGIVSKE_BILE_NEFILTER_05_L_GLASS:
            result = self.getting_prices('beer_chernigibske_bile_nefilter_05_l_glass',
                                         get_beer_chernigivske_bile_nefilter_05_l_glass)
        elif nn_respond == BEER_YANTAR_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_yantar_svitle_05_l_glass', get_beer_yantar_svitle_05_l_glass)
        elif nn_respond == BEER_ZIBERT_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_zibert_svitle_05_l_glass', get_beer_zibert_svitle_05_l_glass)
        elif nn_respond == BEER_ARSENAL_MICNE_05_L_GLASS:
            result = self.getting_prices('beer_arsenal_micne_05_l_glass', get_beer_arsenal_micne_05_l_glass)
        elif nn_respond == BEER_PPB_ZAKARPATSKE_05_L_GLASS:
            result = self.getting_prices('beer_persha_brovarna_zakarpatske_svitle_05_l_glass',
                                         get_beer_persha_brovarna_zakarpatske_05_l_glass)
        elif nn_respond == BEER_LVIVSKE_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_lvivske_svitle_05_l_glass', get_beer_lvivske_svitle_05_l_glass)
        elif nn_respond == BEER_LVIVSKE_1715_05_L_GLASS:
            result = self.getting_prices('beer_lvivske_1715_05_l_glass', get_beer_lvivske_1715_05_l_glass)
        elif nn_respond == BEER_ZLATA_PRAHA_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_zlata_praha_svitle_05_l_glass', get_beer_zlata_praha_05_l_glass)
        elif nn_respond == BEER_TUBORG_GREEN_05_L_GLASS:
            result = self.getting_prices('beer_tuborg_green_05_l_glass', get_beer_tuborg_green_05_l_glass)
        elif nn_respond == BEER_SLAVUTICH_ICE_MIX_LIME_05_L_GLASS:
            result = self.getting_prices('beer_slavutich_ice_mix_lime_05_l_glass',
                                         get_beer_slavutich_ice_mix_lime_05_l_glass)
        elif nn_respond == BEER_TETEREV_05_L_GLASS:
            result = self.getting_prices('beer_teteriv_svitle_05_l_glass', get_beer_teteriv_svitle_05_l_glass)
        elif nn_respond == BEER_KRUSOVICE_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_krusovice_svitle_05_l_glass', get_beer_krusovice_svitle_05_l_glass)
        elif nn_respond == BEER_HEINEKEN_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_heineken_svitle_05_l_glass', get_beer_heineken_svitle_05_l_glass)
        elif nn_respond == BEER_AMSTEL_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_amstel_svitle_05_l_glass', get_beer_amstel_svitle_05_l_glass)
        elif nn_respond == BEER_HIKE_PREMIUM_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_hike_premium_svitle_05_l_glass', get_beer_hike_premium_05_l_glass)
        elif nn_respond == BEER_BOCHKOVE_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_bochkove_svitle_05_l_glass', get_beer_bochkove_svitle_05_l_glass)
        elif nn_respond == BEER_KRONENBOURG_1664_BLANC_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_kronenbourg_1664_blanc_svitle_05_l_glass',
                                         get_beer_kronenbourg_1664_blanc_svitle_05_l_glass)
        elif nn_respond == BEER_OPILLYA_FIRMENNOE_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_opilla_firmove_nepasterizovane_svitle_05_l_glass',
                                         get_beer_opilla_nepasterizovane_svitle_05_l_glass)
        elif nn_respond == BEER_YACHMENNIY_KOLOS_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_yachmenniy_kolos_svitle_05_l_glass',
                                         get_beer_yachmenniy_kolos_svitle_05_l_glass)
        elif nn_respond == BEER_OPILLYA_KORIFEY_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_opilla_korifey_svitle_05_l_glass',
                                         get_beer_opilla_korifey_svitle_05_l_glass)
        elif nn_respond == BEER_CHAYKA_DNIPROVSKAYA_05_L_GLASS:
            result = self.getting_prices('beer_chaika_dniprovska_svitle_05_l_glass',
                                         get_beer_chaika_dneprovskaya_svitle_05_l_glass)
        elif nn_respond == BEER_CHAYKA_CHERNOMORSKAYA_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_chaika_chernomorskaya_svitle_05_l_glass',
                                         get_beer_chaika_chernomorskaya_svitle_05_l_glass)
        elif nn_respond == BEER_UMAN_WAISSBURG_SVITLE_1_L:
            result = self.getting_prices('beer_uman_waissburg_1_l_svitle_plastic',
                                         get_beer_uman_waissburg_svitle_1_l_plastic)
        elif nn_respond == BEER_UMAN_PSHENICHNOE_SVITLE_1_L:
            result = self.getting_prices('beer_uman_pshenichnoe_1_l_svitle_plastic',
                                         get_beer_uman_pshenichnoe_svitle_1_l_plastic)
        elif nn_respond == BEER_BERDICHEVSKOE_HMELNOE_SVITLE_1_L:
            result = self.getting_prices('beer_berdichevske_hmilne_1_l_svitle_plastic',
                                         get_beer_berdichevskoe_hmelnoye_svitle_1_l_plastic)
        elif nn_respond == BEER_BERDICHEVSKOE_LAGER_SVITLE_1_L:
            result = self.getting_prices('beer_berdichevske_lager_1_l_svitle_plastic',
                                         get_beer_berdichevskoe_lager_svitle_1_l_plastic)
        elif nn_respond == BEER_OPILLYA_KORIFEY_11_L:
            result = self.getting_prices('beer_opilla_korifey_11_l_plastic', get_beer_opilla_korifey_11_l_plastic)
        elif nn_respond == BEER_OBOLON_JIGULIVSKE_EXPORTNE_15_L:
            result = self.getting_prices('beer_obolon_jigulivske_eksportne_15_l_plastic',
                                         get_beer_obolon_jigulivske_eksport_15_l_plastic)
        elif nn_respond == BEER_YANTAR_SVITLE_12_L:
            result = self.getting_prices('beer_yantar_svitle_12_l_plastic', get_beer_yantar_svitle_12_l_plastic)
        elif nn_respond == BEER_JASHKOVSKOE_PSHENICHNOE_NEFILTER_1_L:
            result = self.getting_prices('beer_jashkovske_pshenichne_nefiltr_1_l_plastic',
                                         get_beer_jashkovskoe_pshenicnoe_nefilter_1_l_plastic)
        elif nn_respond == BEER_JASHKOVSKOE_SVITLE_NEFILTER_1_L:
            result = self.getting_prices('beer_jashkovske_svitle_nefiltr_1_l_plastic',
                                         get_beer_jashkovskoe_svitle_nefilter_1_l_plastic)
        elif nn_respond == BEER_JASHKOVSKOE_JIGULIVSKE_NEFILTER_1_L:
            result = self.getting_prices('beer_jashkovske_jigulivske_nefiltr_1_l_plastic',
                                         get_beer_jashkovskoe_jigulivske_nefilter_1_l_plastic)
        elif nn_respond == BEER_PPB_BOCHKOVE_1_L:
            result = self.getting_prices('beer_persha_privatna_brovarnya_bochkove_1_l_plastic',
                                         get_beer_persha_privatna_brovarnya_bochkove_1_l_plastic)
        elif nn_respond == BEER_CHAYKA_DNIPROVSKAYA_1_L:
            result = self.getting_prices('beer_chayka_dniprovska_1_l_plastic', get_beer_chayka_dniprovska_1_l_plastic)
        elif nn_respond == KETCHUP_TORCHIN_CHESNOK_270_GR:
            result = self.getting_prices('ketchup_torchin_s_chasnikom_270gr', get_ketchup_torchin_s_chesnokom)
        elif nn_respond == MAYONES_KOROLIVSKIY_SMAK_KOROLIVSKIY_67_300_GR:
            result = self.getting_prices('mayonez_korolivskiy_smak_korolivskiy_67_300gr',
                                         get_mayonez_korolivkiy_smak_korolivskiy_67_300gr)
        elif nn_respond == MUKA_ZOLOTE_ZERNYATKO_PSHENICHNE_2_KG:
            result = self.getting_prices(self.NO_PRICES, get_muka_zolote_zernyatko_pshenichne_2kg)
        elif nn_respond == BEER_CHERNIGOVSKOE_BELOE_NEFILTER_1_L:
            result = self.getting_prices('beer_chernigivske_bile_nefilter_1l', get_beer_chernigivske_bile_1l_plastic)
        elif nn_respond == BEER_OBOLON_SVITLE_1_L:
            result = self.getting_prices('beer_obolon_svitle_1l', get_beer_obolon_svitle_1l_plastic)
        elif nn_respond == BEER_ROGAN_TRADICIYNE_SVITLE_1_L:
            result = self.getting_prices('beer_rogan_tradiciyne_svitle_1l', get_beer_rogan_tradiciyne_svitle_1l_plastic)
        elif nn_respond == SOUS_CHUMAK_CHESNOCHNIY_200_GR:
            result = self.getting_prices('sous_chumak_chesnochniy_200gr', get_sous_chumak_chesnochniy_200gr)
        elif nn_respond == ORBIT_POLYNICA_BANAN:
            result = self.getting_prices('orbit_polunica_banan', get_jvachka_orbit_clubnika_banan)
        elif nn_respond == LM_RED:
            result = self.getting_prices('sigarets_lm_red', get_sigarets_LM_red)
        elif nn_respond == BEER_JIGULIVSKE_SVITLE_2_L:
            result = self.getting_prices('beer_jigulivske_svitle_2l_plastic', get_beer_jigulivske_2l_plastic)
        elif nn_respond == BEER_CHAYKA_DNIPROVSKAYA_2_L:
            result = self.getting_prices('beer_chayka_dniprovska_2l_plastic', get_beer_chayka_dniprovskaya_2l_plastic)
        elif nn_respond == BEER_PIWNY_KEBEK_2_L:
            result = self.getting_prices('beer_piwny_kebek_svitle_2l_plastic', get_beer_piwny_kubek_2l_plastic)
        elif nn_respond == KETCHUP_TORCHIN_DO_SHASHLIKY_270_GR:
            result = self.getting_prices('ketchup_torchin_do_shashliky_270gr', get_ketchup_torchin_do_shasliky_270gr)
        elif nn_respond == MAYONES_CHUMAK_APPETITNIY_50_300_GR:
            result = self.getting_prices('mayonez_chumak_appetitniy_50_300gr', get_mayonez_chumak_appetitniy_50_300gr)
        elif nn_respond == KOLBASA_PERSHA_STOLICA_SALYAMI_FIRMENNAYA_VS:
            result = self.getting_prices(self.NO_PRICES, get_kolbasa_persha_stolica_salyami_firmova_vs)
        elif nn_respond == COFFEE_CHERNA_KARTA_GOLD_50_GR:
            result = self.getting_prices('coffee_chorna_karta_50gr', get_cofee_chorna_karta_gold_50gr)
        elif nn_respond == BEER_ARSENAL_MICNE_SVITLE_2_L:
            result = self.getting_prices('beer_arsenal_micne_2l_plastic', get_beer_arsenal_micne_svitle_2l_plastic)
        elif nn_respond == BEER_PPB_BOCHKOVE_SVITLE_2_L:
            result = self.getting_prices('beer_ppb_bochkove_svitle_2l_plastic',
                                         get_beer_persha_privatna_brovarnya_bochkove_svitle_2l_plastic)
        elif nn_respond == BEER_PPB_ZAKARPATSKE_ORIGINALNE_SVITLE_2_L:
            result = self.getting_prices('beer_ppb_zakarpatske_svitle_2l_plastic',
                                         get_beer_persha_privatna_brovarnya_zakarpatske_svitle_2l_plastic)
        elif nn_respond == BEER_ZIBERT_SVITLE_05_L_JB:
            result = self.getting_prices('beer_zibert_svitle_05l_v_banke', get_beer_zibert_svitle_05_l_banochnoe)
        elif nn_respond == YOGURT_FANNI_240_GR_1_5_LESNIE_YAGODI:
            result = self.getting_prices('yogurt_fanni_lisovi_yagodi_1_5_240gr_stakan',
                                         get_yogurt_fanni_lisovi_yagodi_1_5_240gr)
        elif nn_respond == KEFIR_SLAVIYA_2_5_850_GR:
            result = self.getting_prices(self.NO_PRICES, get_kefir_slaviya_2_5_850gr)
        elif nn_respond == BEER_OBOLON_KIEVSKOE_ROZLIVNOE_SVITLE_195_L:
            result = self.getting_prices('beer_obolon_kievskoe_razlivnoe_svetloe_195l',
                                         get_beer_obolon_kievskoe_razlivnoe_svetloe_195l_plastic)
        elif nn_respond == BEER_CHERNIGOVSKOE_LIGHT_SVITLE_2_L:
            result = self.getting_prices('beer_chernigivske_light_svitle_2l_plastic',
                                         get_beer_chernigivske_light_svitle_2l_plastic)
        elif nn_respond == BEER_OPILLYA_KORIFEY_2_L:
            result = self.getting_prices('beer_opilla_korifey_svitle_2l_plastic',
                                         get_beer_opilla_korifey_svitle_2l_plastic)
        elif nn_respond == BEER_YANTAR_SVITLE_2_L:
            result = self.getting_prices('beer_yantar_svitle_2l_plastic', get_beer_yantar_svitle_2l_plastic)
        elif nn_respond == BEER_TUBORG_GREEN_4_X_05_L:
            result = self.getting_prices('beer_tuborg_green_svitle_4_banki_05l',
                                         get_beer_tuborg_green_svitle_4_banki_05l)
        elif nn_respond == BEER_PPB_ZAKARPATSKE_4_X_05_L:
            result = self.getting_prices('beer_ppb_zakarpatske_svitle_4_banki_05l',
                                         get_beer_ppb_zakarpatske_svitle_4_banki_05l)
        elif nn_respond == BEER_PPB_BOCHKOVE_4_X_05_L:
            result = self.getting_prices('beer_ppb_bochkove_svitle_4_banki_05l',
                                         get_beer_ppb_bochkove_svitle_4_banki_05l)
        elif nn_respond == BEER_BUDWEISER_BUDVAR_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_budweiser_budvar_svitle_05l', get_beer_budweiser_budvar_05l_glass)
        elif nn_respond == BEER_PILSNER_URQUELL_SVITLE_05_L_GLASS:
            result = self.getting_prices('beer_pilsner_urquell_svitle_05l', get_beer_pilsner_urquell_05l_glass)
        elif nn_respond == BEER_ROBERT_DOMS_BELGIYSKIY_SVITLE_NEFILTER_05_L_GLASS:
            result = self.getting_prices('beer_robert_doms_belgiyskiy_svitle_nefilter_05l_glass',
                                         get_beer_robert_doms_belgiyskiy_svitle_nefilter_05l_glass)
        elif nn_respond == BEER_CHERNIGOVSKOE_SVITLE_05_L_JB:
            result = self.getting_prices('beer_chernigivske_svitle_05_l_jb', get_beer_chernigivske_svitle_05l_jb)
        elif nn_respond == BEER_CHERNIGOVSKOE_BELOE_05_L_JB:
            result = self.getting_prices('beer_chernigivske_bile_nefilter_05_l_jb',
                                         get_beer_chernigivske_bile_nefilter_05l_jb)
        elif nn_respond == BEER_VELKOPOPOVICKY_KOZEL_TEMNE_05_L_JB:
            result = self.getting_prices('beer_velkopopovicky_kozel_temne_05_l_jb',
                                         get_beer_velkopopovicky_kozel_temne_05l_jb)
        elif nn_respond == BEER_EDELMEISTER_PILSNER_SVITLE_05_L_JB:
            result = self.getting_prices('beer_edelmeister_pilsner_svitle_05_l_jb',
                                         get_beer_edelmeister_pilsner_svitle_05l_jb)
        elif nn_respond == BEER_FAXE_SVITLE_05_L_JB:
            result = self.getting_prices('beer_faxe_svitle_05_l_jb', get_beer_faxe_svitle_05l_jb)
        elif nn_respond == BEER_LIVU_PILZENES_SVITLE_05_L_JB:
            result = self.getting_prices('beer_livu_pilzenes_svitle_05_l_jb', get_beer_livu_pilzenes_svitle_05l_jb)
        elif nn_respond == BEER_VELKOPOPOVICKY_KOZEL_SVITLE_05_L_JB:
            result = self.getting_prices('beer_velkopopovicky_kozel_svitle_05_l_jb',
                                         get_beer_velkopopovicky_kozel_svitle_05l_jb)
        elif nn_respond == BEER_OBOLON_BEERMIX_LIMON_05_L_JB:
            result = self.getting_prices('beer_obolon_beermix_limon_svitle_05_l_jb',
                                         get_beer_obolon_beermix_limon_svitle_05l_jb)
        elif nn_respond == BEER_EDELMEISTER_WEIZENBIER_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_edelmeister_weizenbier_svitle_nefilter_05_l_jb',
                                         get_beer_edelmeister_weizenbier_nefilter_svitle_05l_jb)
        elif nn_respond == BEER_EDELMEISTER_SCHWARZBIER_TEMNE_05_L_JB:
            result = self.getting_prices('beer_edelmeister_schwarzbier_temne_05_l_jb',
                                         get_beer_edelmeister_schwarzbier_temne_05l_jb)
        elif nn_respond == BEER_HIKE_BLANCHE_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_hike_blanche_nefilter_05_l_jb',
                                         get_beer_hike_blanche_svitle_nefilter_05l_jb)
        elif nn_respond == BEER_ZLATA_PRAHA_SVITLE_05_L_JB:
            result = self.getting_prices('beer_zlata_praha_svitle_05_l_jb', get_beer_zlata_praha_svitle_05l_jb)
        elif nn_respond == BEER_THURINGER_PREMIUM_BEER_SVITLE_05_L_JB:
            result = self.getting_prices('beer_thuringer_premium_beer_svitle_05_l_jb',
                                         get_beer_thuringer_premium_beer_svitle_05l_jb)
        elif nn_respond == BEER_LIVU_SENCU_SVITLE_05_L_JB:
            result = self.getting_prices('beer_livu_sencu_beer_svitle_05_l_jb', get_beer_livu_sencu_svitle_05l_jb)
        elif nn_respond == BEER_GERMANARICH_SVITLE_05_L_JB:
            result = self.getting_prices('beer_germanarich_svitle_05_l_jb', get_beer_germanarich_svitle_05l_jb)
        elif nn_respond == BEER_HIKE_PREMIUM_SVITLE_05_L_JB:
            result = self.getting_prices('beer_hike_premium_svitle_05_l_jb', get_beer_hike_premium_svitle_05l_jb)
        elif nn_respond == BEER_OBOLON_0_NONALCO_NEFILTER_SVITLE_05_L_JB:
            result = self.getting_prices('beer_obolon_nonalcohol_nefilter_svitle_05_l_jb',
                                         get_beer_obolon_svitle_nefilter_nonalcohol_05l_jb)
        elif nn_respond == BEER_ZIBERT_BAVARSKOE_SVITLE_05_L_JB:
            result = self.getting_prices('beer_zibert_bavarskoe_svitle_05_l_jb',
                                         get_beer_zibrert_bavarske_svitle_05l_jb)
        elif nn_respond == BEER_BAVARIYA_LIQUID_APPLE_NONALCO_SVITLE_05_L_JB:
            result = self.getting_prices('beer_bavaria_liquid_apple_ninalco_svitle_05_l_jb',
                                         get_beer_bavaria_liquid_apple_nonalcohol_svitle_05l_jb)
        elif nn_respond == BEER_HEINEKEN_SVITLE_05_L_JB:
            result = self.getting_prices('beer_heineken_svitle_05_l_jb', get_beer_heineken_svitle_05l_jb)
        elif nn_respond == BEER_RYCHTAR_GRANT_11_SVITLE_05_L_JB:
            result = self.getting_prices('beer_rychtar_grant_11_svitle_05_l_jb',
                                         get_beer_rychtar_grunt_11_svitle_05l_jb)
        elif nn_respond == BEER_AMSTEL_SVITLE_05_L_JB:
            result = self.getting_prices('beer_amstel_svitle_05_l_jb', get_beer_amstel_svitle_05l_jb)
        elif nn_respond == BEER_BAVARIA_SVITLE_05_L_JB:
            result = self.getting_prices('beer_bavaria_svitle_05_l_jb', get_beer_bavaria_svitle_05l_jb)
        elif nn_respond == BEER_BAVARIA_SVITLE_NONALCO_05_L_JB:
            result = self.getting_prices('beer_bavaria_svitle_nonalcohol_05_l_jb',
                                         get_beer_bavaria_svitle_nonalcohol_05l_jb)
        elif nn_respond == BEER_EDELBURG_LAGER_SVITLE_05_L_JB:
            result = self.getting_prices('beer_edelburg_lager_05_l_jb', get_beer_edelburg_lager_svitle_05l_jb)
        elif nn_respond == BEER_DONNER_PILS_SVITLE_05_L_JB:
            result = self.getting_prices('beer_donner_pils_svitle_05_l_jb', get_beer_donner_pils_svitle_05l_jb)
        elif nn_respond == BEER_DUTCH_WINDMILL_SVITLE_05_L_JB:
            result = self.getting_prices('beer_dutch_windmill_svitle_05_l_jb', get_beer_dutch_windmill_svitle_05l_jb)
        elif nn_respond == BEER_EDELBURG_HEFEWEIZEN_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_edelburg_hefeweizen_svitle_nefilter_05_l_jb',
                                         get_beer_edelburg_hefeweizen_svitle_nefilter_05l_jb)
        elif nn_respond == BEER_EDELMEISTER_UNFILTERED_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_edelmeister_unfiltered_svitle_nefilter_05_l_jb',
                                         get_beer_edelmeister_unfiltered_svitle_nefilter_05l_jb)
        elif nn_respond == BEER_ESTRELLA_DAMM_BARCELONA_SVITLE_05_L_JB:
            result = self.getting_prices('beer_estrella_damm_barcelona_svitle_05_l_jb',
                                         get_beer_estrella_damm_barcelona_svitle_05l_jb)
        elif nn_respond == BEER_HALNE_JASNE_PELNE_05_L_JB:
            result = self.getting_prices('beer_halne_jasne_pelne_05_l_jb', get_beer_halne_jasne_pelne_05l_jb)
        elif nn_respond == BEER_EUROTOUR_HEFEWEISSBIER_SVITLE_05_L_JB:
            result = self.getting_prices('beer_eurotour_hefeweissbier_svitle_05_l_jb',
                                         get_beer_eurotour_hefeweissbier_svitle_05l_jb)
        elif nn_respond == BEER_HOLLANDIA_STRONG_SVITLE_05_L_JB:
            result = self.getting_prices('beer_hollandia_strong_svitle_05_l_jb',
                                         get_beer_hollandia_strong_svitle_05l_jb)
        elif nn_respond == BEER_LANDER_BRAU_PREMIUM_SVITLE_05_L_JB:
            result = self.getting_prices('beer_lander_brau_premium_svitle_05_l_jb',
                                         get_beer_lander_brau_premium_svitle_05l_jb)
        elif nn_respond == BEER_SAKU_KULD_05_L_JB:
            result = self.getting_prices('beer_saku_kuld_05_l_jb', get_beer_Saku_Kuld_05l_jb)
        elif nn_respond == BEER_SAKU_ORIGINAAL_05_L_JB:
            result = self.getting_prices('beer_saku_originaal_05_l_jb', get_beer_Saku_Originaal_05l_jb)
        elif nn_respond == BEER_STANGEN_LAGER_SVITLE_05_L_JB:
            result = self.getting_prices('beer_stangen_lager_svitle_05_l_jb', get_beer_Stangen_Lager_svitle_05l_jb)
        elif nn_respond == BEER_VAN_PUR_PREMIUM_SVITLE_05_L_JB:
            result = self.getting_prices('beer_van_pur_premium_svitle_05_l_jb', get_beer_Van_Pur_Premium_svitle_05l_jb)
        elif nn_respond == BEER_BAVARIA_MANGO_MARAKUYA_SVITLE_NONALCO_05_L_JB:
            result = self.getting_prices('beer_bavaria_mango_marakya_nonalco_svitle_05_l_jb',
                                         get_beer_Bavaria_mango_marakya_nonalcohol_svitle_05l_jb)
        elif nn_respond == BEER_BAVARIA_GRANAT_NONALCO_05_L_JB:
            result = self.getting_prices('beer_bavaria_granat_nonalco_svitle_05_l_jb',
                                         get_beer_Bavaria_granat_nonalcohol_svitle_05l_jb)
        elif nn_respond == BEER_OBOLON_BEERMIX_MALINA_SVITLE_05_L_JB:
            result = self.getting_prices('beer_obolon_beermix_malina_svitle_05_l_jb',
                                         get_beer_Obolon_Beermix_malina_svitle_05l_jb)
        elif nn_respond == BEER_OBOLON_BEERMIX_VISHNYA_SPECIALNE_SVITLE_05_L_JB:
            result = self.getting_prices('beer_obolon_beermix_vishnya_svitle_05_l_jb',
                                         get_beer_Obolon_Beermix_vishnya_svitle_05l_jb)
        elif nn_respond == BEER_LOMZA_SVITLE_05_L_JB:
            result = self.getting_prices('beer_lomza_svitle_05_l_jb', get_beer_Lomza_svitle_05l_jb)
        elif nn_respond == BEER_PADERBORNER_PILSENER_SVITLE_05_L_JB:
            result = self.getting_prices('beer_paderborner_pilsener_05_l_jb',
                                         get_beer_Paderborner_Pilsener_svitle_05l_jb)
        elif nn_respond == BEER_PADERBORNER_EXPORT_SVITLE_05_L_JB:
            result = self.getting_prices('beer_paderborner_export_05_l_jb', get_beer_Paderborner_Export_svitle_05l_jb)
        elif nn_respond == BEER_CLAUSTHALER_GRAPEFRUIT_NONALCO_05_L_JB:
            result = self.getting_prices('beer_clausthaler_grapefruit_nonalco_05_l_jb',
                                         get_beer_Clausthaler_Grapefruit_nonalcohol_svitle_05l_jb)
        elif nn_respond == BEER_CLAUSTHALER_ORIGINAL_NONALCO_05_L_JB:
            result = self.getting_prices('beer_clausthaler_original_nonalco_05_l_jb',
                                         get_beer_Clausthaler_Original_nonalcohol_svitle_05l_jb)
        elif nn_respond == BEER_CLAUSTHALER_LEMON_NONALCO_05_L_JB:
            result = self.getting_prices('beer_clausthaler_lemon_nonalco_05_l_jb',
                                         get_beer_Clausthaler_Lemon_nonalcohol_svitle_05l_jb)
        elif nn_respond == BEER_FOREVER_ROCK_N_ROLL_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_forever_rock_n_roll_nefilter_svitle_05_l_jb',
                                         get_beer_Forever_Rock_N_Roll_svitle_nefilter_05l_jb)
        elif nn_respond == BEER_FOREVER_BLACK_QUEEN_TEMNE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_forever_black_queen_nefilter_temne_05_l_jb',
                                         get_beer_Forever_Black_Queen_temne_nefilter_05l_jb)
        elif nn_respond == BEER_FOREVER_KITE_SAFARI_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_forever_kite_safari_nefilter_svitle_05_l_jb',
                                         get_beer_Forever_Kite_Safari_svitle_nefilter_05l_jb)
        elif nn_respond == BEER_FOREVER_CRAZY_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_forever_crazy_nefilter_svitle_05_l_jb',
                                         get_beer_Forever_Crazy_svitle_nefilter_05l_jb)
        elif nn_respond == BEER_HIKE_LIGHT_SVITLE_05_L_JB:
            result = self.getting_prices('beer_hike_light_svitle_05_l_jb', get_beer_Hike_Light_svitle_05l_jb)
        elif nn_respond == BEER_HIKE_ZERO_NONALCO_05_L_JB:
            result = self.getting_prices('beer_hike_zero_nonalco_05_l_jb', get_beer_Hike_Zero_nonalco_svitle_05l_jb)
        elif nn_respond == BEER_HORN_DISEL_ICE_PILSNER_SVITLE_0568_L_JB:
            result = self.getting_prices('beer_horn_disel_ice_pilsner_svitle_05_l_jb',
                                         get_beer_Horn_Disel_Ice_Pilsner_svitle_05l_jb)
        elif nn_respond == BEER_HORN_DISEL_ORIGINAL_0568_L_JB:
            result = self.getting_prices('beer_horn_disel_original_svitle_05_l_jb',
                                         get_beer_Horn_Disel_Original_svitle_05l_jb)
        elif nn_respond == BEER_HORN_DISEL_TRADITIONAL_SVITLE_0568_L_JB:
            result = self.getting_prices('beer_horn_disel_traditional_svitle_05_l_jb',
                                         get_beer_Horn_Disel_Traditional_svitle_05l_jb)
        elif nn_respond == BEER_HORN_PREMIUM_DIESEL_SVITLE_05_L_JB:
            result = self.getting_prices('beer_horn_disel_premium_svitle_05_l_jb',
                                         get_beer_Horn_Disel_Premium_svitle_05l_jb)
        elif nn_respond == BEER_KRUSOVICE_CERNE_TEMNE_05_L_JB:
            result = self.getting_prices('beer_krusovice_cerne_temne_05_l_jb', get_beer_Krusovice_Cerne_temne_05l_jb)
        elif nn_respond == BEER_LANDER_BRAU_MICNE_05_L_JB:
            result = self.getting_prices('beer_lander_brau_micne_05_l_jb', get_beer_Lander_Brau_micne_05l_jb)
        elif nn_respond == BEER_LANDER_BRAU_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_lander_brau_svitle_nefilter_05_l_jb',
                                         get_beer_Lander_Brau_svitle_nefilter_05l_jb)
        elif nn_respond == BEER_PADERBORNER_PILGER_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_paderborner_pilger_svitle_nefilter_05_l_jb',
                                         get_beer_Paderborner_Pilger_svitle_nefilter_05l_jb)
        elif nn_respond == BEER_PLATAN_JEDENACTKA_11_SVITLE_05_L_JB:
            result = self.getting_prices('beer_platan_jedenactka_11_svitle_05_l_jb',
                                         get_beer_Platan_Jedenactka_11_svitle_05l_jb)
        elif nn_respond == BEER_PRAGA_SVITLE_05_L_JB:
            result = self.getting_prices('beer_praga_svitle_05_l_jb', get_beer_Praga_svitle_05l_jb)
        elif nn_respond == BEER_SAKU_ROCK_SVITLE_0568_L_JB:
            result = self.getting_prices('beer_saku_rock_svitle_0568_l_jb', get_beer_Saku_Rock_svitle_05l_jb)
        elif nn_respond == BEER_SITNAN_SVITLE_05_L_JB:
            result = self.getting_prices('beer_sitnan_svitle_05_l_jb', get_beer_Sitnan_svitle_05l_jb)
        elif nn_respond == BEER_VIENAS_PREMIUM_GOLDEN_SVITLE_0568_L_JB:
            result = self.getting_prices('beer_vienas_premium_golden_svitle_05_l_jb',
                                         get_beer_Vienas_Premium_Golden_svitle_05l_jb)
        elif nn_respond == BEER_VIENAS_PREMIUM_TRADITIONAL_SVITLE_0568_L_JB:
            result = self.getting_prices('beer_vienas_premium_traditional_svitle_05_l_jb',
                                         get_beer_Vienas_Premium_Traditional_svitle_05l_jb)
        elif nn_respond == BEER_VLYNSKI_BROWAR_FOREVER_SWEET_WIT_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_volynski_browar_forever_sweet_wit_svitle_05_l_jb',
                                         get_beer_Volynski_Browar_Forever_Sweet_Wit_nefilter_svitle_05l_jb)
        elif nn_respond == BEER_ZAHRINGER_PREMIUM_SVITLE_05_L_JB:
            result = self.getting_prices('beer_zahringer_premium_svitle_05_l_jb',
                                         get_beer_Zahringer_premium_svitle_05l_jb)
        elif nn_respond == BEER_ZAHRINGER_HEFEWEIZEN_SVITLE_05_L_JB:
            result = self.getting_prices('beer_zahringer_hefeweizen_svitle_05_l_jb',
                                         get_beer_Zahringer_Hefeweizen_svitle_05l_jb)
        elif nn_respond == BEER_JASHKOVSKOE_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_jajkivske_nefilter_svitle_05_l_jb',
                                         get_beer_jajkivske_nefilter_svitle_05l_jb)
        elif nn_respond == BEER_OBOLON_SVITLE_05_L_JB:
            result = self.getting_prices('beer_obolon_svitle_05_l_jb', get_beer_obolon_svitle_05l_jb)
        elif nn_respond == BEER_PUBSTER_SVITLE_05_L_JB:
            result = self.getting_prices('beer_pubster_svitle_05_l_jb', get_beer_Pubster_svitle_05l_jb)
        elif nn_respond == BEER_CHAYKA_CHERNOMORSKAYA_SVITLE_05_L_JB:
            result = self.getting_prices('beer_chaika_chernomorskaya_05_l_jb',
                                         get_beer_Chaika_Chernomorska_svitle_05l_jb)
        elif nn_respond == BEER_PPB_ZAKARPATSKE_ORIGINALNE_SVITLE_05_L_JB:
            result = self.getting_prices('beer_ppb_zakarpatske_origin_svitle_05_l_jb',
                                         get_beer_PPB_Zakarpatske_origin_svitle_05l_jb)
        elif nn_respond == BEER_PPB_BOCHKOVE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_ppb_bochkove_nefilter_05_l_jb', get_beer_PPB_Bochkove_nefilter_05l_jb)
        elif nn_respond == BEER_PPB_NEFILTROVANE_SVITLE_NONALCO_05_L_JB:
            result = self.getting_prices('beer_ppb_nefilter_svitle_nonalco_05_l_jb',
                                         get_beer_PPB_Nefilter_svitle_nonalco_05l_jb)
        elif nn_respond == BEER_PPB_LIMON_LIME_NONALCO_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_ppb_limon_lime_nonalco_nefilter_05_l_jb',
                                         get_beer_PPB_Limon_lime_nonalco_nefilter_05l_jb)
        elif nn_respond == BEER_CHAYKA_DNIPROVSKAYA_05_L_JB:
            result = self.getting_prices('beer_chaika_dniprovskaya_05_l_jb', get_beer_Chaika_Dniprovska_svitle_05l_jb)
        elif nn_respond == BEER_BROK_EXPORT_SVITLE_05_L_JB:
            result = self.getting_prices('beer_brok_export_svitle_05_l_jb', get_beer_Brok_Export_svitle_05l_jb)
        elif nn_respond == BEER_CARLING_SVITLE_05_L_JB:
            result = self.getting_prices('beer_carling_svitle_05_l_jb', get_beer_Carling_svitle_05l_jb)
        elif nn_respond == BEER_KETEN_BRUG_BLANCHE_ELEGANT_05_L_JB:
            result = self.getting_prices('beer_keten_brug_blanche_elegant_05_l_jb',
                                         get_beer_Keten_Brug_Blanche_Elegant_05l_jb)
        elif nn_respond == BEER_BUDWEISER_NONALCO_05_L_JB:
            result = self.getting_prices('beer_budweiser_nonalco_05_l_jb', get_beer_Budweiser_nonalco_05l_jb)
        elif nn_respond == BEER_FELDSCHLOSSCHEN_WHEAT_BEER_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_feldschlosschenWheatBeer_svitle_nefilter_05_l_jb',
                                         get_beer_Feldschlosschen_Wheat_Beer_svitle_nefilter_05l_jb)
        elif nn_respond == BEER_TETERIV_HMILNA_VISHNYA_NAPIVTEMNE_05_L_JB:
            result = self.getting_prices('beer_teteriv_hmilna_vishnya_napivtemne_05_l_jb',
                                         get_beer_Teteriv_hmilna_vishnya_napivtemne_05l_jb)
        elif nn_respond == BEER_GROTWERG_SVITLE_NONALCO_05_L_JB:
            result = self.getting_prices('beer_grotwerg_svitle_05_l_jb', get_beer_Grotwerg_svitle_nonalco_05l_jb)
        elif nn_respond == BEER_HOLLAND_IMPORT_SVITLE_05_L_JB:
            result = self.getting_prices('beer_holland_import_svitle_05_l_jb', get_beer_Holland_import_svitle_05l_jb)
        elif nn_respond == BEER_GOLDEN_CASTLE_EXPORT_SVITLE_05_L_JB:
            result = self.getting_prices('beer_golden_castle_export_svitle_05_l_jb',
                                         get_beer_Golden_castle_export_svitle_05l_jb)
        elif nn_respond == BEER_5_0_ORIGINAL_CRAFT_BEER_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_5_0_original_craft_beer_nefilter_svitle_05_l_jb',
                                         get_beer_5_0_original_craft_beer_nefilter_svitle_05l_jb)
        elif nn_respond == BEER_GUINESS_DRAUGHT_TEMNE_044_L_JB:
            result = self.getting_prices('beer_guinness_draught_temne_044_l_jb', get_beer_Guinness_draught_temne_05l_jb)
        elif nn_respond == BEER_GRIMBERGEN_DOUBLE_AMBREE_NAPIVTEMNE_05_L_JB:
            result = self.getting_prices('beer_grimbergenDoubleAmbree_napivtemne_05_l_jb',
                                         get_beer_GrimbergenDoubleAmbree_napivtemne_05l_jb)
        elif nn_respond == BEER_WARSTEINER_PREMIUM_VERUM_SVITLE_05_L_JB:
            result = self.getting_prices('beer_warsteinerPremiumVerum_svitle_05_l_jb',
                                         get_beer_WarsteinerPremiumVerum_svitle_05l_jb)
        elif nn_respond == BEER_DAB_TEMNE_05_L_JB:
            result = self.getting_prices('beer_dab_temne_05_l_jb', get_beer_DAB_temne_05l_jb)
        elif nn_respond == BEER_GRIMBERGEN_BLANCHE_SVITLE_05_L_JB:
            result = self.getting_prices('beer_grimbergenBlanche_svitle_05_l_jb',
                                         get_beer_GrimbergenBlanche_svitle_05l_jb)
        elif nn_respond == BEER_KLOSTERKELLER_WEISSBIER_CHINA_SVITLE_NEFILTER_05_L_JB:
            result = self.getting_prices('beer_klosterkellerWeissbierChina_nefilter_svitle_05_l_jb',
                                         get_beer_KlosterkellerWeissbierChina_svitle_05l_jb)
        elif nn_respond == BEER_KARPACKIE_PILS_SVITLE_05_L_JB:
            result = self.getting_prices('beer_karpackiePils_svitle_05_l_jb', get_beer_KarpackiePils_svitle_05l_jb)
        elif nn_respond == BEER_5_0_ORIGINAL_PILLS_SVITLE_05_L_JB:
            result = self.getting_prices('beer_5_0_OriginalPills_svitle_05_l_jb',
                                         get_beer_5_0_OriginalPills_svitle_05l_jb)
        elif nn_respond == BEER_5_0_ORIGINAL_LAGER_SVITLE_05_L_JB:
            result = self.getting_prices('beer_5_0_Original_lager_svitle_05_l_jb',
                                         get_beer_5_0_OriginalLager_svitle_05l_jb)
        elif nn_respond == BEER_5_0_ORIGINAL_WEISS_BEER_SVITLE__NEFILTER_05_L_JB:
            result = self.getting_prices('beer_5_0_Original_weiss_beer_nefilter_svitle_05_l_jb',
                                         get_beer_5_0_Original_Weiss_nefilter_svitle_05l_jb)
        elif nn_respond == BEER_FAHNEN_BRAU_SVITLE_05_L_JB:
            result = self.getting_prices('beer_Fahnen_Brau_svitle_05_l_jb', get_beer_Fahnen_Brau_svitle_05l_jb)
        elif nn_respond == BEER_GOSSER_LIGHT_SVITLE_05_L_JB:
            result = self.getting_prices('beer_Gosser_Light_svitle_05_l_jb', get_beer_Gosser_light_svitle_05l_jb)
        elif nn_respond == BEER_HOLLANDIA_IMPORT_SVITLE_033_L_JB:
            result = self.getting_prices('beer_Hollandia_Import_svitle_033_l_jb',
                                         get_beer_HollandiaImport_svitle_033l_jb)
        elif nn_respond == BEER_HOLSTEN_PILSENER_048_L_JB:
            result = self.getting_prices('beer_Holsten_Pilsner_048_l_jb', get_beer_Holsten_Pilsener_048l_jb)
        elif nn_respond == BEER_OBOLON_PREMIUM_EXTRA_BREW_SVITLE_05_L_JB:
            result = self.getting_prices('beer_Obolon_Premium_Extra_Brew_svitle_05_l_jb',
                                         get_beer_Obolon_Premium_Extra_Brew_svitle_05l_jb)
        elif nn_respond == BEER_LVIVSKE_SVITLE_048_L_JB:
            result = self.getting_prices('beer_Lvivske_svitle_48_l_jb', get_beer_Lvivske_svitle_048l_jb)
        elif nn_respond == BEER_CARLSBERG_PREMIUM_PILSNER_SVITLE_05_L_JB:
            result = self.getting_prices('beer_Carlsberg_Premium_Pilsner_svitle_05_l_jb',
                                         get_beer_Carlsberg_Premium_Pilsner_svitle_05l_jb)
        elif nn_respond == BEER_CARLSBERG_PILSNER_05_L_JB:
            result = self.getting_prices('beer_Carlsberg_Pilsner_05_l_jb', get_beer_Carlsberg_Pilsner_05l_jb)
        elif nn_respond == BANANA:
            result = self.getting_prices('banana', get_banana)
        elif nn_respond == ORANGE:
            result = self.getting_prices('orange', get_orange)
        elif nn_respond == KIWI:
            result = self.getting_prices('kiwi', get_kiwi)
        elif nn_respond == COCONUT:
            result = self.getting_prices('coconut', get_coconut)
        elif nn_respond == GRAPEFRUIT:
            result = self.getting_prices('grapefruit', get_grapefruit)
        elif nn_respond == POMEGRANATE:
            result = self.getting_prices('pomegranate', get_pomegranate)
        elif nn_respond == MANGO:
            result = self.getting_prices('mango', get_mango)
        elif nn_respond == POTATO:
            result = self.getting_prices('potato', get_potato)
        elif nn_respond == TOMATO:
            result = self.getting_prices('tomato', get_tomato)
        elif nn_respond == CUCUMBER:
            result = self.getting_prices('cucumber', get_cucumber)
        elif nn_respond == KABACHKI:
            result = self.getting_prices('kabachki', get_kabachki)
        elif nn_respond == RED_BOLG_PAPPER:
            result = self.getting_prices('red_bolgar_papper', get_red_bolg_papper)
        elif nn_respond == YELLOW_BOLG_PAPPER:
            result = self.getting_prices('yellow_bolgar_papper', get_yellow_bolg_papper)
        elif nn_respond == ASPARAGUS:
            result = self.getting_prices('asparagus', get_asparagus)
        elif nn_respond == BROCCOLI:
            result = self.getting_prices('brokoli', get_broccoli)
        elif nn_respond == CAPTAIN_MORGAN_SPICED_GOLD_1L:
            result = self.getting_prices('captain_morgan_spiced_gold_1_l', get_captain_morgan_spiced_gold_1_l)
        elif nn_respond == BELLS_ORIGINAL_07L:
            result = self.getting_prices('bells_original_07_l', get_bells_original_07_l)
        elif nn_respond == MARTINI_ASTI_BILE_075L:
            result = self.getting_prices('martini_asti_white_075_l', get_martini_asti_bile_075_l)
        elif nn_respond == JAMESON_IRISH_WHISKEY_07L:
            result = self.getting_prices('jameson_07_l', get_jameson_irish_whiskey_075_l)
        elif nn_respond == BELLS_ORIGINAL_1L:
            result = self.getting_prices('bells_original_1_l', get_bells_original_1_l)
        elif nn_respond == CAPTAIN_MORGAN_SPICED_GOLD_05L:
            result = self.getting_prices('captain_morgan_spiced_gold_05_l', get_captain_morgan_spiced_gold_05_l)
        elif nn_respond == JAMESON_IRISH_WHISKEY_05L:
            result = self.getting_prices('jameson_05_l', get_jameson_irish_whiskey_05_l)
        elif nn_respond == JW_RED_LABEL_05L:
            result = self.getting_prices('jw_red_label_05_l', get_jw_red_label_05_l)
        elif nn_respond == BELLS_SPICED_07L:
            result = self.getting_prices('bells_spiced_07_l', get_bells_spiced_07_l)
        elif nn_respond == BALLANTINES_FINEST_07L:
            result = self.getting_prices('ballantines_finest_07_l', get_ballantines_finest_07_l)
        elif nn_respond == JACK_DANILES_07L:
            result = self.getting_prices('jack_daniels_07_l', get_jack_daniels_07_l)
        elif nn_respond == JACK_DANILES_1L:
            result = self.getting_prices('jack_daniels_1_l', get_jack_daniels_1_l)
        elif nn_respond == JIM_BEAM_WHITE_07L:
            result = self.getting_prices('jim_beam_white_07_l', get_jim_beam_white_07_l)
        elif nn_respond == BORJOMI_SILNOGAZ_05L:
            result = self.getting_prices('borjomi_05_l', get_borjomi_silnogaz_05_l)
        elif nn_respond == MORSHINSKAYA_NEGAZ_15L:
            result = self.getting_prices('morshinska_negaz_15_l', get_morshinskaya_negaz_15_l)
        elif nn_respond == MORSHINSKAYA_LOW_GAZ_15L:
            result = self.getting_prices('morshinska_lowgaz_15_l', get_morshinskaya_low_gaz_15_l)
        elif nn_respond == MORSHINSKAYA_HIGH_GAZ_15L:
            result = self.getting_prices('morshinska_highgaz_15_l', get_morshinskaya_high_gaz_15_l)
        elif nn_respond == NASH_SIK_APPLE_GRAPE_02L:
            result = self.getting_prices('nash_sik_apple_grape_02_l', get_nash_sik_apple_grape_02_l)
        elif nn_respond == NASH_SIK_APPLE_CARROT_02L:
            result = self.getting_prices('nash_sik_apple_carrot_02_l', get_nash_sik_apple_carrot_02_l)
        elif nn_respond == NASH_SIK_ORANGE_02L:
            result = self.getting_prices('nash_sik_orange_02_l', get_nash_sik_orange_02_l)
        elif nn_respond == NASH_SIK_MULTIFRUKT_02L:
            result = self.getting_prices('nash_sik_multifrukt_02_l', get_nash_sik_multifrukt_02_l)
        elif nn_respond == NASH_SIK_APPLE_PEACH_02L:
            result = self.getting_prices('nash_sik_apple_peach_02_l', get_nash_sik_apple_peach_02_l)
        elif nn_respond == NASH_SIK_PEAR_APPLE_02L:
            result = self.getting_prices('nash_sik_pear_apple_02_l', get_nash_sik_pear_apple_02_l)
        elif nn_respond == NASH_SIK_MULTIVITAMIN_02L:
            result = self.getting_prices('nash_sik_multivitamin_02_l', get_nash_sik_multivitamin_02_l)
        elif nn_respond == NASH_SIK_APPLE_02L:
            result = self.getting_prices('nash_sik_apple_02_l', get_nash_sik_apple_02_l)
        elif nn_respond == NASH_SIK_APPLE_STRAWBERRY_02L:
            result = self.getting_prices('nash_sik_apple_strawberry_02_l', get_nash_sik_apple_strawberry_02_l)
        elif nn_respond == NON_STOP_ORIGINAL_025L:
            result = self.getting_prices('non_stop_original_025_l', get_non_stop_original_025_l)
        elif nn_respond == NON_STOP_ORIGINAL_05L:
            result = self.getting_prices('non_stop_original_05_l', get_non_stop_original_05_l)
        elif nn_respond == NON_STOP_JUNGLE_025L:
            result = self.getting_prices('non_stop_jungle_025_l', get_non_stop_jungle_025_l)
        elif nn_respond == NON_STOP_BOOST_05L:
            result = self.getting_prices('non_stop_boost_05_l', get_non_stop_boost_05_l)
        elif nn_respond == NON_STOP_ULTRA_05L:
            result = self.getting_prices('non_stop_ultra_05_l', get_non_stop_ultra_05_l)
        elif nn_respond == NON_STOP_BOOST_025L:
            result = self.getting_prices('non_stop_boost_025_l', get_non_stop_boost_025_l)
        elif nn_respond == BURN_CLASSIC_025L:
            result = self.getting_prices('burn_classic_025_l', get_burn_classic_025_l)
        elif nn_respond == BURN_CLASSIC_05L:
            result = self.getting_prices('burn_classic_05_l', get_burn_classic_05_l)
        elif nn_respond == BURN_MANGO_025L:
            result = self.getting_prices('burn_mango_025_l', get_burn_mango_025_l)
        elif nn_respond == BURN_APPLE_KIWI_05L:
            result = self.getting_prices('burn_apple_kiwi_05_l', get_burn_apple_kiwi_05_l)
        elif nn_respond == BURN_DARK_ENERGY_025L:
            result = self.getting_prices('burn_dark_energy_025_l', get_burn_dark_energy_025_l)
        elif nn_respond == RED_BULL_025L:
            result = self.getting_prices('red_bull_025_l', get_red_bull_025_l)
        elif nn_respond == RED_BULL_0355L:
            result = self.getting_prices('red_bull_0355_l', get_red_bull_0355_l)
        elif nn_respond == RED_BULL_0473L:
            result = self.getting_prices('red_bull_0473_l', get_red_bull_0473_l)
        elif nn_respond == RED_BULL_0591L:
            result = self.getting_prices('red_bull_0591_l', get_red_bull_0591_l)
        elif nn_respond == RED_BULL_SUGAR_FREE_025L:
            result = self.getting_prices('red_bull_sugar_free_025_l', get_red_bull_sugar_free_025_l)
        elif nn_respond == RED_BULL_RED_EDITION_CAVUN_025L:
            result = self.getting_prices('red_bull_red_edition_cavun_025_l', get_red_bull_red_edition_cavun_025_l)
        elif nn_respond == RED_BULL_YELLOW_EDITION_TROPIC_FRUITS_025L:
            result = self.getting_prices('red_bull_yellow_edition_tropic_fruits_025_l',
                                         get_red_bull_yellow_edition_tropic_fruits_025_l)
        elif nn_respond == MONSTER_0355L:
            result = self.getting_prices('monster_0355_l', get_monster_0355_l)
        elif nn_respond == MONSTER_THE_DOCTOR_0355L:
            result = self.getting_prices('monster_the_doctor_0355_l', get_monster_the_doctor_0355_l)
        elif nn_respond == MONSTER_ULTRA_ZERO_0355L:
            result = self.getting_prices('monster_ultra_zero_0355_l', get_monster_ultra_zero_0355_l)
        elif nn_respond == MONSTER_JUICED_0355L:
            result = self.getting_prices('monster_juiced_0355_l', get_monster_juiced_0355_l)
        elif nn_respond == PIT_BULL_COFFEE_025L:
            result = self.getting_prices('pit_bull_coffee_0250_l', get_pit_bull_coffee_025_l)
        elif nn_respond == PIT_BULL_POWER_025L:
            result = self.getting_prices('pit_bull_power_0250_l', get_pit_bull_power_025_l)
        elif nn_respond == PIT_BULL_X_025L:
            result = self.getting_prices('pit_bull_X_0250_l', get_pit_bull_x_025_l)
        elif nn_respond == PIT_BULL_EXTRA_VITAMIN_C_025L:
            result = self.getting_prices('pit_bull_extra_vitamin_c_0250_l', get_pit_bull_extra_vitamin_c_025_l)
        elif nn_respond == PIT_BULL_025L:
            result = self.getting_prices('pit_bull_0250_l', get_pit_bull_025_l)
        elif nn_respond == MACCOFFEE_GOLD_ROZCHIN_SOFT_PACK_60_GR:
            result = self.getting_prices('maccoffee_gold_rozch_soft_pack_60_gr',
                                         get_maccoffee_gold_rozch_soft_pack_60_gr)
        elif nn_respond == NESCAFE_GOLD_ROZCH_SOFT_PACK_120_GR:
            result = self.getting_prices('nescafe_gold_rozch_soft_pack_120_gr', get_nescafe_gold_rozch_soft_pack_120_gr)
        elif nn_respond == GRANO_DORADO_GOLD_SOFT_P_130GR:
            result = self.getting_prices('grano_dorado_gold_rozch_soft_pack_130_gr', get_grano_dorado_gold_soft_pack_130_gr)
        elif nn_respond == NESCAFE_CLASSIC_SOFT_P_60GR:
            result = self.getting_prices('nescafe_classic_soft_pack_60_gr', get_nescafe_classic_soft_pack_60_gr)
        elif nn_respond == CHORNA_CARTA_GOLD_SOFT_P_400GR:
            result = self.getting_prices('chorna_karta_gold_soft_pack_400_gr', get_chorna_carta_gold_soft_pack_400_gr)
        elif nn_respond == BOUNTY_SMALL:
            result = self.getting_prices('bounty_57gr', get_bounty_small)
        elif nn_respond == BOUNTY_BIG:
            result = self.getting_prices('bounty_85gr', get_bounty_big)
        elif nn_respond == MARS_SMALL:
            result = self.getting_prices('mars_51gr', get_mars_small)
        elif nn_respond == MARS_BIG:
            result = self.getting_prices('mars_70gr', get_mars_big)
        elif nn_respond == NUTS_STRAWBERRY:
            result = self.getting_prices('nuts_strawberry', get_nuts_strawberry)
        elif nn_respond == NUTS_SMALL:
            result = self.getting_prices('nuts_42gr', get_nuts_small)
        elif nn_respond == NUTS_KING_SIZE:
            result = self.getting_prices('nuts_king_size_60gr', get_nuts_king_size)
        elif nn_respond == SNICKERS_SMALL:
            result = self.getting_prices('snickers_50gr', get_snickers_small)
        elif nn_respond == SNICKERS_SUPER:
            result = self.getting_prices('snickers_super_112_5gr', get_snickers_super)
        elif nn_respond == SNICKERS_CREAMY_PEANUT_BUTTER:
            result = self.getting_prices('snickers_creamy_peanut_butter_54_75gr', get_snickers_creamy_peanut_butter)
        elif nn_respond == SNICKERS_CREAMY_PEANUT_BUTTER_SMALL:
            result = self.getting_prices('snickers_creamy_peanut_butter_36_5gr', get_snickers_creamy_peanut_butter_small)
        elif nn_respond == TWIX_PECHIVO_KARAMEL_50GR:
            result = self.getting_prices('twix_50gr', get_twix_pechivo_karamel_50gr)
        elif nn_respond == TWIX_EXTRA_PECHIVO_KARAMEL_75GR:
            result = self.getting_prices('twix_75gr', get_twix_extra_pechivo_karamel_75gr)
        elif nn_respond == VODKA_ABSOLUT_05L:
            result = self.getting_prices('vodka_absolut_05l', get_vodka_absolut_05l)
        elif nn_respond == VODKA_ABSOLUT_1L:
            result = self.getting_prices('vodka_absolut_1l', get_vodka_absolut_1l)
        elif nn_respond == VODKA_ABSOLUT_07L:
            result = self.getting_prices('vodka_absolut_07l', get_vodka_absolut_07l)
        elif nn_respond == VODKA_ABSOLUT_LIME_07L:
            result = self.getting_prices('vodka_absolut_lime_07l', get_vodka_absolut_lime_07l)
        elif nn_respond == VODKA_ABSOLUT_GRAPEFRUIT_07L:
            result = self.getting_prices('vodka_absolut_grapefruit_07l', get_vodka_absolut_grapefruit_07l)
        elif nn_respond == VODKA_ABSOLUT_ELYX_07L:
            result = self.getting_prices('vodka_absolut_elyx_07l', get_vodka_absolut_elyx_07l)
        elif nn_respond == VODKA_ABSOLUT_CITRON_07L:
            result = self.getting_prices('vodka_absolut_citron_07l', get_vodka_absolut_citron_07l)
        elif nn_respond == VODKA_ABSOLUT_KURANT_07L:
            result = self.getting_prices('vodka_absolut_kurant_07l', get_vodka_absolut_kurant_07l)
        elif nn_respond == VODKA_ABSOLUT_WATERMELON_07L:
            result = self.getting_prices('vodka_absolut_watermelon_07l', get_vodka_absolut_watermelon_07l)
        elif nn_respond == VODKA_ABSOLUT_MANDARIN_07L:
            result = self.getting_prices('vodka_absolut_mandarin_07l', get_vodka_absolut_mandarin_07l)
        elif nn_respond == VODKA_FINLAND_05L:
            result = self.getting_prices('vodka_finland_05l', get_vodka_finland_05l)
        elif nn_respond == VODKA_FINLAND_07L:
            result = self.getting_prices('vodka_finland_07l', get_vodka_finland_07l)
        elif nn_respond == VODKA_FINLAND_1L:
            result = self.getting_prices('vodka_finland_1l', get_vodka_finland_1l)
        elif nn_respond == VODKA_FINLAND_REDBERRY_05L:
            result = self.getting_prices('vodka_finland_redberry_05l', get_vodka_finland_redberry_05l)
        elif nn_respond == VODKA_FINLAND_REDBERRY_1L:
            result = self.getting_prices('vodka_finland_redberry_1l', get_vodka_finland_redberry_1l)
        elif nn_respond == VODKA_FINLAND_CRANBERRY_05L:
            result = self.getting_prices('vodka_finland_cranberry_05l', get_vodka_finland_cranberry_05l)
        elif nn_respond == VODKA_FINLAND_CRANBERRY_1L:
            result = self.getting_prices('vodka_finland_cranberry_1l', get_vodka_finland_cranberry_1l)
        elif nn_respond == VODKA_FINLAND_GRAPEFRUIT_05L:
            result = self.getting_prices('vodka_finland_grapefruit_05l', get_vodka_finland_grapefruit_05l)
        elif nn_respond == VODKA_FINLAND_LIME_05L:
            result = self.getting_prices('vodka_finland_lime_05l', get_vodka_finland_lime_05l)
        elif nn_respond == VODKA_FINLAND_COCONUT_05L:
            result = self.getting_prices('vodka_finland_coconut_05l', get_vodka_finland_coconut_05l)
        elif nn_respond == VODKA_FINLAND_BLACKCURRANT_05L:
            result = self.getting_prices('vodka_finland_blackcurrant_05l', get_vodka_finland_blackcurrant_05l)
        elif nn_respond == VODKA_FINLAND_LIME_1L:
            result = self.getting_prices('vodka_finland_lime_1l', get_vodka_finland_lime_1l)
        elif nn_respond == VODKA_FINLAND_BLACKCURRANT_1L:
            result = self.getting_prices('vodka_finland_blackcurrant_1l', get_vodka_finland_blackcurrant_1l)
        elif nn_respond == VODKA_FINLAND_GRAPEFRUIT_1L:
            result = self.getting_prices('vodka_finland_grapefruit_1l', get_vodka_finland_grapefruit_1l)
        elif nn_respond == VODKA_FINLAND_WHITE_175L:
            result = self.getting_prices('vodka_finland_white_175l', get_vodka_finland_white_175l)
        elif nn_respond == VODKA_NEMIROFF_DELIKAT_SOFT_05L:
            result = self.getting_prices('nemiroff_delicat_05l', get_vodka_nemiroff_delikat_soft_05l)
        elif nn_respond == VODKA_NEMIROFF_SHTOF_05L:
            result = self.getting_prices('nemiroff_shtof_05l', get_vodka_nemiroff_shtof_05l)
        elif nn_respond == VODKA_NEMIROFF_UKR_PSHEN_05L:
            result = self.getting_prices('nemiroff_ukr_pshen_05l', get_vodka_nemiroff_ukr_pshen_05l)
        elif nn_respond == VODKA_NEMIROFF_DELUX_05L:
            result = self.getting_prices('nemiroff_delux_05l', get_vodka_nemiroff_delux_05l)
        elif nn_respond == VODKA_NEMIROFF_LEX_05L:
            result = self.getting_prices('nemiroff_lex_05l', get_vodka_nemiroff_lex_05l)
        elif nn_respond == SHAMP_ARTEMIVSKE_BILE_NAPIVSOLOD:
            result = self.getting_prices('artemivske_bile_napivsolodke', get_artemivske_bile_napivsolod_075l)
        elif nn_respond == SHAMP_ARTEMIVSKE_ROJEVE_NAPIVSUHE:
            result = self.getting_prices('artemivske_rojeve_napivsuhe', get_artemivske_roj_napivsuh_075l)
        elif nn_respond == SHAMP_ARTEMIVSKE_BILE_BRUT:
            result = self.getting_prices('artemivske_bile_brut', get_artemivske_bile_brut_075l)
        elif nn_respond == SHAMP_ARTEMIVSKE_COLLECT_NAPIVSUHE:
            result = self.getting_prices('artemivske_coll_napivsuhe', get_artemivske_coll_napivsuh_075l)
        elif nn_respond == SHAMP_ARTEMIVSKE_CHERVONE_NAPIVSOLOD:
            result = self.getting_prices('artemivske_chervone_napivsolodke', get_artemivske_cherv_napivsuh_075l)
        elif nn_respond == SHAMP_BAGRATIONI_BILE_NAPIVSOLOD:
            result = self.getting_prices('bagrationi_bile_napivsolodke', get_bagrationi_bile_napivsolod_075l)
        elif nn_respond == SHAMP_BAGRATIONI_BILE_NAPIVSUHE:
            result = self.getting_prices('bagrationi_bile_napivsuhe', get_bagrationi_bile_napivsuh_075l)
        elif nn_respond == SHAMP_BAGRATIONI_BILE_BRUT:
            result = self.getting_prices('bagrationi_bile_brut', get_bagrationi_bile_brut_075l)
        elif nn_respond == SHAMP_BAGRATIONI_ROJ_NAPIVSOLOD:
            result = self.getting_prices('bagrationi_roj_napivsolodke', get_bagrationi_rojeve_napivsolod_075l)
        elif nn_respond == SHAMP_BAGRATIONI_GOLD_NAPIVSOLOD:
            result = self.getting_prices('bagrationi_gold_napivsolodke', get_bagrationi_gold_napivsolod_075l)
        elif nn_respond == SHAMP_BOLGRAD_BILE_BRUT:
            result = self.getting_prices('bolgrad_bile_brut', get_bolgrad_bile_brut_075l)
        elif nn_respond == SHAMP_BOLGRAD_BILE_NAPIVSOLOD:
            result = self.getting_prices('bolgrad_bile_napivsolodke', get_bolgrad_bile_napivsolod_075l)
        elif nn_respond == SHAMP_BOLGRAD_NECTAR_BILE_SOLODKE:
            result = self.getting_prices('bolgrad_nectar_bile_solodke', get_bolgrad_nectar_bile_solodke_075l)
        elif nn_respond == SHAMP_FRAN_BULV_BILE_NAPIVSUHE:
            result = self.getting_prices('fran_bulvar_bile_napivsuhe', get_fran_bulv_bile_napivsuh_075l)
        elif nn_respond == SHAMP_FRAN_BULV_BILE_BRUT:
            result = self.getting_prices('fran_bulvar_bile_brut', get_fran_bulv_bile_brut_075l)
        elif nn_respond == SHAMP_FRAN_BULV_BILE_NAPIVSOLOD:
            result = self.getting_prices('fran_bulvar_bile_napivsolodke', get_fran_bulv_bile_napivsolod_075l)
        elif nn_respond == STARIY_KOHETI_3:
            result = self.getting_prices('stariy_kaheti_3', get_stariy_koheti_3)
        elif nn_respond == STARIY_KOHETI_5:
            result = self.getting_prices('stariy_kaheti_5', get_stariy_koheti_5)
        elif nn_respond == BRENDI_KOBLEVO_RESERVE_EXTRA_OLD_8_YEARS_05L:
            result = self.getting_prices('koblevo_extra_old_8', get_brendi_koblevo_reserve_extra_old_8_years)
        elif nn_respond == SHABO_VSOP_5:
            result = self.getting_prices('shabo_vsop_5', get_shabo_vsop_5)
        elif nn_respond == SHABO_VS_3:
            result = self.getting_prices('shabo_vs_3', get_shabo_vs_3)
        elif nn_respond == SHABO_1788_4:
            result = self.getting_prices('shabo_1788_4', get_shabo_1788_4)
        elif nn_respond == SHABO_1788_RESERV:
            result = self.getting_prices('shabo_1788_reserv', get_shabo_1788_reserv)
        elif nn_respond == SHABO_VS_RESERV:
            result = self.getting_prices('shabo_vs_reserv', get_shabo_vs_reserv)
        elif nn_respond == SHABO_VSOP_RESERV:
            result = self.getting_prices('shabo_vsop_reserv', get_shabo_vsop_reserv)
        elif nn_respond == AZNAURI_3:
            result = self.getting_prices('aznauri_3', get_aznauri_3)
        elif nn_respond == AZNAURI_5:
            result = self.getting_prices('aznauri_5', get_aznauri_5)
        elif nn_respond == AZNAURI_4:
            result = self.getting_prices('aznauri_4', get_aznauri_4)
        elif nn_respond == AZNAURI_BLACK_BARREL_5:
            result = self.getting_prices('aznauri_black_barrel_5', get_aznauri_black_barrel_5)
        elif nn_respond == ADJARI_3:
            result = self.getting_prices('adjari_3', get_adjari_3)
        elif nn_respond == ADJARI_5:
            result = self.getting_prices('adjari_5', get_adjari_5)
        elif nn_respond == ADJARI_4:
            result = self.getting_prices('adjari_4', get_adjari_4)
        elif nn_respond == HENNESY_VS:
            result = self.getting_prices('hennesy_vs', get_hennesy_vs)
        elif nn_respond == HENNESY_VSOP:
            result = self.getting_prices('hennesy_vsop', get_hennesy_vsop)
        elif nn_respond == ALEXX_GOLD_VSOP:
            result = self.getting_prices('alexx_gold_vsop', get_alexx_gold_vsop)
        elif nn_respond == ALEXX_SILVER_VS:
            result = self.getting_prices('alexx_silver_vs', get_alexx_silver_vs)
        elif nn_respond == ARARAT_5:
            result = self.getting_prices('ararat_5', get_ararat_5)
        elif nn_respond == ARARAT_AHTAMAR_10:
            result = self.getting_prices('ararat_ahtamar_10', get_ararat_ahtamar_10)
        elif nn_respond == ARARAT_3:
            result = self.getting_prices('ararat_3', get_ararat_3)
        elif nn_respond == ARARAT_NAIRI_20:
            result = self.getting_prices('ararat_nairi_20', get_ararat_nairi_20)
        elif nn_respond == STARIY_KOHETI_4:
            result = self.getting_prices('stariy_kaheti_4', get_stariy_koheti_4)
        elif nn_respond == GREEN_DAY_AIR_05L:
            result = self.getting_prices('green_day_air_05l', get_green_day_air_05l)
        elif nn_respond == GREEN_DAY_ULTRA_SOFT_05L:
            result = self.getting_prices('green_day_ultra_soft_05l', get_green_day_ultra_soft_05l)
        elif nn_respond == GREEN_DAY_ORGANIC_LIFE_05L:
            result = self.getting_prices('green_day_organic_life_05l', get_green_day_organic_life_05l)
        elif nn_respond == GREEN_DAY_CRYSTAL_05L:
            result = self.getting_prices('green_day_crystal_05l', get_green_day_crystal_05l)
        elif nn_respond == GREEN_DAY_05L:
            result = self.getting_prices('green_day_05l', get_green_day_05l)
        elif nn_respond == MEDOFF_CLASSIC_05L:
            result = self.getting_prices('medoff_classic_05l', get_medoff_classic_05l)
        elif nn_respond == SMIRNOFF_RED_05L:
            result = self.getting_prices('smirnoff_red_05l', get_smirnoff_red_05l)
        elif nn_respond == KOZACKA_RADA_CLASSIC_05L:
            result = self.getting_prices('kozacka_rada_classic_05l', get_kozacka_rada_classic_05l)
        elif nn_respond == KOZACKA_RADA_OSOBLIVA_05L:
            result = self.getting_prices('kozacka_rada_osobliva_05l', get_kozacka_rada_osobliva_05l)
        elif nn_respond == ZUBROWKA_BISON_GRASS_05L:
            result = self.getting_prices('zubrowka_bison_grass_05l', get_zubrowka_bison_grass_05l)
        elif nn_respond == ZUBROWKA_BIALA_05L:
            result = self.getting_prices('zubrowka_biala_05l', get_zubrowka_biala_05l)
        elif nn_respond == ZUBROWKA_CZARNA_05L:
            result = self.getting_prices('zubrowka_czarna_05l', get_zubrowka_czarna_05l)
        elif nn_respond == VOZDUH_LEGKA_05L:
            result = self.getting_prices('vozduh_legka_osobliva_05l', get_vozduh_legka_05l)
        elif nn_respond == VOZDUH_ALPHA_05L:
            result = self.getting_prices('vozduh_legka_osobliva_05l', get_vozduh_alpha_05l)
        elif nn_respond == PERSHA_GILDIYA_VERHOVNA_05L:
            result = self.getting_prices('persha_gildiya_verhovna_05l', get_persha_gild_verhovna_05l)
        elif nn_respond == PERSHA_GILDIYA_ZNATNA_05L:
            result = self.getting_prices('persha_gildiya_znatna_05l', get_persha_gild_znatna_05l)
        elif nn_respond == PERSHA_GILDIYA_POVAJNA_05L:
            result = self.getting_prices('persha_gildiya_povajna_05l', get_persha_gild_povajna_05l)
        elif nn_respond == HLIB_DAR_CLASSIC_05L:
            result = self.getting_prices('hlib_dar_classic_05l', get_hlibniy_dar_classic_05l)
        elif nn_respond == HLIB_DAR_PROR_ZERNO_05L:
            result = self.getting_prices('hlib_dar_pror_zerno_05l', get_hlibniy_dar_pror_zerno_05l)
        elif nn_respond == HLIB_DAR_JITNYA_05L:
            result = self.getting_prices('hlib_dar_jitnya_05l', get_hlibniy_dar_jitnya_05l)
        elif nn_respond == HLIB_DAR_PSHENICHNA_05L:
            result = self.getting_prices('hlib_dar_pshenichna_05l', get_hlibniy_dar_pshen_05l)
        elif nn_respond == GREEN_DAY_ORGANIC_LIFE_07L:
            result = self.getting_prices('green_day_organic_life_07l', get_green_day_organic_life_07l)
        elif nn_respond == GREEN_DAY_07L:
            result = self.getting_prices('green_day_07l', get_green_day_07l)
        elif nn_respond == GREEN_DAY_ULTRA_SOFT_07L:
            result = self.getting_prices('green_day_ultra_soft_07l', get_green_day_ultra_soft_07l)
        elif nn_respond == GREEN_DAY_AIR_07L:
            result = self.getting_prices('green_day_air_07l', get_green_day_air_07l)
        elif nn_respond == GREEN_DAY_CRYSTAL_07L:
            result = self.getting_prices('green_day_crystal_07l', get_green_day_crystal_07l)
        elif nn_respond == MEDOFF_CLASSIC_07L:
            result = self.getting_prices('medoff_classic_07l', get_medoff_classic_07l)
        elif nn_respond == NEMIROFF_DELIKAT_MYAKA_07L:
            result = self.getting_prices('nemiroff_delikat_myaka_07l', get_nemiroff_delikat_myaka_07l)
        elif nn_respond == NEMIROFF_OSOBLIVA_SHTOF_07L:
            result = self.getting_prices('nemiroff_osob_shtof_07l', get_nemiroff_osob_shtof_07l)
        elif nn_respond == NEMIROFF_DELUXE_07L:
            result = self.getting_prices('nemiroff_deluxe_07l', get_nemiroff_deluxe_07l)
        elif nn_respond == NEMIROFF_LEX_07L:
            result = self.getting_prices('nemiroff_lex_07l', get_nemiroff_lex_07l)
        elif nn_respond == ZUBROWKA_07L:
            result = self.getting_prices('zubrowka_bison_grass_07l', get_zubrowka_07l)
        elif nn_respond == ZUBROWKA_CZARNA_07L:
            result = self.getting_prices('zubrowka_czarna_07l', get_zubrowka_czarna_07l)
        elif nn_respond == HETMAN_07L:
            result = self.getting_prices('hetman_07l', get_hetman_07l)
        elif nn_respond == KOZACKA_RADA_CLASSIC_07L:
            result = self.getting_prices('kozacka_rada_classic_07l', get_kozacka_rada_classic_07l)
        elif nn_respond == KOZACKA_RADA_PREMIUM_07L:
            result = self.getting_prices('kozacka_rada_premium_07l', get_kozacka_rada_premium_07l)
        elif nn_respond == KOZACKA_RADA_OSOBLIVA_07L:
            result = self.getting_prices('kozacka_rada_osobliva_07l', get_kozacka_rada_osobliva_07l)
        elif nn_respond == PERSHA_GILDIYA_POVAJNA_07L:
            result = self.getting_prices('persha_gildiya_povajna_07l', get_persha_gildya_povajna_07l)
        elif nn_respond == PERSHA_GILDIYA_VERHOVNA_07L:
            result = self.getting_prices('persha_gildiya_verhovna_07l', get_persha_gildya_verhovna_07l)
        elif nn_respond == PERSHA_GILDIYA_ZNATNA_07L:
            result = self.getting_prices('persha_gildiya_znatna_07l', get_persha_gildya_znatna_07l)
        elif nn_respond == HLIB_DAR_CLASSIC_07L:
            result = self.getting_prices('hlibniy_dar_classic_07l', get_hlib_dar_classic_07l)
        elif nn_respond == MEDOFF_CLASSIC_1L:
            result = self.getting_prices('medoff_classic_1l', get_medoff_classic_1l)
        elif nn_respond == NEMIROFF_SHTOF_1L:
            result = self.getting_prices('nemiroff_shtof_1l', get_nemiroff_shtof_1l)
        elif nn_respond == NEMIROFF_DELICAT_SOFT_1L:
            result = self.getting_prices('nemiroff_delicat_1l', get_nemiroff_delicat_soft_1l)
        elif nn_respond == ZUBROWKA_BISON_GRASS_1L:
            result = self.getting_prices('zubrowka_bison_grass_1l', get_zubrowka_bison_grass_1l)
        elif nn_respond == ZUBROWKA_BIALA_1L:
            result = self.getting_prices('zubrowka_biala_1l', get_zubrowka_biala_1l)
        elif nn_respond == HETMAN_1L:
            result = self.getting_prices('hetman_1l', get_hetman_1l)
        elif nn_respond == KOZACKA_RADA_OSOBLIVA_1L:
            result = self.getting_prices('kozacka_rada_osobliva_1l', get_kozacka_rada_osobliva_1l)
        elif nn_respond == KOZACKA_RADA_CLASSIC_1L:
            result = self.getting_prices('kozacka_rada_classic_1l', get_kozacka_rada_classic_1l)
        elif nn_respond == HLIB_DAR_CLASSIC_1L:
            result = self.getting_prices('hlib_dar_classic_1l', get_hlib_dar_classic_1l)
        elif nn_respond == SVINNE_REBRO:
            result = self.getting_prices('svinne_rebro', get_svin_rebro)
        elif nn_respond == SALO:
            result = self.getting_prices('salo', get_salo)
        elif nn_respond == SVINNA_GOMILKA:
            result = self.getting_prices('svinna_gomilka', get_svin_gomilka)
        elif nn_respond == SVIN_PECHINKA:
            result = self.getting_prices('svinna_pechinka', get_pechinka_svin)
        elif nn_respond == SVIN_GULYASH:
            result = self.getting_prices('svin_gulyash', get_svin_gulyash)
        elif nn_respond == SVIN_PIDJARKA:
            result = self.getting_prices('svinna_pidjarka', get_svin_pidjarka)
        elif nn_respond == SVIN_KOREYKA:
            result = self.getting_prices('svin_koreyka', get_svin_koreyka)
        elif nn_respond == SVIN_VIRIZKA:
            result = self.getting_prices('svin_virizka', get_svin_virezka)
        elif nn_respond == SVIN_LOPATKA_BEZ_KISTKI:
            result = self.getting_prices('svin_lopatka_bez_kistki', get_lopatka_bez_kistki)
        elif nn_respond == SVIN_OKIST_BEZ_KISTKI:
            result = self.getting_prices('svin_okist_bez_kistki', get_svin_okist_bez_kistki)
        elif nn_respond == SVIN_FARSH:
            result = self.getting_prices('svin_farsh', get_svin_farsh)
        elif nn_respond == SVIN_BITOK_BEZ_KISTI:
            result = self.getting_prices('svin_bitok_bez_kosti', get_svin_bitok_bez_kistki)
        elif nn_respond == SVIN_RAGU:
            result = self.getting_prices('svin_ragu', get_svin_ragu)
        elif nn_respond == SVIN_OSHEYEK_BEZ_KISTKI:
            result = self.getting_prices('svin_osheek_bez_kistki', get_svin_osheek_bez_kistki)
        elif nn_respond == KURYACHA_CHETVERT:
            result = self.getting_prices('kuryacha_chetvert', get_kuryacha_chetvert)
        elif nn_respond == KURYACHE_STEGNO:
            result = self.getting_prices('kuryache_stegno', get_kuryache_stegno)
        elif nn_respond == KURYACHE_KRILO:
            result = self.getting_prices('kuryache_krilo', get_kuryache_krilo)
        elif nn_respond == KURYACHE_FILE:
            result = self.getting_prices('kuryache_file', get_kuryache_file)
        elif nn_respond == KURYACHA_GOMILKA:
            result = self.getting_prices('kuryacha_gomilka', get_kuryacha_gomilka)
        elif nn_respond == COCA_COLA_ORIGINAL_033_JB:
            result = self.getting_prices('coca_cola_original_033_jb', get_coca_cola_origin_033_jb)
        elif nn_respond == COCA_COLA_ZERO_033_JB:
            result = self.getting_prices('coca_cola_zero_033_jb', get_coca_cola_zero_033_jb)
        elif nn_respond == FANTA_ORANGE_033_JB:
            result = self.getting_prices('fanta_orange_033_jb', get_fanta_orange_033_jb)
        elif nn_respond == FANTA_PINEAPPLE_033_JB:
            result = self.getting_prices('fanta_pineapple_033_jb', get_fanta_pineapple_033_jb)
        elif nn_respond == SPRITE_033_JB:
            result = self.getting_prices('sprite_033_jb', get_sprite_033_jb)
        elif nn_respond == COCA_COLA_ORIGINAL_025_GLASS:
            result = self.getting_prices('coca_cola_original_025_gl', get_coca_cola_025_glass)
        elif nn_respond == COCA_COLA_ZERO_025_GLASS:
            result = self.getting_prices('coca_cola_zero_025_gl', get_coca_cola_zero_025_glass)
        elif nn_respond == COCA_COLA_ORIGINAL_05_PL:
            result = self.getting_prices('coca_cola_original_05_pl', get_coca_cola_original_05_pl)
        elif nn_respond == COCA_COLA_ZERO_05_PL:
            result = self.getting_prices('coca_cola_zero_05_pl', get_coca_cola_zero_05_pl)
        elif nn_respond == FANTA_ORANGE_05_PL:
            result = self.getting_prices('fanta_orange_05_pl', get_fanta_orange_05_pl)
        elif nn_respond == SPRITE_05_PL:
            result = self.getting_prices('sprite_05_pl', get_sprite_05_pl)
        elif nn_respond == COCA_COLA_ORIGINAL_15_PL:
            result = self.getting_prices('coca_cola_original_15_pl', get_coca_cola_original_15_pl)
        elif nn_respond == COCA_COLA_ZERO_15_PL:
            result = self.getting_prices('coca_cola_zero_15_pl', get_coca_cola_zero_15_pl)
        elif nn_respond == SPRITE_15_PL:
            result = self.getting_prices('sprite_15_pl', get_sprite_15_pl)
        elif nn_respond == FANTA_ORANGE_15_PL:
            result = self.getting_prices('fanta_orange_15_pl', get_fanta_orange_15_pl)
        elif nn_respond == FANTA_SHOKATA_15_PL:
            result = self.getting_prices('fanta_shokata_15_pl', get_fanta_shokata_15_pl)
        elif nn_respond == FANTA_MANDARIN_15_PL:
            result = self.getting_prices('fanta_mandarin_15_pl', get_fanta_mandarin_15_pl)
        elif nn_respond == CHIPS_LUXE_BECON_133GR:
            result = self.getting_prices('chips_luxe_becon_133gr', get_chips_luxe_becon_133gr)
        elif nn_respond == CHIPS_LUXE_PAPRIKA_133GR:
            result = self.getting_prices('chips_luxe_paprika_133gr', get_chips_luxe_paprika_133gr)
        elif nn_respond == CHIPS_LUXE_CRAB_133GR:
            result = self.getting_prices('chips_luxe_crab_133gr', get_chips_luxe_crab_133gr)
        elif nn_respond == CHIPS_LUXE_SMETANA_CIBULYA_133GR:
            result = self.getting_prices('chips_luxe_smetana_cibulya_133gr', get_chips_luxe_smetana_cibulya_133gr)
        elif nn_respond == CHIPS_LUXE_SIR_133GR:
            result = self.getting_prices('chips_luxe_sir_133gr', get_chips_luxe_sir_133gr)
        elif nn_respond == CHIPS_LUXE_SIR_71GR:
            result = self.getting_prices('chips_luxe_sir_71gr', get_chips_luxe_sir_71gr)
        elif nn_respond == CHIPS_LUXE_BECON_71GR:
            result = self.getting_prices('chips_luxe_becon_71gr', get_chips_luxe_becon_71gr)
        elif nn_respond == CHIPS_LUXE_PAPRIKA_71GR:
            result = self.getting_prices('chips_luxe_paprika_71gr', get_chips_luxe_paprika_71gr)
        elif nn_respond == CHIPS_LUXE_CRAB_71GR:
            result = self.getting_prices('chips_luxe_crab_71gr', get_chips_luxe_crab_71gr)
        elif nn_respond == CHIPS_LUXE_SMETANA_CIBULYA_71GR:
            result = self.getting_prices('chips_luxe_smetana_cibulya_71gr', get_chips_luxe_smetana_cibulya_71gr)
        elif nn_respond == CHIPS_LUXE_HVIL_LISICHKI_125GR:
            result = self.getting_prices('chips_luxe_hvil_lisichki_125gr', get_chips_luxe_hvilyasti_lisichki_125gr)
        elif nn_respond == CHIPS_LUXE_SMETANA_CIBULYA_183GR:
            result = self.getting_prices('chips_luxe_smetana_cibulya_183gr', get_chips_luxe_smetana_cibulya_183gr)
        elif nn_respond == CHIPS_LUXE_BECON_183GR:
            result = self.getting_prices('chips_luxe_becon_183gr', get_chips_luxe_becon_183gr)
        elif nn_respond == CHIPS_LUXE_SIR_183GR:
            result = self.getting_prices('chips_luxe_sir_183gr', get_chips_luxe_sir_183gr)
        elif nn_respond == CHIPS_PRINGLES_GREECE_SOUCE_CACIKI_185GR:
            result = self.getting_prices('chips_pringles_greece_souce_caciki_185gr', get_chips_pringles_greec_souse_caciki_185gr)
        elif nn_respond == CHIPS_PRINGLES_PAPRIKA_165GR:
            result = self.getting_prices('chips_pringles_paprika_165gr', get_chips_pringles_paprika_165gr)
        elif nn_respond == CHIPS_PRINGLES_PIZZA_PEPERONI_185GR:
            result = self.getting_prices('chips_pringles_pizza_peperoni_185gr', get_chips_pringles_pizza_peperoni_185gr)
        elif nn_respond == CHIPS_PRINGLES_SIR_CIBULYA_165GR:
            result = self.getting_prices('chips_pringles_sir_cubylya_165gr', get_chips_pringles_sir_cibulya_165gr)
        elif nn_respond == CHIPS_PRINGLES_ORIGINAL_165GR:
            result = self.getting_prices('chips_pringles_original_165gr', get_chips_pringles_original_165gr)
        elif nn_respond == CHIPS_PRINGLES_SIR_165GR:
            result = self.getting_prices('chips_pringles_sir_165gr', get_chips_pringles_sir_165gr)
        elif nn_respond == CHIPS_LAYS_PAPRIKA_120GR:
            result = self.getting_prices('chips_lays_paprika_120gr', get_chips_lays_paprika_120gr)
        elif nn_respond == CHIPS_LAYS_CRAB_120GR:
            result = self.getting_prices('chips_lays_crab_120gr', get_chips_lays_crab_120gr)
        elif nn_respond == CHIPS_LAYS_SIR_60GR:
            result = self.getting_prices('chips_lays_sir_60gr', get_chips_lays_sir_60gr)
        elif nn_respond == SIR_SVET_FETA_UKR_ROZSIL_45_1KG:
            result = self.getting_prices('sir_svet_feta_ukr_rozsil_45_1kg', get_sir_svet_feta_ukr_rozsil_45_1kg)
        elif nn_respond == OLIVKI_EXTRA_CHORNI_BEZ_KIST_300GR:
            result = self.getting_prices('olivki_extra_chorni_bez_kist_300gr', get_olivki_extra_chorn_bez_kist_300gr)
        elif nn_respond == OLIV_OIL_POVNA_CHASHA_913GR:
            result = self.getting_prices('oliv_oil_povna_chasha_913gr', get_oliv_oil_povna_chasha_913gr)
        elif nn_respond == BASILIK_CHERVONIY_SVIJIY:
            result = self.getting_prices('basilik_chervoniy_svij', get_basilik_svij)
        elif nn_respond == PELMENI_GERKULES_FIRM_400GR:
            result = self.getting_prices('pelmeni_gerkules_firm_400gr', get_pelmeni_gerkules_firm_400gr)
        elif nn_respond == PELMENI_GERKULES_FIRM_800GR:
            result = self.getting_prices('pelmeni_gerkules_firm_800gr', get_pelmeni_gerkules_firm_800gr)
        elif nn_respond == PELMENI_GERKULES_INDEYKA_400GR:
            result = self.getting_prices('pelmeni_gerkules_indeyka_400gr', get_pelmeni_gerkules_indeyka_400gr)
        elif nn_respond == PELMENI_TRI_VEDMEDI_FIRM_800GR:
            result = self.getting_prices('pelmeni_tri_vedmedi_firm_800gr', get_pelmeni_tri_vedmid_firm_800gr)
        elif nn_respond == PELMENI_TRI_VEDMEDI_MISHUTKA_TELYATINA_400GR:
            result = self.getting_prices('pelmeni_tri_vedmedi_mishutka_400gr', get_pelmeni_tri_vedmid_mishutka_telyatina_400gr)
        elif nn_respond == PELMENI_EXTRA_FIRM_800GR:
            result = self.getting_prices('pelmeni_extra_firm_800gr', get_pelmeni_extra_firm_800gr)
        elif nn_respond == PELMENI_EXTRA_SIBIR_500GR:
            result = self.getting_prices('pelmeni_extra_sibir_500gr', get_pelmeni_extra_sibir_500gr)
        elif nn_respond == PELMENI_EXTRA_RAVIOLI_DOMASHNIE_800GR:
            result = self.getting_prices('pelmeni_extra_ravioli_dom_800gr', get_pelmeni_extra_rav_dom_800gr)
        elif nn_respond == SEVEN_UP_033JB:
            result = self.getting_prices('seven_up_033_jb', get_7up_033_jb)
        elif nn_respond == KAVUN:
            result = self.getting_prices('kavun', get_kavun)
        elif nn_respond == JIVCHIK_APPLE_2l:
            result = self.getting_prices('jivchik_apple_2l', get_jivchik_apple_2l)
        elif nn_respond == JIVCHIK_APPLE_1l:
            result = self.getting_prices('jivchik_apple_1l', get_jivchik_apple_1l)
        elif nn_respond == JIVCHIK_APPLE_05l:
            result = self.getting_prices('jivchik_apple_05l', get_jivchik_apple_05l)
        elif nn_respond == JIVCHIK_GRUSHA_1l:
            result = self.getting_prices('jivchik_grusha_1l', get_jivchik_grusha_1l)
        elif nn_respond == JIVCHIK_SMART_COLA_2l:
            result = self.getting_prices('jivchik_smart_cola_2l', get_jivchik_smart_cola_2l)
        elif nn_respond == JIVCHIK_LIMON_2l:
            result = self.getting_prices('jivchik_limon_2l', get_jivchik_limon_2l)
        elif nn_respond == JIVCHIK_SMART_COLA_1l:
            result = self.getting_prices('jivchik_smart_cola_1l', get_jivchik_smart_cola_1l)
        elif nn_respond == BIOLA_STRAWBERRY_KIWI_2L:
            result = self.getting_prices('biola_strawb_kiwi_2l', get_biola_strawb_kiwi_2l)
        elif nn_respond == BIOLA_LEMONAD_2L:
            result = self.getting_prices('biola_lemonad_2l', get_biola_lemonad_2l)
        elif nn_respond == BON_BOISSON_LIMONAD_1L:
            result = self.getting_prices('bon_boisson_limonad_1l', get_bon_boisson_limonad_1l)
        elif nn_respond == BON_BOISSON_LIMONAD_2L:
            result = self.getting_prices('bon_boisson_limonad_2l', get_bon_boisson_limonad_2l)
        elif nn_respond == BON_BOISSON_LIME_MINT_2L:
            result = self.getting_prices('bon_boisson_lime_mint_2l', get_bon_boisson_lime_mint_2l)
        elif nn_respond == BON_BOISSON_BAIKAL_2L:
            result = self.getting_prices('bon_boisson_baikal_2l', get_bon_boisson_baikal_2l)
        elif nn_respond == BON_BOISSON_TARHUN_2L:
            result = self.getting_prices('bon_boisson_tarhun_2l', get_bon_boisson_tarhun_2l)
        elif nn_respond == BON_BOISSON_BAIKAL_1L:
            result = self.getting_prices('bon_boisson_baikal_1l', get_bon_boisson_baikal_1l)
        elif nn_respond == BON_BOISSON_MULT_SOK_1L:
            result = self.getting_prices('bon_boisson_mult_sok_1l', get_bon_boisson_mult_sok_1l)
        elif nn_respond == BON_BOISSON_MANGO_2L:
            result = self.getting_prices('bon_boisson_mango_2l', get_bon_boisson_mango_2l)
        elif nn_respond == BON_BOISSON_MOHITO_2L:
            result = self.getting_prices('bon_boisson_mohito_2l', get_bon_boisson_mohito_2l)
        elif nn_respond == BON_BOISSON_SITRO_2L:
            result = self.getting_prices('bon_boisson_sitro_2l', get_bon_boisson_sitro_2l)
        elif nn_respond == BON_BOISSON_KREM_SODA_2L:
            result = self.getting_prices('bon_boisson_krem_soda_2l', get_bon_boisson_krem_soda_2l)
        elif nn_respond == BON_BOISSON_MULT_SOK_2L:
            result = self.getting_prices('bon_boisson_mult_sok_2l', get_bon_boisson_mult_sok_2l)
        elif nn_respond == MIRINDA_ORANGE_033JB:
            result = self.getting_prices('mirinda_orange_033jb', get_mirinda_orange_033jb)
        elif nn_respond == MIRINDA_ORANGE_05L:
            result = self.getting_prices('mirinda_orange_05l', get_mirinda_orange_05l)
        elif nn_respond == SCHWEPPES_GRANAT_1L:
            result = self.getting_prices('schweppes_granat_1l', get_schweppes_granat_1l)
        elif nn_respond == SCHWEPPES_INDIAN_TONIC_033JB:
            result = self.getting_prices('schweppes_indian_tonic_033jb', get_schweppes_indian_tonic_033jb)
        elif nn_respond == SCHWEPPES_ORIGINAL_BITTER_LEMON_033JB:
            result = self.getting_prices('schweppes_original_bitter_lemon_033jb', get_schweppes_original_bitter_lemon_033jb)
        elif nn_respond == SCHWEPPES_ORIGINAL_BITTER_LEMON_075pl:
            result = self.getting_prices('schweppes_original_bitter_lemon_075l', get_schweppes_original_bitter_lemon_075pl)
        elif nn_respond == SCHWEPPES_ORIGINAL_BITTER_LEMON_1L:
            result = self.getting_prices('schweppes_original_bitter_lemon_1l', get_schweppes_original_bitter_lemon_1l)
        elif nn_respond == SCHWEPPES_CLASSIC_MOJITO_033JB:
            result = self.getting_prices('schweppes_classic_mojito_033jb', get_schweppes_classic_mojito_033jb)
        elif nn_respond == FARSH_GOVYAJIY:
            result = self.getting_prices('farsh_govyajiy', get_farsh_govyajiy)
        elif nn_respond == RICE_EXTRA_KRUGLIY_1KG:
            result = self.getting_prices('rice_extra_krugliy_1kg', get_rice_krug_extra_1kg)
        elif nn_respond == MASLO_FERMA_SELYANSKE_73JIR_180GR:
            result = self.getting_prices('maslo_ferma_selyanske_73jir_180gr', get_maslo_slivochne_ferma_73jir_180gr)
        elif nn_respond == MASLO_FERMA_CHOCOLAT_62JIR_180GR:
            result = self.getting_prices('maslo_sliv_ferma_chocolat_62jir_180gr', get_maslo_slivochne_ferma_chokolat_kakao_62jir_180gr)
        elif nn_respond == MASLO_FERMA_EXTRA_82JIR_180GR:
            result = self.getting_prices('maslo_sliv_ferma_extra_82_5jir_180gr', get_maslo_slivochne_ferma_extra_82jir_180gr)
        elif nn_respond == MASLO_FERMA_BUTER_63JIR_180GR:
            result = self.getting_prices('maslo_sliv_ferma_buter_63jir_180gr', get_maslo_slivochne_ferma_buter_63jir_180gr)
        elif nn_respond == MASLO_FERMA_SELYANSKE_73JIR_400GR:
            result = self.getting_prices('maslo_ferma_selyanske_73jir_400gr', get_maslo_slivochne_ferma_73jir_400gr)
        elif nn_respond == MASLO_JAGOTINSKE_EXTRA_82_5_180GR:
            result = self.getting_prices('maslo_sliv_jagotinske_extra_82_5_180gr', get_maslo_jagotinske_extra_82_5_180gr)
        elif nn_respond == MASLO_JAGOTINSKE_BUTER_69_2_200GR:
            result = self.getting_prices('maslo_sliv_jagotinske_buter_69_2_200gr', get_maslo_jagotinske_buter_69_2_200gr)
        elif nn_respond == MASLO_SELYANSKE_EXTRA_82_180GR:
            result = self.getting_prices('maslo_sliv_selyanske_extra_82_180gr', get_maslo_selyanske_extra_82_180gr)
        elif nn_respond == MASLO_SELYANSKE_BUTER_63_180GR:
            result = self.getting_prices('maslo_sliv_selyanske_buter_63_180gr', get_maslo_selyanske_buter_63_180gr)
        elif nn_respond == MASLO_SELYANSKE_72_5_180GR:
            result = self.getting_prices('maslo_sliv_selyanske_72_5_180gr', get_maslo_selyanske_72_5_180gr)
        elif nn_respond == MASLO_GLOBINO_EXTRA_82_500GR:
            result = self.getting_prices('maslo_sliv_globino_extra_82_500gr', get_maslo_globino_extra_82_500gr)
        elif nn_respond == MASLO_GLOBINO_BEZLAKTOZ_82_180GR:
            result = self.getting_prices('maslo_sliv_globino_bezlaktoz_82_180gr', get_maslo_globino_bezlaktoz_82_180gr)
        elif nn_respond == MASLO_GALICHINA_82_5_180GR:
            result = self.getting_prices('maslo_sliv_galichina_82_5_180gr', get_maslo_galichina_82_5_180gr)
        elif nn_respond == MASLO_GALICHINA_SELYANSKE_72_6_180GR:
            result = self.getting_prices('maslo_sliv_galichina_selyanske_72_6_180gr', get_maslo_galichina_selyanske_72_6_180gr)
        elif nn_respond == MASLO_MALOKIYA_EXTRA_82_180GR:
            result = self.getting_prices('maslo_sliv_malokiya_82_180gr', get_maslo_malokiya_extra_82_180gr)
        elif nn_respond == MASLO_FARM_FRESH_EXTRA_82_180GR:
            result = self.getting_prices('maslo_sliv_farm_fresh_extra_82_180gr', get_maslo_farm_fresh_extra_82_180gr)
        elif nn_respond == MASLO_FARM_FRESH_SELYANSKE_82_180GR:
            result = self.getting_prices('maslo_sliv_farm_fresh_selyanske_73_180gr', get_maslo_farm_fresh_selyanske_73_180gr)
        elif nn_respond == MASLO_PRESIDENT_82_200GR:
            result = self.getting_prices('maslo_sliv_president_82_200gr', get_maslo_president_82_200gr)
        elif nn_respond == MASLO_PRESIDENT_82_400GR:
            result = self.getting_prices('maslo_sliv_president_82_400gr', get_maslo_president_82_400gr)
        elif nn_respond == MASLO_PRESIDENT_SOLONE_80_200GR:
            result = self.getting_prices('maslo_sliv_president_solone_80_200gr', get_maslo_president_solone_80_200gr)
        elif nn_respond == JACOBS_MONARCH_BANKA_95GR:
            result = self.getting_prices('jacobs_monarch_banka_95gr', get_jacobs_monarch_banka_95gr)
        elif nn_respond == JACOBS_MONARCH_BANKA_190GR:
            result = self.getting_prices('jacobs_monarch_banka_190gr', get_jacobs_monarch_banka_190gr)
        elif nn_respond == JACOBS_MONARCH_BANKA_200GR:
            result = self.getting_prices('jacobs_monarch_banka_200gr', get_jacobs_monarch_banka_200gr)
        elif nn_respond == JACOBS_MONARCH_BANKA_100GR:
            result = self.getting_prices('jacobs_monarch_banka_100gr', get_jacobs_monarch_banka_100gr)
        elif nn_respond == JACOBS_MONARCH_BANKA_50GR:
            result = self.getting_prices('jacobs_monarch_banka_50gr', get_jacobs_monarch_banka_50gr)
        elif nn_respond == JACOBS_MONARCH_CLASSICO_PACK_225GR:
            result = self.getting_prices('jacobs_monarch_classico_pack_225gr', get_jacobs_monarch_classico_pack_225gr)
        elif nn_respond == JACOBS_BARISTA_STRONG_PACK_225GR:
            result = self.getting_prices('jacobs_barista_strong_pack_225gr', get_jacobs_barista_strong_pack_225gr)
        elif nn_respond == JACOBS_KRONUNG_500GR:
            result = self.getting_prices('jacobs_kronung_500gr', get_jacobs_kronung_500gr)
        elif nn_respond == JACOBS_MONARCH_CLASSICO_PACK_70GR:
            result = self.getting_prices('jacobs_monarch_classico_pack_70gr', get_jacobs_monarch_classico_pack_70gr)
        elif nn_respond == JACOBS_MONARCH_INTENSE_PACK_200GR:
            result = self.getting_prices('jacobs_monarch_intense_200gr', get_jacobs_monarch_intense_pack_200gr)
        elif nn_respond == JACOBS_ESPRESSO_PACK_230GR:
            result = self.getting_prices('jacobs_espresso_230gr', get_jacobs_espresso_pack_230gr)
        elif nn_respond == JACOBS_BARISTA_CLASSIC_PACK_225GR:
            result = self.getting_prices('jacobs_barista_classic_pack_225gr', get_jacobs_barista_classic_pack_225gr)
        elif nn_respond == JACOBS_MONARCH_INTENSE_PACK_400GR:
            result = self.getting_prices('jacobs_monarch_intense_400gr', get_jacobs_monarch_intense_pack_400gr)
        elif nn_respond == JACOBS_MONARCH_CLASSICO_PACK_400GR:
            result = self.getting_prices('jacobs_monarch_classico_pack_400gr', get_jacobs_monarch_classic_pack_400gr)
        elif nn_respond == JACOBS_MONARCH_ROZCH_PACK_60GR:
            result = self.getting_prices('jacobs_monarch_rozch_60gr', get_jacobs_monarch__rozch_60gr)
        elif nn_respond == JACOBS_MONARCH_ROZCH_PACK_425GR:
            result = self.getting_prices('jacobs_monarch_rozch_425gr', get_jacobs_monarch__rozch_425gr)
        elif nn_respond == NESCAFE_GOLD_PACK_165_GR:
            result = self.getting_prices('nescafe_gold_rozch_pack_165gr', get_nescafe_gold_rozch_pack_165gr)
        elif nn_respond == NESCAFE_GOLD_PACK_310_GR:
            result = self.getting_prices('nescafe_gold_rozch_pack_310gr', get_nescafe_gold_rozch_pack_310gr)
        elif nn_respond == NESCAFE_CLASSIC_PACK_170_GR:
            result = self.getting_prices('nescafe_classic_rozch_pack_170gr', get_nescafe_classic_rozch_pack_170gr)
        elif nn_respond == NESCAFE_GOLD_PACK_360_GR:
            result = self.getting_prices('nescafe_gold_rozch_pack_360gr', get_nescafe_gold_rozch_pack_360gr)
        elif nn_respond == NESCAFE_CLASSIC_PACK_30_GR:
            result = self.getting_prices('nescafe_classic_rozch_pack_30gr', get_nescafe_classic_rozch_pack_30gr)
        elif nn_respond == NESCAFE_GOLD_PACK_30_GR:
            result = self.getting_prices('nescafe_gold_rozch_pack_30gr', get_nescafe_gold_rozch_pack_30gr)
        elif nn_respond == NESCAFE_GOLD_PACK_60_GR:
            result = self.getting_prices('nescafe_gold_rozch_pack_60gr', get_nescafe_gold_rozch_pack_60gr)
        elif nn_respond == NESCAFE_CLASSIC_PACK_300_GR:
            result = self.getting_prices('nescafe_classic_rozch_pack_300gr', get_nescafe_classic_rozch_pack_300gr)
        elif nn_respond == NESCAFE_GOLD_PACK_260_GR:
            result = self.getting_prices('nescafe_gold_rozch_pack_260gr', get_nescafe_gold_rozch_pack_260gr)
        elif nn_respond == CARTE_NOIRE_PACK_140GR:
            result = self.getting_prices('carte_noire_pack_rozch_140gr', get_carte_noire_rozch_pack_140gr)
        elif nn_respond == CARTE_NOIRE_PACK_70GR:
            result = self.getting_prices('carte_noire_pack_rozch_70gr', get_carte_noire_rozch_pack_70gr)
        elif nn_respond == CARTE_NOIRE_CARAMEL_PACK_120GR:
            result = self.getting_prices('carte_noire_caramel_pack_rozch_120gr', get_carte_noire_caramel_rozch_pack_120gr)
        elif nn_respond == CARTE_NOIRE_PACK_210GR:
            result = self.getting_prices('carte_noire_rozch_pack_210gr', get_carte_noire_rozch_pack_210gr)
        elif nn_respond == CARTE_NOIRE_PACK_280GR:
            result = self.getting_prices('carte_noire_rozch_pack_280gr', get_carte_noire_rozch_pack_280gr)
        elif nn_respond == AMBASSADOR_PREMIUM_PACK_50GR:
            result = self.getting_prices('ambassador_premium_rozch_pack_50gr', get_ambassador_premium_rozch_pack_50gr)
        elif nn_respond == AMBASSADOR_PREMIUM_PACK_100GR:
            result = self.getting_prices('ambassador_premium_rozch_pack_100gr', get_ambassador_premium_rozch_pack_100gr)
        elif nn_respond == AMBASSADOR_PREMIUM_PACK_250GR:
            result = self.getting_prices('ambassador_premium_rozch_pack_250gr', get_ambassador_premium_rozch_pack_250gr)
        elif nn_respond == AMBASSADOR_PREMIUM_PACK_170GR:
            result = self.getting_prices('ambassador_premium_rozch_pack_170gr', get_ambassador_premium_rozch_pack_170gr)
        elif nn_respond == AMBASSADOR_PREMIUM_PACK_400GR:
            result = self.getting_prices('ambassador_premium_rozch_pack_400gr', get_ambassador_premium_rozch_pack_400gr)
        elif nn_respond == AMBASSADOR_PREMIUM_PACK_500GR:
            result = self.getting_prices('ambassador_premium_rozch_pack_500gr', get_ambassador_premium_rozch_pack_500gr)
        elif nn_respond == AMBASSADOR_PREMIUM_JAR_GLASS_190GR:
            result = self.getting_prices('ambassador_premium_rozch_glass_190gr', get_ambassador_premium_rozch_glass_190gr)
        elif nn_respond == CHORNA_CARTA_GOLD_200GR:
            result = self.getting_prices('chorna_carta_gold_rozch_pack_200gr', get_chorna_carta_gold_rozch_pack_200gr)
        elif nn_respond == CHORNA_CARTA_GOLD_100GR:
            result = self.getting_prices('chorna_carta_gold_rozch_pack_100gr', get_chorna_carta_gold_rozch_pack_100gr)
        elif nn_respond == TCHIBO_GOLD_SELECTION_GLASS_JAR_50GR:
            result = self.getting_prices('tchibo_gold_selection_rozch_glass_jar_50gr', get_tchibo_gold_selection_rozch_glass_jar_50gr)
        elif nn_respond == TCHIBO_GOLD_SELECTION_GLASS_JAR_100GR:
            result = self.getting_prices('tchibo_gold_selection_rozch_glass_jar_100gr', get_tchibo_gold_selection_rozch_glass_jar_100gr)
        elif nn_respond == TCHIBO_GOLD_SELECTION_GLASS_JAR_200GR:
            result = self.getting_prices('tchibo_gold_selection_rozch_glass_jar_200gr', get_tchibo_gold_selection_rozch_glass_jar_200gr)
        elif nn_respond == TCHIBO_EXCLUSIVE_GLASS_JAR_200GR:
            result = self.getting_prices('tchibo_exclusive_rozch_glass_jar_200gr', get_tchibo_exclusive_rozch_glass_jar_200gr)
        elif nn_respond == AROMA_GOLD_ROZCH_DECAFF_GLASS_JAR_100GR:
            result = self.getting_prices('aroma_gold_decaff_rozch_glass_jar_100gr', get_aroma_gold_decaff_rozch_glass_jar_100gr)
        elif nn_respond == AROMA_GOLD_ROZCH_FREEZE_DRIED_GLASS_JAR_100GR:
            result = self.getting_prices('aroma_gold_freeze_dried_rozch_glass_jar_100gr', get_aroma_gold_freeze_dried_rozch_glass_jar_100gr)
        elif nn_respond == AROMA_GOLD_ROZCH_FREEZE_DRIED_GLASS_JAR_200GR:
            result = self.getting_prices('aroma_gold_freeze_dried_rozch_glass_jar_200gr', get_aroma_gold_freeze_dried_rozch_glass_jar_200gr)
        elif nn_respond == MACCOFFEE_ARABICA_ROZCH_PACK_120GR:
            result = self.getting_prices('maccoffee_arabica_rozch_glass_jar_120gr', get_maccoffee_arabica_rozch_glass_jar_120gr)
        elif nn_respond == MAXWELL_HOUSE_INSTANT_MILD_BLEND_ROZCH_GLASS_JAR_100GR:
            result = self.getting_prices('maxwell_house_instant_mild_blend_rozch_glass_jar_100gr', get_maxwell_house_instant_mild_blend_rozch_glass_jar_100gr)
        elif nn_respond == MAXWELL_HOUSE_INSTANT_MILD_BLEND_ROZCH_GLASS_JAR_200GR:
            result = self.getting_prices('maxwell_house_instant_mild_blend_rozch_glass_jar_200gr', get_maxwell_house_instant_mild_blend_rozch_glass_jar_200gr)
        elif nn_respond == DALLMAYR_GOLD_ROZCH_GLASS_JAR_100GR:
            result = self.getting_prices('dallmayr_gold_rozch_glass_jar_100gr', get_dallmayr_gold_rozch_glass_jar_100gr)
        elif nn_respond == DALLMAYR_GOLD_ROZCH_GLASS_JAR_200GR:
            result = self.getting_prices('dallmayr_gold_rozch_glass_jar_200gr', get_dallmayr_gold_rozch_glass_jar_200gr)
        elif nn_respond == AROMA_PLATINUM_ROZCH_FREEZE_DRIED_GLASS_JAR_200GR:
            result = self.getting_prices('aroma_platinum_fr_dr_rozch_glass_jar_200gr', get_aroma_platinum_fr_dr_rozch_glass_jar_200gr)
        elif nn_respond == AROMA_PLATINUM_ROZCH_FREEZE_DRIED_GLASS_JAR_100GR:
            result = self.getting_prices('aroma_platinum_fr_dr_rozch_glass_jar_100gr', get_aroma_platinum_fr_dr_rozch_glass_jar_100gr)
        elif nn_respond == BEANIES_MINCE_PIE_ROZCH_GLASS_JAR_50GR:
            result = self.getting_prices('beanies_mince_pie_rozch_glass_jar_50gr', get_beanies_mince_pie_rozch_glass_jar_50gr)
        elif nn_respond == BEANIES_CRISTMAS_PUDDING_ROZCH_GLASS_JAR_50GR:
            result = self.getting_prices('beanies_cristmas_pudding_rozch_glass_jar_50gr', get_beanies_cristmas_pudding_rozch_glass_jar_50gr)
        elif nn_respond == BEANIES_DOUBLE_CHOCOLATE_ROZCH_GLASS_JAR_50GR:
            result = self.getting_prices('beanies_double_chocolate_rozch_glass_jar_50gr', get_beanies_double_chocolate_rozch_glass_jar_50gr)
        elif nn_respond == BEANIES_CINDER_TOFFEE_ROZCH_GLASS_JAR_50GR:
            result = self.getting_prices('beanies_cinder_toffee_rozch_glass_jar_50gr', get_beanies_cinder_toffee_rozch_glass_jar_50gr)
        elif nn_respond == BUSHIDO_KODO_ROZCH_GLASS_JAR_95GR:
            result = self.getting_prices('bushido_kodo_rozch_glass_jar_95gr', get_bushido_kodo_rozch_glass_jar_95gr)
        elif nn_respond == DAVIDOFF_RICH_AROMA_ROZCH_GLASS_JAR_100GR:
            result = self.getting_prices('davidoff_rich_aroma_rozch_glass_jar_100gr', get_davidoff_rich_aroma_rozch_glass_jar_100gr)
        elif nn_respond == DAVIDOFF_FINE_AROMA_ROZCH_GLASS_JAR_100GR:
            result = self.getting_prices('davidoff_fine_aroma_rozch_glass_jar_100gr',get_davidoff_fine_aroma_rozch_glass_jar_100gr)
        elif nn_respond == AHMAD_TEA_ENG_BREAKF_BLACK_PACK_100GR:
            result = self.getting_prices('ahmad_tea_eng_breakf_black_pack_100gr',get_ahmad_tea_eng_breakf_black_pack_100gr)
        elif nn_respond == AHMAD_TEA_GRAF_GREY_BLACK_PACK_100GR:
            result = self.getting_prices('ahmad_tea_graf_grey_black_pack_100gr',get_ahmad_tea_graf_grey_black_pack_100gr)
        elif nn_respond == AHMAD_TEA_LONDON_BLACK_PACK_100GR:
            result = self.getting_prices('ahmad_tea_london_black_pack_100gr',get_ahmad_tea_london_black_pack_100gr)
        elif nn_respond == AHMAD_TEA_ENG_N1_BLACK_PACK_100GR:
            result = self.getting_prices('ahmad_tea_english_n1_black_pack_100gr',get_ahmad_tea_eng_n1_black_pack_100gr)
        elif nn_respond == AHMAD_TEA_ENG_BREAKF_BLACK_PACK_200GR:
            result = self.getting_prices('ahmad_tea_eng_breakf_black_pack_200gr',get_ahmad_tea_eng_breakf_black_pack_200gr)
        elif nn_respond == AHMAD_TEA_GRAF_GREY_BLACK_PACK_200GR:
            result = self.getting_prices('ahmad_tea_graf_grey_black_pack_200gr',get_ahmad_tea_graf_grey_black_pack_200gr)
        elif nn_respond == AHMAD_TEA_LONDON_BLACK_PACK_100PK:
            result = self.getting_prices('ahmad_tea_london_black_pack_100pk',get_ahmad_tea_london_black_pack_100pk)
        elif nn_respond == AHMAD_TEA_GRAF_GREY_BLACK_PACK_40PK:
            result = self.getting_prices('ahmad_tea_graf_grey_black_pack_40pk',get_ahmad_tea_graf_grey_black_pack_40pk)
        elif nn_respond == AHMAD_TEA_LONDON_BLACK_PACK_25PK:
            result = self.getting_prices('ahmad_tea_london_black_pack_25pk',get_ahmad_tea_london_black_pack_25pk)
        elif nn_respond == AHMAD_TEA_LAVANDA_BERGAMOT_BLACK_PACK_20PK:
            result = self.getting_prices('ahmad_tea_lavanda_bergamot_black_pack_20pk',get_ahmad_tea_lavanda_bergamot_black_pack_20pk)
        elif nn_respond == AHMAD_TEA_ENG_BREAKF_BLACK_PACK_25PK:
            result = self.getting_prices('ahmad_tea_eng_breakf_black_pack_25pk',get_ahmad_tea_eng_breakf_black_pack_25pk)
        elif nn_respond == AHMAD_TEA_ENG_N1_BLACK_PACK_25PK:
            result = self.getting_prices('ahmad_tea_english_n1_black_pack_25pk',get_ahmad_tea_english_n1_black_pack_25pk)
        elif nn_respond == AHMAD_TEA_GRAF_GREY_BLACK_PACK_25PK:
            result = self.getting_prices('ahmad_tea_graf_grey_black_pack_25pk',get_ahmad_tea_graf_grey_black_pack_25pk)
        elif nn_respond == AHMAD_TEA_LONDON_BLACK_PACK_40PK:
            result = self.getting_prices('ahmad_tea_london_black_pack_40pk',get_ahmad_tea_london_black_pack_40pk)
        elif nn_respond == AHMAD_TEA_ENG_BREAKF_BLACK_PACK_40PK:
            result = self.getting_prices('ahmad_tea_eng_breakf_black_pack_40pk',get_ahmad_tea_eng_breakf_black_pack_40pk)
        elif nn_respond == AHMAD_TEA_ENG_N1_BLACK_PACK_40PK:
            result = self.getting_prices('ahmad_tea_english_n1_black_pack_40pk',get_ahmad_tea_english_n1_black_pack_40pk)
        elif nn_respond == AHMAD_TEA_ENG_BREAKF_BLACK_PACK_100PK:
            result = self.getting_prices('ahmad_tea_eng_breakf_black_pack_100pk',get_ahmad_tea_eng_breakf_black_pack_100pk)
        elif nn_respond == AHMAD_TEA_GRAF_GREY_BLACK_PACK_100PK:
            result = self.getting_prices('ahmad_tea_graf_grey_black_pack_100pk',get_ahmad_tea_graf_grey_black_pack_100pk)
        elif nn_respond == LIPTON_YELLOW_LABEL_BLACK_PACK_25PK:
            result = self.getting_prices('lipton_yellow_label_black_pack_25pk',get_lipton_yellow_label_black_pack_25pk)
        elif nn_respond == LIPTON_EARL_GRAY_BLACK_PACK_25PK:
            result = self.getting_prices('lipton_earl_gray_black_pack_25pk',get_lipton_earl_gray_black_pack_25pk)
        elif nn_respond == LIPTON_ENG_BREAKFAST_BLACK_PACK_25PK:
            result = self.getting_prices('lipton_eng_breakf_black_pack_25pk',get_lipton_engl_breakfast_black_pack_25pk)
        elif nn_respond == LIPTON_GOLD_TEA_BLACK_PACK_25PK:
            result = self.getting_prices('lipton_gold_tea_black_pack_25pk', get_lipton_gold_tea_black_pack_25pk)
        elif nn_respond == LIPTON_EARL_GREY_ORANGE_BLACK_PACK_25PK:
            result = self.getting_prices('lipton_earl_grey_orange_black_pack_25pk', get_lipton_earl_grey_orange_black_pack_25pk)
        elif nn_respond == LIPTON_FOREST_FRUITS_BLACK_PACK_20PK:
            result = self.getting_prices('lipton_forest_fruits_black_pack_20pk', get_lipton_forest_fruit_black_pack_20pk)
        elif nn_respond == LIPTON_INTENSE_BLACK_BLACK_PACK_25PK:
            result = self.getting_prices('lipton_intense_black_black_pack_25pk', get_lipton_intense_black_black_pack_25pk)
        elif nn_respond == LIPTON_PEACH_MANGO_BLACK_PACK_20PK:
            result = self.getting_prices('lipton_peach_mango_black_black_pack_20pk', get_lipton_peach_mango_black_black_pack_20pk)
        elif nn_respond == LIPTON_YELLOW_LABEL_BLACK_PACK_50PK:
            result = self.getting_prices('lipton_yellow_label_black_pack_50pk',get_lipton_yellow_label_black_pack_50pk)
        elif nn_respond == LIPTON_INTENSE_BLACK_BLACK_PACK_92PK:
            result = self.getting_prices('lipton_intense_black_black_pack_50pk', get_lipton_intense_black_black_pack_92pk)
        elif nn_respond == LIPTON_GOLD_TEA_BLACK_PACK_92PK:
            result = self.getting_prices('lipton_gold_tea_black_pack_92pk', get_lipton_gold_tea_black_pack_92pk)
        elif nn_respond == LIPTON_YELLOW_LABEL_BLACK_PACK_100PK:
            result = self.getting_prices('lipton_yellow_label_black_pack_100pk',get_lipton_yellow_label_black_pack_100pk)
        elif nn_respond == LIPTON_EARL_GREY_BLACK_PACK_50PK:
            result = self.getting_prices('lipton_earl_gray_black_pack_50pk', get_lipton_earl_grey_black_pack_50pk)
        elif nn_respond == LIPTON_INTENSE_MINT_GREEN_PACK_20PK:
            result = self.getting_prices('lipton_intense_mint_green_pack_20pk', get_lipton_intense_mint_green_pack_20pk)
        elif nn_respond == LIPTON_RASPBERRY_POMEGRANATE_GREEN_PACK_20PK:
            result = self.getting_prices('lipton_intense_raspb_pomegran_pack_20pk', get_lipton_raspberry_pomegranate_green_pack_20pk)
        elif nn_respond == LIPTON_CLASSIC_GREEN_PACK_25PK:
            result = self.getting_prices('lipton_classic_green_pack_25pk',get_lipton_classic_green_pack_25pk)
        elif nn_respond == BATIK_KOROLIVSKIY_STANDART_BLACK_PACK_25PK:
            result = self.getting_prices('batik_korol_std_black_pack_25pk',get_batik_korol_std_black_pack_25pk)
        elif nn_respond == BATIK_GOLD_EARL_GREY_BLACK_PACK_25PK:
            result = self.getting_prices('batik_gold_earl_grey_black_pack_25pk',get_batik_gold_earl_grey_bergamot_black_pack_25pk)
        elif nn_respond == BATIK_CHORNIY_BARHAT_BLACK_PACK_25PK:
            result = self.getting_prices('batik_chorniy_barhat_black_pack_25pk',get_batik_chorniy_barhat_black_pack_25pk)
        elif nn_respond == BATIK_JAGIDNIY_CILYNOK_BLACK_PACK_25PK:
            result = self.getting_prices('batik_jagidniy_cilynok_black_pack_25pk',get_batik_jagidniy_cilynok_black_pack_25pk)
        elif nn_respond == BATIK_BADYORIY_LIMON_BLACK_PACK_25PK:
            result = self.getting_prices('batik_badyoriy_limon_black_pack_25pk',get_batik_badyoriy_limon_black_pack_25pk)
        elif nn_respond == BATIK_GOLD_CEYLON_VISOKOGIR_BLACK_PACK_25PK:
            result = self.getting_prices('batik_gold_ceylon_visokogir_black_pack_25pk',get_batik_gold_ceylon_visokogir_black_pack_25pk)
        elif nn_respond == BATIK_BLACK_GRANUL_STANDART_STS_100GR:
            result = self.getting_prices('batik_black_granul_standart_sts_100gr',get_batik_black_granul_standart_sts_100gr)
        elif nn_respond == BATIK_KOROL_STD_BLACK_100GR:
            result = self.getting_prices('batik_korol_std_black_100gr',get_batik_korol_std_black_100gr)
        elif nn_respond == BATIK_CHORNIY_BARHAT_BLACK_PACK_60PK:
            result = self.getting_prices('batik_chorniy_barhat_black_pack_60pk',get_batik_chorniy_barhat_black_pack_60pk)
        elif nn_respond == BATIK_KOROLIVSKIY_STANDART_BLACK_PACK_100PK:
            result = self.getting_prices('batik_korol_std_black_pack_100pk', get_batik_korol_std_black_pack_100pk)
        elif nn_respond == AKBAR_GOLD_BLACK_25PK:
            result = self.getting_prices('akbar_gold_black_25pk', get_akbar_gold_black_pack_25pk)
        elif nn_respond == AKBAR_LIMON_LIME_TWIST_BLACK_20PK:
            result = self.getting_prices('akbar_limon_lime_twist_black_pack_20pk', get_akbar_limon_lime_twist_black_pack_20pk)
        elif nn_respond == AKBAR_PEACH_PASSION_PUNCH_BLACK_20PK:
            result = self.getting_prices('akbar_peach_passion_punch_black_pack_20pk', get_akbar_peach_passion_punch_black_pack_20pk)
        elif nn_respond == AKBAR_STRAWBERRY_KIWI_BLACK_20PK:
            result = self.getting_prices('akbar_strawberry_kiwi_black_pack_20pk', get_akbar_strawberry_kiwi_black_pack_20pk)
        elif nn_respond == PICKWICK_ENGLISH_BLACK_20PK:
            result = self.getting_prices('pickwick_english_black_pack_20pk', get_pickwick_english_black_pack_20pk)
        elif nn_respond == PICKWICK_MANGO_BLACK_20PK:
            result = self.getting_prices('pickwick_mango_black_pack_20pk', get_pickwick_mango_black_pack_20pk)
        elif nn_respond == PICKWICK_FOREST_FRUIT_BLACK_20PK:
            result = self.getting_prices('pickwick_forest_fruit_black_pack_20pk', get_pickwick_forest_fruit_black_pack_20pk)
        elif nn_respond == PICKWICK_EARL_GREY_BLACK_20PK:
            result = self.getting_prices('pickwick_earl_grey_black_pack_20pk', get_pickwick_earl_grey_black_pack_20pk)
        elif nn_respond == PICKWICK_STRAWBERRY_BLACK_20PK:
            result = self.getting_prices('pickwick_strawberry_black_pack_20pk', get_pickwick_strawberry_black_pack_20pk)
        elif nn_respond == PICKWICK_GREEN_PURE_GREEN_20PK:
            result = self.getting_prices('pickwick_green_pure_green_pack_20pk', get_pickwick_green_pure_green_pack_20pk)
        elif nn_respond == PICKWICK_MINT_GREEN_20PK:
            result = self.getting_prices('pickwick_mint_green_pack_20pk', get_pickwick_mint_green_pack_20pk)
        elif nn_respond == PICKWICK_ROMASHKA_GREEN_20PK:
            result = self.getting_prices('pickwick_romashka_green_pack_20pk', get_pickwick_romashka_green_pack_20pk)
        elif nn_respond == PICKWICK_SPICY_CHAI_TRAV_15PK:
            result = self.getting_prices('pickwick_spicy_chai_trav_pack_15pk', get_pickwick_spicy_chai_trav_pack_15pk)
        elif nn_respond == PICKWICK_ROMASHKA_TRAV_15PK:
            result = self.getting_prices('pickwick_romashka_trav_pack_15pk', get_pickwick_romashka_trav_pack_15pk)
        elif nn_respond == PICKWICK_IMBIR_PRYAN_TRAV_15PK:
            result = self.getting_prices('pickwick_imbir_pryan_trav_pack_15pk', get_pickwick_imbir_pryan_trav_pack_15pk)
        elif nn_respond == PICKWICK_ENERGY_TRAV_15PK:
            result = self.getting_prices('pickwick_energy_trav_pack_15pk', get_pickwick_energy_trav_pack_15pk)
        elif nn_respond == PICKWICK_IMMUNITY_TRAV_15PK:
            result = self.getting_prices('pickwick_immunity_trav_pack_15pk', get_pickwick_immunity_trav_pack_15pk)
        elif nn_respond == PICKWICK_EARL_GREY_CITRUS_TRAV_15PK:
            result = self.getting_prices('pickwick_earl_grey_citrus_trav_pack_15pk', get_pickwick_earl_frey_citrus_trav_pack_15pk)
        elif nn_respond == PICKWICK_CITRUS_BUZINA_TRAV_20PK:
            result = self.getting_prices('pickwick_citrus_buzina_trav_pack_20pk', get_pickwick_citrus_buzina_citrus_trav_pack_20pk)
        elif nn_respond == PICKWICK_IMBIR_LEMON_LEMONGRASS_TRAV_20PK:
            result = self.getting_prices('pickwick_imbir_lemon_citrus_trav_pack_20pk', get_pickwick_imbir_lemon_citrus_trav_pack_20pk)
        elif nn_respond == AZERCHAY_BERGAMOT_BLACK_25PK:
            result = self.getting_prices('azerchay_bergamot_black_pack_25pk', get_azerchay_bergamot_black_pack_25pk)
        elif nn_respond == AZERCHAY_BUKET_BLACK_25PK:
            result = self.getting_prices('azerchay_buket_black_pack_25pk', get_azerchay_buket_black_pack_25pk)
        elif nn_respond == AZERCHAY_CHEBREC_BLACK_30PK:
            result = self.getting_prices('azerchay_chebrec_black_pack_30pk', get_azerchay_chebrec_black_pack_30pk)
        elif nn_respond == SIR_PLAV_KOMO_DRUZBA_40_75GR:
            result = self.getting_prices('sir_plav_komo_druzba_40_75gr', get_sir_plav_komo_druzba_40_75gr)
        elif nn_respond == SIR_PLAV_KOMO_VERSHKOVIY_40_75GR:
            result = self.getting_prices('sir_plav_komo_vershk_40_75gr', get_sir_plav_komo_vershk_40_75gr)
        elif nn_respond == SIR_PLAV_KOMO_ZELEN_CHASNIK_40_75GR:
            result = self.getting_prices('sir_plav_komo_zelen_chasnik_40_75gr', get_sir_plav_komo_zelen_chasnik_40_75gr)
        elif nn_respond == SIR_PLAV_KOMO_CRAB_PAL_40_75GR:
            result = self.getting_prices('sir_plav_komo_crab_pal_40_75gr', get_sir_plav_crab_pal_40_75gr)
        elif nn_respond == SIR_PLAV_KOMO_GRIB_40_75GR:
            result = self.getting_prices('sir_plav_komo_grib_40_75gr', get_sir_plav_crab_pal_40_75gr)
        elif nn_respond == MILK_JAGOTINSKE_2_6_PL_870GR:
            result = self.getting_prices('milk_jagot_2_6_pl_870gr', get_milk_jagot_2_6_pl_870gr)
        elif nn_respond == MILK_JAGOTINSKE_3_2_PL_870GR:
            result = self.getting_prices('milk_jagot_3_2_pl_870gr', get_milk_jagot_3_2_pl_870gr)
        elif nn_respond == MILK_JAGOTINSKE_1_PL_870GR:
            result = self.getting_prices('milk_jagot_1_pl_870gr', get_milk_jagot_1_pl_870gr)
        elif nn_respond == MILK_JAGOTINSKE_PRYAJ_2_6_PL_870GR:
            result = self.getting_prices('milk_jagot_pryaj_2_6_pl_870gr', get_milk_jagot_pryaj_2_6_pl_870gr)
        elif nn_respond == MILK_GALICHINA_UKR_2_5_PL_870GR:
            result = self.getting_prices('milk_galichina_ukr_2_5_pl_870gr', get_milk_galichina_ukr_2_5_pl_870gr)
        elif nn_respond == MILK_PREMIYA_PITNE_2_5_PL_900GR:
            result = self.getting_prices('milk_premiya_pitne_2_5_pl_900gr', get_milk_premiya_pitne_2_5_pl_900gr)
        elif nn_respond == MILK_PREMIYA_LOKO_PITNE_2_5_PL_900GR:
            result = self.getting_prices('milk_premiya_loko_pitne_2_5_pl_900gr', get_milk_premiya_loko_pitne_2_5_pl_900gr)
        elif nn_respond == MILK_PREMIYA_LOKO_PITNE_2_5_PL_2L:
            result = self.getting_prices('milk_premiya_loko_pitne_2_5_pl_2l', get_milk_premiya_loko_pitne_2_5_pl_2l)
        elif nn_respond == MILK_PREMIYA_LOKO_PITNE_3_2_PL_2L:
            result = self.getting_prices('milk_premiya_loko_pitne_3_2_pl_2l', get_milk_premiya_loko_pitne_3_2_pl_2l)
        elif nn_respond == MILK_ORGANIC_MILK_3_5_1L:
            result = self.getting_prices('milk_organic_milk_3_5_1l', get_milk_organic_milk_3_5_pl_1l)
        elif nn_respond == MILK_ORGANIC_MILK_2_5_470GR:
            result = self.getting_prices('milk_organic_milk_2_5_470gr', get_milk_organic_milk_2_5_pl_470gr)
        elif nn_respond == MILK_ORGANIC_MILK_2_5_1L:
            result = self.getting_prices('milk_organic_milk_2_5_1l', get_milk_organic_milk_2_5_pl_1l)
        elif nn_respond == MILK_ORGANIC_MILK_BEZLAKTOZ_2_5_1L:
            result = self.getting_prices('milk_organic_milk_bezlatoz_2_5_1l', get_milk_organic_milk_bezlactoz_2_5_pl_1l)
        elif nn_respond == MILK_ORGANIC_MILK_0_5_1L:
            result = self.getting_prices('milk_organic_milk_0_5_1l', get_milk_organic_milk_0_5_pl_1l)
        elif nn_respond == MILK_PROSTONASHE_2_5_870GR:
            result = self.getting_prices('milk_prostonashe_2_5_870gr', get_milk_prostonashe_2_5_pl_870gr)
        elif nn_respond == MILK_PROSTONASHE_PRYAJ_2_5_870GR:
            result = self.getting_prices('milk_prostonashe_pryaj_2_5_870gr', get_milk_prostonashe_pryaj_2_5_pl_870gr)
        elif nn_respond == MILK_PROSTONASHE_1_870GR:
            result = self.getting_prices('milk_prostonashe_1_870gr', get_milk_prostonashe_1_pl_870gr)
        elif nn_respond == MILK_FERMA_2_5_PL_840GR:
            result = self.getting_prices('milk_ferma_2_5_pl_840gr', get_milk_ferma_2_5_pl_840gr)
        elif nn_respond == MILK_FERMA_3_2_PL_840GR:
            result = self.getting_prices('milk_ferma_3_2_pl_840gr', get_milk_ferma_3_2_pl_840gr)
        elif nn_respond == MILK_STRIY_PORICK_3_6_PL_1L:
            result = self.getting_prices('milk_stariy_porick_3_6_pl_1l', get_milk_stariy_porick_3_6_pl_1l)
        elif nn_respond == MILK_STRIY_PORICK_PRYAJ_4_PL_1L:
            result = self.getting_prices('milk_stariy_porick_pryaj_4_pl_1l', get_milk_stariy_porick_pryaj_4_pl_1l)
        elif nn_respond == MILK_STRIY_PORICK_2_5_PL_1L:
            result = self.getting_prices('milk_stariy_porick_2_5_pl_1l', get_milk_stariy_porick_2_5_pl_1l)
        elif nn_respond == MILK_MOLOKIYA_2_5_PL_870GR:
            result = self.getting_prices('milk_molkiya_2_5_pl_870gr', get_milk_molkiya_pl_2_5_870gr)
        elif nn_respond == MILK_VOLOSHKOVE_POLE_2_5_PL_900GR:
            result = self.getting_prices('milk_voloshkove_pole_2_5_pl_900gr', get_milk_voloshkove_pole_2_5_pl_900gr)
        elif nn_respond == MILK_GMZ_2_5_PL_1L:
            result = self.getting_prices('milk_gmz_n1_pl_2_5_1l', get_milk_gmz_n1_pl_2_5_1l)
        elif nn_respond == MILK_GMZ_4_pryaj_PL_1L:
            result = self.getting_prices('milk_gmz_pryaj_n1_pl_4_1l', get_milk_gmz_pryaj_n1_pl_4_1l)
        elif nn_respond == MILK_KOZ_ZOLOTA_KOZA_3_8_PL_500GR:
            result = self.getting_prices('koz_milk_zolota_koza_3_8_pl_500g', get_koz_milk_zolota_koza_3_8_pl_500gr)
        elif nn_respond == MILK_KOZ_VIRTUOSO_BY_LUK_3_8_PL_500GR:
            result = self.getting_prices('koz_milk_virtuoso_by_lukachivka_3_pl_500gr', get_koz_milk_virtuoso_by_lukachivka_3_pl_500gr)
        elif nn_respond == MILK_SVOE_3_4_PL_1L:
            result = self.getting_prices('milk_svoe_3_4_pl_1l', get_milk_svoe_3_4_pl_1l)
        elif nn_respond == MILK_OVEC_SOLOVIOV_LAKON_3_8_6_250GR:
            result = self.getting_prices('milk_ovec_soloviov_lakon_3_8_6_250gr', get_milk_ovec_soloviov_lakon_3_8_6_250gr)
        elif nn_respond == MILK_SELYANSKE_OSOBL_2_5_PAP_PAK_950GR:
            result = self.getting_prices('milk_selyanske_osobl_2_5_pap_pak_950gr', get_milk_selyanske_osobl_2_5_pap_pak_950gr)
        elif nn_respond == MILK_SELYANSKE_MICROF_PITNE_2_5_PAP_PAK_950GR:
            result = self.getting_prices('milk_selyanske_microfil_pitne_2_5_pap_pak_950gr', get_milk_selyanske_microf_pit_2_5_pap_pak_950gr)
        elif nn_respond == MILK_SELYANSKE_OSOBL_3_2_TP_950GR:
            result = self.getting_prices('milk_selyanske_3_2_tp_950gr', get_milk_selyanske_3_2_tp_950gr)
        elif nn_respond == MILK_SELYANSKE_OSOBL_RODINNE_2_5_TP_1500GR:
            result = self.getting_prices('milk_selyanske_rodinne_2_5_tp_1500gr', get_milk_selyanske_rodinne_2_5_tp_1500gr)
        elif nn_respond == MILK_SELYANSKE_OSOBL_RODINNE_2_5_TP_2000GR:
            result = self.getting_prices('milk_selyanske_rodinne_2_5_tp_2000gr', get_milk_selyanske_rodinne_2_5_tp_2000gr)
        elif nn_respond == MILK_SELYANSKE_OSOBL_1_5_TP_950GR:
            result = self.getting_prices('milk_selyanske_osobl_1_5_t_p_950gr', get_milk_selyanske_osobl_1_5_t_p_950gr)
        elif nn_respond == MILK_SELYANSKE_OSOBL_2_5_TP_500GR:
            result = self.getting_prices('milk_selyanske_osoblive_2_5_tp_500gr', get_milk_selyanske_osobl_2_5_tp_500gr)
        elif nn_respond == MILK_SELYANSKE_OSOBL_KIDS_3_2_TP_950GR:
            result = self.getting_prices('milk_selyanske_osoblive_kids_3_2_tp_950gr', get_milk_selyanske_osobl_kids_3_2_tp_950gr)
        elif nn_respond == MILK_SELYANSKE_MICROF_PITNE_3_4_3_8_TP_950GR:
            result = self.getting_prices('milk_selyanske_osobl_micro_f_3_4_3_8_tp_950grmilk_selyanske_osobl_micro_f_3_4_3_8_tp_950gr', get_milk_selyanske_osobl_micro_f_3_4_3_8_tp_950gr)
        elif nn_respond == MILK_JAGOTINSKE_ULTRA_2_6_TP_950GR:
            result = self.getting_prices('milk_jagot_ultra_2_6_tp_950gr', get_milk_jagot_ultra_2_6_tp_950gr)
        elif nn_respond == MILK_JAGOTINSKE_VELIK_2_6_TP_2000GR:
            result = self.getting_prices('milk_jagot_velik_2_6_tp_2000gr', get_milk_jagot_velik_2_6_tp_2000gr)
        elif nn_respond == MILK_JAGOTINSKE_VELIK_2_6_TP_1500GR:
            result = self.getting_prices('milk_jagot_velik_2_6_tp_1500gr', get_milk_jagot_velik_2_6_tp_1500gr)
        elif nn_respond == MOLOKO_ULTRAPASTERIZOVANE__JAGOTINSKE__3_2__T_B_950_G:
            result = self.getting_prices('Moloko_ultrapasterizovane__Jagotinske__3_2__t/b_950_g', get_Moloko_ultrapasterizovane__Jagotinske__3_2__t_b_950_g)

        elif nn_respond == MOLOKO_GALICHINA_ULTRAPASTERIZOVANE_2_5__950_G:
            result = self.getting_prices('Moloko_Galichina_ultrapasterizovane_2_5__950_g', get_Moloko_Galichina_ultrapasterizovane_2_5__950_g)
        elif nn_respond == MOLOKO_GALICHINA_ULTRAPASTERIZOVANE_3_2__950_G:
            result = self.getting_prices('Moloko_Galichina_ultrapasterizovane_3_2__950_g', get_Moloko_Galichina_ultrapasterizovane_3_2__950_g)
        elif nn_respond == MOLOKO_GALICHINA_ULTRAPASTERIZOVANE_1__T_P_950_G:
            result = self.getting_prices('Moloko_Galichina_ultrapasterizovane_1__t_p_950_g', get_Moloko_Galichina_ultrapasterizovane_1__t_p_950_g)
        elif nn_respond == MOLOKO_ULTRAPASTERIZOVANE_NA_ZDOROVJA_BEZLAKTOZNE_0_5__950_G:
            result = self.getting_prices('Moloko_ultrapasterizovane_Na_zdorovja_bezlaktozne_0_5__950_g', get_Moloko_ultrapasterizovane_Na_zdorovja_bezlaktozne_0_5__950_g)
        elif nn_respond == MOLOKO_ULTRAPASTERIZOVANE_NA_ZDOROVJA_0_5__950_G:
            result = self.getting_prices('Moloko_ultrapasterizovane_Na_zdorovja_0_5__950_g', get_Moloko_ultrapasterizovane_Na_zdorovja_0_5__950_g)
        elif nn_respond == MOLOKO_DITJACHE_NA_ZDOROVJA_3_2__500_G:
            result = self.getting_prices('Moloko_ditjache_Na_zdorovja_3_2__500_g', get_Moloko_ditjache_Na_zdorovja_3_2__500_g)
        elif nn_respond == MOLOKO_NA_ZDOROVJA_ULTRAPASTERIZOVANE_2_5__950_G:
            result = self.getting_prices('Moloko_Na_zdorovja_ultrapasterizovane_2_5__950_g', get_Moloko_Na_zdorovja_ultrapasterizovane_2_5__950_g)
        elif nn_respond == MOLOKO_ULTRAPASTERIZOVANE_NA_ZDOROVJA_BEZLAKTOZNE_2_5__950_G:
            result = self.getting_prices('Moloko_ultrapasterizovane_Na_zdorovja_bezlaktozne_2_5__950_g', get_Moloko_ultrapasterizovane_Na_zdorovja_bezlaktozne_2_5__950_g)
        elif nn_respond == MOLOKO_ULTRAPASTERIZOVANE_NA_ZDOROVJA_DITJACHE_3_2__950_G:
            result = self.getting_prices('Moloko_ultrapasterizovane_Na_zdorovja_ditjache_3_2__950_g', get_Moloko_ultrapasterizovane_Na_zdorovja_ditjache_3_2__950_g)
        elif nn_respond == MOLOKO_ULTRAPASTERIZOVANE_LACTEL_BEZLAKTOZ_0_2__950_G:
            result = self.getting_prices('Moloko_ultrapasterizovane_Lactel_bezlak_0_2__950_g', get_Moloko_ultrapasterizovane_Lactel_bezlakt_0_2__950_g)
        elif nn_respond == MOLOKO_ULTRAPASTERIZOVANE_LACTEL_PITNE_Z_VITAMINOM_D_3_2__950_G:
            result = self.getting_prices('Moloko_ultrapasterizovane_Lactel_pitne_z_vіtamіnom_D_3_2__950_g', get_Moloko_ultrapasterizovane_Lactel_pitne_z_vitaminom_D_3_2__950_g)
        elif nn_respond == MOLOKO_ULTRAPASTERIZOVANE_LACTEL_PITNE_BEZLAKTOZNE_1_5__950_G:
            result = self.getting_prices('Moloko_ultrapasterizovane_Lactel_pitne_bezlaktozne_1_5__950_g', get_Moloko_ultrapasterizovane_Lactel_pitne_bezlaktozne_1_5__950_g)
        elif nn_respond == MOLOKO_ULTRAPASTERIZOVANE_LACTEL_PITNE_Z_VІTAMІNOM_D_0_5__950_G:
            result = self.getting_prices('Moloko_ultrapasterizovane_Lactel_pitne_z_vіtamіnom_D_0_5__950_g', get_Moloko_ultrapasterizovane_Lactel_pitne_z_vіtamіnom_D_0_5__950_g)
        elif nn_respond == MOLOKO_ULTRAPASTERIZOVANE_LACTEL_BEZLAKTOZNE_2_5__950_G:
            result = self.getting_prices('Moloko_ultrapasterizovane_Lactel_bezlaktozne_2_5__950_g', get_Moloko_ultrapasterizovane_Lactel_bezlaktozne_2_5__950_g)
        elif nn_respond == MOLOKO_SUPERPASTERIZOVANE_BURONKA_3_2__1000_G:
            result = self.getting_prices('Moloko_superpasterizovane_Buronka_3_2__1000_g', get_Moloko_superpasterizovane_Buronka_3_2__1000_g)
        elif nn_respond == MOLOKO_PITNE_ULTRAPASTERIZOVANE_BURONKA_2_5__1000_G:
            result = self.getting_prices('Moloko_pitne_ultrapasterizovane_Buronka_2_5__1000_g', get_Moloko_pitne_ultrapasterizovane_Buronka_2_5__1000_g)
        elif nn_respond == 	MOLOKO_BURONKA_ULTRAPASTERIZOVANE_3_2__1500_G:
            result = self.getting_prices('Moloko_Buronka_ultrapasterizovane_3_2__1500_g', get_Moloko_Buronka_ultrapasterizovane_3_2__1500_g)
        elif nn_respond == MOLOKO_BURONKA_PITNE_ULTRAPASTERIZOVANE_2_5__1500_G:
            result = self.getting_prices('Moloko_Buronka_pitne_ultrapasterizovane_2_5__1500_g', get_Moloko_Buronka_pitne_ultrapasterizovane_2_5__1500_g)
        elif nn_respond == MOLOKO_ULTRAPASTERIZOVANE_ORGANIC_MILK_ORGANІCHNE_2_5__1000_G:
            result = self.getting_prices('Moloko_ultrapasterizovane_Organic_Milk_organіchne_2_5__1000_g', get_Moloko_ultrapasterizovane_Organic_Milk_organіchne_2_5__1000_g)
        elif nn_respond == MOLOKO_ULTRAPASTERIZOVANE_SLOVJANOCHKA_3_2__1000_G:
            result = self.getting_prices('Moloko_ultrapasterizovane_Slovjanochka_3_2__1000_g', get_Moloko_ultrapasterizovane_Slovjanochka_3_2__1000_g)
        elif nn_respond == MOLOKO_ULTRAPASTERIZOVANE_SLOVJANOCHKA_2_5__1000_G:
            result = self.getting_prices('Moloko_ultrapasterizovane_Slovjanochka_2_5__1000_g', get_Moloko_ultrapasterizovane_Slovjanochka_2_5__1000_g)
        elif nn_respond == MOLOKO_SLOVJANOCHKA_DLJA_ІDEALNOI_PІNKI_2_5__1000_G:
            result = self.getting_prices('Moloko_Slovjanochka_Dlja_іdealnoї_pіnki_2_5__1000_g', get_Moloko_Slovjanochka_Dlja_іdealnoi_pіnki_2_5__1000_g)
        elif nn_respond == MOLOKO_ULTRAPASTERIZOVANE_FERMA_2_5__T_P_980_G:
            result = self.getting_prices('Moloko_ultrapasterizovane_Ferma_2_5__t_p_980_g', get_Moloko_ultrapasterizovane_Ferma_2_5__t_p_980_g)
        elif nn_respond == MOLOKO_ULTRAPASTERIZOVANE_OKZDH_NASHE_MOLOKO_2_5__950_G:
            result = self.getting_prices('Moloko_ultrapasterizovane_OKZDH_Nashe_moloko_2_5__950_g', get_Moloko_ultrapasterizovane_OKZDH_Nashe_moloko_2_5__950_g)
        elif nn_respond == MOLOKO_ULTRAPASTERIZOVANE_OKZDH_NASHE_MOLOKO_3_2__950_G:
            result = self.getting_prices('Moloko_ultrapasterizovane_OKZDH_Nashe_moloko_3_2__950_g', get_Moloko_ultrapasterizovane_OKZDH_Nashe_moloko_3_2__950_g)
        elif nn_respond == MOLOKO_ULTRAPASTERIZOVANE_LOKO_MOKO_VІD_3_ROKІV_2_5__1000_G:
            result = self.getting_prices('Moloko_ultrapasterizovane_Loko_Moko_vіd_3_rokіv_2_5__1000_g', get_Moloko_ultrapasterizovane_Loko_Moko_vіd_3_rokіv_2_5__1000_g)
        elif nn_respond == MOLOKO_SELJANSKE_PITNE_ULTRAPASTERIZOVANE_2_5__900_G:
            result = self.getting_prices('Moloko_Seljanske_pitne_ultrapasterizovane_2_5__900_g', get_Moloko_Seljanske_pitne_ultrapasterizovane_2_5__900_g)
        elif nn_respond == MOLOKO_SELJANSKE_ULTRAPASTERIZOVANE_0_5__900_G:
            result = self.getting_prices('Moloko_Seljanske_ultrapasterizovane_0_5__900_g', get_Moloko_Seljanske_ultrapasterizovane_0_5__900_g)
        elif nn_respond == MOLOKO_ULTRAPASTERIZOVANE_SELJANSKE_1__900_G:
            result = self.getting_prices('Moloko_ultrapasterizovane_Seljanske_1__900_g', get_Moloko_ultrapasterizovane_Seljanske_1__900_g)
        elif nn_respond == MOLOKO_SELJANSKE_ULTRAPASTERIZOVANE_3_2__900_G:
            result = self.getting_prices('Moloko_Seljanske_ultrapasterizovane_3_2__900_g', get_Moloko_Seljanske_ultrapasterizovane_3_2__900_g)
        elif nn_respond == MOLOKO_SELJANSKE_MALJUKAM_VІD_3_ROKІV_2_5__900_G:
            result = self.getting_prices('Moloko_Seljanske_maljukam_vіd_3_rokіv_2_5__900_g', get_Moloko_Seljanske_maljukam_vіd_3_rokіv_2_5__900_g)
        elif nn_respond == MOLOKO_ULTRAPASTERIZOVANE_JAGOTINSKE_2_6__900_G:
            result = self.getting_prices('Moloko_ultrapasterizovane_Jagotinske_2_6__900_g', get_Moloko_ultrapasterizovane_Jagotinske_2_6__900_g)
        elif nn_respond == MOLOKO_JAGOTINSKE_2_6__P_E_900_G:
            result = self.getting_prices('Moloko_Jagotinske_2_6__p_e_900_g', get_Moloko_Jagotinske_2_6__p_e_900_g)
        elif nn_respond == MOLOKO_JAGOTINSKE_3_2__P_E_900_G:
            result = self.getting_prices('Moloko_Jagotinske_3_2__p_e_900_g', get_Moloko_Jagotinske_3_2__p_e_900_g)
        elif nn_respond == MOLOKO_ULTRAPASTERIZOVANE_JAGOTINSKE_3_2__900_G:
            result = self.getting_prices('Moloko_ultrapasterizovane_Jagotinske_3_2__900_g', get_Moloko_ultrapasterizovane_Jagotinske_3_2__900_g)
        elif nn_respond == MOLOKO_JAGOTINSKE_PRJAZHENE_2_6__P_E_900_G:
            result = self.getting_prices('Moloko_Jagotinske_prjazhene_2_6__p_e_900_g', get_Moloko_Jagotinske_prjazhene_2_6__p_e_900_g)
        elif nn_respond == MOLOKO_GALICHINA_Z_CHISTIH_KARPAT_2_5__900_G:
            result = self.getting_prices('Moloko_Galichina_Z_chistih_Karpat_2_5__900_g', get_Moloko_Galichina_Z_chistih_Karpat_2_5__900_g)
        elif nn_respond == MOLOKO_GALICHINA_ІZ_CHISTIH_KARPAT_1__900_G:
            result = self.getting_prices('Moloko_Galichina_Іz_chistih_Karpat_1__900_g', get_Moloko_Galichina_Іz_chistih_Karpat_1__900_g)
        elif nn_respond == MOLOKO_GALICHINA_ULTRAPASTERIZOVANE_3_2___T_F_900_G:
            result = self.getting_prices('Moloko_Galichina_ultrapasterizovane_3_2___t_f_900_g', get_Moloko_Galichina_ultrapasterizovane_3_2___t_f_900_g)
        elif nn_respond == MOLOKO_PREMІJA_ULTRAPASTERIZOVANE_1__900_G:
            result = self.getting_prices('Moloko_Premіja_ultrapasterizovane_1__900_g', get_Moloko_Premіja_ultrapasterizovane_1__900_g)
        elif nn_respond == MOLOKO_PREMІJA_ULTRAPASTERIZOVANE_2_5__900_G:
            result = self.getting_prices('Moloko_Premіja_ultrapasterizovane_2_5__900_g', get_Moloko_Premіja_ultrapasterizovane_2_5__900_g)
        elif nn_respond == MOLOKO_PITNE_POVNA_CHASHA_PASTERIZOVANE_2_5__900_G:
            result = self.getting_prices('Moloko_pitne_Povna_Chasha_pasterizovane_2_5__900_g', get_Moloko_pitne_Povna_Chasha_pasterizovane_2_5__900_g)


























































































































































        # БЛЮДА
        elif nn_respond == RED_BORSH:
            result = self.getting_prices('borsh_red', get_borsh_ukr_info)
        elif nn_respond == VARENIKI_KARTOSHKA:
            result = self.getting_prices('veriniki_potato', get_vareniki_s_kartoshkoy_info)
        elif nn_respond == VARENIKI_KAPUSTA:
            result = self.getting_prices('veriniki_kapusta', get_vareniki_s_kapustoy_info)
        elif nn_respond == GRECHESKIY_SALAT:
            result = self.getting_prices('grecheskiy_salat', get_grecheskiy_salat_info)
        elif nn_respond == GOLUBCI:
            result = self.getting_prices('golubci', get_golubci_info)
        elif nn_respond == CLASSIK_PLOV_V_KAZANE_NA_PLITE_SVININA:
            result = self.getting_prices('classic_plov_v_kazane_na_plite_svinina', get_classik_plov_v_kazane_na_plite_svinina_info)
        elif nn_respond == COTLETI_PO_KIEVSKI:
            result = self.getting_prices('classic_cotleti_po_kievski', get_classik_kotleti_po_kievski_info)

        # ------------------------------------конец подключения блюд------------------------

        else:
            result = self.getting_prices('apple_golden', get_apple_golden)

        return result


class RefersForRNN:
    '''Класс для подготовки текстовых файлов перед обучением НС.'''

    def add_new_item(self, path_tail: str):
        '''Функция для предвариетльной обработки обучающего текстового набора для НС'''

        # загрузка обучающего текста
        path = f'/home/andrey/grocery_data/ALL_TEXT_VARIANTS/{path_tail}'  #for local

        #for docker
        #path = f'/code/ALL_TEXT_VARIANTS/{path_tail}'
        #------------------------------------------------------------

        with open(path, 'r', encoding='utf-8') as f:
            item_text = f.readlines()
        # убираем первый невидимый символ
        item_text[0] = item_text[0].replace('\ufeff', '')
        return item_text

    def get_text_from_DB(self):
        '''Загрзука обучающего текста и его обработка перед обучением НС'''

        texts = []
        count_item_list = []
        for item in get_texts_refers_from_DB():
            item_text = self.add_new_item(item.item_text_file)
            count_item = len(item_text)
            count_item_list.append(count_item)
            texts += item_text

        return texts, count_item_list


def get_dishes_prices(ingredients_prices:tuple, devider:int) -> list:
    '''Метод , который подсчитытвает себестоимость блюд'''

    if len(ingredients_prices) != 9:
        raise AttributeError("You have to include all 9 markets.")
    if type(ingredients_prices) != tuple or type(devider) != int:
        raise AttributeError("Incorrect arguments's types.")

    final_prices = []
    for market in ingredients_prices:
        for ingred in market:
            if ingred == 0:
                market = (0 for x in market)
        final_prices.append(sum(market) / devider)

    return final_prices


class UserAmountConverter:
    '''Класс фомирующий величину (количество) продукто(продуктов)
    для формирования точной цены для пользователе в "Продуктовых наборах"'''

    __slots__ = ("user_request",)

    __KILOGRAMS_SYMB = 'кКkK'
    __GRAMMS_SYMB = 'гГgG'
    __PICES_SYMB = 'ШшПпУуКкБбПпНн'
    __FIRST_SYMBOL = 0

    def __init__(self, user_request:str):
        self.user_request = user_request

    def __convert_coma_to_dot(self, text: str) -> str:
        '''Метод, находящий и преобразовывающий запятые в точки
        в поле запроса пользователя'''

        new_text = []
        for symb in text:
            if symb == ',':
                symb = '.'
            new_text.append(symb)
        res = ''.join(new_text)
        return res

    def __clear_dots(self, text: str) -> str:
        '''Метод который очищает строку от лишних точек в запросе юзера'''

        text = self.__convert_coma_to_dot(text)

        if len(text) < 2:
            text += self.__PICES_SYMB[0]

        if not text[0].isdigit():
            return '0'
        first_part = []
        second_part = []
        for i in range(len(text) - 1):
            if text[i] == '.':
                first_part = list(text[:i + 1])
                second_part = list(text[i + 1:])
                break
            else:
                first_part = list(text[:i + 1])
                second_part = list(text[i + 1:])

        second_part_upgrade = [x for x in second_part if x != '.']
        res = ''.join(first_part + second_part_upgrade)
        return res

    def convert_str_to_num(self) -> float:
        '''Метод , который окончательно формирует множитель
        в зависимости от размерности, указанной пользователем'''

        text = self.__clear_dots(self.user_request)
        dig = [x for x in text if x.isdigit() or x == '.']

        dig_type = [x for x in text if x.isalpha()]

        if len(dig_type) < 1:
            res = float(''.join(dig))
            return res
        else:
            if dig_type[self.__FIRST_SYMBOL] in self.__GRAMMS_SYMB:
                res = float(''.join(dig)) / 1000
                return res

            elif dig_type[self.__FIRST_SYMBOL] in self.__KILOGRAMS_SYMB or dig_type[self.__FIRST_SYMBOL] in self.__PICES_SYMB:
                res = float(''.join(dig))
                return res
            else:
                print("Conversion amount error. Check user's amount request in set feature.")



