from django import template
from my_app.models import *

# оздадим экземпляр класса Library,
# через который происходит регистрация собственных шаблонных тегов
register = template.Library()


# ItemsPicsFromNet
class SimpleTagMakerOneItem:
    '''Класс для формирования шаблонных тегов'''

    @register.simple_tag()
    def create_tag(self, data_base: object, pk):
        '''Формирование самой функции для тега'''
        return data_base.objects.get(pk=pk)


# создаем объект класса для создания тегов для продуктов
tag = SimpleTagMakerOneItem()

# создадим тэги:

'''Тэг, возвращающий информацию о кофе "Aroma Gold Classic 100 g"'''
get_hetman_ICE = tag.create_tag(ItemsPicsFromNet, 1)

'''Тэг, возвращающий информацию о пиве "Пиво "Оболонь Премиум Экстра 1,1 л""'''
get_obolon_premium = tag.create_tag(ItemsPicsFromNet, 2)

'''Тэг, возвращающий информацию о кофе "Aroma Gold Classic 100 g"'''
coffe_aroma_gold_classic_100gr = tag.create_tag(ItemsPicsFromNet, 3)

'''Тэг, возвращающий информацию о подсолнечном масле "Щедрый Дар" 0,85 л'''
get_oil_shedriy_dar_085l = tag.create_tag(ItemsPicsFromNet, 4)

'''Тэг, возвращающий информацию о яблоке сорта Голден, 1 кг'''
get_apple_golden = tag.create_tag(ItemsPicsFromNet, 5)

'''Тэг, возвращающий информацию о напитке Кока-Кола, 2 л'''
get_coca_cola_2l = tag.create_tag(ItemsPicsFromNet, 6)

'''Тэг, возвращающий информацию о сигаретах Кент 8'''
get_sigarets_kent_8 = tag.create_tag(ItemsPicsFromNet, 7)

'''Тэг, возвращающий информацию о сырке плавленном "КОМО Паприкаш"'''
get_KOMO_paprikash = tag.create_tag(ItemsPicsFromNet, 8)

'''Тэг,возвращающий информацию о чесноке'''
get_garlik = tag.create_tag(ItemsPicsFromNet, 9)

'''Тэг,возвращающий информацию о чае "Минутка", 40 пакетиков, черный.'''
get_tea_minutka_black_40_b = tag.create_tag(ItemsPicsFromNet, 10)

'''Тэг,возвращающий информацию о моющем средстве Fairy лимон, 500 г'''
get_fairy_500_lime = tag.create_tag(ItemsPicsFromNet, 11)

'''Тэг,возвращающий информацию о луке'''
get_onion = tag.create_tag(ItemsPicsFromNet, 12)

'''Тэг,возвращающий информацию о яблоке "Черный принц"'''
get_apple_black_prince = tag.create_tag(ItemsPicsFromNet, 13)

'''Тэг,возвращающий информацию о сметане "Смачни традиции 20 % 400 гр"'''
get_smetana_stolica_smaky_20_400gr = tag.create_tag(ItemsPicsFromNet, 14)

'''Тэг,возвращающий информацию о горчице "Колос"'''
get_gorchica_kolos = tag.create_tag(ItemsPicsFromNet, 15)

'''Тэг,возвращающий информацию о лимоне'''
get_limon = tag.create_tag(ItemsPicsFromNet, 16)

'''Тэг,возвращающий информацию о масле "Оленйа" нерафинированное, 850 г'''
get_oil_oleyna_neraf_850 = tag.create_tag(ItemsPicsFromNet, 17)

'''Тэг,возвращающий информацию о харьковских дрожжах 100 гр'''
get_drojji_hark = tag.create_tag(ItemsPicsFromNet, 18)

'''Тэг,возвращающий информацию о чае "Мономах Кения", 90 гр'''
get_tea_monomah_kenya = tag.create_tag(ItemsPicsFromNet, 19)

'''Тэг,возвращающий информацию о капусте'''
get_cabbage = tag.create_tag(ItemsPicsFromNet, 20)

'''Тэг,возвращающий информацию о моркови'''
get_carrot = tag.create_tag(ItemsPicsFromNet, 21)

'''Тэг,возвращающий информацию о пене для бритья "Arko Cool 300 гр +100 бонус"'''
get_arko_cool_300_100 = tag.create_tag(ItemsPicsFromNet, 22)

'''Тэг,возвращающий информацию о пене для бритья "Arko Sensitive 300 гр +100 бонус"'''
get_arko_sensitive_300_100 = tag.create_tag(ItemsPicsFromNet, 23)

'''Тэг,возвращающий информацию о куринных яйцах'''
get_chicken_eggs = tag.create_tag(ItemsPicsFromNet, 24)

'''Тэг,возвращающий информацию о майонезе домашнем детском "Щедро" 67%'''
get_mayonez_dom_detsk_shedro_67 = tag.create_tag(ItemsPicsFromNet, 25)

'''Тэг,возвращающий информацию о пене для дезодаратнта "Rexona Aloe Vera" женский'''
get_reksona_aloe_vera_w = tag.create_tag(ItemsPicsFromNet, 26)

'''Тэг,возвращающий информацию о туалетной бумаге "Киев" 63м '''
get_toilet_papir_kiev_63m = tag.create_tag(ItemsPicsFromNet, 27)

'''Тэг,возвращающий информацию о сигаретах "Мальборо" красные '''
get_marlboro_red = tag.create_tag(ItemsPicsFromNet, 28)

'''Тэг,возвращающий информацию о пиве "Львовское светлое" 2,4 л '''
get_pivo_lvivske_svitle = tag.create_tag(ItemsPicsFromNet, 29)

'''Тэг,возвращающий информацию о сметане "Столиця Смаку 400 гр 15% жирности"'''
get_smetana_stol_smaku_400_15 = tag.create_tag(ItemsPicsFromNet, 30)

'''Тэг,возвращающий информацию о дезодоранте "Garnier Magniy мужской"'''
get_dezodorant_garnier_magniy_m = tag.create_tag(ItemsPicsFromNet, 31)

'''Тэг,возвращающий информацию о чае "Мономах черный Цейлон"'''
get_tea_monomah_ceylon_black = tag.create_tag(ItemsPicsFromNet, 32)

'''Тэг,возвращающий информацию о кофе "Арома Голд freeze dried 70 грамм"'''
get_coffee_aroma_gold_freeze_dried_70 = tag.create_tag(ItemsPicsFromNet, 33)

'''Тэг,возвращающий информацию о горчице "Верес мицна украинская 120 грамм"'''
get_gorchica_veres_micna_ukr_120g = tag.create_tag(ItemsPicsFromNet, 34)

'''Тэг,возвращающий информацию о чае "Мономах оригинал 100% цейлон 90 грамм"'''
get_tea_monomah_original_ceylon_90g = tag.create_tag(ItemsPicsFromNet, 35)

'''Тэг,возвращающий информацию о дезодоранте "Garnier весенняя сежесть"'''
get_desodorant_garnier_spring_spirit = tag.create_tag(ItemsPicsFromNet, 36)

'''Тэг,возвращающий информацию о яблоках Гала'''
get_apple_gala = tag.create_tag(ItemsPicsFromNet, 37)

'''Тэг,возвращающий информацию о сметане "Галичанська 15% 370 грамм"'''
get_smetana_galichanska_15_370gr = tag.create_tag(ItemsPicsFromNet, 38)

'''Тэг,возвращающий информацию о чипсах "Lays с солью 30 гр" большая пачка'''
get_chips_lays_salt_big_pack_30g = tag.create_tag(ItemsPicsFromNet, 39)

'''Тэг,возвращающий информацию о напитке "Sprite 2 литра"'''
get_sprite_2l = tag.create_tag(ItemsPicsFromNet, 40)

'''Тэг,возвращающий информацию о напитке "Fanta 2 литра"'''
get_fanta_2l = tag.create_tag(ItemsPicsFromNet, 41)

'''Тэг,возвращающий информацию о сигаретах "BOND STREET BLUE SELECTION"'''
get_bond_street_blue_selection = tag.create_tag(ItemsPicsFromNet, 42)

'''Тэг,возвращающий информацию о сигаретах "CAMEL BLUE"'''
get_camel_blue = tag.create_tag(ItemsPicsFromNet, 43)

'''Тэг,возвращающий информацию о сигаретах "LD RED"'''
get_ld_red = tag.create_tag(ItemsPicsFromNet, 44)

'''Тэг,возвращающий информацию о сигаретах "MARLBORO GOLD"'''
get_marlboro_gold = tag.create_tag(ItemsPicsFromNet, 45)

'''Тэг,возвращающий информацию о сигаретах "ROTHMANS DEMI BLUE EXCLUSIVE"'''
get_rothmans_demi_blue_exclusive = tag.create_tag(ItemsPicsFromNet, 46)

'''Тэг,возвращающий информацию о сигаретах "ROTHMANS DEMI CLICK PURPLE"'''
get_rothmans_demi_click_purple = tag.create_tag(ItemsPicsFromNet, 47)

'''Тэг,возвращающий информацию о сигаретах "WINSTON CASTER"'''
get_winston_caster = tag.create_tag(ItemsPicsFromNet, 48)

'''Тэг,возвращающий информацию о сигаретах "PARLAMENT AQUA BLUE"'''
get_parlament_aqua_blue = tag.create_tag(ItemsPicsFromNet, 49)

'''Тэг,возвращающий информацию о сигаретах "WINSTON BLUE"'''
get_winston_blue = tag.create_tag(ItemsPicsFromNet, 50)

'''Тэг,возвращающий информацию о сигаретах "BOND STREET RED SELECTION"'''
get_bond_street_red_selection = tag.create_tag(ItemsPicsFromNet, 51)

'''Тэг,возвращающий информацию о сигаретах "LD BLUE"'''
get_ld_blue = tag.create_tag(ItemsPicsFromNet, 52)

'''Тэг,возвращающий информацию о сигаретах "KENT SILVER"'''
get_kent_silver = tag.create_tag(ItemsPicsFromNet, 53)

'''Тэг,возвращающий информацию о сигаретах "KENT NAVI BLUE NEW"'''
get_kent_navi_blue_new = tag.create_tag(ItemsPicsFromNet, 54)

'''Тэг,возвращающий информацию о пиве "Черниговское Светлое 0,5 в стеклянной бутылке"'''
get_beer_chernigivske_svitle_05_l_glass = tag.create_tag(ItemsPicsFromNet, 55)

'''Тэг,возвращающий информацию о пиве "Stella Artois 0,5 в стеклянной бутылке"'''
get_beer_stella_artois_05_l_glass = tag.create_tag(ItemsPicsFromNet, 56)

'''Тэг,возвращающий информацию о пиве "Оболонь Светлое 0,5 в стеклянной бутылке"'''
get_beer_obolon_svitle_05_l_glass = tag.create_tag(ItemsPicsFromNet, 57)

'''Тэг,возвращающий информацию о пиве "Жигулевское Светлое 0,5 в стеклянной бутылке"'''
get_beer_jigulivsle_svitle_05_l_glass = tag.create_tag(ItemsPicsFromNet, 58)

'''Тэг,возвращающий информацию о пиве "Рогань традиционное Светлое 0,5 в стеклянной бутылке"'''
get_beer_rogan_tradiciyne_svitle_05_l_glass = tag.create_tag(ItemsPicsFromNet, 59)

'''Тэг,возвращающий информацию о пиве "Corona Extra светлое 0,33 в стеклянной бутылке"'''
get_beer_corona_extra_svitle_033_l_glass = tag.create_tag(ItemsPicsFromNet, 60)

'''Тэг,возвращающий информацию о пиве "Черниговоское Белое нефильтрованное 0,5 в стеклянной бутылке"'''
get_beer_chernigivske_bile_nefilter_05_l_glass = tag.create_tag(ItemsPicsFromNet, 61)

'''Тэг,возвращающий информацию о пиве "Янтарь Светлое 0,5 в стеклянной бутылке"'''
get_beer_yantar_svitle_05_l_glass = tag.create_tag(ItemsPicsFromNet, 62)

'''Тэг,возвращающий информацию о пиве "Zibert Светлое 0,5 в стеклянной бутылке"'''
get_beer_zibert_svitle_05_l_glass = tag.create_tag(ItemsPicsFromNet, 63)

'''Тэг,возвращающий информацию о пиве "Арсенал мицне 0,5 в стеклянной бутылке"'''
get_beer_arsenal_micne_05_l_glass = tag.create_tag(ItemsPicsFromNet, 64)

'''Тэг,возвращающий информацию о пиве "Перша Броварня Закарпатське 0,5 в стеклянной бутылке"'''
get_beer_persha_brovarna_zakarpatske_05_l_glass = tag.create_tag(ItemsPicsFromNet, 65)

'''Тэг,возвращающий информацию о пиве "Львовское Светлое 0,5 в стеклянной бутылке"'''
get_beer_lvivske_svitle_05_l_glass = tag.create_tag(ItemsPicsFromNet, 66)

'''Тэг,возвращающий информацию о пиве "Львовское 1715 0,5 в стеклянной бутылке"'''
get_beer_lvivske_1715_05_l_glass = tag.create_tag(ItemsPicsFromNet, 67)

'''Тэг,возвращающий информацию о пиве "Zlata Praha 0,5 в стеклянной бутылке"'''
get_beer_zlata_praha_05_l_glass = tag.create_tag(ItemsPicsFromNet, 68)

'''Тэг,возвращающий информацию о пиве "Tuborg Green 0,5 в стеклянной бутылке"'''
get_beer_tuborg_green_05_l_glass = tag.create_tag(ItemsPicsFromNet, 69)

'''Тэг,возвращающий информацию о пиве "Славутич ICE MIX Lime 0,5 в стеклянной бутылке"'''
get_beer_slavutich_ice_mix_lime_05_l_glass = tag.create_tag(ItemsPicsFromNet, 70)

'''Тэг,возвращающий информацию о пиве "Тетерев светлое 0,5 в стеклянной бутылке"'''
get_beer_teteriv_svitle_05_l_glass = tag.create_tag(ItemsPicsFromNet, 71)

'''Тэг,возвращающий информацию о пиве "Krusovice сетлое 0,5 в стеклянной бутылке"'''
get_beer_krusovice_svitle_05_l_glass = tag.create_tag(ItemsPicsFromNet, 72)

'''Тэг,возвращающий информацию о пиве "Heineken светлое 0,5 в стеклянной бутылке"'''
get_beer_heineken_svitle_05_l_glass = tag.create_tag(ItemsPicsFromNet, 73)

'''Тэг,возвращающий информацию о пиве "Amstel светлое 0,5 в стеклянной бутылке"'''
get_beer_amstel_svitle_05_l_glass = tag.create_tag(ItemsPicsFromNet, 74)

'''Тэг,возвращающий информацию о пиве "Hike premium 0,5 в стеклянной бутылке"'''
get_beer_hike_premium_05_l_glass = tag.create_tag(ItemsPicsFromNet, 75)

'''Тэг,возвращающий информацию о пиве "Бочкове светлое 0,5 в стеклянной бутылке"'''
get_beer_bochkove_svitle_05_l_glass = tag.create_tag(ItemsPicsFromNet, 76)

'''Тэг,возвращающий информацию о пиве "Kronenbourg 1664 Blanc светлое 0,5 в стеклянной бутылке"'''
get_beer_kronenbourg_1664_blanc_svitle_05_l_glass = tag.create_tag(ItemsPicsFromNet, 77)

'''Тэг,возвращающий информацию о пиве "Опилля непастеризоване  светлое 0,5 в стеклянной бутылке"'''
get_beer_opilla_nepasterizovane_svitle_05_l_glass = tag.create_tag(ItemsPicsFromNet, 78)

'''Тэг,возвращающий информацию о пиве "Ячменный Колос светлое 0,5 в стеклянной бутылке"'''
get_beer_yachmenniy_kolos_svitle_05_l_glass = tag.create_tag(ItemsPicsFromNet, 79)

'''Тэг,возвращающий информацию о пиве "Опилля Корифей светлое 0,5 в стеклянной бутылке"'''
get_beer_opilla_korifey_svitle_05_l_glass = tag.create_tag(ItemsPicsFromNet, 80)

'''Тэг,возвращающий информацию о пиве "Чайка Днепроская светлое 0,5 в стеклянной бутылке"'''
get_beer_chaika_dneprovskaya_svitle_05_l_glass = tag.create_tag(ItemsPicsFromNet, 81)

'''Тэг,возвращающий информацию о пиве "Чайка Черноморская светлое 0,5 в стеклянной бутылке"'''
get_beer_chaika_chernomorskaya_svitle_05_l_glass = tag.create_tag(ItemsPicsFromNet, 82)

'''Тэг,возвращающий информацию о пиве "Умань пиво Waissburg светлое 1 л в пластиковой бутылке"'''
get_beer_uman_waissburg_svitle_1_l_plastic = tag.create_tag(ItemsPicsFromNet, 83)

'''Тэг,возвращающий информацию о пиве "Умань пиво пшеничное светлое 1 л в пластиковой бутылке"'''
get_beer_uman_pshenichnoe_svitle_1_l_plastic = tag.create_tag(ItemsPicsFromNet, 84)

'''Тэг,возвращающий информацию о пиве "Бердичевское хмельное пиво светлое 1 л в пластиковой бутылке"'''
get_beer_berdichevskoe_hmelnoye_svitle_1_l_plastic = tag.create_tag(ItemsPicsFromNet, 85)

'''Тэг,возвращающий информацию о пиве "Бердичевское лагер светлое 1 л в пластиковой бутылке"'''
get_beer_berdichevskoe_lager_svitle_1_l_plastic = tag.create_tag(ItemsPicsFromNet, 86)

'''Тэг,возвращающий информацию о пиве "Опилля Корифей 1.1 л в пластиковой бутылке"'''
get_beer_opilla_korifey_11_l_plastic = tag.create_tag(ItemsPicsFromNet, 87)

'''Тэг,возвращающий информацию о пиве "Оболонь жигулевское экспортное 1,5 л в пластиковой бутылке"'''
get_beer_obolon_jigulivske_eksport_15_l_plastic = tag.create_tag(ItemsPicsFromNet, 88)

'''Тэг,возвращающий информацию о пиве "Янтарь светлое 1,2 л в пластиковой бутылке"'''
get_beer_yantar_svitle_12_l_plastic = tag.create_tag(ItemsPicsFromNet, 89)

'''Тэг,возвращающий информацию о пиве "Жашковское пшеничное нефильтрованное 1 л в пластиковой бутылке"'''
get_beer_jashkovskoe_pshenicnoe_nefilter_1_l_plastic = tag.create_tag(ItemsPicsFromNet, 90)

'''Тэг,возвращающий информацию о пиве "Жашковское светлое нефильтрованное 1 л в пластиковой бутылке"'''
get_beer_jashkovskoe_svitle_nefilter_1_l_plastic = tag.create_tag(ItemsPicsFromNet, 91)

'''Тэг,возвращающий информацию о пиве "Жашковское жигулевское нефильтрованное 1 л в пластиковой бутылке"'''
get_beer_jashkovskoe_jigulivske_nefilter_1_l_plastic = tag.create_tag(ItemsPicsFromNet, 92)

'''Тэг,возвращающий информацию о пиве "Перша приватна броварня бочкове 1 л в пластиковой бутылке"'''
get_beer_persha_privatna_brovarnya_bochkove_1_l_plastic = tag.create_tag(ItemsPicsFromNet, 93)

'''Тэг,возвращающий информацию о пиве "Чайка днипровська 1 л в пластиковой бутылке"'''
get_beer_chayka_dniprovska_1_l_plastic = tag.create_tag(ItemsPicsFromNet, 94)

'''Тэг,возвращающий информацию о "Кетчуп Торчин с чесноком 270 гр"'''
get_ketchup_torchin_s_chesnokom = tag.create_tag(ItemsPicsFromNet, 95)

'''Тэг,возвращающий информацию о "Майонез Королевский смак королевский 300 гр"'''
get_mayonez_korolivkiy_smak_korolivskiy_67_300gr = tag.create_tag(ItemsPicsFromNet, 96)

'''Тэг,возвращающий информацию о "Мука ЗОЛОТЕ ЗЕРНЯТКО пшеничное 2 кг"'''
get_muka_zolote_zernyatko_pshenichne_2kg = tag.create_tag(ItemsPicsFromNet, 97)

'''Тэг,возвращающий информацию о "Пиво Черниговское Белое 1 литр в пластике"'''
get_beer_chernigivske_bile_1l_plastic = tag.create_tag(ItemsPicsFromNet, 98)

'''Тэг,возвращающий информацию о "Пиво Оболонь светлое 1 литр в пластике"'''
get_beer_obolon_svitle_1l_plastic = tag.create_tag(ItemsPicsFromNet, 99)

'''Тэг,возвращающий информацию о "Пиво Рогань традиционное светлое 1 литр в пластике"'''
get_beer_rogan_tradiciyne_svitle_1l_plastic = tag.create_tag(ItemsPicsFromNet, 100)

'''Тэг,возвращающий информацию о "Соус Чумак чесночный 200 грамм"'''
get_sous_chumak_chesnochniy_200gr = tag.create_tag(ItemsPicsFromNet, 101)

'''Тэг,возвращающий информацию о "Орбит клубника-банан"'''
get_jvachka_orbit_clubnika_banan = tag.create_tag(ItemsPicsFromNet, 102)

'''Тэг,возвращающий информацию о "Сигареты LM красные"'''
get_sigarets_LM_red = tag.create_tag(ItemsPicsFromNet, 103)

'''Тэг,возвращающий информацию о "Пиво Жигулевское 2л в пластике"'''
get_beer_jigulivske_2l_plastic = tag.create_tag(ItemsPicsFromNet, 104)

'''Тэг,возвращающий информацию о "Пиво Чайка днипровская 2л в пластике"'''
get_beer_chayka_dniprovskaya_2l_plastic = tag.create_tag(ItemsPicsFromNet, 105)

'''Тэг,возвращающий информацию о "Пиво Piwny Kubek  2л в пластике"'''
get_beer_piwny_kubek_2l_plastic = tag.create_tag(ItemsPicsFromNet, 106)

'''Тэг,возвращающий информацию о "Кетчуп Торчин до шашлику 270 грамм"'''
get_ketchup_torchin_do_shasliky_270gr = tag.create_tag(ItemsPicsFromNet, 107)

'''Тэг,возвращающий информацию о "Майонез Чумак аппетитный 50% 300 грамм"'''
get_mayonez_chumak_appetitniy_50_300gr = tag.create_tag(ItemsPicsFromNet, 108)

'''Тэг,возвращающий информацию о "Колбаса Перша Столиця Салями Фирменная высший сорт"'''
get_kolbasa_persha_stolica_salyami_firmova_vs = tag.create_tag(ItemsPicsFromNet, 109)

'''Тэг,возвращающий информацию о "Кофе Чорна Карта GOLD 50 грамм"'''
get_cofee_chorna_karta_gold_50gr = tag.create_tag(ItemsPicsFromNet, 110)

'''Тэг,возвращающий информацию о "Пиво Арсенал "Міцне" світле, 2л"'''
get_beer_arsenal_micne_svitle_2l_plastic = tag.create_tag(ItemsPicsFromNet, 111)

'''Тэг,возвращающий информацию о "Пиво "ППБ Бочкове" світле, 2л"'''
get_beer_persha_privatna_brovarnya_bochkove_svitle_2l_plastic = tag.create_tag(ItemsPicsFromNet, 112)

'''Тэг,возвращающий информацию о "Пиво "ППБ Закарпатське оригінальне" світле, 2л"'''
get_beer_persha_privatna_brovarnya_zakarpatske_svitle_2l_plastic = tag.create_tag(ItemsPicsFromNet, 113)

'''Тэг,возвращающий информацию о "Пиво Zibert сетлое 0,5 л в банке"'''
get_beer_zibert_svitle_05_l_banochnoe = tag.create_tag(ItemsPicsFromNet, 114)

'''Тэг,возвращающий информацию о "Йогурт Фанни лесные ягоды 1,5% 240 грамм"'''
get_yogurt_fanni_lisovi_yagodi_1_5_240gr = tag.create_tag(ItemsPicsFromNet, 115)

'''Тэг,возвращающий информацию о "Кефир Славия 2,5 % 850 грамм"'''
get_kefir_slaviya_2_5_850gr = tag.create_tag(ItemsPicsFromNet, 116)

'''Тэг,возвращающий информацию о "Пиво Оболонь Киевское разливное светлое 1,95 л в пластике"'''
get_beer_obolon_kievskoe_razlivnoe_svetloe_195l_plastic = tag.create_tag(ItemsPicsFromNet, 117)

'''Тэг,возвращающий информацию о "Пиво Черниговское light светлое 2,0 л в пластике"'''
get_beer_chernigivske_light_svitle_2l_plastic = tag.create_tag(ItemsPicsFromNet, 118)

'''Тэг,возвращающий информацию о "Пиво Опилля Корифей светлое 2,0 л в пластике"'''
get_beer_opilla_korifey_svitle_2l_plastic = tag.create_tag(ItemsPicsFromNet, 119)

'''Тэг,возвращающий информацию о "Пиво Янтарь светлое 2,0 л в пластике"'''
get_beer_yantar_svitle_2l_plastic = tag.create_tag(ItemsPicsFromNet, 120)

'''Тэг,возвращающий информацию о "Пиво Tuborg Green 4 банки х 0,5 л"'''
get_beer_tuborg_green_svitle_4_banki_05l = tag.create_tag(ItemsPicsFromNet, 121)

'''Тэг,возвращающий информацию о "Пиво ППБ Закарпатське 4 банки х 0,5 л"'''
get_beer_ppb_zakarpatske_svitle_4_banki_05l = tag.create_tag(ItemsPicsFromNet, 122)

'''Тэг,возвращающий информацию о "Пиво ППБ Бочкове 4 банки х 0,5 л"'''
get_beer_ppb_bochkove_svitle_4_banki_05l = tag.create_tag(ItemsPicsFromNet, 123)

'''Тэг,возвращающий информацию о "Пиво Budweiser Budvar светлое 0,5 л в стекле"'''
get_beer_budweiser_budvar_05l_glass = tag.create_tag(ItemsPicsFromNet, 124)

'''Тэг,возвращающий информацию о "Пиво Pilsner Urquell светлое 0,5 л в стекле"'''
get_beer_pilsner_urquell_05l_glass = tag.create_tag(ItemsPicsFromNet, 125)

'''Тэг,возвращающий информацию о "Пиво Robert Doms бельгийский светлое нефильтрованное 0,5 л в стекле"'''
get_beer_robert_doms_belgiyskiy_svitle_nefilter_05l_glass = tag.create_tag(ItemsPicsFromNet, 126)

'''Тэг,возвращающий информацию о "Пиво 0,5 л Чернігівське світле жб"'''
get_beer_chernigivske_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 127)

'''Тэг,возвращающий информацию о "Пивo 0,5 л Чepнігівськe Білe жб"'''
get_beer_chernigivske_bile_nefilter_05l_jb = tag.create_tag(ItemsPicsFromNet, 128)

'''Тэг,возвращающий информацию о "Пиво 0,5л Velkopopovicky Kozel темне жб"'''
get_beer_velkopopovicky_kozel_temne_05l_jb = tag.create_tag(ItemsPicsFromNet, 129)

'''Тэг,возвращающий информацию о "Пиво 0,5 л Edelmeister Pilsner світле фільтроване жб"'''
get_beer_edelmeister_pilsner_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 130)

'''Тэг,возвращающий информацию о "Пиво 0,5 л Faxe світле фільтроване жб"'''
get_beer_faxe_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 131)

'''Тэг,возвращающий информацию о "Пиво 0,5л Livu Pilzenes світле фільтроване жб"'''
get_beer_livu_pilzenes_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 132)

'''Тэг,возвращающий информацию о "Пиво 0,5л Velkopopovicky Kozel світле жб"'''
get_beer_velkopopovicky_kozel_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 133)

'''Тэг,возвращающий информацию о "Пиво 0,5л Оболонь BeerMix Лимон жб"'''
get_beer_obolon_beermix_limon_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 134)

'''Тэг,возвращающий информацию о "Пиво 0,5 л Edelmeister Weizenbier світле нефільтроване жб"'''
get_beer_edelmeister_weizenbier_nefilter_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 135)

'''Тэг,возвращающий информацию о "Пиво 0,5 л Edelmeister Schwarzbier темне фільтроване жб"'''
get_beer_edelmeister_schwarzbier_temne_05l_jb = tag.create_tag(ItemsPicsFromNet, 136)

'''Тэг,возвращающий информацию о "Пивo 0,5л Hike Blanche світлe нeфільтpoвaнe жб"'''
get_beer_hike_blanche_svitle_nefilter_05l_jb = tag.create_tag(ItemsPicsFromNet, 137)

'''Тэг,возвращающий информацию о "Пиво 0,5л Zlata Praha світле жб"'''
get_beer_zlata_praha_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 138)

'''Тэг,возвращающий информацию о "Пиво 0,5л Thuringer Premium Beer світле фільтроване жб"'''
get_beer_thuringer_premium_beer_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 139)

'''Тэг,возвращающий информацию о "Пиво 0,5л Livu Sencu світле фільтроване жб"'''
get_beer_livu_sencu_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 140)

'''Тэг,возвращающий информацию о "Пиво 0,5 л Germanarich светлое жб"'''
get_beer_germanarich_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 141)

'''Тэг,возвращающий информацию о "Пиво 0,5л Hike Преміум світле жб"'''
get_beer_hike_premium_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 142)

'''Тэг,возвращающий информацию о "Пивo бeзaлкoгoльнe 0,5л Обoлoнь 0 світлe нефільтроване пaстepизoвaнe жб"'''
get_beer_obolon_svitle_nefilter_nonalcohol_05l_jb = tag.create_tag(ItemsPicsFromNet, 143)

'''Тэг,возвращающий информацию о "Пиво Zibert Баварське світле 5% 0,5л жб"'''
get_beer_zibrert_bavarske_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 144)

'''Тэг,возвращающий информацию о "Пиво Bavaria Liquid Apple світле безалкогольне 0,5л жб"'''
get_beer_bavaria_liquid_apple_nonalcohol_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 145)

'''Тэг,возвращающий информацию о "Пиво Heineken світле 5% 0,5л жб"'''
get_beer_heineken_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 146)

'''Тэг,возвращающий информацию о "Пиво Rychtar Grunt 11 світле 4,6% 0,5л жб"'''
get_beer_rychtar_grunt_11_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 147)

'''Тэг,возвращающий информацию о "Пиво Amstel світле фільтроване 5% 0,5л жб"'''
get_beer_amstel_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 148)

'''Тэг,возвращающий информацию о "Пиво Bavaria світле фільтроване 5% 0,5л жб"'''
get_beer_bavaria_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 149)

'''Тэг,возвращающий информацию о "Пиво Bavaria світле 0% 0,5л безалкогольное жб"'''
get_beer_bavaria_svitle_nonalcohol_05l_jb = tag.create_tag(ItemsPicsFromNet, 150)

'''Тэг,возвращающий информацию о "Пиво Edelburg Lager світле 5,2% 0,5л жб"'''
get_beer_edelburg_lager_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 151)

'''Тэг,возвращающий информацию о "Пиво Donner Pils світле 3,5% 0,5л жб"'''
get_beer_donner_pils_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 152)

'''Тэг,возвращающий информацию о "Пиво Dutch Windmill світле 4,6% 0,5л жб"'''
get_beer_dutch_windmill_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 153)

'''Тэг,возвращающий информацию о "Пиво Edelburg Hefeweizen світле нефільтроване 5,1% 0,5л жб"'''
get_beer_edelburg_hefeweizen_svitle_nefilter_05l_jb = tag.create_tag(ItemsPicsFromNet, 154)

'''Тэг,возвращающий информацию о "Пиво Edelmeister Unfiltered світле нефільтроване 5,7% 0,5л жб"'''
get_beer_edelmeister_unfiltered_svitle_nefilter_05l_jb = tag.create_tag(ItemsPicsFromNet, 155)

'''Тэг,возвращающий информацию о "Пиво Estrella Damm Barcelona світле 4,6% 0,5л жб"'''
get_beer_estrella_damm_barcelona_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 156)

'''Тэг,возвращающий информацию о "Пиво Halne Jasne Pelne з/б 6% 0,5л жб"'''
get_beer_halne_jasne_pelne_05l_jb = tag.create_tag(ItemsPicsFromNet, 157)

'''Тэг,возвращающий информацию о "Пиво Eurotour Hefeweissbier світле 5% 0,5л жб"'''
get_beer_eurotour_hefeweissbier_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 158)

'''Тэг,возвращающий информацию о "Пиво Hollandia Strong світле 7,5% 0,5л жб"'''
get_beer_hollandia_strong_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 159)

'''Тэг,возвращающий информацию о "Пиво Lander Brau Premium світле 4,9% 0,5л жб"'''
get_beer_lander_brau_premium_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 160)

'''Тэг,возвращающий информацию о "Пиво Saku Kuld 5,2% 0,5л жб"'''
get_beer_Saku_Kuld_05l_jb = tag.create_tag(ItemsPicsFromNet, 161)

'''Тэг,возвращающий информацию о "Пиво Saku Originaal 4,7% 0,5л л жб"'''
get_beer_Saku_Originaal_05l_jb = tag.create_tag(ItemsPicsFromNet, 162)

'''Тэг,возвращающий информацию о "Пиво Stangen Lager світле 5,4% 0,5л л жб"'''
get_beer_Stangen_Lager_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 163)

'''Тэг,возвращающий информацию о "Пиво Van Pur Premium світле 5% 0,5л жб"'''
get_beer_Van_Pur_Premium_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 164)

'''Тэг,возвращающий информацию о "Пиво Bavaria манго-маракуйя світле безалкогольне 0,5л жб"'''
get_beer_Bavaria_mango_marakya_nonalcohol_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 165)

'''Тэг,возвращающий информацию о "Пиво Bavaria Гранат безалкогольне 0,5л жб"'''
get_beer_Bavaria_granat_nonalcohol_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 166)

'''Тэг,возвращающий информацию о "Пиво Оболонь Beermix Малина світле 2,5% 0,5л жб"'''
get_beer_Obolon_Beermix_malina_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 167)

'''Тэг,возвращающий информацию о "Пиво Оболонь Beermix Вишня спеціальне світле 2,5% 0,5л жб"'''
get_beer_Obolon_Beermix_vishnya_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 168)

'''Тэг,возвращающий информацию о "Пиво Lomza світле 5,7% 0,5л жб"'''
get_beer_Lomza_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 169)

'''Тэг,возвращающий информацию о "Пиво Paderborner Pilsener світле 4,8% 0,5л жб"'''
get_beer_Paderborner_Pilsener_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 170)

'''Тэг,возвращающий информацию о "Пиво Paderborner Export світле 5,5% 0,5л жб"'''
get_beer_Paderborner_Export_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 171)

'''Тэг,возвращающий информацию о "Пиво Clausthaler Grapefruit безалкогольне 0,5л жб"'''
get_beer_Clausthaler_Grapefruit_nonalcohol_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 172)

'''Тэг,возвращающий информацию о "Пиво Clausthaler Original безалкогольне 0,5л жб"'''
get_beer_Clausthaler_Original_nonalcohol_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 173)

'''Тэг,возвращающий информацию о "Пиво Clausthaler Lemon безалкогольне 0,5л жб"'''
get_beer_Clausthaler_Lemon_nonalcohol_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 174)

'''Тэг,возвращающий информацию о "Пиво Forever Rock & Roll світле нефільтроване 7,5% 0,5л жб"'''
get_beer_Forever_Rock_N_Roll_svitle_nefilter_05l_jb = tag.create_tag(ItemsPicsFromNet, 175)

'''Тэг,возвращающий информацию о "Пиво Forever Black Queen темне нефільтроване 5,5% 0,5л жб"'''
get_beer_Forever_Black_Queen_temne_nefilter_05l_jb = tag.create_tag(ItemsPicsFromNet, 176)

'''Тэг,возвращающий информацию о "Пиво Forever Kite Safari світле нефільтроване 7% 0,5л жб"'''
get_beer_Forever_Kite_Safari_svitle_nefilter_05l_jb = tag.create_tag(ItemsPicsFromNet, 177)

'''Тэг,возвращающий информацию о "Пиво Forever Crazy світле нефільтроване 6,5% 0,5л жб"'''
get_beer_Forever_Crazy_svitle_nefilter_05l_jb = tag.create_tag(ItemsPicsFromNet, 178)

'''Тэг,возвращающий информацию о "Пиво Hike Light світле 3,5% 0,5л жб"'''
get_beer_Hike_Light_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 179)

'''Тэг,возвращающий информацию о "Пиво Hike Zero безалкогольне 0,5л жб"'''
get_beer_Hike_Zero_nonalco_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 180)

'''Тэг,возвращающий информацию о "Пиво Horn Disel Ice Pilsner світле 4,7% 0,568л жб"'''
get_beer_Horn_Disel_Ice_Pilsner_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 181)

'''Тэг,возвращающий информацию о "Пиво Horn Disel Original 5,3% 0,568л жб"'''
get_beer_Horn_Disel_Original_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 182)

'''Тэг,возвращающий информацию о "Пиво Horn Disel Traditional світле 6% 0,568л жб"'''
get_beer_Horn_Disel_Traditional_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 183)

'''Тэг,возвращающий информацию о "Пиво Horn Premium Diesel світле 5% 0,5л жб"'''
get_beer_Horn_Disel_Premium_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 184)

'''Тэг,возвращающий информацию о "Пиво Krusovice Cerne темне 3,8% 0,5л жб"'''
get_beer_Krusovice_Cerne_temne_05l_jb = tag.create_tag(ItemsPicsFromNet, 185)

'''Тэг,возвращающий информацию о "Пиво Lander Brau міцне 4,9% 0,5л жб"'''
get_beer_Lander_Brau_micne_05l_jb = tag.create_tag(ItemsPicsFromNet, 186)

'''Тэг,возвращающий информацию о "Пиво Lander Brau світле нефільтроване 4,7% 0,5л жб"'''
get_beer_Lander_Brau_svitle_nefilter_05l_jb = tag.create_tag(ItemsPicsFromNet, 187)

'''Тэг,возвращающий информацию о "Пиво Paderborner Pilger світле нефільтроване пастеризоване 5% 0,5л жб"'''
get_beer_Paderborner_Pilger_svitle_nefilter_05l_jb = tag.create_tag(ItemsPicsFromNet, 188)

'''Тэг,возвращающий информацию о "Пиво Platan Jedenactka 11 світле 4,6% 0,5л жб"'''
get_beer_Platan_Jedenactka_11_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 189)

'''Тэг,возвращающий информацию о "Пиво Praga світле фільтроване 4,7% 0,5л жб"'''
get_beer_Praga_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 190)

'''Тэг,возвращающий информацию о "Пиво Saku Rock світле 5,3% 0,568л жб"'''
get_beer_Saku_Rock_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 191)

'''Тэг,возвращающий информацию о "Пиво Sitnan світле 5% 0,5л жб"'''
get_beer_Sitnan_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 192)

'''Тэг,возвращающий информацию о "Пиво Vienas Premium Golden світле 5% 0,568л жб"'''
get_beer_Vienas_Premium_Golden_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 193)

'''Тэг,возвращающий информацию о "Пиво Vienas Premium Traditional світле 5,8% 0,568л жб"'''
get_beer_Vienas_Premium_Traditional_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 194)

'''Тэг,возвращающий информацию о "Пиво Volynski Browar Forever Sweet Wit пшеничне світле нефільтроване 4,5% 0,5л жб"'''
get_beer_Volynski_Browar_Forever_Sweet_Wit_nefilter_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 195)

'''Тэг,возвращающий информацию о "Пиво Zahringer Преміум світле 0,5л жб"'''
get_beer_Zahringer_premium_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 196)

'''Тэг,возвращающий информацию о "Пиво Zahringer Hefeweizen світле 0,5л жб"'''
get_beer_Zahringer_Hefeweizen_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 197)

'''Тэг,возвращающий информацию о "Пиво Жашківське світле нефільтроване 4,5% 0,5л жб"'''
get_beer_jajkivske_nefilter_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 198)

'''Тэг,возвращающий информацию о "Пиво Оболонь світле 4,5% 0,5л жб"'''
get_beer_obolon_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 199)

'''Тэг,возвращающий информацию о "Пиво Pubster світле 5% 0,5л жб"'''
get_beer_Pubster_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 200)

'''Тэг,возвращающий информацию о "Пиво ППБ Чайка Чорноморська 4,5% 0,5л жб"'''
get_beer_Chaika_Chernomorska_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 201)

'''Тэг,возвращающий информацию о "Пиво ППБ Закарпатське Оригінальне світле 4,4% 0,5л"'''
get_beer_PPB_Zakarpatske_origin_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 202)

'''Тэг,возвращающий информацию о "Пиво ППБ Бочкове Нефільтроване з/б 4,8% 0,5л"'''
get_beer_PPB_Bochkove_nefilter_05l_jb = tag.create_tag(ItemsPicsFromNet, 203)

'''Тэг,возвращающий информацию о "Пиво ППБ Нефільтроване світле безалкогольне 0,5л"'''
get_beer_PPB_Nefilter_svitle_nonalco_05l_jb = tag.create_tag(ItemsPicsFromNet, 204)

'''Тэг,возвращающий информацию о "Пиво ППБ Лимон-Лайм безалкогольне нефільтроване 0,5л"'''
get_beer_PPB_Limon_lime_nonalco_nefilter_05l_jb = tag.create_tag(ItemsPicsFromNet, 205)

'''Тэг,возвращающий информацию о "Пиво Чайка Дніпровська світле фільтроване 4,8% 0,5л"'''
get_beer_Chaika_Dniprovska_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 206)

'''Тэг,возвращающий информацию о "Пиво Brok Export світле 5,2% 0,5л"'''
get_beer_Brok_Export_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 207)

'''Тэг,возвращающий информацию о "Пиво Carling світле фільроване з/б 4% 0.5 л"'''
get_beer_Carling_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 208)

'''Тэг,возвращающий информацию о "Пиво Keten Brug Blanche Elegant 4.8% 0.5 л"'''
get_beer_Keten_Brug_Blanche_Elegant_05l_jb = tag.create_tag(ItemsPicsFromNet, 209)

'''Тэг,возвращающий информацию о "Пиво Budweiser безалкогольне 0.5 л"'''
get_beer_Budweiser_nonalco_05l_jb = tag.create_tag(ItemsPicsFromNet, 210)

'''Тэг,возвращающий информацию о "Пиво Feldschlosschen Wheat Beer світле нефільтроване 5% 0.5 л"'''
get_beer_Feldschlosschen_Wheat_Beer_svitle_nefilter_05l_jb = tag.create_tag(ItemsPicsFromNet, 211)

'''Тэг,возвращающий информацию о "Пиво Тетерів Хмільна Вишня напівтемне фільтроване з/б 8% 0.5 л"'''
get_beer_Teteriv_hmilna_vishnya_napivtemne_05l_jb = tag.create_tag(ItemsPicsFromNet, 212)

'''Тэг,возвращающий информацию о "Пиво Grotwerg світле пастеризоване фільтроване безалкогольне 0.5 л"'''
get_beer_Grotwerg_svitle_nonalco_05l_jb = tag.create_tag(ItemsPicsFromNet, 213)

'''Тэг,возвращающий информацию о "Пиво Holland Import світле фільтроване 4.8% 0.5 л"'''
get_beer_Holland_import_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 214)

'''Тэг,возвращающий информацию о "Пиво Golden Castle Export світле 4.8% 0.5 л"'''
get_beer_Golden_castle_export_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 215)

'''Тэг,возвращающий информацию о "Пиво 5.0 Original Craft Beer сітле нефільтроване 4.1% 0.5 л"'''
get_beer_5_0_original_craft_beer_nefilter_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 216)

'''Тэг,возвращающий информацию о "Пиво Guinness Draught темне фільтроване 4.1% 0.44 л"'''
get_beer_Guinness_draught_temne_05l_jb = tag.create_tag(ItemsPicsFromNet, 217)

'''Тэг,возвращающий информацию о "Пиво Grimbergen Double Ambree напівтемне фільтроване 6.5% 0.5 л"'''
get_beer_GrimbergenDoubleAmbree_napivtemne_05l_jb = tag.create_tag(ItemsPicsFromNet, 218)

'''Тэг,возвращающий информацию о "Пиво Warsteiner Premium Verum світле фільтроване 4.8% 0.5 л"'''
get_beer_WarsteinerPremiumVerum_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 219)

'''Тэг,возвращающий информацию о "Пиво DAB темне фільтроване 4.9% 0.5 л"'''
get_beer_DAB_temne_05l_jb = tag.create_tag(ItemsPicsFromNet, 220)

'''Тэг,возвращающий информацию о "Пиво спеціальне Grimbergen Blanche світле пастеризоване 6% 0.5 л"'''
get_beer_GrimbergenBlanche_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 221)

'''Тэг,возвращающий информацию о "Пиво Klosterkeller Weissbier China світле нефільтроване 5.4% 0.5 л"'''
get_beer_KlosterkellerWeissbierChina_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 222)

'''Тэг,возвращающий информацию о "Пиво Karpackie Pils світле фільтроване 4% 0.5 л"'''
get_beer_KarpackiePils_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 223)

'''Тэг,возвращающий информацию о "Пиво 5,0 Original Pills світле фільтроване 5% 0.5 л"'''
get_beer_5_0_OriginalPills_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 224)

'''Тэг,возвращающий информацию о "Пиво 5,0 Original Lager світле фільтроване 5.4% 0.5 л"'''
get_beer_5_0_OriginalLager_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 225)

'''Тэг,возвращающий информацию о "Пиво 5,0 Original Weiss Beer світле нефільтроване 5% 0.5 л"'''
get_beer_5_0_Original_Weiss_nefilter_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 226)

'''Тэг,возвращающий информацию о "Пиво Fahnen Brau світле фільтроване 4.7% 0.5 л"'''
get_beer_Fahnen_Brau_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 227)

'''Тэг,возвращающий информацию о "Пиво Gosser Light світле фільтроване 5.2% 0.5 л"'''
get_beer_Gosser_light_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 228)

'''Тэг,возвращающий информацию о "Пиво Hollandia Import світле фільтроване 4.8% 0.33 л"'''
get_beer_HollandiaImport_svitle_033l_jb = tag.create_tag(ItemsPicsFromNet, 229)

'''Тэг,возвращающий информацию о "Пиво Holsten Pilsener 4.7% 0.48 л"'''
get_beer_Holsten_Pilsener_048l_jb = tag.create_tag(ItemsPicsFromNet, 230)

'''Тэг,возвращающий информацию о "Пиво Оболонь Premium Extra Brew світле фільтроване з/б 4.6% 0.5 л"'''
get_beer_Obolon_Premium_Extra_Brew_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 231)

'''Тэг,возвращающий информацию о "Пиво Львівське світле 4,3% 0,48 л"'''
get_beer_Lvivske_svitle_048l_jb = tag.create_tag(ItemsPicsFromNet, 232)

'''Тэг,возвращающий информацию о "Пиво Carlsberg Premium Pilsner світле фільтроване з/б 5% 0.5 л"'''
get_beer_Carlsberg_Premium_Pilsner_svitle_05l_jb = tag.create_tag(ItemsPicsFromNet, 233)

'''Тэг,возвращающий информацию о "Пиво Carlsberg Pilsner 0.5 л"'''
get_beer_Carlsberg_Pilsner_05l_jb = tag.create_tag(ItemsPicsFromNet, 234)

'''Тэг,возвращающий информацию о "Банан, кг"'''
get_banana = tag.create_tag(ItemsPicsFromNet, 235)

'''Тэг,возвращающий информацию о "Апельсин, кг"'''
get_orange = tag.create_tag(ItemsPicsFromNet, 236)

'''Тэг,возвращающий информацию о "Киви, кг"'''
get_kiwi = tag.create_tag(ItemsPicsFromNet, 237)

'''Тэг,возвращающий информацию о "Кокос"'''
get_coconut = tag.create_tag(ItemsPicsFromNet, 238)

'''Тэг,возвращающий информацию о "Грейпфрут"'''
get_grapefruit = tag.create_tag(ItemsPicsFromNet, 239)

'''Тэг,возвращающий информацию о "Гранат, кг"'''
get_pomegranate = tag.create_tag(ItemsPicsFromNet, 240)

'''Тэг,возвращающий информацию о "Манго, кг"'''
get_mango = tag.create_tag(ItemsPicsFromNet, 241)

'''Тэг,возвращающий информацию о "Картошка, кг"'''
get_potato = tag.create_tag(ItemsPicsFromNet, 242)

'''Тэг,возвращающий информацию о "Помидоры, кг"'''
get_tomato = tag.create_tag(ItemsPicsFromNet, 243)

'''Тэг,возвращающий информацию о "Огурцы, кг"'''
get_cucumber = tag.create_tag(ItemsPicsFromNet, 244)

'''Тэг,возвращающий информацию о "Кабачки, кг"'''
get_kabachki = tag.create_tag(ItemsPicsFromNet, 245)

'''Тэг,возвращающий информацию о "Красный болгарский перец, кг"'''
get_red_bolg_papper = tag.create_tag(ItemsPicsFromNet, 246)

'''Тэг,возвращающий информацию о "Желтый болгарский перец, кг"'''
get_yellow_bolg_papper = tag.create_tag(ItemsPicsFromNet, 247)

'''Тэг,возвращающий информацию о "Спаржа"'''
get_asparagus = tag.create_tag(ItemsPicsFromNet, 248)

'''Тэг,возвращающий информацию о "Брокколи"'''
get_broccoli = tag.create_tag(ItemsPicsFromNet, 249)

'''Тэг,возвращающий информацию о "Напиток ромовый Captain Morgan Spiced Gold 1 литр"'''
get_captain_morgan_spiced_gold_1_l = tag.create_tag(ItemsPicsFromNet, 250)

'''Тэг,возвращающий информацию о "Виски Bell's Original 0,7 л"'''
get_bells_original_07_l = tag.create_tag(ItemsPicsFromNet, 251)

'''Тэг,возвращающий информацию о "Вино игристое Martini Asti белое 0,75 л"'''
get_martini_asti_bile_075_l = tag.create_tag(ItemsPicsFromNet, 252)

'''Тэг,возвращающий информацию о "Виски Jameson Irish Whiskey 0.7 л"'''
get_jameson_irish_whiskey_075_l = tag.create_tag(ItemsPicsFromNet, 253)

'''Тэг,возвращающий информацию о "Виски Bell's Original 1 л"'''
get_bells_original_1_l = tag.create_tag(ItemsPicsFromNet, 254)

'''Тэг,возвращающий информацию о "Напиток ромовый Captain Morgan Spiced Gold 0.5 л"'''
get_captain_morgan_spiced_gold_05_l = tag.create_tag(ItemsPicsFromNet, 255)

'''Тэг,возвращающий информацию о "Виски Jameson Irish Whiskey 0.5 л"'''
get_jameson_irish_whiskey_05_l = tag.create_tag(ItemsPicsFromNet, 256)

'''Тэг,возвращающий информацию о "Виски JW Red Label 0.5 л"'''
get_jw_red_label_05_l = tag.create_tag(ItemsPicsFromNet, 257)

'''Тэг,возвращающий информацию о "Виски Bell's Spiced 0.7 л"'''
get_bells_spiced_07_l = tag.create_tag(ItemsPicsFromNet, 258)

'''Тэг,возвращающий информацию о "Виски Ballantines Finest 0.7 л"'''
get_ballantines_finest_07_l = tag.create_tag(ItemsPicsFromNet, 259)

'''Тэг,возвращающий информацию о "Виски Jack Daniel's old n.7 tennesi 0.7 л"'''
get_jack_daniels_07_l = tag.create_tag(ItemsPicsFromNet, 260)

'''Тэг,возвращающий информацию о "Виски Jack Daniel's old n.7 tennesi 1 л"'''
get_jack_daniels_1_l = tag.create_tag(ItemsPicsFromNet, 261)

'''Тэг,возвращающий информацию о "Бурбон Jim Beam White 0.7 л"'''
get_jim_beam_white_07_l = tag.create_tag(ItemsPicsFromNet, 262)

'''Тэг,возвращающий информацию о "Минеральная вода Borjomi сильногазированная 0,5 л"'''
get_borjomi_silnogaz_05_l = tag.create_tag(ItemsPicsFromNet, 263)

'''Тэг,возвращающий информацию о "Минеральная вода Морщинская негазированная 1,5 л"'''
get_morshinskaya_negaz_15_l = tag.create_tag(ItemsPicsFromNet, 264)

'''Тэг,возвращающий информацию о "Минеральная вода Морщинская слабогазированная 1,5 л"'''
get_morshinskaya_low_gaz_15_l = tag.create_tag(ItemsPicsFromNet, 265)

'''Тэг,возвращающий информацию о "Минеральная вода Морщинская сильногазированная 1,5 л"'''
get_morshinskaya_high_gaz_15_l = tag.create_tag(ItemsPicsFromNet, 266)

'''Тэг,возвращающий информацию о "Нектар Наш Сік яблуко-виноград 200 грам"'''
get_nash_sik_apple_grape_02_l = tag.create_tag(ItemsPicsFromNet, 267)

'''Тэг,возвращающий информацию о "Сік Наш Сік яблуко-морква 200 грам"'''
get_nash_sik_apple_carrot_02_l = tag.create_tag(ItemsPicsFromNet, 268)

'''Тэг,возвращающий информацию о "Нектар Наш Сік апельсин 200 грам"'''
get_nash_sik_orange_02_l = tag.create_tag(ItemsPicsFromNet, 269)

'''Тэг,возвращающий информацию о "Нектар Наш Сік мультифрукт 200 грам"'''
get_nash_sik_multifrukt_02_l = tag.create_tag(ItemsPicsFromNet, 270)

'''Тэг,возвращающий информацию о "Сік Наш Сік яблуко-персик 200 грам"'''
get_nash_sik_apple_peach_02_l = tag.create_tag(ItemsPicsFromNet, 271)

'''Тэг,возвращающий информацию о "Сік Наш Сік груша-яблуко 200 грам"'''
get_nash_sik_pear_apple_02_l = tag.create_tag(ItemsPicsFromNet, 272)

'''Тэг,возвращающий информацию о "Сік Наш Сік мультивітамін 200 грам"'''
get_nash_sik_multivitamin_02_l = tag.create_tag(ItemsPicsFromNet, 273)

'''Тэг,возвращающий информацию о "Сік Наш Сік яблучний 200 грам"'''
get_nash_sik_apple_02_l = tag.create_tag(ItemsPicsFromNet, 274)

'''Тэг,возвращающий информацию о "Сік Наш Сік яблуко-полуниця 200 грам"'''
get_nash_sik_apple_strawberry_02_l = tag.create_tag(ItemsPicsFromNet, 275)

'''Тэг,возвращающий информацию о "Енергетичний напій Non Stop Original 250 мл"'''
get_non_stop_original_025_l = tag.create_tag(ItemsPicsFromNet, 276)

'''Тэг,возвращающий информацию о "Енергетичний напій Non Stop Original 500 мл"'''
get_non_stop_original_05_l = tag.create_tag(ItemsPicsFromNet, 277)

'''Тэг,возвращающий информацию о "Енергетичний напій Non Stop Jungle 250 мл"'''
get_non_stop_jungle_025_l = tag.create_tag(ItemsPicsFromNet, 278)

'''Тэг,возвращающий информацию о "Енергетичний напій Non Stop Boost 500 мл"'''
get_non_stop_boost_05_l = tag.create_tag(ItemsPicsFromNet, 279)

'''Тэг,возвращающий информацию о "Енергетичний напій Non Stop Ultra 500 мл"'''
get_non_stop_ultra_05_l = tag.create_tag(ItemsPicsFromNet, 280)

'''Тэг,возвращающий информацию о "Енергетичний напій Non Stop Boost 250 мл"'''
get_non_stop_boost_025_l = tag.create_tag(ItemsPicsFromNet, 281)

'''Тэг,возвращающий информацию о "Енергетичний напій Burn Classic 250 мл"'''
get_burn_classic_025_l = tag.create_tag(ItemsPicsFromNet, 282)

'''Тэг,возвращающий информацию о "Енергетичний напій Burn Classic 500 мл"'''
get_burn_classic_05_l = tag.create_tag(ItemsPicsFromNet, 283)

'''Тэг,возвращающий информацию о "Енергетичний напій Burn Mango 500 мл"'''
get_burn_mango_025_l = tag.create_tag(ItemsPicsFromNet, 284)

'''Тэг,возвращающий информацию о "Енергетичний напій Burn Apple-Kiwi 500 мл"'''
get_burn_apple_kiwi_05_l = tag.create_tag(ItemsPicsFromNet, 285)

'''Тэг,возвращающий информацию о "Енергетичний напій Burn dark energy 250 мл"'''
get_burn_dark_energy_025_l = tag.create_tag(ItemsPicsFromNet, 286)

'''Тэг,возвращающий информацию о "Енергетичний напій Red Bull 250 мл"'''
get_red_bull_025_l = tag.create_tag(ItemsPicsFromNet, 287)

'''Тэг,возвращающий информацию о "Енергетичний напій Red Bull 355 мл"'''
get_red_bull_0355_l = tag.create_tag(ItemsPicsFromNet, 288)

'''Тэг,возвращающий информацию о "Енергетичний напій Red Bull 473 мл"'''
get_red_bull_0473_l = tag.create_tag(ItemsPicsFromNet, 289)

'''Тэг,возвращающий информацию о "Енергетичний напій Red Bull 591 мл"'''
get_red_bull_0591_l = tag.create_tag(ItemsPicsFromNet, 290)

'''Тэг,возвращающий информацию о "Енергетичний напій Red Bull Sugar Free 250 мл"'''
get_red_bull_sugar_free_025_l = tag.create_tag(ItemsPicsFromNet, 291)

'''Тэг,возвращающий информацию о "Енергетичний напій Red Bull Red Edition зі смаком кавуна 250 мл"'''
get_red_bull_red_edition_cavun_025_l = tag.create_tag(ItemsPicsFromNet, 292)

'''Тэг,возвращающий информацию о "Енергетичний напій Red Bull Yellow Edition зі смаком тропічних фруктів 250 мл"'''
get_red_bull_yellow_edition_tropic_fruits_025_l = tag.create_tag(ItemsPicsFromNet, 293)

'''Тэг,возвращающий информацию о "Енергетичний напій Monster 355 мл"'''
get_monster_0355_l = tag.create_tag(ItemsPicsFromNet, 294)

'''Тэг,возвращающий информацию о "Енергетичний напій Monster The Doctor 355 мл"'''
get_monster_the_doctor_0355_l = tag.create_tag(ItemsPicsFromNet, 295)

'''Тэг,возвращающий информацию о "Енергетичний напій Monster Ultra Zero 355 мл"'''
get_monster_ultra_zero_0355_l = tag.create_tag(ItemsPicsFromNet, 296)

'''Тэг,возвращающий информацию о "Енергетичний напій Monster Juiced 355 мл"'''
get_monster_juiced_0355_l = tag.create_tag(ItemsPicsFromNet, 297)

'''Тэг,возвращающий информацию о "Енергетичний напій Pit Bull Coffee 250 мл"'''
get_pit_bull_coffee_025_l = tag.create_tag(ItemsPicsFromNet, 298)

'''Тэг,возвращающий информацию о "Енергетичний напій Pit Bull Power 250 мл"'''
get_pit_bull_power_025_l = tag.create_tag(ItemsPicsFromNet, 299)

'''Тэг,возвращающий информацию о "Енергетичний напій Pit Bull X 250 мл"'''
get_pit_bull_x_025_l = tag.create_tag(ItemsPicsFromNet, 300)

'''Тэг,возвращающий информацию о "Енергетичний напій Pit Bull Extra Vitamin C 250 мл"'''
get_pit_bull_extra_vitamin_c_025_l = tag.create_tag(ItemsPicsFromNet, 301)

'''Тэг,возвращающий информацию о "Енергетичний напій Pit Bull 250 мл"'''
get_pit_bull_025_l = tag.create_tag(ItemsPicsFromNet, 302)

'''Тэг,возвращающий информацию о "Кава розчинна MacCoffee Gold натуральна д/п, 60г"'''
get_maccoffee_gold_rozch_soft_pack_60_gr = tag.create_tag(ItemsPicsFromNet, 303)

'''Тэг,возвращающий информацию о "Кава розчинна Nescafe Gold м`яка упаковка, 120г"'''
get_nescafe_gold_rozch_soft_pack_120_gr = tag.create_tag(ItemsPicsFromNet, 304)

'''Тэг,возвращающий информацию о "Кава розчинна Grano Dorado Gold, 130г"'''
get_grano_dorado_gold_soft_pack_130_gr = tag.create_tag(ItemsPicsFromNet, 305)

'''Тэг,возвращающий информацию о "Кава розчинна Nescafe Classic, 60г"'''
get_nescafe_classic_soft_pack_60_gr = tag.create_tag(ItemsPicsFromNet, 306)

'''Тэг,возвращающий информацию о "Кава розчинна Чорна карта GOLD пакет, 400г"'''
get_chorna_carta_gold_soft_pack_400_gr = tag.create_tag(ItemsPicsFromNet, 307)

'''Тэг,возвращающий информацию о "Батончик Bounty з м`якоттю кокоса в молочному шоколаді, 57г"'''
get_bounty_small = tag.create_tag(ItemsPicsFromNet, 308)

'''Тэг,возвращающий информацию о "Батончик Bounty з м`якоттю кокоса в молочному шоколаді, 85г"'''
get_bounty_big = tag.create_tag(ItemsPicsFromNet, 309)

'''Тэг,возвращающий информацию о "Батончик Mars з нугою і карамеллю в молочному шоколаді, 51г"'''
get_mars_small = tag.create_tag(ItemsPicsFromNet, 310)

'''Тэг,возвращающий информацию о "Батончик Mars нуга/карамель в молочному шоколаді, 70г"'''
get_mars_big = tag.create_tag(ItemsPicsFromNet, 311)

'''Тэг,возвращающий информацию о "Батончик Nuts Strawberry, 42 г"'''
get_nuts_strawberry = tag.create_tag(ItemsPicsFromNet, 312)

'''Тэг,возвращающий информацию о "Батончик Nuts шоколадний, 42г"'''
get_nuts_small = tag.create_tag(ItemsPicsFromNet, 313)

'''Тэг,возвращающий информацию о "Батончик Nuts King size шоколадний, 60г"'''
get_nuts_king_size = tag.create_tag(ItemsPicsFromNet, 314)

'''Тэг,возвращающий информацию о "Батончик Snickers з арахісом у молочному шоколаді, 50г"'''
get_snickers_small = tag.create_tag(ItemsPicsFromNet, 315)

'''Тэг,возвращающий информацию о "Батончик Snickers Super з арахісом в молочному шоколаді, 112,5г"'''
get_snickers_super = tag.create_tag(ItemsPicsFromNet, 316)

'''Тэг,возвращающий информацию о "Батончик Snickers з арахісовим маслом, 54,75г"'''
get_snickers_creamy_peanut_butter = tag.create_tag(ItemsPicsFromNet, 317)

'''Тэг,возвращающий информацию о "Батончик Snickers з арахісовим маслом, 36,5г"'''
get_snickers_creamy_peanut_butter_small = tag.create_tag(ItemsPicsFromNet, 318)

'''Тэг,возвращающий информацию о "Батончик Twix з печивом і карамеллю в молочному шоколаді, 50г"'''
get_twix_pechivo_karamel_50gr = tag.create_tag(ItemsPicsFromNet, 319)

'''Тэг,возвращающий информацию о "Батончик Twix Extra печиво-карамель в молочному шоколаді, 75г"'''
get_twix_extra_pechivo_karamel_75gr = tag.create_tag(ItemsPicsFromNet, 320)

'''Тэг,возвращающий информацию о "Горілка Absolut, 0,5л"'''
get_vodka_absolut_05l = tag.create_tag(ItemsPicsFromNet, 321)

'''Тэг,возвращающий информацию о "Горілка Absolut, 1 л"'''
get_vodka_absolut_1l = tag.create_tag(ItemsPicsFromNet, 322)

'''Тэг,возвращающий информацию о "Горілка Absolut, 0,7л"'''
get_vodka_absolut_07l = tag.create_tag(ItemsPicsFromNet, 323)

'''Тэг,возвращающий информацию о "Горілка Absolut Lime, 0,7л"'''
get_vodka_absolut_lime_07l = tag.create_tag(ItemsPicsFromNet, 324)

'''Тэг,возвращающий информацию о "Горілка Absolut Grapefruit, 0,7л"'''
get_vodka_absolut_grapefruit_07l = tag.create_tag(ItemsPicsFromNet, 325)

'''Тэг,возвращающий информацию о "Горілка Absolut Elyx, 0,7л"'''
get_vodka_absolut_elyx_07l = tag.create_tag(ItemsPicsFromNet, 326)

'''Тэг,возвращающий информацию о "Горілка Absolut Citron, 0,7л"'''
get_vodka_absolut_citron_07l = tag.create_tag(ItemsPicsFromNet, 327)

'''Тэг,возвращающий информацию о "Горілка Absolut Kurant, 0,7л"'''
get_vodka_absolut_kurant_07l = tag.create_tag(ItemsPicsFromNet, 328)

'''Тэг,возвращающий информацию о "Горілка Absolut Watermelon, 0,7л"'''
get_vodka_absolut_watermelon_07l = tag.create_tag(ItemsPicsFromNet, 329)

'''Тэг,возвращающий информацию о "Горілка Absolut Mandarin, 0,7л"'''
get_vodka_absolut_mandarin_07l = tag.create_tag(ItemsPicsFromNet, 330)

'''Тэг,возвращающий информацию о "Горілка Finlandia, 0,5л"'''
get_vodka_finland_05l = tag.create_tag(ItemsPicsFromNet, 331)

'''Тэг,возвращающий информацию о "Горілка Finlandia, 0,7л"'''
get_vodka_finland_07l = tag.create_tag(ItemsPicsFromNet, 332)

'''Тэг,возвращающий информацию о "Горілка Finlandia, 1л"'''
get_vodka_finland_1l = tag.create_tag(ItemsPicsFromNet, 333)

'''Тэг,возвращающий информацию о "Горілка Finlandia Redberry, 0.5 л"'''
get_vodka_finland_redberry_05l = tag.create_tag(ItemsPicsFromNet, 334)

'''Тэг,возвращающий информацию о "Горілка Finlandia Redberry, 1 л"'''
get_vodka_finland_redberry_1l = tag.create_tag(ItemsPicsFromNet, 335)

'''Тэг,возвращающий информацию о "Горілка Finlandia Cranberry, 0.5 л"'''
get_vodka_finland_cranberry_05l = tag.create_tag(ItemsPicsFromNet, 336)

'''Тэг,возвращающий информацию о "Горілка Finlandia Cranberry, 1 л"'''
get_vodka_finland_cranberry_1l = tag.create_tag(ItemsPicsFromNet, 337)

'''Тэг,возвращающий информацию о "Горілка Finlandia Grapefruit, 0.5 л"'''
get_vodka_finland_grapefruit_05l = tag.create_tag(ItemsPicsFromNet, 338)

'''Тэг,возвращающий информацию о "Горілка Finlandia Lime, 0.5 л"'''
get_vodka_finland_lime_05l = tag.create_tag(ItemsPicsFromNet, 339)

'''Тэг,возвращающий информацию о "Горілка Finlandia Coconut, 0.5 л"'''
get_vodka_finland_coconut_05l = tag.create_tag(ItemsPicsFromNet, 340)

'''Тэг,возвращающий информацию о "Горілка Finlandia Blackcurrant, 0.5 л"'''
get_vodka_finland_blackcurrant_05l = tag.create_tag(ItemsPicsFromNet, 341)

'''Тэг,возвращающий информацию о "Горілка Finlandia Lime, 1 л"'''
get_vodka_finland_lime_1l = tag.create_tag(ItemsPicsFromNet, 342)

'''Тэг,возвращающий информацию о "Горілка Finlandia Blackcurrant, 1 л"'''
get_vodka_finland_blackcurrant_1l = tag.create_tag(ItemsPicsFromNet, 343)

'''Тэг,возвращающий информацию о "Горілка Finlandia Grapefruit, 1 л"'''
get_vodka_finland_grapefruit_1l = tag.create_tag(ItemsPicsFromNet, 344)

'''Тэг,возвращающий информацию о "Горілка Finlandia Grapefruit, 1.75 л"'''
get_vodka_finland_white_175l = tag.create_tag(ItemsPicsFromNet, 345)

'''Тэг,возвращающий информацию о "Горілка Nemiroff Delikat м'яка, 0,5л"'''
get_vodka_nemiroff_delikat_soft_05l = tag.create_tag(ItemsPicsFromNet, 346)

'''Тэг,возвращающий информацию о "Горілка Nemiroff Штоф особлива, 0,5л"'''
get_vodka_nemiroff_shtof_05l = tag.create_tag(ItemsPicsFromNet, 347)

'''Тэг,возвращающий информацию о "Горілка Nemiroff українська пшениця, 0,5л"'''
get_vodka_nemiroff_ukr_pshen_05l = tag.create_tag(ItemsPicsFromNet, 348)

'''Тэг,возвращающий информацию о "Горілка Nemiroff Де Люкс, 0,5л"'''
get_vodka_nemiroff_delux_05l = tag.create_tag(ItemsPicsFromNet, 349)

'''Тэг,возвращающий информацию о "Горілка Nemiroff Lex, 0,5л"'''
get_vodka_nemiroff_lex_05l = tag.create_tag(ItemsPicsFromNet, 350)

'''Тэг,возвращающий информацию о "Шампанське АЗШВ Артемівське біле напівсолодке, 0,75л"'''
get_artemivske_bile_napivsolod_075l = tag.create_tag(ItemsPicsFromNet, 351)

'''Тэг,возвращающий информацию о "Шампанське АЗШВ Артемівське рожеве напівсухе, 0,75л"'''
get_artemivske_roj_napivsuh_075l = tag.create_tag(ItemsPicsFromNet, 352)

'''Тэг,возвращающий информацию о "Шампанське АЗШВ Артемівське біле брют, 0,75л"'''
get_artemivske_bile_brut_075l = tag.create_tag(ItemsPicsFromNet, 353)

'''Тэг,возвращающий информацию о "Шампанське АЗШВ Артемівське коллекційне напівсухе, 0,75л"'''
get_artemivske_coll_napivsuh_075l = tag.create_tag(ItemsPicsFromNet, 354)

'''Тэг,возвращающий информацию о "Шампанське АЗШВ Артемівське червоне напівсолодке, 0,75л"'''
get_artemivske_cherv_napivsuh_075l = tag.create_tag(ItemsPicsFromNet, 355)

'''Тэг,возвращающий информацию о "Шампанське Bagrationi біле напівсолодке, 0,75л"'''
get_bagrationi_bile_napivsolod_075l = tag.create_tag(ItemsPicsFromNet, 356)

'''Тэг,возвращающий информацию о "Шампанське Bagrationi біле напівсухе, 0,75л"'''
get_bagrationi_bile_napivsuh_075l = tag.create_tag(ItemsPicsFromNet, 357)

'''Тэг,возвращающий информацию о "Шампанське Bagrationi біле брют, 0,75л"'''
get_bagrationi_bile_brut_075l = tag.create_tag(ItemsPicsFromNet, 358)

'''Тэг,возвращающий информацию о "Шампанське Bagrationi рожеве напівсолодке, 0,75л"'''
get_bagrationi_rojeve_napivsolod_075l = tag.create_tag(ItemsPicsFromNet, 359)

'''Тэг,возвращающий информацию о "Шампанське Bagrationi Gold напівсолодке, 0,75л"'''
get_bagrationi_gold_napivsolod_075l = tag.create_tag(ItemsPicsFromNet, 360)

'''Тэг,возвращающий информацию о "Шампанське Bolgrad біле брют, 0,75л"'''
get_bolgrad_bile_brut_075l = tag.create_tag(ItemsPicsFromNet, 361)

'''Тэг,возвращающий информацию о "Шампанське Bolgrad біле напівсолодке, 0,75л"'''
get_bolgrad_bile_napivsolod_075l = tag.create_tag(ItemsPicsFromNet, 362)

'''Тэг,возвращающий информацию о "Шампанське Bolgrad Nectar біле солодке, 0,75л"'''
get_bolgrad_nectar_bile_solodke_075l = tag.create_tag(ItemsPicsFromNet, 363)

'''Тэг,возвращающий информацию о "Шампанське Французький Бульвар біле напівсухе, 0,75л"'''
get_fran_bulv_bile_napivsuh_075l = tag.create_tag(ItemsPicsFromNet, 364)

'''Тэг,возвращающий информацию о "Шампанське Французький Бульвар біле брют, 0,75л"'''
get_fran_bulv_bile_brut_075l = tag.create_tag(ItemsPicsFromNet, 365)

'''Тэг,возвращающий информацию о "Шампанське Французький Бульвар біле напівсолодке, 0,75л"'''
get_fran_bulv_bile_napivsolod_075l = tag.create_tag(ItemsPicsFromNet, 366)

'''Тэг,возвращающий информацию о "Коньяк Старий Кахеті 3 зірки, 0,5л"'''
get_stariy_koheti_3 = tag.create_tag(ItemsPicsFromNet, 370)                   #смещение индекса товара

'''Тэг,возвращающий информацию о "Коньяк Старий Кахеті 3 зірки, 0,5л"'''
get_stariy_koheti_5 = tag.create_tag(ItemsPicsFromNet, 371)

'''Тэг,возвращающий информацию о "Коньяк Старий Кахеті 4 зірки, 0,5л"'''
get_stariy_koheti_4 = tag.create_tag(ItemsPicsFromNet, 372)

'''Тэг,возвращающий информацию о "Бренді Коблево Reserve Extra Old 8 років, 0,5л"'''
get_brendi_koblevo_reserve_extra_old_8_years = tag.create_tag(ItemsPicsFromNet, 373)

'''Тэг,возвращающий информацию о "Коньяк 'Шабо VSOP' 5 зірок, 0,5л"'''
get_shabo_vsop_5 = tag.create_tag(ItemsPicsFromNet, 374)

'''Тэг,возвращающий информацию о "Коньяк 'Шабо VS' 3 зірки, 0,5л"'''
get_shabo_vs_3 = tag.create_tag(ItemsPicsFromNet, 375)

'''Тэг,возвращающий информацию о "Коньяк 'Шабо 1788' 4 зірки, 0,5л"'''
get_shabo_1788_4 = tag.create_tag(ItemsPicsFromNet, 376)

'''Тэг,возвращающий информацию о "Коньяк 'Шабо 1788' резерв, 0,5л"'''
get_shabo_1788_reserv = tag.create_tag(ItemsPicsFromNet, 377)

'''Тэг,возвращающий информацию о "Коньяк 'Шабо VS' резерв, 0,5л"'''
get_shabo_vs_reserv = tag.create_tag(ItemsPicsFromNet, 378)

'''Тэг,возвращающий информацию о "Коньяк 'Шабо VSOP' резерв, 0,5л"'''
get_shabo_vsop_reserv = tag.create_tag(ItemsPicsFromNet, 379)

'''Тэг,возвращающий информацию о "Коньяк 'Азнаурі' 3 зірки, 0,5л"'''
get_aznauri_3 = tag.create_tag(ItemsPicsFromNet, 380)

'''Тэг,возвращающий информацию о "Коньяк 'Азнаурі' 5 зірок, 0,5л"'''
get_aznauri_5 = tag.create_tag(ItemsPicsFromNet, 381)

'''Тэг,возвращающий информацию о "Коньяк 'Азнаурі' 4 зірки, 0,5л"'''
get_aznauri_4 = tag.create_tag(ItemsPicsFromNet, 382)

'''Тэг,возвращающий информацию о "Коньяк 'Азнаурі' 4 зірки, 0,5л"'''
get_aznauri_black_barrel_5 = tag.create_tag(ItemsPicsFromNet, 383)

'''Тэг,возвращающий информацию о "Коньяк 'Adjari' 3 зірки, 0,5л"'''
get_adjari_3 = tag.create_tag(ItemsPicsFromNet, 384)

'''Тэг,возвращающий информацию о "Коньяк 'Adjari' 5 зірок, 0,5л"'''
get_adjari_5 = tag.create_tag(ItemsPicsFromNet, 385)

'''Тэг,возвращающий информацию о "Коньяк 'Adjari' 4 зірки, 0,5л"'''
get_adjari_4 = tag.create_tag(ItemsPicsFromNet, 386)

'''Тэг,возвращающий информацию о "Коньяк 'Hennesy' в подарунковій упаковці, 0,5л"'''
get_hennesy_vs = tag.create_tag(ItemsPicsFromNet, 387)

'''Тэг,возвращающий информацию о "Коньяк 'Hennesy VSOP' в подарунковій упаковці, 0,5л"'''
get_hennesy_vsop = tag.create_tag(ItemsPicsFromNet, 388)

'''Тэг,возвращающий информацию о "Коньяк 'AleXX Gold VSOP' в тубусі, 0,5л"'''
get_alexx_gold_vsop = tag.create_tag(ItemsPicsFromNet, 389)

'''Тэг,возвращающий информацию о "Коньяк 'AleXX Silver VS' в тубусі, 0,5л"'''
get_alexx_silver_vs = tag.create_tag(ItemsPicsFromNet, 390)

'''Тэг,возвращающий информацию о "Коньяк 'Ararat' 5 зірок, 0,5л"'''
get_ararat_5 = tag.create_tag(ItemsPicsFromNet, 391)

'''Тэг,возвращающий информацию о "Коньяк 'Ararat Ahtamar' 10 років, 0,5л"'''
get_ararat_ahtamar_10 = tag.create_tag(ItemsPicsFromNet, 392)

'''Тэг,возвращающий информацию о "Коньяк 'Ararat' 3 зірки, 0,5л"'''
get_ararat_3 = tag.create_tag(ItemsPicsFromNet, 393)

'''Тэг,возвращающий информацию о "Коньяк 'Ararat Nairi' 20 років, 0,5л"'''
get_ararat_nairi_20 = tag.create_tag(ItemsPicsFromNet, 394)

'''Тэг,возвращающий информацию о "Горілка Green Day Air, 0,5л"'''
get_green_day_air_05l = tag.create_tag(ItemsPicsFromNet, 395)

'''Тэг,возвращающий информацию о "Горілка Green Day Ultra Soft 40%, 0,5л"'''
get_green_day_ultra_soft_05l = tag.create_tag(ItemsPicsFromNet, 396)

'''Тэг,возвращающий информацию о "Горілка Green Day Organic Life, 0,5л"'''
get_green_day_organic_life_05l = tag.create_tag(ItemsPicsFromNet, 397)

'''Тэг,возвращающий информацию о "Горілка Green Day Crystal 40%, 0,5л"'''
get_green_day_crystal_05l = tag.create_tag(ItemsPicsFromNet, 398)

'''Тэг,возвращающий информацию о "Горілка Green Day, 0,5л"'''
get_green_day_05l = tag.create_tag(ItemsPicsFromNet, 399)

'''Тэг,возвращающий информацию о "Горілка Medoff Класік New, 0,5л"'''
get_medoff_classic_05l = tag.create_tag(ItemsPicsFromNet, 400)

'''Тэг,возвращающий информацию о "Горілка Smirnoff Red, 0,5л"'''
get_smirnoff_red_05l = tag.create_tag(ItemsPicsFromNet, 401)

'''Тэг,возвращающий информацию о "Горілка Класична "Козацька рада", 0,5л"'''
get_kozacka_rada_classic_05l = tag.create_tag(ItemsPicsFromNet, 402)

'''Тэг,возвращающий информацию о "Горілка "Козацька рада" Особлива, 0,5л"'''
get_kozacka_rada_osobliva_05l = tag.create_tag(ItemsPicsFromNet, 403)

'''Тэг,возвращающий информацию о "Горілка Zubrowka Bison Grass, 0,5л"'''
get_zubrowka_bison_grass_05l = tag.create_tag(ItemsPicsFromNet, 404)

'''Тэг,возвращающий информацию о "Горілка Zubrowka Biala, 0,5л"'''
get_zubrowka_biala_05l = tag.create_tag(ItemsPicsFromNet, 405)

'''Тэг,возвращающий информацию о "Горілка Zubrowka Сzarna, 0,5л"'''
get_zubrowka_czarna_05l = tag.create_tag(ItemsPicsFromNet, 406)

'''Тэг,возвращающий информацию о "Горілка Воздух Легка особлива, 0,5л"'''
get_vozduh_legka_05l = tag.create_tag(ItemsPicsFromNet, 407)

'''Тэг,возвращающий информацию о "Горілка Повітря Альфа, 0,5л"'''
get_vozduh_alpha_05l = tag.create_tag(ItemsPicsFromNet, 408)

'''Тэг,возвращающий информацию о "Горілка "Перша гільдія" Верховна, 0,5л"'''
get_persha_gild_verhovna_05l = tag.create_tag(ItemsPicsFromNet, 409)

'''Тэг,возвращающий информацию о "Горілка "Перша гільдія" Знатна, 0,5л"'''
get_persha_gild_znatna_05l = tag.create_tag(ItemsPicsFromNet, 410)

'''Тэг,возвращающий информацию о "Горілка "Перша гільдія" Поважна, 0,5л"'''
get_persha_gild_povajna_05l = tag.create_tag(ItemsPicsFromNet, 411)

'''Тэг,возвращающий информацию о "Горілка "Хлібний Дар" Класична, 0,5л"'''
get_hlibniy_dar_classic_05l = tag.create_tag(ItemsPicsFromNet, 412)

'''Тэг,возвращающий информацию о "Горілка "Хлібний Дар" на пророщеному зерні, 0,5л"'''
get_hlibniy_dar_pror_zerno_05l = tag.create_tag(ItemsPicsFromNet, 413)

'''Тэг,возвращающий информацию о "Горілка "Хлібний Дар" Житня, 0,5л"'''
get_hlibniy_dar_jitnya_05l = tag.create_tag(ItemsPicsFromNet, 414)

'''Тэг,возвращающий информацию о "Горілка "Хлібний Дар" Пшенична, 0,5л"'''
get_hlibniy_dar_pshen_05l = tag.create_tag(ItemsPicsFromNet, 415)

'''Тэг,возвращающий информацию о "Горілка Green Day Organic Life, 0,7л"'''
get_green_day_organic_life_07l = tag.create_tag(ItemsPicsFromNet, 416)

'''Тэг,возвращающий информацию о "Горілка Green Day, 0,7л"'''
get_green_day_07l = tag.create_tag(ItemsPicsFromNet, 417)

'''Тэг,возвращающий информацию о "Горілка Green Day Ultra Soft 40%, 0,7л"'''
get_green_day_ultra_soft_07l = tag.create_tag(ItemsPicsFromNet, 418)

'''Тэг,возвращающий информацию о "Горілка Green Day Air, 0,7л"'''
get_green_day_air_07l = tag.create_tag(ItemsPicsFromNet, 419)

'''Тэг,возвращающий информацию о "Горілка Green Day Crystal 40%, 0,7л"'''
get_green_day_crystal_07l = tag.create_tag(ItemsPicsFromNet, 420)

'''Тэг,возвращающий информацию о "Горілка Medoff Класік, 0,7л"'''
get_medoff_classic_07l = tag.create_tag(ItemsPicsFromNet, 421)

'''Тэг,возвращающий информацию о "Горілка Nemiroff Delikat м`яка, 0,7л"'''
get_nemiroff_delikat_myaka_07l = tag.create_tag(ItemsPicsFromNet, 422)

'''Тэг,возвращающий информацию о "Горілка Nemiroff Особлива штоф, 0,7л"'''
get_nemiroff_osob_shtof_07l = tag.create_tag(ItemsPicsFromNet, 423)

'''Тэг,возвращающий информацию о "Горілка Nemiroff Де Люкс, 0,7л"'''
get_nemiroff_deluxe_07l = tag.create_tag(ItemsPicsFromNet, 424)

'''Тэг,возвращающий информацию о "Горілка Nemiroff Lex, 0,7л"'''
get_nemiroff_lex_07l = tag.create_tag(ItemsPicsFromNet, 425)

'''Тэг,возвращающий информацию о "Горілка Zubrowka, 0,7л"'''
get_zubrowka_07l = tag.create_tag(ItemsPicsFromNet, 426)

'''Тэг,возвращающий информацию о "Горілка Zubrowka Сzarna, 0,7л"'''
get_zubrowka_czarna_07l = tag.create_tag(ItemsPicsFromNet, 427)

'''Тэг,возвращающий информацию о "Горілка Гетьман, 0,7л"'''
get_hetman_07l = tag.create_tag(ItemsPicsFromNet, 428)

'''Тэг,возвращающий информацию о "Горілка "Козацька рада" Класична, 0,7л"'''
get_kozacka_rada_classic_07l = tag.create_tag(ItemsPicsFromNet, 429)

'''Тэг,возвращающий информацию о "Горілка "Козацька рада" Преміум, 0,7л"'''
get_kozacka_rada_premium_07l = tag.create_tag(ItemsPicsFromNet, 430)

'''Тэг,возвращающий информацию о "Горілка "Козацька рада" Особлива, 0,7л"'''
get_kozacka_rada_osobliva_07l = tag.create_tag(ItemsPicsFromNet, 431)

'''Тэг,возвращающий информацию о "Горілка "Перша гільдія" Поважна, 0,7л"'''
get_persha_gildya_povajna_07l = tag.create_tag(ItemsPicsFromNet, 432)

'''Тэг,возвращающий информацию о "Горілка "Перша гільдія" Верховна, 0,7л"'''
get_persha_gildya_verhovna_07l = tag.create_tag(ItemsPicsFromNet, 433)

'''Тэг,возвращающий информацию о "Горілка "Перша гільдія" Знатна, 0,7л"'''
get_persha_gildya_znatna_07l = tag.create_tag(ItemsPicsFromNet, 434)

'''Тэг,возвращающий информацию о "Горілка "Хлібний Дар" Класична, 0,7л"'''
get_hlib_dar_classic_07l = tag.create_tag(ItemsPicsFromNet, 435)

'''Тэг,возвращающий информацию о "Горілка Medoff Класік , 1л"'''
get_medoff_classic_1l = tag.create_tag(ItemsPicsFromNet, 436)

'''Тэг,возвращающий информацию о "Горілка Nemiroff Особлива штоф, 1л"'''
get_nemiroff_shtof_1l = tag.create_tag(ItemsPicsFromNet, 437)

'''Тэг,возвращающий информацию о "Горілка Nemiroff Delikat м`яка, 1л"'''
get_nemiroff_delicat_soft_1l = tag.create_tag(ItemsPicsFromNet, 438)

'''Тэг,возвращающий информацию о "Горілка Zubrowka Bison Grass, 1л"'''
get_zubrowka_bison_grass_1l = tag.create_tag(ItemsPicsFromNet, 439)

'''Тэг,возвращающий информацию о "Горілка Zubrowka Biala, 1л"'''
get_zubrowka_biala_1l = tag.create_tag(ItemsPicsFromNet, 440)

'''Тэг,возвращающий информацию о "Горілка Гетьман, 1000мл"'''
get_hetman_1l = tag.create_tag(ItemsPicsFromNet, 441)

'''Тэг,возвращающий информацию о "Горілка "Козацька рада" Особлива, 1л"'''
get_kozacka_rada_osobliva_1l = tag.create_tag(ItemsPicsFromNet, 442)

'''Тэг,возвращающий информацию о "Горілка "Козацька рада" Класична, 1л"'''
get_kozacka_rada_classic_1l = tag.create_tag(ItemsPicsFromNet, 443)

'''Тэг,возвращающий информацию о "Горілка "Хлібний Дар" Класична, 1л"'''
get_hlib_dar_classic_1l = tag.create_tag(ItemsPicsFromNet, 444)

'''Тэг,возвращающий информацию о "Свинне ребро, кг"'''
get_svin_rebro = tag.create_tag(ItemsPicsFromNet, 445)

'''Тэг,возвращающий информацию о "Свиняче сало фермерське, кг"'''
get_salo = tag.create_tag(ItemsPicsFromNet, 446)

'''Тэг,возвращающий информацию о "Свинна гомілка, кг"'''
get_svin_gomilka = tag.create_tag(ItemsPicsFromNet, 447)

'''Тэг,возвращающий информацию о "Печінка свинна охолоджена, кг"'''
get_pechinka_svin = tag.create_tag(ItemsPicsFromNet, 448)

'''Тэг,возвращающий информацию о "Свинячий гуляш, кг"'''
get_svin_gulyash = tag.create_tag(ItemsPicsFromNet, 449)

'''Тэг,возвращающий информацию о "Свинна піджарка, кг"'''
get_svin_pidjarka = tag.create_tag(ItemsPicsFromNet, 450)

'''Тэг,возвращающий информацию о "Горілка "Свинна корейка, кг"'''
get_svin_koreyka = tag.create_tag(ItemsPicsFromNet, 451)

'''Тэг,возвращающий информацию о "Свинна вирізка, кг"'''
get_svin_virezka = tag.create_tag(ItemsPicsFromNet, 452)

'''Тэг,возвращающий информацию о "Свинна лопатка без кістки, кг"'''
get_lopatka_bez_kistki = tag.create_tag(ItemsPicsFromNet, 453)

'''Тэг,возвращающий информацию о "Свинний окіст без кістки, кг"'''
get_svin_okist_bez_kistki = tag.create_tag(ItemsPicsFromNet, 454)

'''Тэг,возвращающий информацию о "Фарш свинний, кг"'''
get_svin_farsh = tag.create_tag(ItemsPicsFromNet, 455)

'''Тэг,возвращающий информацию о "Свинний биток без кістки, кг"'''
get_svin_bitok_bez_kistki = tag.create_tag(ItemsPicsFromNet, 456)

'''Тэг,возвращающий информацию о "Свинне рагу, кг"'''
get_svin_ragu = tag.create_tag(ItemsPicsFromNet, 457)

'''Тэг,возвращающий информацию о "Свинний ошийок без кістки, кг"'''
get_svin_osheek_bez_kistki = tag.create_tag(ItemsPicsFromNet, 458)

'''Тэг,возвращающий информацию о "Куряча четвертина, кг"'''
get_kuryacha_chetvert = tag.create_tag(ItemsPicsFromNet, 459)

'''Тэг,возвращающий информацию о "Куряче стегно, кг"'''
get_kuryache_stegno = tag.create_tag(ItemsPicsFromNet, 460)

'''Тэг,возвращающий информацию о "Куряче крило, кг"'''
get_kuryache_krilo = tag.create_tag(ItemsPicsFromNet, 461)

'''Тэг,возвращающий информацию о "Куряче філе, кг"'''
get_kuryache_file = tag.create_tag(ItemsPicsFromNet, 462)

'''Тэг,возвращающий информацию о "Куряча гомілка, кг"'''
get_kuryacha_gomilka = tag.create_tag(ItemsPicsFromNet, 463)

'''Тэг,возвращающий информацию о "Напій Coca-Cola банка, 0,33л"'''
get_coca_cola_origin_033_jb = tag.create_tag(ItemsPicsFromNet, 464)

'''Тэг,возвращающий информацию о "Напій Coca-Cola Zero м/б, 0,33л"'''
get_coca_cola_zero_033_jb = tag.create_tag(ItemsPicsFromNet, 465)

'''Тэг,возвращающий информацию о "Напій Fanta Orange м/б, 0,33л"'''
get_fanta_orange_033_jb = tag.create_tag(ItemsPicsFromNet, 466)

'''Тэг,возвращающий информацию о "Напій Fanta Pineapple м/б, 0,33л"'''
get_fanta_pineapple_033_jb = tag.create_tag(ItemsPicsFromNet, 467)

'''Тэг,возвращающий информацию о "Напій Sprite м/б, 0,33л"'''
get_sprite_033_jb = tag.create_tag(ItemsPicsFromNet, 468)

'''Тэг,возвращающий информацию о "Напиток Coca-Cola ст.бут., 0,25л"'''
get_coca_cola_025_glass = tag.create_tag(ItemsPicsFromNet, 469)

'''Тэг,возвращающий информацию о "Напиток Coca-Cola Zero стекло, 0,25л"'''
get_coca_cola_zero_025_glass = tag.create_tag(ItemsPicsFromNet, 470)

'''Тэг,возвращающий информацию о "Напиток Coca-Cola 0,5л"'''
get_coca_cola_original_05_pl = tag.create_tag(ItemsPicsFromNet, 471)

'''Тэг,возвращающий информацию о "Напиток Coca-Cola Zero, 0,5л"'''
get_coca_cola_zero_05_pl = tag.create_tag(ItemsPicsFromNet, 472)

'''Тэг,возвращающий информацию о "Напиток Fanta Orange 0,5л"'''
get_fanta_orange_05_pl = tag.create_tag(ItemsPicsFromNet, 473)

'''Тэг,возвращающий информацию о "Напиток Sprite 0,5л"'''
get_sprite_05_pl = tag.create_tag(ItemsPicsFromNet, 474)

'''Тэг,возвращающий информацию о "Напиток Coca-Cola 1,5л"'''
get_coca_cola_original_15_pl = tag.create_tag(ItemsPicsFromNet, 475)

'''Тэг,возвращающий информацию о "Напиток Coca-Cola Zero"'''
get_coca_cola_zero_15_pl = tag.create_tag(ItemsPicsFromNet, 476)

'''Тэг,возвращающий информацию о "Напиток Sprite 1,5л"'''
get_sprite_15_pl = tag.create_tag(ItemsPicsFromNet, 477)

'''Тэг,возвращающий информацию о "Напиток Fanta Orange 1,5л"'''
get_fanta_orange_15_pl = tag.create_tag(ItemsPicsFromNet, 478)

'''Тэг,возвращающий информацию о "Напиток сокосодержащий Fanta Shokata сильногазированный, 1,5л"'''
get_fanta_shokata_15_pl = tag.create_tag(ItemsPicsFromNet, 479)

'''Тэг,возвращающий информацию о "Напиток Fanta Мандарин, 1,5л"'''
get_fanta_mandarin_15_pl = tag.create_tag(ItemsPicsFromNet, 480)

'''Тэг,возвращающий информацию о "Чіпси Люкс бекон, 133г"'''
get_chips_luxe_becon_133gr = tag.create_tag(ItemsPicsFromNet, 481)

'''Тэг,возвращающий информацию о "Чіпси Люкс паприка, 133г"'''
get_chips_luxe_paprika_133gr = tag.create_tag(ItemsPicsFromNet, 482)

'''Тэг,возвращающий информацию о "Чіпси Люкс краб, 133г"'''
get_chips_luxe_crab_133gr = tag.create_tag(ItemsPicsFromNet, 483)

'''Тэг,возвращающий информацию о "Чіпси Люкс сметана-цибуля, 133г"'''
get_chips_luxe_smetana_cibulya_133gr = tag.create_tag(ItemsPicsFromNet, 484)

'''Тэг,возвращающий информацию о "Чіпси Люкс сир, 133г"'''
get_chips_luxe_sir_133gr = tag.create_tag(ItemsPicsFromNet, 485)

'''Тэг,возвращающий информацию о "Чіпси Люкс сир, 71г"'''
get_chips_luxe_sir_71gr = tag.create_tag(ItemsPicsFromNet, 486)

'''Тэг,возвращающий информацию о "Чіпси Люкс бекон, 71г"'''
get_chips_luxe_becon_71gr = tag.create_tag(ItemsPicsFromNet, 487)

'''Тэг,возвращающий информацию о "Чіпси Люкс паприка, 71г"'''
get_chips_luxe_paprika_71gr = tag.create_tag(ItemsPicsFromNet, 488)

'''Тэг,возвращающий информацию о "Чіпси Люкс краб, 71г"'''
get_chips_luxe_crab_71gr = tag.create_tag(ItemsPicsFromNet, 489)

'''Тэг,возвращающий информацию о "Чіпси Люкс сметана-цибуля, 71г"'''
get_chips_luxe_smetana_cibulya_71gr = tag.create_tag(ItemsPicsFromNet, 490)

'''Тэг,возвращающий информацию о "Чіпси Люкс хвилясті зі смаком лисичок, 125г"'''
get_chips_luxe_hvilyasti_lisichki_125gr = tag.create_tag(ItemsPicsFromNet, 491)

'''Тэг,возвращающий информацию о "Чіпси Люкс зі смаком сметани та цибулі, 183г"'''
get_chips_luxe_smetana_cibulya_183gr = tag.create_tag(ItemsPicsFromNet, 492)

'''Тэг,возвращающий информацию о "Чіпси Люкс зі смаком бекону, 183г"'''
get_chips_luxe_becon_183gr = tag.create_tag(ItemsPicsFromNet, 493)

'''Тэг,возвращающий информацию о "Чіпси Люкс зі смаком сиру, 183г"'''
get_chips_luxe_sir_183gr = tag.create_tag(ItemsPicsFromNet, 494)

'''Тэг,возвращающий информацию о "Снек пікантний Pringles Грецький соус цацикі, 185г"'''
get_chips_pringles_greec_souse_caciki_185gr = tag.create_tag(ItemsPicsFromNet, 495)

'''Тэг,возвращающий информацию о "Снек пікантний Pringles Паприка, 165г"'''
get_chips_pringles_paprika_165gr = tag.create_tag(ItemsPicsFromNet, 496)

'''Тэг,возвращающий информацию о "Снек пікантний Pringles Піца пепероні, 185г"'''
get_chips_pringles_pizza_peperoni_185gr = tag.create_tag(ItemsPicsFromNet, 497)

'''Тэг,возвращающий информацию о "Чіпси Pringles сир-цибуля, 165г"'''
get_chips_pringles_sir_cibulya_165gr = tag.create_tag(ItemsPicsFromNet, 498)

'''Тэг,возвращающий информацию о "Чіпси Pringles Оригінал, 165г"'''
get_chips_pringles_original_165gr = tag.create_tag(ItemsPicsFromNet, 499)

'''Тэг,возвращающий информацию о "Чіпси Pringles сир, 165г"'''
get_chips_pringles_sir_165gr = tag.create_tag(ItemsPicsFromNet, 500)

'''Тэг,возвращающий информацию о "Чипси Lay`s картопляні зі смаком паприки, 120г"'''
get_chips_lays_paprika_120gr = tag.create_tag(ItemsPicsFromNet, 501)

'''Тэг,возвращающий информацию о "Чипси Lay`s картопляні зі смаком краба, 120г"'''
get_chips_lays_crab_120gr = tag.create_tag(ItemsPicsFromNet, 502)

'''Тэг,возвращающий информацию о "Чіпси Lay`s картопляні зі смаком сиру, 60г"'''
get_chips_lays_sir_60gr = tag.create_tag(ItemsPicsFromNet, 503)

'''Тэг,возвращающий информацию о "Сир Свет Сыр Фета Українська розсільний 45% в/у"'''
get_sir_svet_feta_ukr_rozsil_45_1kg = tag.create_tag(ItemsPicsFromNet, 504)

'''Тэг,возвращающий информацию о "Оливки Extra! чорні без кісточки, 300г"'''
get_olivki_extra_chorn_bez_kist_300gr = tag.create_tag(ItemsPicsFromNet, 505)

'''Тэг,возвращающий информацию о "Масло оливковое Повна Чаша, 913г"'''
get_oliv_oil_povna_chasha_913gr = tag.create_tag(ItemsPicsFromNet, 506)

'''Тэг,возвращающий информацию о "Базилік Вершки та Корінці червоний свіжий з коренем, 50г"'''
get_basilik_svij = tag.create_tag(ItemsPicsFromNet, 507)

'''Тэг,возвращающий информацию о "Пельмени Геркулес Фирменные , 400г"'''
get_pelmeni_gerkules_firm_400gr = tag.create_tag(ItemsPicsFromNet, 508)

'''Тэг,возвращающий информацию о "Пельмени Геркулес Фирменные , 800г"'''
get_pelmeni_gerkules_firm_800gr = tag.create_tag(ItemsPicsFromNet, 509)

'''Тэг,возвращающий информацию о "Пельмени Геркулес з м'ясом індички , 400г"'''
get_pelmeni_gerkules_indeyka_400gr = tag.create_tag(ItemsPicsFromNet, 510)

'''Тэг,возвращающий информацию о "Пельмени Три Ведмеді Фірмові , 800г"'''
get_pelmeni_tri_vedmid_firm_800gr = tag.create_tag(ItemsPicsFromNet, 511)

'''Тэг,возвращающий информацию о "Пельмени Три ведмеді Мишутка телятина, 400г"'''
get_pelmeni_tri_vedmid_mishutka_telyatina_400gr = tag.create_tag(ItemsPicsFromNet, 512)

'''Тэг,возвращающий информацию о "Пельмени Extra! Фирменные, 800г"'''
get_pelmeni_extra_firm_800gr = tag.create_tag(ItemsPicsFromNet, 513)

'''Тэг,возвращающий информацию о "Пельмени Extra! сибирські, 500г"'''
get_pelmeni_extra_sibir_500gr = tag.create_tag(ItemsPicsFromNet, 514)

'''Тэг,возвращающий информацию о "Равиоли Extra! Домашние, 800г"'''
get_pelmeni_extra_rav_dom_800gr = tag.create_tag(ItemsPicsFromNet, 515)

'''Тэг,возвращающий информацию о "Напиток 7UP безалкогольный, сильногазированный, ж/б, 0,33л"'''
get_7up_033_jb = tag.create_tag(ItemsPicsFromNet, 516)

'''Тэг,возвращающий информацию о "Кавун, кг"'''
get_kavun = tag.create_tag(ItemsPicsFromNet, 517)

'''Тэг,возвращающий информацию о "Напиток Живчик яблоко 2л"'''
get_jivchik_apple_2l = tag.create_tag(ItemsPicsFromNet, 518)

'''Тэг,возвращающий информацию о "Напиток Живчик яблоко 1л"'''
get_jivchik_apple_1l = tag.create_tag(ItemsPicsFromNet, 519)

'''Тэг,возвращающий информацию о "Напиток Живчик яблоко 0.5 л"'''
get_jivchik_apple_05l = tag.create_tag(ItemsPicsFromNet, 520)

'''Тэг,возвращающий информацию о "Напиток Живчик груша 1 л"'''
get_jivchik_grusha_1l = tag.create_tag(ItemsPicsFromNet, 521)

'''Тэг,возвращающий информацию о "Напиток сокосодержащий Живчик Smart Сola, 2л"'''
get_jivchik_smart_cola_2l = tag.create_tag(ItemsPicsFromNet, 522)

'''Тэг,возвращающий информацию о "Напиток Живчик лимон, 2л"'''
get_jivchik_limon_2l = tag.create_tag(ItemsPicsFromNet, 523)






# @register.simple_tag()
# def get_obolon_premium():
#     '''Тэг, возвращающий информацию о пиве "Оболонь Прмиум 1,1 л из БД"'''
#     return ItemsPicsFromNet.objects.get(pk=2)


# ТЕГИ ДЛЯ БЛЮД
'''Тег , возвращающий информацю о борще украинском'''
get_borsh_ukr_info = tag.create_tag(AvailableDishes, 1)

'''Тег , возвращающий информацю о варениках с картошкой'''
get_vareniki_s_kartoshkoy_info = tag.create_tag(AvailableDishes, 2)

'''Тег , возвращающий информацю о варениках с капустой'''
get_vareniki_s_kapustoy_info = tag.create_tag(AvailableDishes, 3)

'''Тег , возвращающий информацю о гречеськом салаті'''
get_grecheskiy_salat_info = tag.create_tag(AvailableDishes, 4)


# ТЕГ ДЛЯ ПРОДУКТОВОГО НАБОРА
class SimpleTagMakerAllItems:
    '''Класс для формирования шаблонных тегов для множества объектов из БД'''

    @register.simple_tag()
    def create_tag(self, data_base: object):
        '''Формирование самой функции для тега'''
        return data_base.objects.all()


mul_tag = SimpleTagMakerAllItems()

'''Возьмем все продукты,что есть в наборе пользователя'''
#get_product_set_from_data_base = mul_tag.create_tag(SetOfProducts)
@register.simple_tag()
def get_product_set_from_data_base():
    '''Возьмем все продукты,что есть в наборе пользователя'''
    return SetOfProducts.objects.all()


# ТЕГ ДЛЯ ДОСУТПА КО ВСЕМ СУПЕРМАРКЕТАМ
'''С помощью этого тега получаем доступ ко всем названиям досутпных супермаркетов'''
get_all_markets = mul_tag.create_tag(RelevantMarkets)
# @register.simple_tag()
# def get_all_markets():
#     '''С помощбю этого тега получаем доступ ко всем названиям досутпных супермаркетов'''
#     return RelevantMarkets.objects.all()


#ТЕГ для доступа ко всем ссылкам на файлы для обучения RNN
@register.simple_tag()
def get_texts_refers_from_DB():
    '''Сбор всех ссылок на текстовые файлы для обучения RNN'''
    return AllTextsStorage.objects.all()



