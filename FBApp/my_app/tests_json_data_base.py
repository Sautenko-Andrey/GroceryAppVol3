from django.test import TestCase
import json
from .parsers import ProductParserVol2

with open('/home/andrey/GroceryApp/FBApp/my_app/prices_store.json') as f:
    store=json.load(f)

class AllProductsPricesTest(TestCase):
    '''Класс для тестирования базы данных "prices_store.json"
    на актуальность цен всех продуктов по всем доступным супермаркетам.
    '''
    parser=ProductParserVol2()

    # with open('/home/andrey/GroceryApp/FBApp/my_app/prices_store.json') as f:
    #     store = json.load(f)

    def verifying_price(self,product:str,parser,atb=None,
                        eko=None,varus=None,silpo=None,
                        ashan=None,novus=None,metro=None,
                        nash_kray=None,fozzy=None):
        print(f'Тестируем {product}.............')
        try:
            atb_price=store[product][atb]
            get_atb_price=parser[0]
            self.assertEquals(atb_price,get_atb_price)
        except Exception:
            print("parser for ATB doesn't exist!!!")
        try:
            eko_price = store[product][eko]
            get_eko_price = parser[1]
            self.assertEquals(eko_price, get_eko_price)
        except Exception:
            print("parser for EKO doesn't exist!!!")
        try:
            varus_price = store[product][varus]
            get_varus_price = parser[2]
            self.assertEquals(varus_price, get_varus_price)
        except Exception:
            print("parser for Varus doesn't exist!!!")
        try:
            silpo_price = store[product][silpo]
            get_silpo_price = parser[3]
            self.assertEquals(silpo_price, get_silpo_price)
        except Exception:
            print("parser for Silpo doesn't exist!!!")
        try:
            ashan_price = store[product][ashan]
            get_ashan_price = parser[4]
            self.assertEquals(ashan_price, get_ashan_price)
        except Exception:
            print("parser for Ashan doesn't exist!!!")
        try:
            novus_price=store[product][novus]
            get_novus_price = parser[5]
            self.assertEquals(novus_price,get_novus_price)
        except Exception:
            print("parser for Novus doesn't exist!!!")
        try:
            metro_price=store[product][metro]
            get_metro_price = parser[6]
            self.assertEquals(metro_price,get_metro_price)
        except Exception:
            print("parser for Metro doesn't exist!!!")
        try:
            nash_kray_price=store[product][nash_kray]
            get_nash_kray_price = parser[7]
            self.assertEquals(nash_kray_price,get_nash_kray_price)
        except Exception:
            print("parser for Наш Край doesn't exist!!!")
        try:
            fozzy_price=store[product][fozzy]
            get_fozzy_price = parser[8]
            self.assertEquals(fozzy_price,get_fozzy_price)
        except Exception:
            print("parser for Fozzy doesn't exist!!!")


    def test_obolon_premium_extra_11l(self):
        self.verifying_price('obolon_premium_1.1_l',self.parser.obolon_premium_parser(),
                             atb='atb',eko='eko',varus='varus')

    def test_vodka_hetman_ice_07(self):
        self.verifying_price('vodka_hetman_ice_07',self.parser.vodka_getman_ICE_parcer(),atb='atb')

    def test_coca_cola_2l(self):
        self.verifying_price('coca_cola_2l',self.parser.coca_cola_2l_parcer(),
                             atb='atb',eko='eko',varus='varus',silpo='silpo',ashan='ashan',
                             novus='novus',metro='metro',nash_kray='nash_kray',fozzy='fozzy')

    def test_garlik(self):
        self.verifying_price('garlik', self.parser.garlik_parcer(),
                             atb='atb',eko='eko',varus='varus',silpo='silpo',
                             novus='novus',nash_kray='nash_kray',fozzy='fozzy')

    def test_tea_minutka(self):
        self.verifying_price('tea_minutka',self.parser.tea_minutka_black_40_b_parcer(),
                             atb='atb',eko='eko',metro='metro')

    def test_apple_golden(self):
        self.verifying_price('apple_golden',self.parser.apple_golden_parcer(),
                             atb='atb',eko='eko',varus='varus',silpo='silpo',
                             metro='metro',nash_kray='nash_kray',fozzy='fozzy')

    def test_sigarets_kent_8(self):
        self.verifying_price('sigarets_kent_8',self.parser.kent_8_parcer(),
                             atb='atb',eko='eko',varus='varus',silpo='silpo',ashan="ashan",
                             novus='novus',fozzy='fozzy')

    def test_coffee_aroma_gold(self):
        self.verifying_price('coffee_aroma_gold',self.parser.coffee_aroma_gold_parcer(),
                             eko='eko',fozzy='fozzy')

    def test_oil_shedriy_dar_raf_850(self):
        self.verifying_price('oil_shedriy_dar_raf_850',self.parser.oil_shedriy_dar_850_parcer(),
                             atb='atb',eko='eko',varus='varus',silpo='silpo',ashan="ashan",
                             novus='novus',metro='metro',fozzy='fozzy')

    def test_fairy_limon_500(self):
        self.verifying_price('fairy_limon_500',self.parser.fairy_limon_500_parcer(),
                             atb='atb',eko='eko',varus='varus',silpo='silpo',
                             novus='novus',metro='metro',fozzy='fozzy')

    def test_onion(self):
        self.verifying_price('onion',self.parser.onion_parcer(),
                             atb='atb',eko='eko',varus='varus',silpo='silpo',
                             novus='novus', metro='metro', nash_kray='nash_kray',fozzy='fozzy')

    def test_apple_black_prince(self):
        self.verifying_price('apple_black_prince',self.parser.apple_black_prince_parcer(),
                             atb='atb',eko='eko',varus='varus',silpo='silpo',
                             metro='metro',fozzy='fozzy')

    def test_smetana_stol_smaky_20(self):
        self.verifying_price('smetana_stol_smaky_20%',self.parser.smetana_stolica_smaky_400_20(),
                             varus='varus')

    def test_limon(self):
        self.verifying_price('limon',self.parser.limon_parcer(),
                             atb='atb',eko='eko',varus='varus',silpo='silpo',
                             novus='novus', metro='metro', nash_kray='nash_kray',fozzy='fozzy')

    def test_oil_oleyna_neraf_850(self):
        self.verifying_price('oil_oleyna_neraf_850',self.parser.oil_oleyna_neraf_850_parcer(),
                             eko='eko',ashan='ashan')

    def test_tea_monomah_kenya_90(self):
        self.verifying_price('tea_monomah_kenya_90',self.parser.tea_monomah_black_kenya_90_parcer(),
                             eko='eko')

    def test_arko_cool_200(self):
        self.verifying_price('arko_cool_200',self.parser.arko_cool_200_bonus100_parcer(),
                             atb='atb',eko='eko',varus='varus',silpo='silpo',ashan="ashan",
                             novus='novus', metro='metro', fozzy='fozzy')

    def test_arko_sensitive_200(self):
        self.verifying_price('arko_sensitive_200',self.parser.arko_sensitive_200_bonus100_parcer(),
                             atb='atb',eko='eko',varus='varus',silpo='silpo',ashan="ashan",
                             novus='novus', metro='metro', nash_kray='nash_kray',fozzy='fozzy')

    def test_carrot(self):
        self.verifying_price('carrot',self.parser.carrot_parcer(),
                             atb='atb',eko='eko',varus='varus',silpo='silpo',
                             novus='novus',metro='metro', nash_kray='nash_kray',fozzy='fozzy')

    def test_cabbage(self):
        self.verifying_price('cabbage',self.parser.cabbage_parcer(),
                             atb='atb',eko='eko',varus='varus',silpo='silpo',
                             novus='novus',metro='metro', nash_kray='nash_kray',fozzy='fozzy')

    def test_eggs(self):
        self.verifying_price('eggs',self.parser.egg_parcer(),
                             atb='atb',eko='eko',varus='varus',silpo='silpo',ashan="ashan",
                             novus='novus',metro='metro', nash_kray='nash_kray',fozzy='fozzy')

    def test_mayonez_detsk_shedro_67(self):
        self.verifying_price('mayonez_detsk_shedro_67%',self.parser.mayonez_detsk_shedro_67_parcer(),
                             atb='atb',eko='eko',varus='varus',silpo='silpo',
                             metro='metro',fozzy='fozzy')

    def test_rexona_aloe_vera(self):
        self.verifying_price('rexona_aloe_vera',self.parser.rexona_aloe_vera_w_parcer(),
                             eko='eko',ashan="ashan")

    def test_marlboro_red(self):
        self.verifying_price('marlboro_red',self.parser.marloboro_red_parcer(),
                             atb='atb',eko='eko',varus='varus',silpo='silpo',ashan='ashan',
                             novus='novus',fozzy='fozzy')

    def test_beer_lvivske_svetl_2_4_l(self):
        self.verifying_price('beer_lvivske_svetl_2.4 l',self.parser.beer_lvivske_svitle_24l(),
                             varus='varus',silpo='silpo',ashan="ashan",fozzy='fozzy')

    def test_smetana_stol_smaky_15(self):
        self.verifying_price('smetana_stol_smaky_15%',self.parser.smetana_stolica_smaky_400_15_parcer(),
                             varus='varus')

    def test_water_in_bottle_6l(self):
        self.verifying_price('water_in_bottle_6l',self.parser.water_in_6l_bottle_parser(),
                             atb='atb',eko='eko',varus='varus',
                             novus='novus', nash_kray='nash_kray',fozzy='fozzy')

    def test_pork_lopatka(self):
        self.verifying_price('pork_lopatka',self.parser.pork_lopatka_parser(),
                             atb='atb',eko='eko',varus='varus',
                             novus='novus',metro='metro',fozzy='fozzy')

    def test_potato(self):
        self.verifying_price('potato',self.parser.potato_parser(),
                             atb='atb',eko='eko',varus='varus',
                             novus='novus',metro='metro',fozzy='fozzy')

    def test_beet(self):
        self.verifying_price('beet',self.parser.beet_parser(),
                             atb='atb',eko='eko',varus='varus',silpo='silpo',
                             novus='novus',metro='metro',fozzy='fozzy')

    def test_four(self):
        self.verifying_price('four',self.parser.four_parser(),
                             atb='atb',eko='eko',varus='varus',
                             novus='novus',metro='metro',nash_kray='nash_kray',fozzy='fozzy')

    def test_oil_for_dish(self):
        self.verifying_price('oil_for_dish', self.parser.oil_for_dishes_parser(),
                             atb='atb', eko='eko', varus='varus',
                             novus='novus',metro='metro',nash_kray='nash_kray',fozzy='fozzy')

    def test_smetana_for_dish(self):
        self.verifying_price('smetana_for_dish',self.parser.sour_cream_for_dishes_parser(),
                             atb='atb', eko='eko', varus='varus',
                             novus='novus',metro='metro',fozzy='fozzy')

    def test_desodorant_garnier_man(self):
        self.verifying_price('desodorant_garnier_man',self.parser.desodorant_garnier_magniy_man_parser(),
                             silpo='silpo',fozzy='fozzy')

    def test_cofee_aroma_gold_freeze_dried_70g(self):
        self.verifying_price('cofee_aroma_gold_freeze_dried_70g',self.parser.coffee_aroma_gold_freeze_dried_70g_parser(),
                             eko='eko',silpo='silpo',nash_kray='nash_kray')

    def test_gorchica_veres_ukrainska_micna_120g(self):
        self.verifying_price('gorchica_veres_ukrainska_micna_120g',self.parser.gorchica_veres_ukrainska_micna_120g_parser(),
                             silpo='silpo',novus='novus',metro='metro')

    def test_sir_plavlenniy_komo_paprikash(self):
        self.verifying_price('sir_plavlenniy_komo_paprikash',self.parser.sir_plavlenniy_komo_paprikash_parser(),
                             novus='novus',metro='metro',nash_kray='nash_kray',fozzy='fozzy')

    def test_apple_gala(self):
        self.verifying_price('apple_gala',self.parser.apple_gala_parser(),
                             atb='atb',eko='eko',varus='varus',silpo='silpo',
                             novus='novus', metro='metro', fozzy='fozzy')

    def test_smetana_galichanska_15_370gr(self):
        self.verifying_price('smetana_galichanska_15_370gr',self.parser.smetana_galichanska_15_370g_parser(),
                             atb='atb',eko='eko',novus='novus', metro='metro', fozzy='fozzy')

    def test_desodorant_garnier_spring_spirit(self):
        self.verifying_price('desodorant_garnier_spring_spirit',self.parser.desodorant_garnier_spring_spirit_parser(),
                             silpo='silpo',novus='novus', metro='metro', fozzy='fozzy')

    def test_chips_lays_with_salt_big_pack(self):
        self.verifying_price('chips_lays_with_salt_big_pack',self.parser.chips_lays_with_salt_parser(),
                             eko='eko',fozzy='fozzy')

    def test_sprite_2l(self):
        self.verifying_price('sprite_2l', self.parser.sprite_2l_parser(),
                             eko='eko', varus='varus', silpo='silpo', ashan='ashan',
                             novus='novus', metro='metro', nash_kray='nash_kray', fozzy='fozzy')

    def test_fanta_2l(self):
        self.verifying_price('fanta_2l', self.parser.fanta_2l_parser(),
                             eko='eko', varus='varus', silpo='silpo', ashan='ashan',
                             novus='novus', metro='metro', nash_kray='nash_kray', fozzy='fozzy')


