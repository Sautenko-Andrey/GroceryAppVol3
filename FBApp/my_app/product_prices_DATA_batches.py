import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FBApp.settings")

import django

django.setup()

import json
import pandas as pd
from parsers import ProductParserVol2

#вспомагательные коэффициенты, благодаря которым корректируется цена продукта
water_var = 0.033
oliv_var = 0.27
addition_ingredients = 5
double_price = 2
half_price = 0.5
ten_percent_price = 0.1
fifteen_percent_price = 0.15
twenty_percent_price = 0.2
twenty_five_percent_price = 0.25
fourty_percent_rate = 0.4
sixty_percent_price = 0.6
six_percent_price = 0.06
ninety_percent_price = 0.9
five_percent_price = 0.05
three_percent_price = 0.03
eighty_percent_price = 0.8
mul_price_by_10 = 10
devide_by_3 = 3
devide_by_4 = 4
devide_by_5 = 5
devide_by_6 = 6
rate_3 = 3

# в каждом батче по 100 продуктов
batch_1_path = "../prices_store_batch_1.json"
batch_2_path = "../prices_store_batch_2.json"
batch_3_path = "../prices_store_batch_3.json"
batch_4_path = "../prices_store_batch_4.json"
batch_5_path = "../prices_store_batch_5.json"
batch_6_path = "../prices_store_batch_6.json"
batch_7_path = "../prices_store_batch_7.json"
batch_8_path = "../prices_store_batch_8.json"

parser = ProductParserVol2()

def write_prices_to_json(batch: list, json_data: str, mode: str):
    '''Функция записи цен в json для batch '''
    to_json = dict()
    for item in batch:
        for product, values in item.items():
            to_json[product] = values

    if mode == "w":
        with open(json_data, 'w') as f:
            json.dump(to_json, f, sort_keys=False, indent=len(batch))
            print(f'Все продукты и их цены добавлены в базу данных (batch {batch})!')
    elif mode == "a":
        with open(json_data, 'a') as f:
            json.dump(to_json, f, sort_keys=False, indent=len(batch))
            print(f'Все продукты и их цены добавлены в базу данных (batch {batch})!')


# функция парсинга цен для разных батчей
def price_parcing(batch_name: str):
    if type(batch_name) != str:
        raise AttributeError("Input data types are inopropriate!")

    # названия батчей
    batch_name_1 = "all_products_names_batch_1"
    batch_name_2 = "all_products_names_batch_2"
    batch_name_3 = "all_products_names_batch_3"
    batch_name_4 = "all_products_names_batch_4"
    batch_name_5 = "all_products_names_batch_5"
    batch_name_6 = "all_products_names_batch_6"
    batch_name_7 = "all_products_names_batch_7"
    batch_name_8 = "all_products_names_batch_8"

    mode_type_first_write = "w"

    # для первого батча
    if batch_name == batch_name_1:
        all_products_names_batch_1 = [
            {'obolon_premium_1.1_l': {
                "atb": parser.obolon_premium_parser()[0],
                "eko": parser.obolon_premium_parser()[1]
            }},
            {'vodka_hetman_ice_07': {
                "atb": parser.vodka_getman_ICE_parcer()[0]
            }},
            {'coca_cola_2l': {
                "atb": parser.coca_cola_2l_parcer()[0],
                "eko": parser.coca_cola_2l_parcer()[1],
                "varus": parser.coca_cola_2l_parcer()[2],
                "silpo": parser.coca_cola_2l_parcer()[3],
                "ashan": parser.coca_cola_2l_parcer()[4],
                "novus": parser.coca_cola_2l_parcer()[5],
                "metro": parser.coca_cola_2l_parcer()[6],
                "nash_kray": parser.coca_cola_2l_parcer()[7],
                "fozzy": parser.coca_cola_2l_parcer()[8]
            }},
            {'garlik': {
                "atb": parser.garlik_parcer()[0],
                "eko": parser.garlik_parcer()[1],
                "varus": parser.garlik_parcer()[2],
                "silpo": parser.garlik_parcer()[3] * mul_price_by_10,
                "novus": parser.garlik_parcer()[5],
                "nash_kray": parser.garlik_parcer()[7] * mul_price_by_10,
                "fozzy": parser.garlik_parcer()[8]
            }},
            {'tea_minutka': {
                "atb": parser.tea_minutka_black_40_b_parcer()[0],
                "eko": parser.tea_minutka_black_40_b_parcer()[1],
                "metro": parser.tea_minutka_black_40_b_parcer()[6]
            }},
            {'apple_golden': {
                "atb": parser.apple_golden_parcer()[0],
                "eko": parser.apple_golden_parcer()[1],
                "varus": parser.apple_golden_parcer()[2],
                "silpo": parser.apple_golden_parcer()[3] * mul_price_by_10,
                "metro": parser.apple_golden_parcer()[6],
                "nash_kray": parser.apple_golden_parcer()[7],
                "fozzy": parser.apple_golden_parcer()[8]
            }},
            {'sigarets_kent_8': {
                "atb": parser.kent_8_parcer()[0],
                "eko": parser.kent_8_parcer()[1],
                "varus": parser.kent_8_parcer()[2],
                "silpo": parser.kent_8_parcer()[3],
                "ashan": parser.kent_8_parcer()[4],
                "novus": parser.kent_8_parcer()[5],
                "fozzy": parser.kent_8_parcer()[8]
            }},
            {'coffee_aroma_gold': {
                "eko": parser.coffee_aroma_gold_parcer()[1],
                "fozzy": parser.coffee_aroma_gold_parcer()[8]
            }},
            {'oil_shedriy_dar_raf_850': {
                "atb": parser.oil_shedriy_dar_850_parcer()[0],
                "eko": parser.oil_shedriy_dar_850_parcer()[1],
                "varus": parser.oil_shedriy_dar_850_parcer()[2],
                "silpo": parser.oil_shedriy_dar_850_parcer()[3],
                "ashan": parser.oil_shedriy_dar_850_parcer()[4],
                "novus": parser.oil_shedriy_dar_850_parcer()[5],
                "metro": parser.oil_shedriy_dar_850_parcer()[6],
                "fozzy": parser.oil_shedriy_dar_850_parcer()[8]
            }},
            {'fairy_limon_500': {
                "atb": parser.fairy_limon_500_parcer()[0],
                "eko": parser.fairy_limon_500_parcer()[1],
                "varus": parser.fairy_limon_500_parcer()[2],
                "silpo": parser.fairy_limon_500_parcer()[3],
                "novus": parser.fairy_limon_500_parcer()[5],
                "metro": parser.fairy_limon_500_parcer()[6],
                "fozzy": parser.fairy_limon_500_parcer()[8]
            }},
            {'onion': {
                "atb": parser.onion_parcer()[0],
                "eko": parser.onion_parcer()[1],
                "varus": parser.onion_parcer()[2],
                "silpo": parser.onion_parcer()[3] * mul_price_by_10,
                "novus": parser.onion_parcer()[5],
                "metro": parser.onion_parcer()[6],
                "nash_kray": parser.onion_parcer()[7],
                "fozzy": parser.onion_parcer()[8]
            }},
            {'apple_black_prince': {
                "atb": parser.apple_black_prince_parcer()[0],
                "eko": parser.apple_black_prince_parcer()[1],
                "varus": parser.apple_black_prince_parcer()[2],
                "silpo": parser.apple_black_prince_parcer()[3] * mul_price_by_10,
                "metro": parser.apple_black_prince_parcer()[6],
                "fozzy": parser.apple_black_prince_parcer()[8]
            }},
            {'smetana_stol_smaky_20%': {
                "varus": parser.smetana_stolica_smaky_400_20()[2]
            }},
            {'limon': {
                "atb": parser.limon_parcer()[0],
                "eko": parser.limon_parcer()[1],
                "varus": parser.limon_parcer()[2],
                "silpo": parser.limon_parcer()[3] * mul_price_by_10,
                "novus": parser.limon_parcer()[5],
                "metro": parser.limon_parcer()[6],
                "nash_kray": parser.limon_parcer()[7],
                "fozzy": parser.limon_parcer()[8]
            }},
            {'oil_oleyna_neraf_850': {
                "eko": parser.oil_oleyna_neraf_850_parcer()[1],
                "ashan": parser.oil_oleyna_neraf_850_parcer()[4]
            }},
            {'tea_monomah_kenya_90': {
                "eko": parser.tea_monomah_black_kenya_90_parcer()[1]
            }},
            {'arko_cool_200': {
                "atb": parser.arko_cool_200_bonus100_parcer()[0],
                "eko": parser.arko_cool_200_bonus100_parcer()[1],
                "varus": parser.arko_cool_200_bonus100_parcer()[2],
                "silpo": parser.arko_cool_200_bonus100_parcer()[3],
                "ashan": parser.arko_cool_200_bonus100_parcer()[4],
                "novus": parser.arko_cool_200_bonus100_parcer()[5],
                "metro": parser.arko_cool_200_bonus100_parcer()[6],
                "fozzy": parser.arko_cool_200_bonus100_parcer()[8]
            }},
            {'arko_sensitive_200': {
                "atb": parser.arko_sensitive_200_bonus100_parcer()[0],
                "eko": parser.arko_sensitive_200_bonus100_parcer()[1],
                "varus": parser.arko_sensitive_200_bonus100_parcer()[2],
                "silpo": parser.arko_sensitive_200_bonus100_parcer()[3],
                "ashan": parser.arko_sensitive_200_bonus100_parcer()[4],
                "novus": parser.arko_sensitive_200_bonus100_parcer()[5],
                "metro": parser.arko_sensitive_200_bonus100_parcer()[6],
                "nash_kray": parser.arko_sensitive_200_bonus100_parcer()[7],
                "fozzy": parser.arko_sensitive_200_bonus100_parcer()[8]
            }},
            {'carrot': {
                "atb": parser.carrot_parcer()[0],
                "eko": parser.carrot_parcer()[1],
                "varus": parser.carrot_parcer()[2],
                "silpo": parser.carrot_parcer()[3] * mul_price_by_10,
                "novus": parser.carrot_parcer()[5],
                "metro": parser.carrot_parcer()[6],
                "nash_kray": parser.carrot_parcer()[7],
                "fozzy": parser.carrot_parcer()[8]
            }},
            {'cabbage': {
                "atb": parser.cabbage_parcer()[0],
                "eko": parser.cabbage_parcer()[1],
                "varus": parser.cabbage_parcer()[2],
                "silpo": parser.cabbage_parcer()[3] * mul_price_by_10,
                "novus": parser.cabbage_parcer()[5],
                "metro": parser.cabbage_parcer()[6],
                "nash_kray": parser.cabbage_parcer()[7],
                "fozzy": parser.cabbage_parcer()[8]
            }},
            {'eggs': {
                "atb": parser.egg_parcer()[0],
                "eko": parser.egg_parcer()[1] * mul_price_by_10,
                "varus": parser.egg_parcer()[2] * mul_price_by_10,
                "silpo": parser.egg_parcer()[3],
                "ashan": parser.egg_parcer()[4],
                "novus": parser.egg_parcer()[5],
                "metro": parser.egg_parcer()[6],
                "nash_kray": parser.egg_parcer()[7],
                "fozzy": parser.egg_parcer()[8] * mul_price_by_10
            }},
            {'mayonez_detsk_shedro_67%': {
                "atb": parser.mayonez_detsk_shedro_67_parcer()[0],
                "eko": parser.mayonez_detsk_shedro_67_parcer()[1],
                "varus": parser.mayonez_detsk_shedro_67_parcer()[2],
                "silpo": parser.mayonez_detsk_shedro_67_parcer()[3],
                "metro": parser.mayonez_detsk_shedro_67_parcer()[6],
                "fozzy": parser.mayonez_detsk_shedro_67_parcer()[8]
            }},
            {'rexona_aloe_vera': {
                "eko": parser.rexona_aloe_vera_w_parcer()[1],
                "ashan": parser.rexona_aloe_vera_w_parcer()[4]
            }},
            {'marlboro_red': {
                "atb": parser.marloboro_red_parcer()[0],
                "eko": parser.marloboro_red_parcer()[1],
                "varus": parser.marloboro_red_parcer()[2],
                "silpo": parser.marloboro_red_parcer()[3],
                "ashan": parser.marloboro_red_parcer()[4],
                "novus": parser.marloboro_red_parcer()[5],
                "fozzy": parser.marloboro_red_parcer()[8]
            }},
            {'beer_lvivske_svetl_2.4 l': {
                "varus": parser.beer_lvivske_svitle_24l()[2],
                "silpo": parser.beer_lvivske_svitle_24l()[3],
                "ashan": parser.beer_lvivske_svitle_24l()[4],
                "fozzy": parser.beer_lvivske_svitle_24l()[8]
            }},
            {'smetana_stol_smaky_15%': {
                "varus": parser.smetana_stolica_smaky_400_15_parcer()[2]
            }},
            {'water_in_bottle_6l': {
                "atb": parser.water_in_6l_bottle_parser()[0],
                "eko": parser.water_in_6l_bottle_parser()[1],
                "varus": parser.water_in_6l_bottle_parser()[2],
                "silpo": parser.water_in_6l_bottle_parser()[3],
                "ashan": parser.water_in_6l_bottle_parser()[4],
                "novus": parser.water_in_6l_bottle_parser()[5],
                "metro": parser.water_in_6l_bottle_parser()[6],
                "nash_kray": parser.water_in_6l_bottle_parser()[7],
                "fozzy": parser.water_in_6l_bottle_parser()[8]
            }},
            {'pork_lopatka': {
                "atb": parser.pork_lopatka_parser()[0],
                "eko": parser.pork_lopatka_parser()[1],
                "varus": parser.pork_lopatka_parser()[2],
                "silpo": parser.pork_lopatka_parser()[3] * mul_price_by_10,
                "novus": parser.pork_lopatka_parser()[5],
                "metro": parser.pork_lopatka_parser()[6],
                "nash_kray": parser.pork_lopatka_parser()[7] * mul_price_by_10,
                "fozzy": parser.pork_lopatka_parser()[8]
            }},
            {'potato': {
                "atb": parser.potato_parser()[0],
                "eko": parser.potato_parser()[1],
                "varus": parser.potato_parser()[2],
                "silpo": parser.pork_lopatka_parser()[3],
                "novus": parser.potato_parser()[5],
                "metro": parser.potato_parser()[6],
                "fozzy": parser.potato_parser()[8]
            }},
            {'beet': {
                "atb": parser.beet_parser()[0],
                "eko": parser.beet_parser()[1],
                "varus": parser.beet_parser()[2],
                "silpo": parser.beet_parser()[3] * mul_price_by_10,
                "novus": parser.beet_parser()[5],
                "metro": parser.beet_parser()[6],
                "fozzy": parser.beet_parser()[8]
            }},
            {'four': {
                "atb": parser.four_parser()[0],
                "eko": parser.four_parser()[1],
                "varus": parser.four_parser()[2],
                "silpo": parser.four_parser()[3],
                "novus": parser.four_parser()[5],
                "metro": parser.four_parser()[6],
                "nash_kray": parser.four_parser()[7],
                "fozzy": parser.four_parser()[8]
            }},
            {'oil_for_dish': {
                "atb": parser.oil_for_dishes_parser()[0],
                "eko": parser.oil_for_dishes_parser()[1],
                "varus": parser.oil_for_dishes_parser()[2],
                "novus": parser.oil_for_dishes_parser()[5],
                "metro": parser.oil_for_dishes_parser()[6],
                "nash_kray": parser.oil_for_dishes_parser()[7],
                "fozzy": parser.oil_for_dishes_parser()[8]
            }},
            {'smetana_for_dish': {
                "atb": parser.sour_cream_for_dishes_parser()[0],
                "eko": parser.sour_cream_for_dishes_parser()[1],
                "varus": parser.sour_cream_for_dishes_parser()[2],
                "silpo": parser.sour_cream_for_dishes_parser()[3],
                "novus": parser.sour_cream_for_dishes_parser()[5],
                "metro": parser.sour_cream_for_dishes_parser()[6],
                "fozzy": parser.sour_cream_for_dishes_parser()[8]
            }},
            {'desodorant_garnier_man': {
                "silpo": parser.desodorant_garnier_magniy_man_parser()[3],
                "fozzy": parser.sour_cream_for_dishes_parser()[8]
            }},
            {'cofee_aroma_gold_freeze_dried_70g': {
                "eko": parser.coffee_aroma_gold_freeze_dried_70g_parser()[1],
                "silpo": parser.coffee_aroma_gold_freeze_dried_70g_parser()[3],
                "nash_kray": parser.coffee_aroma_gold_freeze_dried_70g_parser()[7],
            }},
            {'gorchica_veres_ukrainska_micna_120g': {
                "silpo": parser.gorchica_veres_ukrainska_micna_120g_parser()[3],
                "novus": parser.gorchica_veres_ukrainska_micna_120g_parser()[5],
                "metro": parser.gorchica_veres_ukrainska_micna_120g_parser()[6],
            }},
            {'sir_plavlenniy_komo_paprikash': {
                "novus": parser.sir_plavlenniy_komo_paprikash_parser()[5],
                "metro": parser.sir_plavlenniy_komo_paprikash_parser()[6],
                "nash_kray": parser.sir_plavlenniy_komo_paprikash_parser()[7],
                "fozzy": parser.sir_plavlenniy_komo_paprikash_parser()[8]
            }},
            {'apple_gala': {
                "atb": parser.apple_gala_parser()[0],
                "eko": parser.apple_gala_parser()[1],
                "varus": parser.apple_gala_parser()[2],
                "silpo": parser.apple_gala_parser()[3],
                "novus": parser.apple_gala_parser()[5],
                "metro": parser.apple_gala_parser()[6],
                "fozzy": parser.apple_gala_parser()[8]
            }},
            {'smetana_galichanska_15_370gr': {
                "atb": parser.smetana_galichanska_15_370g_parser()[0],
                "eko": parser.smetana_galichanska_15_370g_parser()[1],
                "novus": parser.smetana_galichanska_15_370g_parser()[5],
                "metro": parser.smetana_galichanska_15_370g_parser()[6],
                "fozzy": parser.smetana_galichanska_15_370g_parser()[8]
            }},
            {'desodorant_garnier_spring_spirit': {
                "silpo": parser.desodorant_garnier_spring_spirit_parser()[3],
                "novus": parser.desodorant_garnier_spring_spirit_parser()[5],
                "metro": parser.desodorant_garnier_spring_spirit_parser()[6],
                "fozzy": parser.desodorant_garnier_spring_spirit_parser()[8]
            }},
            {'chips_lays_with_salt_big_pack': {
                "eko": parser.chips_lays_with_salt_parser()[1],
                "fozzy": parser.chips_lays_with_salt_parser()[8]
            }},
            {'sprite_2l': {
                "eko": parser.sprite_2l_parser()[1],
                "varus": parser.sprite_2l_parser()[2],
                "silpo": parser.sprite_2l_parser()[3],
                "ashan": parser.sprite_2l_parser()[4],
                "novus": parser.sprite_2l_parser()[5],
                "metro": parser.sprite_2l_parser()[6],
                "nash_kray": parser.sprite_2l_parser()[7],
                "fozzy": parser.sprite_2l_parser()[8]
            }},
            {'fanta_2l': {
                "eko": parser.fanta_2l_parser()[1],
                "varus": parser.fanta_2l_parser()[2],
                "silpo": parser.fanta_2l_parser()[3],
                "ashan": parser.fanta_2l_parser()[4],
                "novus": parser.fanta_2l_parser()[5],
                "metro": parser.fanta_2l_parser()[6],
                "nash_kray": parser.fanta_2l_parser()[7],
                "fozzy": parser.fanta_2l_parser()[8]
            }},
            {'bond_street_blue_selection': {
                "atb": parser.bond_street_blue_selection_parser()[0],
                "eko": parser.bond_street_blue_selection_parser()[1],
                "varus": parser.bond_street_blue_selection_parser()[2],
                "silpo": parser.bond_street_blue_selection_parser()[3],
                "ashan": parser.bond_street_blue_selection_parser()[4],
                "novus": parser.bond_street_blue_selection_parser()[5],
                "fozzy": parser.bond_street_blue_selection_parser()[8]
            }},
            {'camel_blue': {
                "atb": parser.camel_blue_parser()[0],
                "eko": parser.camel_blue_parser()[1],
                "varus": parser.camel_blue_parser()[2],
                "silpo": parser.camel_blue_parser()[3],
                "ashan": parser.camel_blue_parser()[4],
                "novus": parser.camel_blue_parser()[5],
                "fozzy": parser.camel_blue_parser()[8]
            }},
            {'ld_red': {
                "atb": parser.camel_blue_parser()[0],
                "eko": parser.camel_blue_parser()[1],
                "silpo": parser.camel_blue_parser()[3],
                "fozzy": parser.camel_blue_parser()[8]
            }},
            {'marlboro_gold': {
                "atb": parser.marlboro_gold_parser()[0],
                "eko": parser.marlboro_gold_parser()[1],
                "varus": parser.marlboro_gold_parser()[2],
                "silpo": parser.marlboro_gold_parser()[3],
                "ashan": parser.marlboro_gold_parser()[4],
                "novus": parser.marlboro_gold_parser()[5],
                "fozzy": parser.marlboro_gold_parser()[8]
            }},
            {'rothmans_demi_blue_exclusive': {
                "atb": parser.rothmans_demi_blue_exclusive_parser()[0],
                "eko": parser.rothmans_demi_blue_exclusive_parser()[1],
                "varus": parser.rothmans_demi_blue_exclusive_parser()[2],
                "silpo": parser.rothmans_demi_blue_exclusive_parser()[3],
                "ashan": parser.rothmans_demi_blue_exclusive_parser()[4],
                "novus": parser.rothmans_demi_blue_exclusive_parser()[5]
            }},
            {'rothmans_demi_click_purple': {
                "atb": parser.rothmans_demi_click_purple_parser()[0],
                "eko": parser.rothmans_demi_click_purple_parser()[1],
                "ashan": parser.rothmans_demi_click_purple_parser()[4]
            }},
            {'rothmans_demi_click_purple': {
                "atb": parser.rothmans_demi_click_purple_parser()[0],
                "eko": parser.rothmans_demi_click_purple_parser()[1],
                "ashan": parser.rothmans_demi_click_purple_parser()[4]
            }},
            {'winston_caster': {
                "atb": parser.winston_caster_parser()[0]
            }},
            {'parlament_aqua_blue': {
                "atb": parser.parlament_aqua_blue_parser()[0],
                "eko": parser.parlament_aqua_blue_parser()[1],
                "varus": parser.parlament_aqua_blue_parser()[2],
                "silpo": parser.parlament_aqua_blue_parser()[3],
                "ashan": parser.parlament_aqua_blue_parser()[4],
                "novus": parser.parlament_aqua_blue_parser()[5],
                "fozzy": parser.parlament_aqua_blue_parser()[8]
            }},
            {'winston_blue': {
                "atb": parser.winston_blue_parser()[0],
                "eko": parser.winston_blue_parser()[1],
                "varus": parser.winston_blue_parser()[2],
                "silpo": parser.winston_blue_parser()[3],
                "ashan": parser.winston_blue_parser()[4],
                "novus": parser.winston_blue_parser()[5],
                "fozzy": parser.winston_blue_parser()[8]
            }},
            {'bond_street_red_selection': {
                "atb": parser.bond_street_red_selection_parser()[0],
                "varus": parser.bond_street_red_selection_parser()[2],
                "silpo": parser.bond_street_red_selection_parser()[3],
                "ashan": parser.bond_street_red_selection_parser()[4],
            }},
            {'ld_blue': {
                "atb": parser.ld_blue_parser()[0],
                "silpo": parser.ld_blue_parser()[3],
                "fozzy": parser.ld_blue_parser()[8]
            }},
            {'kent_silver': {
                "atb": parser.kent_silver_parser()[0],
                "eko": parser.kent_silver_parser()[1],
                "varus": parser.kent_silver_parser()[2],
                "ashan": parser.kent_silver_parser()[4],
                "novus": parser.kent_silver_parser()[5],
                "fozzy": parser.kent_silver_parser()[8]
            }},
            {'kent_navy_blue': {
                "atb": parser.kent_navy_blue_new_parser()[0],
                "eko": parser.kent_navy_blue_new_parser()[1],
                "varus": parser.kent_navy_blue_new_parser()[2],
                "silpo": parser.kent_navy_blue_new_parser()[3],
                "ashan": parser.kent_navy_blue_new_parser()[4],
                "novus": parser.kent_navy_blue_new_parser()[5],
                "fozzy": parser.kent_navy_blue_new_parser()[8]
            }},
            {'beer_chernigivske_svitle_05_l_glass': {
                "atb": parser.beer_chernigivske_svitle_05_l_glass_parser()[0],
                "silpo": parser.beer_chernigivske_svitle_05_l_glass_parser()[3],
                "ashan": parser.beer_chernigivske_svitle_05_l_glass_parser()[4],
                "novus": parser.beer_chernigivske_svitle_05_l_glass_parser()[5],
                "metro": parser.beer_chernigivske_svitle_05_l_glass_parser()[6],
                "nash_kray": parser.beer_chernigivske_svitle_05_l_glass_parser()[7],
                "fozzy": parser.beer_chernigivske_svitle_05_l_glass_parser()[8]
            }},
            {'beer_stella_artois_05_l_glass': {
                "atb": parser.beer_chernigivske_svitle_05_l_glass_parser()[0],
                "silpo": parser.beer_chernigivske_svitle_05_l_glass_parser()[3],
                "ashan": parser.beer_chernigivske_svitle_05_l_glass_parser()[4],
                "novus": parser.beer_chernigivske_svitle_05_l_glass_parser()[5],
                "metro": parser.beer_chernigivske_svitle_05_l_glass_parser()[6],
                "fozzy": parser.beer_chernigivske_svitle_05_l_glass_parser()[8]
            }},

            {'beer_obolon_svitle_05_l_glass': {
                "atb": parser.beer_obolon_svitle_05_l_glass_parser()[0],
                "eko": parser.beer_obolon_svitle_05_l_glass_parser()[1],
                "varus": parser.beer_obolon_svitle_05_l_glass_parser()[2],
                "novus": parser.beer_obolon_svitle_05_l_glass_parser()[5],
                "metro": parser.beer_obolon_svitle_05_l_glass_parser()[6],
                "nash_kray": parser.beer_obolon_svitle_05_l_glass_parser()[7],
                "fozzy": parser.beer_obolon_svitle_05_l_glass_parser()[8]
            }},
            {'beer_jugulivske_svitle_05_l_glass': {
                "atb": parser.beer_jugulivske_svitle_05_l_glass_parser()[0],
                "eko": parser.beer_jugulivske_svitle_05_l_glass_parser()[1],
                "varus": parser.beer_jugulivske_svitle_05_l_glass_parser()[2],
                "novus": parser.beer_jugulivske_svitle_05_l_glass_parser()[5],
                "metro": parser.beer_jugulivske_svitle_05_l_glass_parser()[6],
                "fozzy": parser.beer_jugulivske_svitle_05_l_glass_parser()[8]
            }},
            {'beer_rogan_tradicionnoe_svitle_05_l_glass': {
                "atb": parser.beer_rogan_tradicionnoe_svitle_05_l_glass_parser()[0],
                "silpo": parser.beer_rogan_tradicionnoe_svitle_05_l_glass_parser()[3],
                "novus": parser.beer_rogan_tradicionnoe_svitle_05_l_glass_parser()[5],
                "metro": parser.beer_rogan_tradicionnoe_svitle_05_l_glass_parser()[6],
                "nash_kray": parser.beer_rogan_tradicionnoe_svitle_05_l_glass_parser()[7],
                "fozzy": parser.beer_rogan_tradicionnoe_svitle_05_l_glass_parser()[8]
            }},
            {'beer_corona_extra_svitle_033_l_glass': {
                "atb": parser.beer_corona_extra_svitle_033_l_glass_parser()[0],
                "eko": parser.beer_corona_extra_svitle_033_l_glass_parser()[1],
                "varus": parser.beer_corona_extra_svitle_033_l_glass_parser()[2],
                "silpo": parser.beer_corona_extra_svitle_033_l_glass_parser()[3],
                "ashan": parser.beer_corona_extra_svitle_033_l_glass_parser()[4],
                "novus": parser.beer_corona_extra_svitle_033_l_glass_parser()[5],
                "metro": parser.beer_corona_extra_svitle_033_l_glass_parser()[6],
                "fozzy": parser.beer_corona_extra_svitle_033_l_glass_parser()[8]
            }},
            {'beer_chernigibske_bile_nefilter_05_l_glass': {
                "atb": parser.beer_chernigibske_bile_nefilter_05_l_glass_parser()[0],
                "silpo": parser.beer_chernigibske_bile_nefilter_05_l_glass_parser()[3],
                "novus": parser.beer_chernigibske_bile_nefilter_05_l_glass_parser()[5],
                "metro": parser.beer_chernigibske_bile_nefilter_05_l_glass_parser()[6],
                "nash_kray": parser.beer_chernigibske_bile_nefilter_05_l_glass_parser()[7],
                "fozzy": parser.beer_chernigibske_bile_nefilter_05_l_glass_parser()[8]
            }},
            {'beer_yantar_svitle_05_l_glass': {
                "atb": parser.beer_yantar_svitle_05_l_glass_parser()[0],
                "ashan": parser.beer_yantar_svitle_05_l_glass_parser()[4],
                "metro": parser.beer_yantar_svitle_05_l_glass_parser()[6],
                "fozzy": parser.beer_yantar_svitle_05_l_glass_parser()[8]
            }},
            {'beer_zlata_praha_svitle_05_l_glass': {
                "eko": parser.beer_zlata_praha_svitle_05_l_glass_parser()[1],
                "varus": parser.beer_zlata_praha_svitle_05_l_glass_parser()[2],
                "silpo": parser.beer_zlata_praha_svitle_05_l_glass_parser()[3],
                "novus": parser.beer_zlata_praha_svitle_05_l_glass_parser()[5],
                "fozzy": parser.beer_zlata_praha_svitle_05_l_glass_parser()[8]
            }},
            {'beer_zibert_svitle_05_l_glass': {
                "atb": parser.beer_zibert_svitle_05_l_glass_parser()[0],
                "eko": parser.beer_zibert_svitle_05_l_glass_parser()[1],
                "varus": parser.beer_zibert_svitle_05_l_glass_parser()[2],
                "novus": parser.beer_zibert_svitle_05_l_glass_parser()[5],
                "fozzy": parser.beer_zibert_svitle_05_l_glass_parser()[8]
            }},
            {'beer_arsenal_micne_05_l_glass': {
                "novus": parser.beer_arsenal_micne_05_l_glass_parser()[5],
                "metro": parser.beer_arsenal_micne_05_l_glass_parser()[6],
                "nash_kray": parser.beer_arsenal_micne_05_l_glass_parser()[7],
                "fozzy": parser.beer_arsenal_micne_05_l_glass_parser()[8]
            }},
            {'beer_persha_brovarna_zakarpatske_svitle_05_l_glass': {
                "eko": parser.beer_persha_brovarna_zakarpatske_05_l_glass_parser()[1],
                "varus": parser.beer_persha_brovarna_zakarpatske_05_l_glass_parser()[2],
                "silpo": parser.beer_persha_brovarna_zakarpatske_05_l_glass_parser()[3],
                "ashan": parser.beer_persha_brovarna_zakarpatske_05_l_glass_parser()[4],
                "novus": parser.beer_persha_brovarna_zakarpatske_05_l_glass_parser()[5],
                "metro": parser.beer_persha_brovarna_zakarpatske_05_l_glass_parser()[6],
                "nash_kray": parser.beer_persha_brovarna_zakarpatske_05_l_glass_parser()[7],
                "fozzy": parser.beer_persha_brovarna_zakarpatske_05_l_glass_parser()[8]
            }},
            {'beer_lvivske_svitle_05_l_glass': {
                "metro": parser.beer_lvivske_svitle_05_l_glass_parser()[6],
                "nash_kray": parser.beer_lvivske_svitle_05_l_glass_parser()[7],
                "fozzy": parser.beer_lvivske_svitle_05_l_glass_parser()[8]
            }},
            {'beer_lvivske_1715_05_l_glass': {
                "varus": parser.beer_lvivske_1715_05_l_glass_parser()[2],
                "silpo": parser.beer_lvivske_1715_05_l_glass_parser()[3],
                "ashan": parser.beer_lvivske_1715_05_l_glass_parser()[4],
                "metro": parser.beer_lvivske_1715_05_l_glass_parser()[6],
                "nash_kray": parser.beer_lvivske_1715_05_l_glass_parser()[7],
                "fozzy": parser.beer_lvivske_1715_05_l_glass_parser()[8]
            }},
            {'beer_tuborg_green_05_l_glass': {
                "varus": parser.beer_tuborg_green_05_l_glass_parser()[2],
                "silpo": parser.beer_tuborg_green_05_l_glass_parser()[3],
                "ashan": parser.beer_tuborg_green_05_l_glass_parser()[4],
                "metro": parser.beer_tuborg_green_05_l_glass_parser()[6],
                "nash_kray": parser.beer_tuborg_green_05_l_glass_parser()[7],
                "fozzy": parser.beer_tuborg_green_05_l_glass_parser()[8]
            }},
            {'beer_slavutich_ice_mix_lime_05_l_glass': {
                "varus": parser.beer_slavutich_ice_mix_lime_05_l_glass_parser()[2],
                "silpo": parser.beer_slavutich_ice_mix_lime_05_l_glass_parser()[3],
                "metro": parser.beer_slavutich_ice_mix_lime_05_l_glass_parser()[6],
                "nash_kray": parser.beer_slavutich_ice_mix_lime_05_l_glass_parser()[7]
            }},
            {'beer_teteriv_svitle_05_l_glass': {
                "eko": parser.beer_teteriv_svitle_05_l_glass_parser()[1],
                "silpo": parser.beer_teteriv_svitle_05_l_glass_parser()[3],
                "novus": parser.beer_teteriv_svitle_05_l_glass_parser()[5],
                "nash_kray": parser.beer_teteriv_svitle_05_l_glass_parser()[7],
                "fozzy": parser.beer_teteriv_svitle_05_l_glass_parser()[8]
            }},
            {'beer_krusovice_svitle_05_l_glass': {
                "eko": parser.beer_krusovice_svitle_05_l_glass_parser()[1],
                "varus": parser.beer_krusovice_svitle_05_l_glass_parser()[2],
                "silpo": parser.beer_krusovice_svitle_05_l_glass_parser()[3],
                "ashan": parser.beer_krusovice_svitle_05_l_glass_parser()[4],
                "novus": parser.beer_krusovice_svitle_05_l_glass_parser()[5],
                "metro": parser.beer_krusovice_svitle_05_l_glass_parser()[6],
                "nash_kray": parser.beer_krusovice_svitle_05_l_glass_parser()[7],
                "fozzy": parser.beer_krusovice_svitle_05_l_glass_parser()[8]
            }},
            {'beer_heineken_svitle_05_l_glass': {
                "eko": parser.beer_heineken_svitle_05_l_glass_parser()[1],
                "silpo": parser.beer_heineken_svitle_05_l_glass_parser()[3],
                "ashan": parser.beer_heineken_svitle_05_l_glass_parser()[4],
                "novus": parser.beer_heineken_svitle_05_l_glass_parser()[5],
                "metro": parser.beer_heineken_svitle_05_l_glass_parser()[6],
                "nash_kray": parser.beer_heineken_svitle_05_l_glass_parser()[7],
                "fozzy": parser.beer_heineken_svitle_05_l_glass_parser()[8]
            }},
            {'beer_amstel_svitle_05_l_glass': {
                "eko": parser.beer_amstel_svitle_05_l_glass_parser()[1],
                "silpo": parser.beer_amstel_svitle_05_l_glass_parser()[3],
                "ashan": parser.beer_amstel_svitle_05_l_glass_parser()[4],
                "novus": parser.beer_amstel_svitle_05_l_glass_parser()[5],
                "metro": parser.beer_amstel_svitle_05_l_glass_parser()[6],
                "nash_kray": parser.beer_amstel_svitle_05_l_glass_parser()[7],
                "fozzy": parser.beer_amstel_svitle_05_l_glass_parser()[8]
            }},
            {'beer_hike_premium_svitle_05_l_glass': {
                "eko": parser.beer_hike_premium_svitle_05_l_glass_parser()[1],
                "varus": parser.beer_hike_premium_svitle_05_l_glass_parser()[2],
                "silpo": parser.beer_hike_premium_svitle_05_l_glass_parser()[3],
                "ashan": parser.beer_hike_premium_svitle_05_l_glass_parser()[4],
                "novus": parser.beer_hike_premium_svitle_05_l_glass_parser()[5],
                "metro": parser.beer_hike_premium_svitle_05_l_glass_parser()[6],
                "nash_kray": parser.beer_hike_premium_svitle_05_l_glass_parser()[7],
                "fozzy": parser.beer_hike_premium_svitle_05_l_glass_parser()[8]
            }},
            {'beer_bochkove_svitle_05_l_glass': {
                "eko": parser.beer_bochkove_svitle_05_l_glass_parser()[1],
                "varus": parser.beer_bochkove_svitle_05_l_glass_parser()[2],
                "silpo": parser.beer_bochkove_svitle_05_l_glass_parser()[3],
                "ashan": parser.beer_bochkove_svitle_05_l_glass_parser()[4],
                "novus": parser.beer_bochkove_svitle_05_l_glass_parser()[5],
                "metro": parser.beer_bochkove_svitle_05_l_glass_parser()[6],
                "nash_kray": parser.beer_bochkove_svitle_05_l_glass_parser()[7],
                "fozzy": parser.beer_bochkove_svitle_05_l_glass_parser()[8]
            }},
            {'beer_kronenbourg_1664_blanc_svitle_05_l_glass': {
                "varus": parser.beer_kronenbourg_1664_blanc_svitle_05_l_glass_parser()[2],
                "silpo": parser.beer_kronenbourg_1664_blanc_svitle_05_l_glass_parser()[3],
                "ashan": parser.beer_kronenbourg_1664_blanc_svitle_05_l_glass_parser()[4],
                "metro": parser.beer_kronenbourg_1664_blanc_svitle_05_l_glass_parser()[6],
                "nash_kray": parser.beer_kronenbourg_1664_blanc_svitle_05_l_glass_parser()[7],
                "fozzy": parser.beer_kronenbourg_1664_blanc_svitle_05_l_glass_parser()[8]
            }},

            {'beer_opilla_firmove_nepasterizovane_svitle_05_l_glass': {
                "ashan": parser.beer_opilla_firmove_nepasterizovane_svitle_05_l_glass_parser()[4],
                "novus": parser.beer_opilla_firmove_nepasterizovane_svitle_05_l_glass_parser()[5],
                "metro": parser.beer_opilla_firmove_nepasterizovane_svitle_05_l_glass_parser()[6],
                "fozzy": parser.beer_opilla_firmove_nepasterizovane_svitle_05_l_glass_parser()[8]
            }},
            {'beer_yachmenniy_kolos_svitle_05_l_glass': {
                "fozzy": parser.beer_yachmenniy_kolos_svitle_05_l_glass_parser()[8]
            }},
            {'beer_opilla_korifey_svitle_05_l_glass': {
                "varus": parser.beer_opilla_korifey_svitle_05_l_glass_parser()[2],
                "ashan": parser.beer_opilla_korifey_svitle_05_l_glass_parser()[4],
                "novus": parser.beer_opilla_korifey_svitle_05_l_glass_parser()[5],
                "metro": parser.beer_opilla_korifey_svitle_05_l_glass_parser()[6],
                "fozzy": parser.beer_opilla_korifey_svitle_05_l_glass_parser()[8]
            }},
            {'beer_chaika_dniprovska_svitle_05_l_glass': {
                "eko": parser.beer_chaika_dniprovskaya_svitle_05_l_glass_parser()[1],
                "silpo": parser.beer_chaika_dniprovskaya_svitle_05_l_glass_parser()[3],
                "novus": parser.beer_chaika_dniprovskaya_svitle_05_l_glass_parser()[5],
                "metro": parser.beer_chaika_dniprovskaya_svitle_05_l_glass_parser()[6],
                "fozzy": parser.beer_chaika_dniprovskaya_svitle_05_l_glass_parser()[8]
            }},
            {'beer_chaika_chernomorskaya_svitle_05_l_glass': {
                "eko": parser.beer_chaika_chernomorskaya_svitle_05_l_glass_parser()[1],
                "silpo": parser.beer_chaika_chernomorskaya_svitle_05_l_glass_parser()[3],
                "novus": parser.beer_chaika_chernomorskaya_svitle_05_l_glass_parser()[5],
                "metro": parser.beer_chaika_chernomorskaya_svitle_05_l_glass_parser()[6],
                "fozzy": parser.beer_chaika_chernomorskaya_svitle_05_l_glass_parser()[8]
            }},

            {'beer_uman_waissburg_1_l_svitle_plastic': {
                "varus": parser.beer_uman_waissburg_svitle_1l_plastic_parser()[2],
                "ashan": parser.beer_uman_waissburg_svitle_1l_plastic_parser()[4],
                "novus": parser.beer_uman_waissburg_svitle_1l_plastic_parser()[5],
                "fozzy": parser.beer_uman_waissburg_svitle_1l_plastic_parser()[8]

            }},

            {'beer_uman_pshenichnoe_1_l_svitle_plastic': {
                "novus": parser.beer_uman_pshenichnoe_svitle_1l_plastic_parser()[5],
                "fozzy": parser.beer_uman_pshenichnoe_svitle_1l_plastic_parser()[8]

            }},
            {'beer_berdichevske_hmilne_1_l_svitle_plastic': {
                "silpo": parser.beer_berdichevske_hmilne_svitle_1l_plastic_parser()[3],
                "novus": parser.beer_berdichevske_hmilne_svitle_1l_plastic_parser()[5],
                "fozzy": parser.beer_berdichevske_hmilne_svitle_1l_plastic_parser()[8]
            }},
            {'beer_berdichevske_lager_1_l_svitle_plastic': {
                "silpo": parser.beer_berdichevske_lager_svitle_1l_plastic_parser()[3],
                "metro": parser.beer_berdichevske_lager_svitle_1l_plastic_parser()[6],
                "fozzy": parser.beer_berdichevske_lager_svitle_1l_plastic_parser()[8]
            }},
            {'beer_opilla_korifey_11_l_plastic': {
                "atb": parser.beer_opilla_korifey_11l_plastic_parser()[0],
                "novus": parser.beer_opilla_korifey_11l_plastic_parser()[5],
                "metro": parser.beer_opilla_korifey_11l_plastic_parser()[6]
            }},
            {'beer_obolon_jigulivske_eksportne_15_l_plastic': {
                "atb": parser.beer_obolon_jigulivske_eksportne_15l_plastic_parser()[0]
            }},
            {'beer_yantar_svitle_12_l_plastic': {
                "atb": parser.beer_yantar_svitle_12l_plastic_parser()[0],
                "ashan": parser.beer_yantar_svitle_12l_plastic_parser()[4],
                "novus": parser.beer_yantar_svitle_12l_plastic_parser()[5],
                "metro": parser.beer_yantar_svitle_12l_plastic_parser()[6],
                "fozzy": parser.beer_yantar_svitle_12l_plastic_parser()[8]

            }},
            {'beer_jashkovske_pshenichne_nefiltr_1_l_plastic': {
                "eko": parser.beer_jashkovske_pshenichne_1l_plastic_parser()[1],
                "novus": parser.beer_jashkovske_pshenichne_1l_plastic_parser()[5]
            }},
            {'beer_jashkovske_svitle_nefiltr_1_l_plastic': {
                "eko": parser.beer_jashkovske_svitle_1l_plastic_parser()[1],
                "novus": parser.beer_jashkovske_svitle_1l_plastic_parser()[5]
            }},
            {'beer_jashkovske_jigulivske_nefiltr_1_l_plastic': {
                "eko": parser.beer_jashkovske_jigulivske_nefilter_1l_plastic_parser()[1],
                "silpo": parser.beer_jashkovske_jigulivske_nefilter_1l_plastic_parser()[3],
                "novus": parser.beer_jashkovske_jigulivske_nefilter_1l_plastic_parser()[5]
            }},
            {'beer_persha_privatna_brovarnya_bochkove_1_l_plastic': {
                "eko": parser.beer_persha_privatna_brovarnya_bochkove_1l_plastic_parser()[1],
                "novus": parser.beer_persha_privatna_brovarnya_bochkove_1l_plastic_parser()[5]
            }},
            {'beer_chayka_dniprovska_1_l_plastic': {
                "eko": parser.beer_chayka_dniprovska_1l_plastic_parser()[1],
                "silpo": parser.beer_chayka_dniprovska_1l_plastic_parser()[3]
            }},
            {'ketchup_torchin_s_chasnikom_270gr': {
                "eko": parser.beer_ketchup_torchin_s_chasnikom_parser()[1],
                "varus": parser.beer_ketchup_torchin_s_chasnikom_parser()[2],
                "metro": parser.beer_ketchup_torchin_s_chasnikom_parser()[6],
                "fozzy": parser.beer_ketchup_torchin_s_chasnikom_parser()[8]
            }},
            {'mayonez_korolivskiy_smak_korolivskiy_67_300gr': {
                "atb": parser.mayonez_korolivskiy_smak_korolivskiy_67_300gr_parser()[0],
                "eko": parser.mayonez_korolivskiy_smak_korolivskiy_67_300gr_parser()[1],
                "varus": parser.mayonez_korolivskiy_smak_korolivskiy_67_300gr_parser()[2],
                "novus": parser.mayonez_korolivskiy_smak_korolivskiy_67_300gr_parser()[5],
                "metro": parser.mayonez_korolivskiy_smak_korolivskiy_67_300gr_parser()[6],
                "fozzy": parser.mayonez_korolivskiy_smak_korolivskiy_67_300gr_parser()[8]
            }},
            {'sous_chumak_chesnochniy_200gr': {
                "eko": parser.sous_chumak_chesnochniy_200gr_parser()[1],
                "varus": parser.sous_chumak_chesnochniy_200gr_parser()[2],
                "novus": parser.sous_chumak_chesnochniy_200gr_parser()[5]
            }},

            {'orbit_polunica_banan': {
                "atb": parser.orbit_banan_polunica_parser()[0],
                "eko": parser.orbit_banan_polunica_parser()[1],
                "varus": parser.orbit_banan_polunica_parser()[2],
                "ashan": parser.orbit_banan_polunica_parser()[4],
                "novus": parser.orbit_banan_polunica_parser()[5],
                "metro": parser.orbit_banan_polunica_parser()[6],
                "nash_kray": parser.orbit_banan_polunica_parser()[7],
                "fozzy": parser.orbit_banan_polunica_parser()[8]
            }},
            {'sigarets_lm_red': {
                "ashan": parser.sigarets_lm_red_parser()[4],
                "novus": parser.sigarets_lm_red_parser()[5],
                "fozzy": parser.sigarets_lm_red_parser()[8]
            }},
            {'beer_chernigivske_bile_nefilter_1l': {
                "novus": parser.beer_chernigivske_bile_nefilter_1l_parser()[5],
                "metro": parser.beer_chernigivske_bile_nefilter_1l_parser()[6],
                "fozzy": parser.beer_chernigivske_bile_nefilter_1l_parser()[8]
            }}
        ]
        # далее записываем цены в json-файл
        write_prices_to_json(all_products_names_batch_1, batch_1_path, mode_type_first_write)
        # write_prices_to_json(all_products_names_batch_1, overall_batch_path, mode_type_first_write)

    # для второго батча
    elif batch_name == batch_name_2:
        all_products_names_batch_2 = [
            {'beer_obolon_svitle_1l': {
                "varus": parser.beer_obolon_svitle_1l_parser()[2],
                "novus": parser.beer_obolon_svitle_1l_parser()[5],
            }},
            {'beer_rogan_tradiciyne_svitle_1l': {
                "atb": parser.beer_rogan_tradiciyne_svitle_1l_parser()[0],
                "ashan": parser.beer_rogan_tradiciyne_svitle_1l_parser()[4],
                "novus": parser.beer_rogan_tradiciyne_svitle_1l_parser()[5],
                "metro": parser.beer_rogan_tradiciyne_svitle_1l_parser()[6],
                "nash_kray": parser.beer_rogan_tradiciyne_svitle_1l_parser()[7],
                "fozzy": parser.beer_rogan_tradiciyne_svitle_1l_parser()[8]
            }},
            {'beer_jigulivske_svitle_2l_plastic': {
                "varus": parser.beer_jigulivske_svitle_2l_plastic_parser()[2]
            }},
            {'beer_chayka_dniprovska_2l_plastic': {
                "silpo": parser.beer_chayka_dniprovska_2l_plastic_parser()[3],
                "novus": parser.beer_chayka_dniprovska_2l_plastic_parser()[5],
                "metro": parser.beer_chayka_dniprovska_2l_plastic_parser()[6],
                "fozzy": parser.beer_chayka_dniprovska_2l_plastic_parser()[8]
            }},
            {'beer_piwny_kebek_svitle_2l_plastic': {
                "varus": parser.beer_piwny_kebek_svitle_2l_plastic_parser()[2]
            }},
            {'ketchup_torchin_do_shashliky_270gr': {
                "eko": parser.ketchup_torchin_do_shashliky_270gr_parser()[1],
                "varus": parser.ketchup_torchin_do_shashliky_270gr_parser()[2],
                "silpo": parser.ketchup_torchin_do_shashliky_270gr_parser()[3],
                "ashan": parser.ketchup_torchin_do_shashliky_270gr_parser()[4],
                "novus": parser.ketchup_torchin_do_shashliky_270gr_parser()[5],
                "fozzy": parser.ketchup_torchin_do_shashliky_270gr_parser()[8]
            }},
            {'mayonez_chumak_appetitniy_50_300gr': {
                "eko": parser.mayonez_chumak_appetitniy_50_300gr_parser()[1],
                "varus": parser.mayonez_chumak_appetitniy_50_300gr_parser()[2],
                "silpo": parser.mayonez_chumak_appetitniy_50_300gr_parser()[3],
                "novus": parser.mayonez_chumak_appetitniy_50_300gr_parser()[5],
                "metro": parser.mayonez_chumak_appetitniy_50_300gr_parser()[6]
            }},
            {'coffee_chorna_karta_50gr': {
                "eko": parser.coffee_chorna_karta_50gr_parser()[1]
            }},
            {'beer_arsenal_micne_2l_plastic': {
                "metro": parser.beer_arsenal_micne_2l_plastic_parser()[6],
                "nash_kray": parser.beer_arsenal_micne_2l_plastic_parser()[7],
                "fozzy": parser.beer_arsenal_micne_2l_plastic_parser()[8]
            }},
            {'beer_ppb_bochkove_svitle_2l_plastic': {
                "eko": parser.beer_ppb_bochkove_svitle_2l_plastic_parser()[1],
                "silpo": parser.beer_ppb_bochkove_svitle_2l_plastic_parser()[3],
                "novus": parser.beer_ppb_bochkove_svitle_2l_plastic_parser()[5],
                "metro": parser.beer_ppb_bochkove_svitle_2l_plastic_parser()[6]
            }},
            {'beer_ppb_zakarpatske_svitle_2l_plastic': {
                "silpo": parser.beer_ppb_zakarpatske_svitle_2l_plastic_parser()[3],
                "novus": parser.beer_ppb_zakarpatske_svitle_2l_plastic_parser()[5],
                "metro": parser.beer_ppb_zakarpatske_svitle_2l_plastic_parser()[6]
            }},
            {'beer_zibert_svitle_05l_v_banke': {
                "atb": parser.beer_zibert_svitle_05l_v_banke_parser()[0],
                "eko": parser.beer_zibert_svitle_05l_v_banke_parser()[1],
                "varus": parser.beer_zibert_svitle_05l_v_banke_parser()[2],
                "novus": parser.beer_zibert_svitle_05l_v_banke_parser()[5],
                "metro": parser.beer_zibert_svitle_05l_v_banke_parser()[6]
            }},
            {'yogurt_fanni_lisovi_yagodi_1_5_240gr_stakan': {
                "varus": parser.yogurt_fanni_lisovi_yagodi_1_5_240gr_stakan_parser()[2],
                "silpo": parser.yogurt_fanni_lisovi_yagodi_1_5_240gr_stakan_parser()[3]

            }},
            {'beer_obolon_kievskoe_razlivnoe_svetloe_195l': {
                "eko": parser.beer_obolon_kievskoe_razlivnoe_svetloe_195l_parser()[1],
                "varus": parser.beer_obolon_kievskoe_razlivnoe_svetloe_195l_parser()[2],
                "novus": parser.beer_obolon_kievskoe_razlivnoe_svetloe_195l_parser()[5],
                "metro": parser.beer_obolon_kievskoe_razlivnoe_svetloe_195l_parser()[6]
            }},
            {'beer_chernigivske_light_svitle_2l_plastic': {
                "atb": parser.beer_chernigivske_light_svitle_2l_plastic_parser()[0],
                "silpo": parser.beer_chernigivske_light_svitle_2l_plastic_parser()[3],
                "metro": parser.beer_chernigivske_light_svitle_2l_plastic_parser()[6]
            }},
            {'beer_opilla_korifey_svitle_2l_plastic': {
                "ashan": parser.beer_opilla_korifey_svitle_2l_plastic_parser()[4],
                "novus": parser.beer_opilla_korifey_svitle_2l_plastic_parser()[5],
                "metro": parser.beer_opilla_korifey_svitle_2l_plastic_parser()[6]
            }},
            {'beer_yantar_svitle_2l_plastic': {
                "metro": parser.beer_yantar_svitle_2l_plastic_parser()[6]
            }},
            {'beer_tuborg_green_svitle_4_banki_05l': {
                "silpo": parser.beer_tuborg_green_svitle_4_banki_05l_parser()[3],
                "ashan": parser.beer_tuborg_green_svitle_4_banki_05l_parser()[4],
                "metro": parser.beer_tuborg_green_svitle_4_banki_05l_parser()[6],
                "fozzy": parser.beer_tuborg_green_svitle_4_banki_05l_parser()[8]
            }},
            {'beer_ppb_zakarpatske_svitle_4_banki_05l': {
                "silpo": parser.beer_ppb_zakarpatske_svitle_4_banki_05l_parser()[3],
                "ashan": parser.beer_ppb_zakarpatske_svitle_4_banki_05l_parser()[4],
                "novus": parser.beer_ppb_zakarpatske_svitle_4_banki_05l_parser()[5],
                "metro": parser.beer_ppb_zakarpatske_svitle_4_banki_05l_parser()[6]
            }},
            {'beer_ppb_bochkove_svitle_4_banki_05l': {
                "silpo": parser.beer_ppb_bochkove_svitle_4_banki_05l_parser()[3],
                "novus": parser.beer_ppb_bochkove_svitle_4_banki_05l_parser()[5],
                "metro": parser.beer_ppb_bochkove_svitle_4_banki_05l_parser()[6]
            }},
            {'beer_budweiser_budvar_svitle_05l': {
                "varus": parser.beer_budweiser_budvar_svitle_05l_parser()[2],
                "ashan": parser.beer_budweiser_budvar_svitle_05l_parser()[4],
                "novus": parser.beer_budweiser_budvar_svitle_05l_parser()[5],
                "metro": parser.beer_budweiser_budvar_svitle_05l_parser()[6]
            }},
            {'beer_pilsner_urquell_svitle_05l': {
                "metro": parser.beer_pilsner_urquell_05l_glass_parser()[6]
            }},
            {'beer_robert_doms_belgiyskiy_svitle_nefilter_05l_glass': {
                "varus": parser.beer_robert_doms_belgiyskiy_svitle_nefilter_05l_glass_parser()[2],
                "silpo": parser.beer_robert_doms_belgiyskiy_svitle_nefilter_05l_glass_parser()[3],
                "metro": parser.beer_robert_doms_belgiyskiy_svitle_nefilter_05l_glass_parser()[6]
            }},
            {'beer_chernigivske_svitle_05_l_jb': {
                "ashan": parser.beer_chernigivske_svitle_05_l_jb_parser()[4],
                "novus": parser.beer_chernigivske_svitle_05_l_jb_parser()[5],
                "fozzy": parser.beer_chernigivske_svitle_05_l_jb_parser()[8]
            }},
            {'beer_chernigivske_bile_nefilter_05_l_jb': {
                "atb": parser.beer_chernigivske_bile_nefilter_05_l_jb_parser()[0],
                "silpo": parser.beer_chernigivske_bile_nefilter_05_l_jb_parser()[3],
                "ashan": parser.beer_chernigivske_bile_nefilter_05_l_jb_parser()[4],
                "metro": parser.beer_chernigivske_bile_nefilter_05_l_jb_parser()[6],
                "fozzy": parser.beer_chernigivske_bile_nefilter_05_l_jb_parser()[8]
            }},
            {'beer_velkopopovicky_kozel_temne_05_l_jb': {
                "atb": parser.beer_velkopopovicky_kozel_temne_05_l_jb_parser()[0],
                "ashan": parser.beer_velkopopovicky_kozel_temne_05_l_jb_parser()[4],
                "novus": parser.beer_velkopopovicky_kozel_temne_05_l_jb_parser()[5],
                "metro": parser.beer_velkopopovicky_kozel_temne_05_l_jb_parser()[6],
                "fozzy": parser.beer_velkopopovicky_kozel_temne_05_l_jb_parser()[8]
            }},
            {'beer_edelmeister_pilsner_svitle_05_l_jb': {
                "atb": parser.beer_edelmeister_pilsner_svitle_05_l_jb_parser()[0]
            }},
            {'beer_faxe_svitle_05_l_jb': {
                "atb": parser.beer_faxe_svitle_05_l_jb_parser()[0]
            }},
            {'beer_livu_pilzenes_svitle_05_l_jb': {
                "atb": parser.beer_livu_pilzenes_svitle_05_l_jb_parser()[0]
            }},
            {'beer_velkopopovicky_kozel_svitle_05_l_jb': {
                "atb": parser.beer_velkopopovicky_kozel_svitle_05_l_jb_parser()[0],
                "silpo": parser.beer_velkopopovicky_kozel_svitle_05_l_jb_parser()[3],
                "ashan": parser.beer_velkopopovicky_kozel_svitle_05_l_jb_parser()[4],
                "novus": parser.beer_velkopopovicky_kozel_svitle_05_l_jb_parser()[5],
                "metro": parser.beer_velkopopovicky_kozel_svitle_05_l_jb_parser()[6],
            }},
            {'beer_obolon_beermix_limon_svitle_05_l_jb': {
                "atb": parser.beer_obolon_beermix_limon_05_l_jb_parser()[0],
                "eko": parser.beer_obolon_beermix_limon_05_l_jb_parser()[1],
                "varus": parser.beer_obolon_beermix_limon_05_l_jb_parser()[2],
                "silpo": parser.beer_obolon_beermix_limon_05_l_jb_parser()[3],
                "ashan": parser.beer_obolon_beermix_limon_05_l_jb_parser()[4],
                "novus": parser.beer_obolon_beermix_limon_05_l_jb_parser()[5],
                "metro": parser.beer_obolon_beermix_limon_05_l_jb_parser()[6],
                "nash_kray": parser.beer_obolon_beermix_limon_05_l_jb_parser()[7],
                "fozzy": parser.beer_obolon_beermix_limon_05_l_jb_parser()[8]
            }},
            {'beer_edelmeister_weizenbier_svitle_nefilter_05_l_jb': {
                "atb": parser.beer_edelmeister_weizenbier_svitle_nefilter_05_l_jb_parser()[0]
            }},
            {'beer_edelmeister_schwarzbier_temne_05_l_jb': {
                "atb": parser.beer_edelmeister_schwarzbier_temne_05_l_jb_parser()[0]
            }},
            {'beer_hike_blanche_nefilter_05_l_jb': {
                "atb": parser.beer_hike_blanche_nefilter_05_l_jb_parser()[0],
                "eko": parser.beer_hike_blanche_nefilter_05_l_jb_parser()[1],
                "varus": parser.beer_hike_blanche_nefilter_05_l_jb_parser()[2],
                "ashan": parser.beer_hike_blanche_nefilter_05_l_jb_parser()[4],
                "novus": parser.beer_hike_blanche_nefilter_05_l_jb_parser()[5],
                "metro": parser.beer_hike_blanche_nefilter_05_l_jb_parser()[6]
            }},
            {'beer_zlata_praha_svitle_05_l_jb': {
                "atb": parser.beer_zlata_praha_svitle_05_l_jb_parser()[0],
                "varus": parser.beer_zlata_praha_svitle_05_l_jb_parser()[2],
                "ashan": parser.beer_zlata_praha_svitle_05_l_jb_parser()[4],
            }},
            {'beer_thuringer_premium_beer_svitle_05_l_jb': {
                "atb": parser.beer_thuringer_premium_beer_svitle_05_l_jb_parser()[0]
            }},
            {'beer_livu_sencu_beer_svitle_05_l_jb': {
                "atb": parser.beer_livu_sencu_beer_svitle_05_l_jb_parser()[0]
            }},
            {'beer_germanarich_svitle_05_l_jb': {
                "atb": parser.beer_germanarich_svitle_05_l_jb_parser()[0]
            }},
            {'beer_hike_premium_svitle_05_l_jb': {
                "atb": parser.beer_hike_premium_svitle_05_l_jb_parser()[0],
                "eko": parser.beer_hike_premium_svitle_05_l_jb_parser()[1],
                "varus": parser.beer_hike_premium_svitle_05_l_jb_parser()[2],
                "silpo": parser.beer_hike_premium_svitle_05_l_jb_parser()[3],
                "ashan": parser.beer_hike_premium_svitle_05_l_jb_parser()[4],
                "novus": parser.beer_hike_premium_svitle_05_l_jb_parser()[5],
                "metro": parser.beer_hike_premium_svitle_05_l_jb_parser()[6],
                "fozzy": parser.beer_hike_premium_svitle_05_l_jb_parser()[8]
            }},
            {'beer_obolon_nonalcohol_nefilter_svitle_05_l_jb': {
                "atb": parser.beer_hike_premium_svitle_05_l_jb_parser()[0],
                "varus": parser.beer_hike_premium_svitle_05_l_jb_parser()[2],
                "ashan": parser.beer_hike_premium_svitle_05_l_jb_parser()[4]
            }},
            {'beer_zibert_bavarskoe_svitle_05_l_jb': {
                "eko": parser.beer_zibert_bavarskoe_svitle_05_l_jb_parser()[1],
                "novus": parser.beer_zibert_bavarskoe_svitle_05_l_jb_parser()[5],
                "metro": parser.beer_zibert_bavarskoe_svitle_05_l_jb_parser()[6]
            }},
            {'beer_bavaria_liquid_apple_ninalco_svitle_05_l_jb': {
                "eko": parser.beer_bavaria_liquid_apple_ninalco_svitle_05_l_jb_parser()[1]
            }},
            {'beer_heineken_svitle_05_l_jb': {
                "eko": parser.beer_heineken_svitle_05_l_jb_parser()[1],
                "varus": parser.beer_heineken_svitle_05_l_jb_parser()[2],
                "silpo": parser.beer_heineken_svitle_05_l_jb_parser()[3],
                "ashan": parser.beer_heineken_svitle_05_l_jb_parser()[4],
                "novus": parser.beer_heineken_svitle_05_l_jb_parser()[5],
                "metro": parser.beer_heineken_svitle_05_l_jb_parser()[6],
                "fozzy": parser.beer_heineken_svitle_05_l_jb_parser()[8]
            }},
            {'beer_rychtar_grant_11_svitle_05_l_jb': {
                "eko": parser.beer_rychtar_grant_11_svitle_05_l_jb_parser()[1]
            }},
            {'beer_amstel_svitle_05_l_jb': {
                "eko": parser.beer_amstel_svitle_05_l_jb_parser()[1],
                "varus": parser.beer_amstel_svitle_05_l_jb_parser()[2],
                "silpo": parser.beer_amstel_svitle_05_l_jb_parser()[3],
                "ashan": parser.beer_amstel_svitle_05_l_jb_parser()[4],
                "novus": parser.beer_amstel_svitle_05_l_jb_parser()[5],
                "metro": parser.beer_amstel_svitle_05_l_jb_parser()[6],
                "fozzy": parser.beer_amstel_svitle_05_l_jb_parser()[8]
            }},
            {'beer_bavaria_svitle_05_l_jb': {
                "eko": parser.beer_bavaria_svitle_05_l_jb_parser()[1],
                "varus": parser.beer_bavaria_svitle_05_l_jb_parser()[2],
                "ashan": parser.beer_bavaria_svitle_05_l_jb_parser()[4],
                "metro": parser.beer_bavaria_svitle_05_l_jb_parser()[6]
            }},
            {'beer_bavaria_svitle_nonalcohol_05_l_jb': {
                "eko": parser.beer_bavaria_svitle_nonalcohol_05_l_jb_parser()[1],
                "varus": parser.beer_bavaria_svitle_nonalcohol_05_l_jb_parser()[2]
            }},
            {'beer_edelburg_lager_05_l_jb': {
                "eko": parser.beer_edelburg_lager_05_l_jb_parser()[1],
                "metro": parser.beer_edelburg_lager_05_l_jb_parser()[6]
            }},
            {'beer_donner_pils_svitle_05_l_jb': {
                "eko": parser.beer_donner_pils_svitle_05_l_jb_parser()[1]
            }},
            {'beer_dutch_windmill_svitle_05_l_jb': {
                "eko": parser.beer_dutch_windmill_svitle_05_l_jb_parser()[1],
                "varus": parser.beer_dutch_windmill_svitle_05_l_jb_parser()[2],
                "novus": parser.beer_dutch_windmill_svitle_05_l_jb_parser()[5]
            }},
            {'beer_edelburg_hefeweizen_svitle_nefilter_05_l_jb': {
                "eko": parser.beer_edelburg_hefeweizen_svitle_nefilter_05_l_jb_parser()[1],
                "metro": parser.beer_edelburg_hefeweizen_svitle_nefilter_05_l_jb_parser()[6]
            }},
            {'beer_edelmeister_unfiltered_svitle_nefilter_05_l_jb': {
                "eko": parser.beer_edelmeister_unfiltered_svitle_nefilter_05_l_jb_parser()[1]
            }},
            {'beer_estrella_damm_barcelona_svitle_05_l_jb': {
                "eko": parser.beer_estrella_damm_barcelona_svitle_05_l_jb_parser()[1],
                "silpo": parser.beer_estrella_damm_barcelona_svitle_05_l_jb_parser()[3],
                "novus": parser.beer_estrella_damm_barcelona_svitle_05_l_jb_parser()[5],
                "metro": parser.beer_estrella_damm_barcelona_svitle_05_l_jb_parser()[6],
                "fozzy": parser.beer_estrella_damm_barcelona_svitle_05_l_jb_parser()[8]
            }},
            {'beer_halne_jasne_pelne_05_l_jb': {
                "eko": parser.beer_halne_jasne_pelne_05_l_jb_parser()[1],
                "novus": parser.beer_halne_jasne_pelne_05_l_jb_parser()[5]
            }},
            {'beer_eurotour_hefeweissbier_svitle_05_l_jb': {
                "eko": parser.beer_eurotour_hefeweissbier_svitle_05_l_jb_parser()[1]
            }},
            {'beer_hollandia_strong_svitle_05_l_jb': {
                "eko": parser.beer_hollandia_strong_svitle_05_l_jb_parser()[1],
                "varus": parser.beer_hollandia_strong_svitle_05_l_jb_parser()[2],
                "ashan": parser.beer_hollandia_strong_svitle_05_l_jb_parser()[4]
            }},
            {'beer_lander_brau_premium_svitle_05_l_jb': {
                "eko": parser.beer_lander_brau_premium_svitle_05_l_jb_parser()[1],
                "varus": parser.beer_lander_brau_premium_svitle_05_l_jb_parser()[2],
                "metro": parser.beer_lander_brau_premium_svitle_05_l_jb_parser()[6]
            }},
            {'beer_saku_kuld_05_l_jb': {
                "eko": parser.beer_saku_kuld_05_l_jb_parser()[1]
            }},
            {'beer_saku_originaal_05_l_jb': {
                "eko": parser.beer_saku_originaal_05_l_jb_parser()[1]
            }},
            {'beer_stangen_lager_svitle_05_l_jb': {
                "eko": parser.beer_stangen_lager_svitle_05_l_jb_parser()[1]
            }},
            {'beer_van_pur_premium_svitle_05_l_jb': {
                "eko": parser.beer_van_pur_premium_svitle_05_l_jb_parser()[1]
            }},
            {'beer_bavaria_mango_marakya_nonalco_svitle_05_l_jb': {
                "eko": parser.beer_bavaria_mango_marakya_nonalco_svitle_05_l_jb_parser()[1]
            }},
            {'beer_bavaria_granat_nonalco_svitle_05_l_jb': {
                "eko": parser.beer_bavaria_granat_nonalco_svitle_05_l_jb_parser()[1]
            }},
            {'beer_obolon_beermix_malina_svitle_05_l_jb': {
                "atb": parser.beer_obolon_beermix_malina_svitle_05_l_jb_parser()[0],
                "eko": parser.beer_obolon_beermix_malina_svitle_05_l_jb_parser()[1],
                "ashan": parser.beer_obolon_beermix_malina_svitle_05_l_jb_parser()[4],
                "nash_kray": parser.beer_obolon_beermix_malina_svitle_05_l_jb_parser()[7]
            }},
            {'beer_obolon_beermix_vishnya_svitle_05_l_jb': {
                "eko": parser.beer_obolon_beermix_vishnya_svitle_05_l_jb_parser()[1],
                "varus": parser.beer_obolon_beermix_vishnya_svitle_05_l_jb_parser()[2],
                "silpo": parser.beer_obolon_beermix_vishnya_svitle_05_l_jb_parser()[3],
                "ashan": parser.beer_obolon_beermix_vishnya_svitle_05_l_jb_parser()[4],
                "novus": parser.beer_obolon_beermix_vishnya_svitle_05_l_jb_parser()[5],
                "metro": parser.beer_obolon_beermix_vishnya_svitle_05_l_jb_parser()[6],
                "nash_kray": parser.beer_obolon_beermix_vishnya_svitle_05_l_jb_parser()[7],
                "fozzy": parser.beer_obolon_beermix_vishnya_svitle_05_l_jb_parser()[8]
            }},
            {'beer_lomza_svitle_05_l_jb': {
                "eko": parser.beer_lomza_svitle_05_l_jb_parser()[1]
            }},
            {'beer_paderborner_pilsener_05_l_jb': {
                "eko": parser.beer_paderborner_pilsener_05_l_jb_parser()[1],
                "silpo": parser.beer_paderborner_pilsener_05_l_jb_parser()[3],
                "novus": parser.beer_paderborner_pilsener_05_l_jb_parser()[5],
                "metro": parser.beer_paderborner_pilsener_05_l_jb_parser()[6],
                "fozzy": parser.beer_paderborner_pilsener_05_l_jb_parser()[8]
            }},
            {'beer_paderborner_export_05_l_jb': {
                "eko": parser.beer_paderborner_export_05_l_jb_parser()[1],
                "silpo": parser.beer_paderborner_export_05_l_jb_parser()[3],
                "novus": parser.beer_paderborner_export_05_l_jb_parser()[5],
                "metro": parser.beer_paderborner_export_05_l_jb_parser()[6]
            }},
            {'beer_clausthaler_grapefruit_nonalco_05_l_jb': {
                "eko": parser.beer_clausthaler_grapefruit_nonalco_05_l_jb_parser()[1],
                "varus": parser.beer_clausthaler_grapefruit_nonalco_05_l_jb_parser()[2],
                "metro": parser.beer_clausthaler_grapefruit_nonalco_05_l_jb_parser()[6]
            }},
            {'beer_clausthaler_original_nonalco_05_l_jb': {
                "eko": parser.beer_clausthaler_original_nonalco_05_l_jb_parser()[1],
                "varus": parser.beer_clausthaler_original_nonalco_05_l_jb_parser()[2],
                "metro": parser.beer_clausthaler_original_nonalco_05_l_jb_parser()[6]
            }},
            {'beer_clausthaler_lemon_nonalco_05_l_jb': {
                "eko": parser.beer_clausthaler_lemon_nonalco_05_l_jb_parser()[1],
                "varus": parser.beer_clausthaler_lemon_nonalco_05_l_jb_parser()[2],
                "novus": parser.beer_clausthaler_lemon_nonalco_05_l_jb_parser()[5]
            }},
            {'beer_forever_rock_n_roll_nefilter_svitle_05_l_jb': {
                "eko": parser.beer_forever_rock_n_roll_nefilter_svitle_05_l_jb_parser()[1]
            }},
            {'beer_forever_black_queen_nefilter_temne_05_l_jb': {
                "eko": parser.beer_forever_black_queen_nefilter_temne_05_l_jb_parser()[1]
            }},
            {'beer_forever_kite_safari_nefilter_svitle_05_l_jb': {
                "eko": parser.beer_forever_kite_safari_nefilter_svitle_05_l_jb_parser()[1]
            }},
            {'beer_forever_crazy_nefilter_svitle_05_l_jb': {
                "eko": parser.beer_forever_crazy_nefilter_svitle_05_l_jb_parser()[1]
            }},
            {'beer_hike_light_svitle_05_l_jb': {
                "atb": parser.beer_hike_light_svitle_05_l_jb_parser()[0],
                "eko": parser.beer_hike_light_svitle_05_l_jb_parser()[1],
                "varus": parser.beer_hike_light_svitle_05_l_jb_parser()[2],
                "silpo": parser.beer_hike_light_svitle_05_l_jb_parser()[3],
                "metro": parser.beer_hike_light_svitle_05_l_jb_parser()[6]
            }},
            {'beer_hike_zero_nonalco_05_l_jb': {
                "atb": parser.beer_hike_zero_nonalco_05_l_jb_parser()[0],
                "eko": parser.beer_hike_zero_nonalco_05_l_jb_parser()[1],
                "varus": parser.beer_hike_zero_nonalco_05_l_jb_parser()[2],
                "silpo": parser.beer_hike_zero_nonalco_05_l_jb_parser()[3],
                "novus": parser.beer_hike_zero_nonalco_05_l_jb_parser()[5],
                "metro": parser.beer_hike_zero_nonalco_05_l_jb_parser()[6],
                "fozzy": parser.beer_hike_zero_nonalco_05_l_jb_parser()[8]
            }},
            {'beer_horn_disel_ice_pilsner_svitle_05_l_jb': {
                "eko": parser.beer_horn_disel_ice_pilsner_svitle_05_l_jb_parser()[1]
            }},
            {'beer_horn_disel_original_svitle_05_l_jb': {
                "eko": parser.beer_horn_disel_original_svitle_05_l_jb_parser()[1]
            }},
            {'beer_horn_disel_traditional_svitle_05_l_jb': {
                "eko": parser.beer_horn_disel_traditional_svitle_05_l_jb_parser()[1]
            }},
            {'beer_horn_disel_premium_svitle_05_l_jb': {
                "eko": parser.beer_horn_disel_premium_svitle_05_l_jb_parser()[1]
            }},
            {'beer_krusovice_cerne_temne_05_l_jb': {
                "eko": parser.beer_krusovice_cerne_temne_05_l_jb_parser()[1],
                "varus": parser.beer_krusovice_cerne_temne_05_l_jb_parser()[2],
                "silpo": parser.beer_krusovice_cerne_temne_05_l_jb_parser()[3],
                "novus": parser.beer_krusovice_cerne_temne_05_l_jb_parser()[5],
                "metro": parser.beer_krusovice_cerne_temne_05_l_jb_parser()[6],
                "nash_kray": parser.beer_krusovice_cerne_temne_05_l_jb_parser()[7],
                "fozzy": parser.beer_krusovice_cerne_temne_05_l_jb_parser()[8]
            }},
            {'beer_lander_brau_micne_05_l_jb': {
                "eko": parser.beer_lander_brau_micne_05_l_jb_parser()[1],
                "metro": parser.beer_lander_brau_micne_05_l_jb_parser()[6]
            }},
            {'beer_lander_brau_svitle_nefilter_05_l_jb': {
                "eko": parser.beer_lander_brau_svitle_nefilter_05_l_jb_parser()[1],
                "varus": parser.beer_lander_brau_svitle_nefilter_05_l_jb_parser()[2],
                "metro": parser.beer_lander_brau_svitle_nefilter_05_l_jb_parser()[6]
            }},
            {'beer_paderborner_pilger_svitle_nefilter_05_l_jb': {
                "eko": parser.beer_paderborner_pilger_svitle_nefilter_05_l_jb_parser()[1],
                "silpo": parser.beer_paderborner_pilger_svitle_nefilter_05_l_jb_parser()[3],
                "novus": parser.beer_paderborner_pilger_svitle_nefilter_05_l_jb_parser()[5],
                "metro": parser.beer_paderborner_pilger_svitle_nefilter_05_l_jb_parser()[6],
                "fozzy": parser.beer_paderborner_pilger_svitle_nefilter_05_l_jb_parser()[8]
            }},
            {'beer_platan_jedenactka_11_svitle_05_l_jb': {
                "eko": parser.beer_platan_jedenactka_11_svitle_05_l_jb_parser()[1]
            }},
            {'beer_praga_svitle_05_l_jb': {
                "eko": parser.beer_praga_svitle_05_l_jb_parser()[1],
                "novus": parser.beer_praga_svitle_05_l_jb_parser()[5],
                "metro": parser.beer_praga_svitle_05_l_jb_parser()[6]
            }},
            {'beer_saku_rock_svitle_0568_l_jb': {
                "eko": parser.beer_saku_rock_svitle_0568_l_jb_parser()[1]
            }},
            {'beer_sitnan_svitle_05_l_jb': {
                "eko": parser.beer_sitnan_svitle_05_l_jb_parser()[1],
                "novus": parser.beer_sitnan_svitle_05_l_jb_parser()[5]
            }},
            {'beer_vienas_premium_golden_svitle_05_l_jb': {
                "eko": parser.beer_vienas_premium_golden_svitle_05_l_jb_parser()[1]
            }},
            {'beer_vienas_premium_traditional_svitle_05_l_jb': {
                "eko": parser.beer_vienas_premium_traditional_svitle_05_l_jb_parser()[1]
            }},
            {'beer_volynski_browar_forever_sweet_wit_svitle_05_l_jb': {
                "eko": parser.beer_volynski_browar_forever_sweet_wit_svitle_05_l_jb_parser()[1]
            }},
            {'beer_zahringer_premium_svitle_05_l_jb': {
                "eko": parser.beer_zahringer_premium_svitle_05_l_jb_parser()[1]
            }},
            {'beer_zahringer_hefeweizen_svitle_05_l_jb': {
                "eko": parser.beer_zahringer_hefeweizen_svitle_05_l_jb_parser()[1]
            }},
            {'beer_jajkivske_nefilter_svitle_05_l_jb': {
                "atb": parser.beer_jajkivske_nefilter_svitle_05_l_jb_parser()[0],
                "eko": parser.beer_jajkivske_nefilter_svitle_05_l_jb_parser()[1],
                "silpo": parser.beer_jajkivske_nefilter_svitle_05_l_jb_parser()[3],
                "novus": parser.beer_jajkivske_nefilter_svitle_05_l_jb_parser()[5]
            }}
        ]
        # далее записываем цены в json-файл
        write_prices_to_json(all_products_names_batch_2, batch_2_path, mode_type_first_write)

    # для 3-го батча
    elif batch_name == batch_name_3:
        all_products_names_batch_3 = [
            {'beer_obolon_svitle_05_l_jb': {
                "eko": parser.beer_obolon_svitle_05_l_jb_parser()[1],
                "varus": parser.beer_obolon_svitle_05_l_jb_parser()[2],
                "silpo": parser.beer_obolon_svitle_05_l_jb_parser()[3],
                "novus": parser.beer_obolon_svitle_05_l_jb_parser()[5],
                "metro": parser.beer_obolon_svitle_05_l_jb_parser()[6],
                "fozzy": parser.beer_obolon_svitle_05_l_jb_parser()[8]
            }},
            {'beer_pubster_svitle_05_l_jb': {
                "eko": parser.beer_pubster_svitle_05_l_jb_parser()[1],
                "varus": parser.beer_pubster_svitle_05_l_jb_parser()[2],
                "silpo": parser.beer_pubster_svitle_05_l_jb_parser()[3],
                "novus": parser.beer_pubster_svitle_05_l_jb_parser()[5],
                "metro": parser.beer_pubster_svitle_05_l_jb_parser()[6]
            }},
            {'beer_chaika_chernomorskaya_05_l_jb': {
                "eko": parser.beer_chaika_chernomorskaya_05_l_jb_parser()[1],
                "silpo": parser.beer_chaika_chernomorskaya_05_l_jb_parser()[3],
                "novus": parser.beer_chaika_chernomorskaya_05_l_jb_parser()[5],
                "metro": parser.beer_chaika_chernomorskaya_05_l_jb_parser()[6],
                "fozzy": parser.beer_chaika_chernomorskaya_05_l_jb_parser()[8]
            }},
            {'beer_ppb_zakarpatske_origin_svitle_05_l_jb': {
                "eko": parser.beer_ppb_zakarpatske_origin_svitle_05_l_jb_parser()[1],
                "varus": parser.beer_ppb_zakarpatske_origin_svitle_05_l_jb_parser()[2],
                "silpo": parser.beer_ppb_zakarpatske_origin_svitle_05_l_jb_parser()[3],
                "novus": parser.beer_ppb_zakarpatske_origin_svitle_05_l_jb_parser()[5],
                "fozzy": parser.beer_ppb_zakarpatske_origin_svitle_05_l_jb_parser()[8]
            }},
            {'beer_ppb_bochkove_nefilter_05_l_jb': {
                "eko": parser.beer_ppb_bochkove_nefilter_05_l_jb_parser()[1],
                "silpo": parser.beer_ppb_bochkove_nefilter_05_l_jb_parser()[3],
                "ashan": parser.beer_ppb_bochkove_nefilter_05_l_jb_parser()[4],
                "novus": parser.beer_ppb_bochkove_nefilter_05_l_jb_parser()[5],
                "metro": parser.beer_ppb_bochkove_nefilter_05_l_jb_parser()[6],
                "nash_kray": parser.beer_ppb_bochkove_nefilter_05_l_jb_parser()[7]
            }},
            {'beer_ppb_nefilter_svitle_nonalco_05_l_jb': {
                "eko": parser.beer_ppb_nefilter_svitle_nonalco_05_l_jb_parser()[1],
                "varus": parser.beer_ppb_nefilter_svitle_nonalco_05_l_jb_parser()[2],
                "silpo": parser.beer_ppb_nefilter_svitle_nonalco_05_l_jb_parser()[3],
                "novus": parser.beer_ppb_nefilter_svitle_nonalco_05_l_jb_parser()[5],
                "metro": parser.beer_ppb_nefilter_svitle_nonalco_05_l_jb_parser()[6],
                "fozzy": parser.beer_ppb_nefilter_svitle_nonalco_05_l_jb_parser()[8]
            }},
            {'beer_ppb_limon_lime_nonalco_nefilter_05_l_jb': {
                "eko": parser.beer_ppb_limon_lime_nonalco_nefilter_05_l_jb_parser()[1],
                "varus": parser.beer_ppb_limon_lime_nonalco_nefilter_05_l_jb_parser()[2],
                "novus": parser.beer_ppb_limon_lime_nonalco_nefilter_05_l_jb_parser()[5]
            }},
            {'beer_chaika_dniprovskaya_05_l_jb': {
                "eko": parser.beer_chaika_dniprovskaya_05_l_jb_parser()[1],
                "silpo": parser.beer_chaika_dniprovskaya_05_l_jb_parser()[3],
                "novus": parser.beer_chaika_dniprovskaya_05_l_jb_parser()[5],
                "metro": parser.beer_chaika_dniprovskaya_05_l_jb_parser()[6],
                "nash_kray": parser.beer_chaika_dniprovskaya_05_l_jb_parser()[7],
                "fozzy": parser.beer_chaika_dniprovskaya_05_l_jb_parser()[8]
            }},
            {'beer_brok_export_svitle_05_l_jb': {
                "eko": parser.beer_brok_export_svitle_05_l_jb_parser()[1],
                "novus": parser.beer_brok_export_svitle_05_l_jb_parser()[5]
            }},
            {'beer_carling_svitle_05_l_jb': {
                "atb": parser.beer_carling_svitle_05_l_jb_parser()[0],
                "varus": parser.beer_carling_svitle_05_l_jb_parser()[2],
                "silpo": parser.beer_carling_svitle_05_l_jb_parser()[3],
                "novus": parser.beer_carling_svitle_05_l_jb_parser()[5]
            }},
            {'beer_keten_brug_blanche_elegant_05_l_jb': {
                "atb": parser.beer_keten_brug_blanche_elegant_05_l_jb_parser()[0],
                "varus": parser.beer_keten_brug_blanche_elegant_05_l_jb_parser()[2],
                "silpo": parser.beer_keten_brug_blanche_elegant_05_l_jb_parser()[3],
                "novus": parser.beer_keten_brug_blanche_elegant_05_l_jb_parser()[5]
            }},
            {'beer_budweiser_nonalco_05_l_jb': {
                "varus": parser.beer_budweiser_nonalco_05_l_jb_parser()[2],
                "silpo": parser.beer_budweiser_nonalco_05_l_jb_parser()[3]
            }},
            {'beer_feldschlosschenWheatBeer_svitle_nefilter_05_l_jb': {
                "varus": parser.beer_FeldschlosschenWheatBeer_svitle_nefilter_05_l_jb_parser()[2]
            }},
            {'beer_teteriv_hmilna_vishnya_napivtemne_05_l_jb': {
                "eko": parser.beer_teteriv_hmilna_vishnya_napivtemne_05_l_jb_parser()[1],
                "varus": parser.beer_teteriv_hmilna_vishnya_napivtemne_05_l_jb_parser()[2],
                "silpo": parser.beer_teteriv_hmilna_vishnya_napivtemne_05_l_jb_parser()[3],
                "ashan": parser.beer_teteriv_hmilna_vishnya_napivtemne_05_l_jb_parser()[4],
                "novus": parser.beer_teteriv_hmilna_vishnya_napivtemne_05_l_jb_parser()[5],
                "nash_kray": parser.beer_teteriv_hmilna_vishnya_napivtemne_05_l_jb_parser()[7]
            }},
            {'beer_grotwerg_svitle_05_l_jb': {
                "varus": parser.beer_grotwerg_svitle_05_l_jb_parser()[2]
            }},
            {'beer_holland_import_svitle_05_l_jb': {
                "eko": parser.beer_holland_import_svitle_05_l_jb_parser()[1],
                "varus": parser.beer_holland_import_svitle_05_l_jb_parser()[2],
                "novus": parser.beer_holland_import_svitle_05_l_jb_parser()[5]
            }},
            {'beer_golden_castle_export_svitle_05_l_jb': {
                "varus": parser.beer_golden_castle_export_svitle_05_l_jb_parser()[2],
                "silpo": parser.beer_golden_castle_export_svitle_05_l_jb_parser()[3],
                "novus": parser.beer_golden_castle_export_svitle_05_l_jb_parser()[5]
            }},
            {'beer_5_0_original_craft_beer_nefilter_svitle_05_l_jb': {
                "eko": parser.beer_5_0_original_craft_beer_nefilter_svitle_05_l_jb_parser()[1],
                "varus": parser.beer_5_0_original_craft_beer_nefilter_svitle_05_l_jb_parser()[2]
            }},

            {'beer_guinness_draught_temne_044_l_jb': {
                "varus": parser.beer_guinness_draught_temne_044_l_jb_parser()[2],
                "silpo": parser.beer_guinness_draught_temne_044_l_jb_parser()[3],
                "ashan": parser.beer_guinness_draught_temne_044_l_jb_parser()[4],
                "metro": parser.beer_guinness_draught_temne_044_l_jb_parser()[6],
                "fozzy": parser.beer_guinness_draught_temne_044_l_jb_parser()[8]
            }},
            {'beer_grimbergenDoubleAmbree_napivtemne_05_l_jb': {
                "varus": parser.beer_grimbergenDoubleAmbree_napivtemne_05_l_jb_parser()[2],
                "silpo": parser.beer_grimbergenDoubleAmbree_napivtemne_05_l_jb_parser()[3],
                "metro": parser.beer_grimbergenDoubleAmbree_napivtemne_05_l_jb_parser()[6],
                "fozzy": parser.beer_grimbergenDoubleAmbree_napivtemne_05_l_jb_parser()[8]
            }},
            {'beer_warsteinerPremiumVerum_svitle_05_l_jb': {
                "varus": parser.beer_warsteinerPremiumVerum_svitle_05_l_jb_parser()[2],
                "silpo": parser.beer_warsteinerPremiumVerum_svitle_05_l_jb_parser()[3]
            }},
            {'beer_dab_temne_05_l_jb': {
                "varus": parser.beer_dab_temne_05_l_jb_parser()[2],
                "silpo": parser.beer_dab_temne_05_l_jb_parser()[3],
                "metro": parser.beer_dab_temne_05_l_jb_parser()[6]
            }},
            {'beer_grimbergenBlanche_svitle_05_l_jb': {
                "varus": parser.beer_grimbergenBlanche_svitle_05_l_jb_parser()[2],
                "silpo": parser.beer_grimbergenBlanche_svitle_05_l_jb_parser()[3],
                "metro": parser.beer_grimbergenBlanche_svitle_05_l_jb_parser()[6],
                "fozzy": parser.beer_grimbergenBlanche_svitle_05_l_jb_parser()[8]
            }},
            {'beer_klosterkellerWeissbierChina_nefilter_svitle_05_l_jb': {
                "varus": parser.beer_klosterkellerWeissbierChina_nefilter_svitle_05_l_jb_parser()[2]
            }},
            {'beer_karpackiePils_svitle_05_l_jb': {
                "varus": parser.beer_karpackiePils_svitle_05_l_jb_parser()[2]
            }},
            {'beer_5_0_OriginalPills_svitle_05_l_jb': {
                "varus": parser.beer_5_0_OriginalPills_svitle_05_l_jb_parser()[2]
            }},
            {'beer_5_0_Original_lager_svitle_05_l_jb': {
                "varus": parser.beer_5_0_Original_lager_svitle_05_l_jb_parser()[2]
            }},
            {'beer_5_0_Original_weiss_beer_nefilter_svitle_05_l_jb': {
                "varus": parser.beer_5_0_Original_weiss_beer_nefilter_svitle_05_l_jb_parser()[2]
            }},
            {'beer_Fahnen_Brau_svitle_05_l_jb': {
                "varus": parser.beer_Fahnen_Brau_svitle_05_l_jb_parser()[2],
                "novus": parser.beer_Fahnen_Brau_svitle_05_l_jb_parser()[5]
            }},
            {'beer_Gosser_Light_svitle_05_l_jb': {
                "varus": parser.beer_Gosser_Light_svitle_05_l_jb_parser()[2],
                "silpo": parser.beer_Gosser_Light_svitle_05_l_jb_parser()[3]
            }},
            {'beer_Hollandia_Import_svitle_033_l_jb': {
                "varus": parser.beer_Hollandia_Import_svitle_033_l_jb_parser()[2]
            }},
            {'beer_Holsten_Pilsner_048_l_jb': {
                "varus": parser.beer_Holsten_Pilsner_048_l_jb_parser()[2],
                "silpo": parser.beer_Holsten_Pilsner_048_l_jb_parser()[3],
                "metro": parser.beer_Holsten_Pilsner_048_l_jb_parser()[6],
                "fozzy": parser.beer_Holsten_Pilsner_048_l_jb_parser()[8]
            }},
            {'beer_Obolon_Premium_Extra_Brew_svitle_05_l_jb': {
                "varus": parser.beer_Obolon_Premium_Extra_Brew_svitle_05_l_jb_parser()[2],
                "silpo": parser.beer_Obolon_Premium_Extra_Brew_svitle_05_l_jb_parser()[3]
            }},
            {'beer_Lvivske_svitle_48_l_jb': {
                "varus": parser.beer_Lvivske_svitle_48_l_jb_parser()[2],
                "silpo": parser.beer_Lvivske_svitle_48_l_jb_parser()[3],
                "metro": parser.beer_Lvivske_svitle_48_l_jb_parser()[6],
                "nash_kray": parser.beer_Lvivske_svitle_48_l_jb_parser()[7]
            }},
            {'beer_Carlsberg_Premium_Pilsner_svitle_05_l_jb': {
                "varus": parser.beer_Carlsberg_Premium_Pilsner_svitle_05_l_jb_parser()[2],
                "silpo": parser.beer_Carlsberg_Premium_Pilsner_svitle_05_l_jb_parser()[3]
            }},
            {'beer_Carlsberg_Pilsner_05_l_jb': {
                "varus": parser.beer_Carlsberg_Pilsner_05_l_jb_parser()[2],
                "silpo": parser.beer_Carlsberg_Pilsner_05_l_jb_parser()[3],
                "metro": parser.beer_Carlsberg_Pilsner_05_l_jb_parser()[6],
                "fozzy": parser.beer_Carlsberg_Pilsner_05_l_jb_parser()[8]
            }},

            {'banana': {
                "atb": parser.banana_parser()[0],
                "eko": parser.banana_parser()[1],
                "varus": parser.banana_parser()[2],
                "silpo": parser.banana_parser()[3] * mul_price_by_10,
                "novus": parser.banana_parser()[5],
                "metro": parser.banana_parser()[6],
                "nash_kray": parser.banana_parser()[7],
                "fozzy": parser.banana_parser()[8]
            }},

            {'orange': {
                "atb": parser.orange_parser()[0],
                "eko": parser.orange_parser()[1],
                "varus": parser.orange_parser()[2],
                "silpo": parser.orange_parser()[3] * mul_price_by_10,
                "novus": parser.orange_parser()[5],
                "metro": parser.orange_parser()[6],
                "nash_kray": parser.orange_parser()[7],
                "fozzy": parser.orange_parser()[8]
            }},

            {'kiwi': {
                "atb": parser.kiwi_parser()[0],
                "eko": parser.kiwi_parser()[1],
                "varus": parser.kiwi_parser()[2],
                "silpo": parser.kiwi_parser()[3] * mul_price_by_10,
                "metro": parser.kiwi_parser()[6],
                "nash_kray": parser.kiwi_parser()[7],
                "fozzy": parser.kiwi_parser()[8]
            }},

            {'coconut': {
                "atb": parser.coconut_parser()[0],
                "varus": parser.coconut_parser()[2],
                "silpo": parser.coconut_parser()[3] * mul_price_by_10,
                "metro": parser.coconut_parser()[6],
                "nash_kray": parser.coconut_parser()[7],
                "fozzy": parser.coconut_parser()[8]
            }},

            {'grapefruit': {
                "atb": parser.grapefruit_parser()[0],
                "eko": parser.grapefruit_parser()[1],
                "varus": parser.grapefruit_parser()[2],
                "silpo": parser.grapefruit_parser()[3] * mul_price_by_10,
                "novus": parser.grapefruit_parser()[5],
                "metro": parser.grapefruit_parser()[6],
                "nash_kray": parser.grapefruit_parser()[7],
                "fozzy": parser.grapefruit_parser()[8]
            }},

            {'pomegranate': {
                "atb": parser.pomegranate_parser()[0],
                "eko": parser.pomegranate_parser()[1],
                "varus": parser.pomegranate_parser()[2],
                "silpo": parser.pomegranate_parser()[3] * mul_price_by_10,
                "metro": parser.pomegranate_parser()[6],
                "fozzy": parser.pomegranate_parser()[8]
            }},

            {'mango': {
                "atb": parser.pomegranate_parser()[0],
                "eko": parser.pomegranate_parser()[1],
                "varus": parser.pomegranate_parser()[2],
                "silpo": parser.pomegranate_parser()[3],
                "metro": parser.pomegranate_parser()[6],
                "fozzy": parser.pomegranate_parser()[8]
            }},

            {'tomato': {
                "atb": parser.tomato_parser()[0],
                "eko": parser.tomato_parser()[1],
                "varus": parser.tomato_parser()[2],
                "metro": parser.tomato_parser()[6],
                "nash_kray": parser.tomato_parser()[7],
                "fozzy": parser.tomato_parser()[8]
            }},

            {'cucumber': {
                "atb": parser.cucumber_parser()[0],
                "eko": parser.cucumber_parser()[1],
                "varus": parser.cucumber_parser()[2],
                "silpo": parser.cucumber_parser()[3] * mul_price_by_10,
                "novus": parser.cucumber_parser()[5],
                "metro": parser.cucumber_parser()[6],
                "nash_kray": parser.cucumber_parser()[7],
                "fozzy": parser.cucumber_parser()[8]
            }},

            {'kabachki': {
                "atb": parser.kabachki_parser()[0],
                "eko": parser.kabachki_parser()[1],
                "varus": parser.kabachki_parser()[2],
                "silpo": parser.kabachki_parser()[3] * mul_price_by_10,
                "novus": parser.kabachki_parser()[5],
                "metro": parser.kabachki_parser()[6],
                "nash_kray": parser.kabachki_parser()[7],
                "fozzy": parser.kabachki_parser()[8]
            }},

            {'red_bolgar_papper': {
                "atb": parser.red_bolg_papper_parser()[0],
                "eko": parser.red_bolg_papper_parser()[1],
                "silpo": parser.red_bolg_papper_parser()[3] * mul_price_by_10,
                "novus": parser.red_bolg_papper_parser()[5],
                "metro": parser.red_bolg_papper_parser()[6],
                "nash_kray": parser.red_bolg_papper_parser()[7],
                "fozzy": parser.red_bolg_papper_parser()[8]
            }},

            {'yellow_bolgar_papper': {
                "atb": parser.yellow_bolg_papper_parser()[0],
                "silpo": parser.yellow_bolg_papper_parser()[3] * mul_price_by_10,
                "novus": parser.yellow_bolg_papper_parser()[5],
                "metro": parser.yellow_bolg_papper_parser()[6],
                "nash_kray": parser.yellow_bolg_papper_parser()[7],
                "fozzy": parser.yellow_bolg_papper_parser()[8]
            }},

            {'asparagus': {
                "atb": parser.asparagus_parser()[0],
                "varus": parser.asparagus_parser()[2],
                "silpo": parser.asparagus_parser()[3],
                "novus": parser.asparagus_parser()[5],
                "metro": parser.asparagus_parser()[6],
                "fozzy": parser.asparagus_parser()[8]
            }},

            {'brokoli': {
                "silpo": parser.brokoli_parser()[3] * mul_price_by_10,
                "novus": parser.brokoli_parser()[5],
                "nash_kray": parser.brokoli_parser()[7],
                "fozzy": parser.brokoli_parser()[8]
            }},

            {'captain_morgan_spiced_gold_1_l': {
                "eko": parser.captain_morgan_spiced_gold_1L_parser()[1],
                "varus": parser.captain_morgan_spiced_gold_1L_parser()[2],
                "silpo": parser.captain_morgan_spiced_gold_1L_parser()[3],
                "metro": parser.captain_morgan_spiced_gold_1L_parser()[6],
                "fozzy": parser.captain_morgan_spiced_gold_1L_parser()[8]
            }},

            {'captain_morgan_spiced_gold_05_l': {
                "atb": parser.captain_morgan_spiced_gold_05L_parser()[0],
                "eko": parser.captain_morgan_spiced_gold_05L_parser()[1],
                "varus": parser.captain_morgan_spiced_gold_05L_parser()[2],
                "silpo": parser.captain_morgan_spiced_gold_05L_parser()[3],
                "metro": parser.captain_morgan_spiced_gold_05L_parser()[6],
                "nash_kray": parser.captain_morgan_spiced_gold_05L_parser()[7],
                "fozzy": parser.captain_morgan_spiced_gold_05L_parser()[8]
            }},

            {'bells_original_07_l': {
                "atb": parser.bells_original_07L_parser()[0],
                "eko": parser.bells_original_07L_parser()[1],
                "varus": parser.bells_original_07L_parser()[2],
                "silpo": parser.bells_original_07L_parser()[3],
                "novus": parser.bells_original_07L_parser()[5],
                "metro": parser.bells_original_07L_parser()[6],
                "nash_kray": parser.bells_original_07L_parser()[7],
                "fozzy": parser.bells_original_07L_parser()[8]
            }},

            {'bells_original_1_l': {
                "eko": parser.bells_original_1L_parser()[1],
                "varus": parser.bells_original_1L_parser()[2],
                "silpo": parser.bells_original_1L_parser()[3],
                "novus": parser.bells_original_1L_parser()[5],
                "metro": parser.bells_original_1L_parser()[6],
                "fozzy": parser.bells_original_1L_parser()[8]
            }},

            {'bells_spiced_07_l': {
                "eko": parser.bells_spiced_07L_parser()[1],
                "varus": parser.bells_spiced_07L_parser()[2],
                "silpo": parser.bells_spiced_07L_parser()[3],
                "novus": parser.bells_spiced_07L_parser()[5],
                "metro": parser.bells_spiced_07L_parser()[6],
                "fozzy": parser.bells_spiced_07L_parser()[8]
            }},

            {'martini_asti_white_075_l': {
                "atb": parser.martini_asti_bile_075_L_parser()[0],
                "varus": parser.martini_asti_bile_075_L_parser()[2],
                "silpo": parser.martini_asti_bile_075_L_parser()[3],
                "ashan": parser.martini_asti_bile_075_L_parser()[4],
                "novus": parser.martini_asti_bile_075_L_parser()[5],
                "metro": parser.martini_asti_bile_075_L_parser()[6],
                "fozzy": parser.martini_asti_bile_075_L_parser()[8]
            }},

            {'jameson_07_l': {
                "atb": parser.jameson_07_L_parser()[0],
                "varus": parser.jameson_07_L_parser()[2],
                "silpo": parser.jameson_07_L_parser()[3],
                "ashan": parser.jameson_07_L_parser()[4],
                "novus": parser.jameson_07_L_parser()[5],
                "metro": parser.jameson_07_L_parser()[6],
                "nash_kray": parser.jameson_07_L_parser()[7],
                "fozzy": parser.jameson_07_L_parser()[8]
            }},

            {'jameson_05_l': {
                "varus": parser.jameson_07_L_parser()[2],
                "silpo": parser.jameson_07_L_parser()[3],
                "ashan": parser.jameson_07_L_parser()[4],
                "novus": parser.jameson_07_L_parser()[5],
                "metro": parser.jameson_07_L_parser()[6],
                "nash_kray": parser.jameson_07_L_parser()[7]
            }},

            {'jw_red_label_05_l': {
                "atb": parser.jw_red_label_05_L_parser()[0],
                "eko": parser.jw_red_label_05_L_parser()[1],
                "varus": parser.jw_red_label_05_L_parser()[2],
                "silpo": parser.jw_red_label_05_L_parser()[3],
                "ashan": parser.jw_red_label_05_L_parser()[4],
                "novus": parser.jw_red_label_05_L_parser()[5],
                "metro": parser.jw_red_label_05_L_parser()[6],
                "nash_kray": parser.jw_red_label_05_L_parser()[7],
                "fozzy": parser.jw_red_label_05_L_parser()[8]
            }},

            {'ballantines_finest_07_l': {
                "varus": parser.ballantines_finest_07_L_parser()[2],
                "silpo": parser.ballantines_finest_07_L_parser()[3],
                "ashan": parser.ballantines_finest_07_L_parser()[4],
                "novus": parser.ballantines_finest_07_L_parser()[5],
                "metro": parser.ballantines_finest_07_L_parser()[6],
                "fozzy": parser.ballantines_finest_07_L_parser()[8]
            }},

            {'jack_daniels_07_l': {
                "eko": parser.jack_daniels_07_L_parser()[1],
                "varus": parser.jack_daniels_07_L_parser()[2],
                "novus": parser.jack_daniels_07_L_parser()[5],
                "metro": parser.jack_daniels_07_L_parser()[6],
                "nash_kray": parser.jack_daniels_07_L_parser()[7],
                "fozzy": parser.jack_daniels_07_L_parser()[8]
            }},

            {'jack_daniels_1_l': {
                "varus": parser.jack_daniels_1_L_parser()[2],
                "silpo": parser.jack_daniels_1_L_parser()[3],
                "novus": parser.jack_daniels_1_L_parser()[5],
                "metro": parser.jack_daniels_1_L_parser()[6],
                "fozzy": parser.jack_daniels_1_L_parser()[8]
            }},

            {'jim_beam_white_07_l': {
                "atb": parser.jim_beam_white_07L_parser()[0],
                "varus": parser.jim_beam_white_07L_parser()[2],
                "silpo": parser.jim_beam_white_07L_parser()[3],
                "ashan": parser.jim_beam_white_07L_parser()[4],
                "novus": parser.jim_beam_white_07L_parser()[5],
                "metro": parser.jim_beam_white_07L_parser()[6],
                "fozzy": parser.jim_beam_white_07L_parser()[8]
            }},

            {'borjomi_05_l': {
                "varus": parser.jim_beam_white_07L_parser()[2]
            }},

            {'morshinska_negaz_15_l': {
                "atb": parser.morshinska_negaz_15L_parser()[0],
                "eko": parser.morshinska_negaz_15L_parser()[1],
                "varus": parser.morshinska_negaz_15L_parser()[2],
                "silpo": parser.morshinska_negaz_15L_parser()[3],
                "ashan": parser.morshinska_negaz_15L_parser()[4],
                "novus": parser.morshinska_negaz_15L_parser()[5],
                "nash_kray": parser.morshinska_negaz_15L_parser()[7],
                "fozzy": parser.morshinska_negaz_15L_parser()[8]
            }},

            {'morshinska_lowgaz_15_l': {
                "atb": parser.morshinska_lowgaz_15L_parser()[0],
                "eko": parser.morshinska_lowgaz_15L_parser()[1],
                "varus": parser.morshinska_lowgaz_15L_parser()[2],
                "silpo": parser.morshinska_lowgaz_15L_parser()[3],
                "ashan": parser.morshinska_lowgaz_15L_parser()[4],
                "novus": parser.morshinska_lowgaz_15L_parser()[5],
                "nash_kray": parser.morshinska_lowgaz_15L_parser()[7],
                "fozzy": parser.morshinska_lowgaz_15L_parser()[8]
            }},

            {'morshinska_highgaz_15_l': {
                "atb": parser.morshinska_highgaz_15L_parser()[0],
                "eko": parser.morshinska_highgaz_15L_parser()[1],
                "varus": parser.morshinska_highgaz_15L_parser()[2],
                "silpo": parser.morshinska_highgaz_15L_parser()[3],
                "ashan": parser.morshinska_highgaz_15L_parser()[4],
                "novus": parser.morshinska_highgaz_15L_parser()[5],
                "nash_kray": parser.morshinska_highgaz_15L_parser()[7],
                "fozzy": parser.morshinska_highgaz_15L_parser()[8]
            }},

            {'nash_sik_apple_grape_02_l': {
                "silpo": parser.nash_sik_apple_grape_02L_parser()[3],
                "ashan": parser.nash_sik_apple_grape_02L_parser()[4],
                "novus": parser.nash_sik_apple_grape_02L_parser()[5],
                "fozzy": parser.nash_sik_apple_grape_02L_parser()[8]
            }},

            {'nash_sik_apple_carrot_02_l': {
                "atb": parser.nash_sik_apple_carrot_02L_parser()[0],
                "varus": parser.nash_sik_apple_carrot_02L_parser()[2],
                "ashan": parser.nash_sik_apple_carrot_02L_parser()[4],
                "novus": parser.nash_sik_apple_carrot_02L_parser()[5],
                "fozzy": parser.nash_sik_apple_carrot_02L_parser()[8]
            }},

            {'nash_sik_orange_02_l': {
                "varus": parser.nash_sik_orange_02L_parser()[2],
                "novus": parser.nash_sik_orange_02L_parser()[5],
                "fozzy": parser.nash_sik_orange_02L_parser()[8]
            }},

            {'nash_sik_multifrukt_02_l': {
                "atb": parser.nash_sik_multifrukt_02L_parser()[0],
                "varus": parser.nash_sik_multifrukt_02L_parser()[2],
                "silpo": parser.nash_sik_multifrukt_02L_parser()[3],
                "novus": parser.nash_sik_multifrukt_02L_parser()[5],
                "metro": parser.nash_sik_multifrukt_02L_parser()[6],
                "fozzy": parser.nash_sik_multifrukt_02L_parser()[8]
            }},

            {'nash_sik_apple_peach_02_l': {
                "atb": parser.nash_sik_apple_peach_02L_parser()[0],
                "varus": parser.nash_sik_apple_peach_02L_parser()[2],
                "silpo": parser.nash_sik_apple_peach_02L_parser()[3],
                "novus": parser.nash_sik_apple_peach_02L_parser()[5]
            }},

            {'nash_sik_pear_apple_02_l': {
                "varus": parser.nash_sik_pear_apple_02L_parser()[2],
                "silpo": parser.nash_sik_pear_apple_02L_parser()[3],
                "novus": parser.nash_sik_pear_apple_02L_parser()[5]
            }},

            {'nash_sik_multivitamin_02_l': {
                "varus": parser.nash_sik_multivitamin_02L_parser()[2],
                "silpo": parser.nash_sik_multivitamin_02L_parser()[3],
                "ashan": parser.nash_sik_multivitamin_02L_parser()[4],
                "novus": parser.nash_sik_multivitamin_02L_parser()[5],
                "fozzy": parser.nash_sik_multivitamin_02L_parser()[8]
            }},

            {'nash_sik_apple_02_l': {
                "atb": parser.nash_sik_apple_02L_parser()[0],
                "varus": parser.nash_sik_apple_02L_parser()[2],
                "silpo": parser.nash_sik_apple_02L_parser()[3],
                "ashan": parser.nash_sik_apple_02L_parser()[4],
                "novus": parser.nash_sik_apple_02L_parser()[5],
                "metro": parser.nash_sik_apple_02L_parser()[6],
                "fozzy": parser.nash_sik_apple_02L_parser()[8]
            }},

            {'nash_sik_apple_strawberry_02_l': {
                "varus": parser.nash_sik_apple_strawberry_02L_parser()[2],
                "silpo": parser.nash_sik_apple_strawberry_02L_parser()[3],
                "novus": parser.nash_sik_apple_strawberry_02L_parser()[5],
                "metro": parser.nash_sik_apple_strawberry_02L_parser()[6],
                "fozzy": parser.nash_sik_apple_strawberry_02L_parser()[8]
            }},

            {'non_stop_original_025_l': {
                "atb": parser.non_stop_original_025L_parser()[0],
                "eko": parser.non_stop_original_025L_parser()[1],
                "varus": parser.non_stop_original_025L_parser()[2],
                "silpo": parser.non_stop_original_025L_parser()[3],
                "ashan": parser.non_stop_original_025L_parser()[4],
                "novus": parser.non_stop_original_025L_parser()[5],
                "metro": parser.non_stop_original_025L_parser()[6],
                "fozzy": parser.non_stop_original_025L_parser()[8]
            }},

            {'non_stop_original_05_l': {
                "atb": parser.non_stop_original_05L_parser()[0],
                "varus": parser.non_stop_original_05L_parser()[2],
                "silpo": parser.non_stop_original_05L_parser()[3],
                "ashan": parser.non_stop_original_05L_parser()[4],
                "novus": parser.non_stop_original_05L_parser()[5],
                "metro": parser.non_stop_original_05L_parser()[6],
                "fozzy": parser.non_stop_original_05L_parser()[8]
            }},

            {'non_stop_jungle_025_l': {
                "eko": parser.non_stop_jungle_025L_parser()[1],
                "varus": parser.non_stop_jungle_025L_parser()[2],
                "silpo": parser.non_stop_jungle_025L_parser()[3],
                "ashan": parser.non_stop_jungle_025L_parser()[4],
                "novus": parser.non_stop_jungle_025L_parser()[5],
                "metro": parser.non_stop_jungle_025L_parser()[6],
                "fozzy": parser.non_stop_jungle_025L_parser()[8]
            }},

            {'non_stop_boost_05_l': {
                "eko": parser.non_stop_boost_05L_parser()[1],
                "varus": parser.non_stop_boost_05L_parser()[2],
                "silpo": parser.non_stop_boost_05L_parser()[3],
                "ashan": parser.non_stop_boost_05L_parser()[4],
                "novus": parser.non_stop_boost_05L_parser()[5],
                "metro": parser.non_stop_boost_05L_parser()[6],
                "fozzy": parser.non_stop_boost_05L_parser()[8]
            }},

            {'non_stop_ultra_05_l': {
                "eko": parser.non_stop_ultra_05L_parser()[1],
                "varus": parser.non_stop_ultra_05L_parser()[2],
                "silpo": parser.non_stop_ultra_05L_parser()[3],
                "metro": parser.non_stop_ultra_05L_parser()[6],
                "fozzy": parser.non_stop_ultra_05L_parser()[8]
            }},

            {'non_stop_boost_025_l': {
                "eko": parser.non_stop_boost_025L_parser()[1],
                "varus": parser.non_stop_boost_025L_parser()[2],
                "silpo": parser.non_stop_boost_025L_parser()[3],
                "metro": parser.non_stop_boost_025L_parser()[6],
                "fozzy": parser.non_stop_boost_025L_parser()[8]
            }},

            {'burn_classic_025_l': {
                "eko": parser.burn_classic_025L_parser()[1],
                "varus": parser.burn_classic_025L_parser()[2],
                "silpo": parser.burn_classic_025L_parser()[3],
                "ashan": parser.burn_classic_025L_parser()[4],
                "novus": parser.burn_classic_025L_parser()[5],
                "metro": parser.burn_classic_025L_parser()[6],
                "fozzy": parser.burn_classic_025L_parser()[8]
            }},

            {'burn_classic_05_l': {
                "atb": parser.burn_classic_05L_parser()[0],
                "eko": parser.burn_classic_05L_parser()[1],
                "varus": parser.burn_classic_05L_parser()[2],
                "silpo": parser.burn_classic_05L_parser()[3],
                "ashan": parser.burn_classic_05L_parser()[4],
                "novus": parser.burn_classic_05L_parser()[5],
                "metro": parser.burn_classic_05L_parser()[6],
                "fozzy": parser.burn_classic_05L_parser()[8]
            }},

            {'burn_mango_025_l': {
                "eko": parser.burn_mango_025L_parser()[1],
                "varus": parser.burn_mango_025L_parser()[2],
                "silpo": parser.burn_mango_025L_parser()[3],
                "novus": parser.burn_mango_025L_parser()[5],
                "fozzy": parser.burn_mango_025L_parser()[8]
            }},

            {'burn_apple_kiwi_05_l': {
                "eko": parser.burn_apple_kiwi_05L_parser()[1],
                "varus": parser.burn_apple_kiwi_05L_parser()[2],
                "silpo": parser.burn_apple_kiwi_05L_parser()[3],
                "ashan": parser.burn_apple_kiwi_05L_parser()[4],
                "novus": parser.burn_apple_kiwi_05L_parser()[5],
                "metro": parser.burn_apple_kiwi_05L_parser()[6],
                "fozzy": parser.burn_apple_kiwi_05L_parser()[8]
            }},

            {'burn_dark_energy_025_l': {
                "eko": parser.burn_dark_energy_025L_parser()[1],
                "varus": parser.burn_dark_energy_025L_parser()[2],
                "silpo": parser.burn_dark_energy_025L_parser()[3],
                "novus": parser.burn_dark_energy_025L_parser()[5]
            }},

            {'red_bull_025_l': {
                "atb": parser.red_bull_025L_parser()[0],
                "silpo": parser.red_bull_025L_parser()[3],
                "ashan": parser.red_bull_025L_parser()[4],
                "novus": parser.red_bull_025L_parser()[5],
                "metro": parser.red_bull_025L_parser()[6],
                "fozzy": parser.red_bull_025L_parser()[8]
            }},

            {'red_bull_0355_l': {
                "atb": parser.red_bull_0355L_parser()[0],
                "varus": parser.red_bull_0355L_parser()[2],
                "silpo": parser.red_bull_0355L_parser()[3],
                "ashan": parser.red_bull_0355L_parser()[4],
                "novus": parser.red_bull_0355L_parser()[5],
                "metro": parser.red_bull_0355L_parser()[6],
                "fozzy": parser.red_bull_0355L_parser()[8]
            }},

            {'red_bull_0473_l': {
                "atb": parser.red_bull_0473L_parser()[0],
                "varus": parser.red_bull_0473L_parser()[2],
                "silpo": parser.red_bull_0473L_parser()[3],
                "ashan": parser.red_bull_0473L_parser()[4],
                "novus": parser.red_bull_0473L_parser()[5],
                "metro": parser.red_bull_0473L_parser()[6],
                "fozzy": parser.red_bull_0473L_parser()[8]
            }},

            {'red_bull_0591_l': {
                "varus": parser.red_bull_0591L_parser()[2],
                "silpo": parser.red_bull_0591L_parser()[3],
                "novus": parser.red_bull_0591L_parser()[5],
                "fozzy": parser.red_bull_0591L_parser()[8]
            }},

            {'red_bull_sugar_free_025_l': {
                "varus": parser.red_bull_sugar_free_025L_parser()[2],
                "silpo": parser.red_bull_sugar_free_025L_parser()[3],
                "ashan": parser.red_bull_sugar_free_025L_parser()[4],
                "novus": parser.red_bull_sugar_free_025L_parser()[5],
                "metro": parser.red_bull_sugar_free_025L_parser()[6],
                "fozzy": parser.red_bull_sugar_free_025L_parser()[8]
            }},

            {'red_bull_red_edition_cavun_025_l': {
                "varus": parser.red_bull_red_edition_cavun_025L_parser()[2],
                "silpo": parser.red_bull_red_edition_cavun_025L_parser()[3],
                "novus": parser.red_bull_red_edition_cavun_025L_parser()[5],
                "fozzy": parser.red_bull_red_edition_cavun_025L_parser()[8]
            }},

            {'red_bull_yellow_edition_tropic_fruits_025_l': {
                "varus": parser.red_bull_yellow_edition_tropic_fruits_025L_parser()[2],
                "silpo": parser.red_bull_yellow_edition_tropic_fruits_025L_parser()[3],
                "ashan": parser.red_bull_yellow_edition_tropic_fruits_025L_parser()[4],
                "novus": parser.red_bull_yellow_edition_tropic_fruits_025L_parser()[5],
                "metro": parser.red_bull_yellow_edition_tropic_fruits_025L_parser()[6],
                "fozzy": parser.red_bull_yellow_edition_tropic_fruits_025L_parser()[8]
            }},

            {'monster_0355_l': {
                "eko": parser.monster_0355L_parser()[1],
                "silpo": parser.monster_0355L_parser()[3],
                "ashan": parser.monster_0355L_parser()[4],
                "novus": parser.monster_0355L_parser()[5],
                "metro": parser.monster_0355L_parser()[6],
                "nash_kray": parser.monster_0355L_parser()[7],
                "fozzy": parser.monster_0355L_parser()[8]
            }},

            {'monster_the_doctor_0355_l': {
                "eko": parser.monster_the_doctor_0355L_parser()[1],
                "varus": parser.monster_the_doctor_0355L_parser()[2],
                "silpo": parser.monster_the_doctor_0355L_parser()[3],
                "ashan": parser.monster_the_doctor_0355L_parser()[4],
                "novus": parser.monster_the_doctor_0355L_parser()[5],
                "metro": parser.monster_the_doctor_0355L_parser()[6],
                "nash_kray": parser.monster_the_doctor_0355L_parser()[7],
                "fozzy": parser.monster_the_doctor_0355L_parser()[8]
            }},

            {'monster_ultra_zero_0355_l': {
                "eko": parser.monster_ultra_zero_0355L_parser()[1],
                "varus": parser.monster_ultra_zero_0355L_parser()[2],
                "silpo": parser.monster_ultra_zero_0355L_parser()[3],
                "ashan": parser.monster_ultra_zero_0355L_parser()[4],
                "novus": parser.monster_ultra_zero_0355L_parser()[5],
                "metro": parser.monster_ultra_zero_0355L_parser()[6],
                "nash_kray": parser.monster_ultra_zero_0355L_parser()[7],
                "fozzy": parser.monster_ultra_zero_0355L_parser()[8]
            }},

            {'monster_juiced_0355_l': {
                "eko": parser.monster_juiced_0355L_parser()[1],
                "varus": parser.monster_juiced_0355L_parser()[2],
                "silpo": parser.monster_juiced_0355L_parser()[3],
                "novus": parser.monster_juiced_0355L_parser()[5],
                "metro": parser.monster_juiced_0355L_parser()[6],
                "nash_kray": parser.monster_juiced_0355L_parser()[7],
                "fozzy": parser.monster_juiced_0355L_parser()[8]
            }},

            {'pit_bull_coffee_0250_l': {
                "atb": parser.pit_bull_coffee_250L_parser()[0],
                "eko": parser.pit_bull_coffee_250L_parser()[1],
                "silpo": parser.pit_bull_coffee_250L_parser()[3],
                "novus": parser.pit_bull_coffee_250L_parser()[5],
                "fozzy": parser.pit_bull_coffee_250L_parser()[8]
            }},

            {'pit_bull_power_0250_l': {
                "atb": parser.pit_bull_power_250L_parser()[0],
                "eko": parser.pit_bull_power_250L_parser()[1],
                "varus": parser.pit_bull_power_250L_parser()[2],
                "silpo": parser.pit_bull_power_250L_parser()[3],
                "novus": parser.pit_bull_power_250L_parser()[5],
                "metro": parser.pit_bull_power_250L_parser()[6],
                "fozzy": parser.pit_bull_power_250L_parser()[8]
            }}
        ]
        # далее записываем цены в json-файл
        write_prices_to_json(all_products_names_batch_3, batch_3_path, mode_type_first_write)

    # для 4-го батча
    elif batch_name == batch_name_4:
        all_products_names_batch_4 = [
            {'pit_bull_X_0250_l': {
                "eko": parser.pit_bull_X_250L_parser()[1],
                "varus": parser.pit_bull_X_250L_parser()[2],
                "silpo": parser.pit_bull_X_250L_parser()[3],
                "novus": parser.pit_bull_X_250L_parser()[5],
                "fozzy": parser.pit_bull_X_250L_parser()[8]
            }},

            {'pit_bull_extra_vitamin_c_0250_l': {
                "eko": parser.pit_bull_extra_vitamin_C_250L_parser()[1],
                "varus": parser.pit_bull_extra_vitamin_C_250L_parser()[2],
                "silpo": parser.pit_bull_extra_vitamin_C_250L_parser()[3],
                "metro": parser.pit_bull_extra_vitamin_C_250L_parser()[6],
                "fozzy": parser.pit_bull_extra_vitamin_C_250L_parser()[8]
            }},

            {'pit_bull_0250_l': {
                "varus": parser.pit_bull_250L_parser()[2],
                "ashan": parser.pit_bull_250L_parser()[4]
            }},

            {'maccoffee_gold_rozch_soft_pack_60_gr': {
                "silpo": parser.maccoffee_gold_rozch_soft_pack_60_gr_parser()[3],
                "fozzy": parser.maccoffee_gold_rozch_soft_pack_60_gr_parser()[8]
            }},

            {'nescafe_gold_rozch_soft_pack_120_gr': {
                "varus": parser.nescafe_gold_rozch_soft_pack_120_gr_parser()[2],
                "silpo": parser.nescafe_gold_rozch_soft_pack_120_gr_parser()[3],
                "ashan": parser.nescafe_gold_rozch_soft_pack_120_gr_parser()[4],
                "novus": parser.nescafe_gold_rozch_soft_pack_120_gr_parser()[5],
                "metro": parser.nescafe_gold_rozch_soft_pack_120_gr_parser()[6],
                "fozzy": parser.nescafe_gold_rozch_soft_pack_120_gr_parser()[8]
            }},

            {'grano_dorado_gold_rozch_soft_pack_130_gr': {
                "fozzy": parser.grano_dorado_gold_soft_pack_130_gr_parser()[8]
            }},

            {'nescafe_classic_soft_pack_60_gr': {
                "eko": parser.nescafe_classic_soft_pack_60_gr_parser()[1],
                "varus": parser.nescafe_classic_soft_pack_60_gr_parser()[2],
                "silpo": parser.nescafe_classic_soft_pack_60_gr_parser()[3],
                "ashan": parser.nescafe_classic_soft_pack_60_gr_parser()[4],
                "novus": parser.nescafe_classic_soft_pack_60_gr_parser()[5],
                "metro": parser.nescafe_classic_soft_pack_60_gr_parser()[6],
                "fozzy": parser.nescafe_classic_soft_pack_60_gr_parser()[8]
            }},

            {'chorna_karta_gold_soft_pack_400_gr': {
                "silpo": parser.chorna_karta_gold_soft_pack_400_gr_parser()[3],
                "ashan": parser.chorna_karta_gold_soft_pack_400_gr_parser()[4],
                "novus": parser.chorna_karta_gold_soft_pack_400_gr_parser()[5],
                "fozzy": parser.chorna_karta_gold_soft_pack_400_gr_parser()[8]
            }},

            {'bounty_57gr': {
                "atb": parser.bounty_small_gr_parser()[0],
                "eko": parser.bounty_small_gr_parser()[1],
                "varus": parser.bounty_small_gr_parser()[2],
                "silpo": parser.bounty_small_gr_parser()[3],
                "ashan": parser.bounty_small_gr_parser()[4],
                "novus": parser.bounty_small_gr_parser()[5],
                "metro": parser.bounty_small_gr_parser()[6],
                "nash_kray": parser.bounty_small_gr_parser()[7],
                "fozzy": parser.bounty_small_gr_parser()[8]
            }},

            {'bounty_85gr': {
                "atb": parser.bounty_big_gr_parser()[0],
                "eko": parser.bounty_big_gr_parser()[1],
                "varus": parser.bounty_big_gr_parser()[2],
                "silpo": parser.bounty_big_gr_parser()[3],
                "ashan": parser.bounty_big_gr_parser()[4],
                "novus": parser.bounty_big_gr_parser()[5],
                "metro": parser.bounty_big_gr_parser()[6],
                "fozzy": parser.bounty_big_gr_parser()[8]
            }},

            {'mars_51gr': {
                "eko": parser.mars_51gr_parser()[1],
                "varus": parser.mars_51gr_parser()[2],
                "silpo": parser.mars_51gr_parser()[3],
                "metro": parser.mars_51gr_parser()[6],
                "nash_kray": parser.mars_51gr_parser()[7],
                "fozzy": parser.mars_51gr_parser()[8]
            }},

            {'mars_70gr': {
                "atb": parser.mars_70gr_parser()[0],
                "eko": parser.mars_70gr_parser()[1],
                "varus": parser.mars_70gr_parser()[2],
                "silpo": parser.mars_70gr_parser()[3],
                "novus": parser.mars_70gr_parser()[5],
                "metro": parser.mars_70gr_parser()[6],
                "nash_kray": parser.mars_70gr_parser()[7],
                "fozzy": parser.mars_70gr_parser()[8]
            }},

            {'nuts_strawberry': {
                "eko": parser.nuts_strawberry_parser()[1],
                "varus": parser.nuts_strawberry_parser()[2],
                "silpo": parser.nuts_strawberry_parser()[3],
                "ashan": parser.nuts_strawberry_parser()[4],
                "metro": parser.nuts_strawberry_parser()[6],
                "fozzy": parser.nuts_strawberry_parser()[8]
            }},

            {'nuts_42gr': {
                "eko": parser.nuts_42gr_parser()[1],
                "varus": parser.nuts_42gr_parser()[2],
                "silpo": parser.nuts_42gr_parser()[3],
                "ashan": parser.nuts_42gr_parser()[4],
                "novus": parser.nuts_42gr_parser()[5],
                "metro": parser.nuts_42gr_parser()[6],
                "nash_kray": parser.nuts_42gr_parser()[7],
                "fozzy": parser.nuts_42gr_parser()[8]
            }},

            {'nuts_king_size_60gr': {
                "eko": parser.nuts_king_size_60gr_parser()[1],
                "varus": parser.nuts_king_size_60gr_parser()[2],
                "ashan": parser.nuts_king_size_60gr_parser()[4],
                "novus": parser.nuts_king_size_60gr_parser()[5],
                "metro": parser.nuts_king_size_60gr_parser()[6],
                "nash_kray": parser.nuts_king_size_60gr_parser()[7],
                "fozzy": parser.nuts_king_size_60gr_parser()[8]
            }},

            {'snickers_50gr': {
                "atb": parser.snickers_50gr_parser()[0],
                "eko": parser.snickers_50gr_parser()[1],
                "varus": parser.snickers_50gr_parser()[2],
                "silpo": parser.snickers_50gr_parser()[3],
                "ashan": parser.snickers_50gr_parser()[4],
                "novus": parser.snickers_50gr_parser()[5],
                "metro": parser.snickers_50gr_parser()[6],
                "nash_kray": parser.snickers_50gr_parser()[7],
                "fozzy": parser.snickers_50gr_parser()[8]
            }},

            {'snickers_super_112_5gr': {
                "atb": parser.snickers_super_112_5gr_parser()[0],
                "varus": parser.snickers_super_112_5gr_parser()[2],
                "silpo": parser.snickers_super_112_5gr_parser()[3],
                "ashan": parser.snickers_super_112_5gr_parser()[4],
                "novus": parser.snickers_super_112_5gr_parser()[5],
                "metro": parser.snickers_super_112_5gr_parser()[6],
                "nash_kray": parser.snickers_super_112_5gr_parser()[7],
                "fozzy": parser.snickers_super_112_5gr_parser()[8]
            }},

            {'snickers_creamy_peanut_butter_54_75gr': {
                "atb": parser.snickers_creamy_peanut_butter_54_75gr_parser()[0],
                "eko": parser.snickers_creamy_peanut_butter_54_75gr_parser()[1],
                "varus": parser.snickers_creamy_peanut_butter_54_75gr_parser()[2],
                "silpo": parser.snickers_creamy_peanut_butter_54_75gr_parser()[3],
                "ashan": parser.snickers_creamy_peanut_butter_54_75gr_parser()[4],
                "metro": parser.snickers_creamy_peanut_butter_54_75gr_parser()[6],
                "nash_kray": parser.snickers_creamy_peanut_butter_54_75gr_parser()[7],
                "fozzy": parser.snickers_creamy_peanut_butter_54_75gr_parser()[8]
            }},

            {'snickers_creamy_peanut_butter_36_5gr': {
                "varus": parser.snickers_creamy_peanut_butter_36_5gr_parser()[2],
                "silpo": parser.snickers_creamy_peanut_butter_36_5gr_parser()[3],
                "ashan": parser.snickers_creamy_peanut_butter_36_5gr_parser()[4],
                "metro": parser.snickers_creamy_peanut_butter_36_5gr_parser()[6],
                "nash_kray": parser.snickers_creamy_peanut_butter_36_5gr_parser()[7],
                "fozzy": parser.snickers_creamy_peanut_butter_36_5gr_parser()[8]
            }},

            {'twix_50gr': {
                "atb": parser.twix_50gr_parser()[0],
                "eko": parser.twix_50gr_parser()[1],
                "varus": parser.twix_50gr_parser()[2],
                "silpo": parser.twix_50gr_parser()[3],
                "ashan": parser.twix_50gr_parser()[4],
                "novus": parser.twix_50gr_parser()[5],
                "metro": parser.twix_50gr_parser()[6],
                "nash_kray": parser.twix_50gr_parser()[7],
                "fozzy": parser.twix_50gr_parser()[8]
            }},

            {'twix_75gr': {
                "atb": parser.twix_75gr_parser()[0],
                "eko": parser.twix_75gr_parser()[1],
                "varus": parser.twix_75gr_parser()[2],
                "silpo": parser.twix_75gr_parser()[3],
                "ashan": parser.twix_75gr_parser()[4],
                "novus": parser.twix_75gr_parser()[5],
                "metro": parser.twix_75gr_parser()[6],
                "nash_kray": parser.twix_75gr_parser()[7],
                "fozzy": parser.twix_75gr_parser()[8]
            }},

            {'vodka_absolut_05l': {
                "eko": parser.vodka_absolut_05l_parser()[1],
                "varus": parser.vodka_absolut_05l_parser()[2],
                "silpo": parser.vodka_absolut_05l_parser()[3],
                "ashan": parser.vodka_absolut_05l_parser()[4],
                "novus": parser.vodka_absolut_05l_parser()[5],
                "metro": parser.vodka_absolut_05l_parser()[6],
                "nash_kray": parser.vodka_absolut_05l_parser()[7],
                "fozzy": parser.vodka_absolut_05l_parser()[8]
            }},

            {'vodka_absolut_1l': {
                "varus": parser.vodka_absolut_1l_parser()[2],
                "silpo": parser.vodka_absolut_1l_parser()[3],
                "ashan": parser.vodka_absolut_1l_parser()[4],
                "novus": parser.vodka_absolut_1l_parser()[5],
                "metro": parser.vodka_absolut_1l_parser()[6],
                "fozzy": parser.vodka_absolut_1l_parser()[8]
            }},

            {'vodka_absolut_07l': {
                "varus": parser.vodka_absolut_07l_parser()[2],
                "silpo": parser.vodka_absolut_07l_parser()[3],
                "ashan": parser.vodka_absolut_07l_parser()[4],
                "novus": parser.vodka_absolut_07l_parser()[5],
                "metro": parser.vodka_absolut_07l_parser()[6],
                "fozzy": parser.vodka_absolut_07l_parser()[8]
            }},

            {'vodka_absolut_lime_07l': {
                "eko": parser.vodka_absolut_lime_07l_parser()[1],
                "silpo": parser.vodka_absolut_lime_07l_parser()[3],
                "ashan": parser.vodka_absolut_lime_07l_parser()[4],
                "novus": parser.vodka_absolut_lime_07l_parser()[5],
                "metro": parser.vodka_absolut_lime_07l_parser()[6],
                "fozzy": parser.vodka_absolut_lime_07l_parser()[8]
            }},

            {'vodka_absolut_grapefruit_07l': {
                "silpo": parser.vodka_absolut_grapefruit_07l_parser()[3],
                "ashan": parser.vodka_absolut_grapefruit_07l_parser()[4],
                "novus": parser.vodka_absolut_grapefruit_07l_parser()[5],
                "metro": parser.vodka_absolut_grapefruit_07l_parser()[6],
                "fozzy": parser.vodka_absolut_grapefruit_07l_parser()[8]
            }},

            {'vodka_absolut_elyx_07l': {
                "ashan": parser.vodka_absolut_elyx_07l_parser()[4],
                "fozzy": parser.vodka_absolut_elyx_07l_parser()[8]
            }},

            {'vodka_absolut_citron_07l': {
                "varus": parser.vodka_absolut_citron_07l_parser()[2],
                "silpo": parser.vodka_absolut_citron_07l_parser()[3],
                "ashan": parser.vodka_absolut_citron_07l_parser()[4],
                "novus": parser.vodka_absolut_citron_07l_parser()[5],
                "metro": parser.vodka_absolut_citron_07l_parser()[6],
                "fozzy": parser.vodka_absolut_citron_07l_parser()[8]
            }},

            {'vodka_absolut_kurant_07l': {
                "silpo": parser.vodka_absolut_kurant_07l_parser()[3],
                "ashan": parser.vodka_absolut_kurant_07l_parser()[4],
                "novus": parser.vodka_absolut_kurant_07l_parser()[5],
                "metro": parser.vodka_absolut_kurant_07l_parser()[6],
                "fozzy": parser.vodka_absolut_kurant_07l_parser()[8]
            }},

            {'vodka_absolut_watermelon_07l': {
                "silpo": parser.vodka_absolut_watermelon_07l_parser()[3],
                "ashan": parser.vodka_absolut_watermelon_07l_parser()[4],
                "novus": parser.vodka_absolut_watermelon_07l_parser()[5],
                "metro": parser.vodka_absolut_watermelon_07l_parser()[6],
                "fozzy": parser.vodka_absolut_watermelon_07l_parser()[8]
            }},

            {'vodka_absolut_mandarin_07l': {
                "silpo": parser.vodka_absolut_mandarin_07l_parser()[3],
                "novus": parser.vodka_absolut_mandarin_07l_parser()[5],
                "fozzy": parser.vodka_absolut_mandarin_07l_parser()[8]
            }},

            {'vodka_finland_05l': {
                "atb": parser.vodka_finland_05l_parser()[0],
                "eko": parser.vodka_finland_05l_parser()[1],
                "silpo": parser.vodka_finland_05l_parser()[3],
                "ashan": parser.vodka_finland_05l_parser()[4],
                "novus": parser.vodka_finland_05l_parser()[5],
                "metro": parser.vodka_finland_05l_parser()[6],
                "nash_kray": parser.vodka_finland_05l_parser()[7],
                "fozzy": parser.vodka_finland_05l_parser()[8]
            }},

            {'vodka_finland_07l': {
                "eko": parser.vodka_finland_07l_parser()[1],
                "varus": parser.vodka_finland_07l_parser()[2],
                "silpo": parser.vodka_finland_07l_parser()[3],
                "ashan": parser.vodka_finland_07l_parser()[4],
                "novus": parser.vodka_finland_07l_parser()[5],
                "metro": parser.vodka_finland_07l_parser()[6],
                "fozzy": parser.vodka_finland_07l_parser()[8]
            }},

            {'vodka_finland_1l': {
                "eko": parser.vodka_finland_1l_parser()[1],
                "varus": parser.vodka_finland_1l_parser()[2],
                "silpo": parser.vodka_finland_1l_parser()[3],
                "ashan": parser.vodka_finland_1l_parser()[4],
                "novus": parser.vodka_finland_1l_parser()[5],
                "metro": parser.vodka_finland_1l_parser()[6],
                "fozzy": parser.vodka_finland_1l_parser()[8]
            }},

            {'vodka_finland_redberry_05l': {
                "varus": parser.vodka_finland_redberry_05l_parser()[2],
                "silpo": parser.vodka_finland_redberry_05l_parser()[3],
                "ashan": parser.vodka_finland_redberry_05l_parser()[4],
                "metro": parser.vodka_finland_redberry_05l_parser()[6],
                "nash_kray": parser.vodka_finland_redberry_05l_parser()[7],
                "fozzy": parser.vodka_finland_redberry_05l_parser()[8]
            }},

            {'vodka_finland_redberry_1l': {
                "silpo": parser.vodka_finland_redberry_1l_parser()[3],
                "novus": parser.vodka_finland_redberry_1l_parser()[5],
            }},

            {'vodka_finland_cranberry_05l': {
                "atb": parser.vodka_finland_cranberry_05l_parser()[0],
                "eko": parser.vodka_finland_cranberry_05l_parser()[1],
                "silpo": parser.vodka_finland_cranberry_05l_parser()[3],
                "ashan": parser.vodka_finland_cranberry_05l_parser()[4],
                "novus": parser.vodka_finland_cranberry_05l_parser()[5],
                "metro": parser.vodka_finland_cranberry_05l_parser()[6],
                "nash_kray": parser.vodka_finland_cranberry_05l_parser()[7],
                "fozzy": parser.vodka_finland_cranberry_05l_parser()[8]
            }},

            {'vodka_finland_cranberry_1l': {
                "eko": parser.vodka_finland_cranberry_1l_parser()[1],
                "silpo": parser.vodka_finland_cranberry_1l_parser()[3],
                "novus": parser.vodka_finland_cranberry_1l_parser()[5],
                "metro": parser.vodka_finland_cranberry_1l_parser()[6],
                "fozzy": parser.vodka_finland_cranberry_1l_parser()[8]
            }},

            {'vodka_finland_grapefruit_05l': {
                "eko": parser.vodka_finland_grapefruit_05l_parser()[1],
                "varus": parser.vodka_finland_grapefruit_05l_parser()[2],
                "silpo": parser.vodka_finland_grapefruit_05l_parser()[3],
                "ashan": parser.vodka_finland_grapefruit_05l_parser()[4],
                "novus": parser.vodka_finland_grapefruit_05l_parser()[5],
                "metro": parser.vodka_finland_grapefruit_05l_parser()[6],
                "nash_kray": parser.vodka_finland_grapefruit_05l_parser()[7],
                "fozzy": parser.vodka_finland_grapefruit_05l_parser()[8]
            }},

            {'vodka_finland_lime_05l': {
                "eko": parser.vodka_finland_lime_05l_parser()[1],
                "varus": parser.vodka_finland_lime_05l_parser()[2],
                "silpo": parser.vodka_finland_lime_05l_parser()[3],
                "ashan": parser.vodka_finland_lime_05l_parser()[4],
                "novus": parser.vodka_finland_lime_05l_parser()[5],
                "metro": parser.vodka_finland_lime_05l_parser()[6],
                "nash_kray": parser.vodka_finland_lime_05l_parser()[7],
                "fozzy": parser.vodka_finland_lime_05l_parser()[8]
            }},

            {'vodka_finland_coconut_05l': {
                "eko": parser.vodka_finland_coconut_05l_parser()[1],
                "silpo": parser.vodka_finland_coconut_05l_parser()[3],
                "ashan": parser.vodka_finland_coconut_05l_parser()[4],
                "novus": parser.vodka_finland_coconut_05l_parser()[5],
                "metro": parser.vodka_finland_coconut_05l_parser()[6],
                "nash_kray": parser.vodka_finland_coconut_05l_parser()[7],
                "fozzy": parser.vodka_finland_coconut_05l_parser()[8]
            }},

            {'vodka_finland_blackcurrant_05l': {
                "varus": parser.vodka_finland_blackcurrant_05l_parser()[2],
                "silpo": parser.vodka_finland_blackcurrant_05l_parser()[3],
                "fozzy": parser.vodka_finland_blackcurrant_05l_parser()[8]
            }},

            {'vodka_finland_lime_1l': {
                "silpo": parser.vodka_finland_lime_1l_parser()[3],
                "novus": parser.vodka_finland_lime_1l_parser()[5],
                "metro": parser.vodka_finland_lime_1l_parser()[6],
                "fozzy": parser.vodka_finland_lime_1l_parser()[8]
            }},

            {'vodka_finland_blackcurrant_1l': {
                "silpo": parser.vodka_finland_blackcurrant_1l_parser()[3],
                "novus": parser.vodka_finland_blackcurrant_1l_parser()[5],
                "metro": parser.vodka_finland_blackcurrant_1l_parser()[6],
                "fozzy": parser.vodka_finland_blackcurrant_1l_parser()[8]
            }},

            {'vodka_finland_grapefruit_1l': {
                "silpo": parser.vodka_finland_grapefruit_1l_parser()[3],
                "novus": parser.vodka_finland_grapefruit_1l_parser()[5],
                "metro": parser.vodka_finland_grapefruit_1l_parser()[6],
                "fozzy": parser.vodka_finland_grapefruit_1l_parser()[8]
            }},

            {'vodka_finland_white_175l': {
                "novus": parser.vodka_finland_grapefruit_1l_parser()[5],
                "fozzy": parser.vodka_finland_grapefruit_1l_parser()[8]
            }},

            {'nemiroff_delicat_05l': {
                "atb": parser.vodka_nemiroff_delicat_soft_05l_parser()[0],
                "eko": parser.vodka_nemiroff_delicat_soft_05l_parser()[1],
                "silpo": parser.vodka_nemiroff_delicat_soft_05l_parser()[3],
                "novus": parser.vodka_nemiroff_delicat_soft_05l_parser()[5],
                "metro": parser.vodka_nemiroff_delicat_soft_05l_parser()[6],
                "nash_kray": parser.vodka_nemiroff_delicat_soft_05l_parser()[7],
                "fozzy": parser.vodka_nemiroff_delicat_soft_05l_parser()[8]
            }},

            {'nemiroff_shtof_05l': {
                "atb": parser.vodka_nemiroff_shtof_05l_parser()[0],
                "eko": parser.vodka_nemiroff_shtof_05l_parser()[1],
                "varus": parser.vodka_nemiroff_shtof_05l_parser()[2],
                "silpo": parser.vodka_nemiroff_shtof_05l_parser()[3],
                "novus": parser.vodka_nemiroff_shtof_05l_parser()[5],
                "metro": parser.vodka_nemiroff_shtof_05l_parser()[6],
                "fozzy": parser.vodka_nemiroff_shtof_05l_parser()[8]
            }},

            {'nemiroff_ukr_pshen_05l': {
                "atb": parser.vodka_nemiroff_ukr_pshen_05l_parser()[0],
                "eko": parser.vodka_nemiroff_ukr_pshen_05l_parser()[1],
                "varus": parser.vodka_nemiroff_ukr_pshen_05l_parser()[2],
                "silpo": parser.vodka_nemiroff_ukr_pshen_05l_parser()[3],
                "novus": parser.vodka_nemiroff_ukr_pshen_05l_parser()[5],
                "fozzy": parser.vodka_nemiroff_ukr_pshen_05l_parser()[8]
            }},

            {'nemiroff_delux_05l': {
                "varus": parser.vodka_nemiroff_delux_05l_parser()[2],
                "silpo": parser.vodka_nemiroff_delux_05l_parser()[3],
                "ashan": parser.vodka_nemiroff_delux_05l_parser()[4],
                "novus": parser.vodka_nemiroff_delux_05l_parser()[5],
                "nash_kray": parser.vodka_nemiroff_delux_05l_parser()[7],
                "fozzy": parser.vodka_nemiroff_delux_05l_parser()[8]
            }},

            {'nemiroff_lex_05l': {
                "eko": parser.vodka_nemiroff_lex_05l_parser()[1],
                "silpo": parser.vodka_nemiroff_lex_05l_parser()[3],
                "novus": parser.vodka_nemiroff_lex_05l_parser()[5],
                "fozzy": parser.vodka_nemiroff_lex_05l_parser()[8]
            }},

            {'artemivske_bile_napivsolodke': {
                "atb": parser.artemivske_bile_napivsolodke_parser()[0],
                "eko": parser.artemivske_bile_napivsolodke_parser()[1],
                "varus": parser.artemivske_bile_napivsolodke_parser()[2],
                "ashan": parser.artemivske_bile_napivsolodke_parser()[4],
                "novus": parser.artemivske_bile_napivsolodke_parser()[5],
                "metro": parser.artemivske_bile_napivsolodke_parser()[6],
                "nash_kray": parser.artemivske_bile_napivsolodke_parser()[7],
                "fozzy": parser.artemivske_bile_napivsolodke_parser()[8]
            }},

            {'artemivske_rojeve_napivsuhe': {
                "varus": parser.artemivske_rojeve_napivsuhe_parser()[2],
                "silpo": parser.artemivske_rojeve_napivsuhe_parser()[3],
                "ashan": parser.artemivske_rojeve_napivsuhe_parser()[4],
                "novus": parser.artemivske_rojeve_napivsuhe_parser()[5],
                "fozzy": parser.artemivske_rojeve_napivsuhe_parser()[8]
            }},

            {'artemivske_bile_brut': {
                "atb": parser.artemivske_bile_brut_parser()[0],
                "eko": parser.artemivske_bile_brut_parser()[1],
                "varus": parser.artemivske_bile_brut_parser()[2],
                "silpo": parser.artemivske_bile_brut_parser()[3],
                "ashan": parser.artemivske_bile_brut_parser()[4],
                "novus": parser.artemivske_bile_brut_parser()[5],
                "metro": parser.artemivske_bile_brut_parser()[6],
                "nash_kray": parser.artemivske_bile_brut_parser()[7],
                "fozzy": parser.artemivske_bile_brut_parser()[8]
            }},

            {'artemivske_coll_napivsuhe': {
                "fozzy": parser.artemivske_coll_napivsuhe_parser()[8]
            }},

            {'artemivske_chervone_napivsolodke': {
                "varus": parser.artemivske_chervone_napivsolodke_parser()[2],
                "ashan": parser.artemivske_chervone_napivsolodke_parser()[4],
                "novus": parser.artemivske_chervone_napivsolodke_parser()[5],
                "fozzy": parser.artemivske_chervone_napivsolodke_parser()[8]
            }},

            {'bagrationi_bile_napivsolodke': {
                "varus": parser.bagrationi_bile_napivsolodke_parser()[2],
                "silpo": parser.bagrationi_bile_napivsolodke_parser()[3],
                "novus": parser.bagrationi_bile_napivsolodke_parser()[5],
                "metro": parser.bagrationi_bile_napivsolodke_parser()[6],
                "fozzy": parser.bagrationi_bile_napivsolodke_parser()[8]
            }},

            {'bagrationi_bile_napivsuhe': {
                "varus": parser.bagrationi_bile_napivsuhe_parser()[2],
                "silpo": parser.bagrationi_bile_napivsuhe_parser()[3],
                "novus": parser.bagrationi_bile_napivsuhe_parser()[5],
                "metro": parser.bagrationi_bile_napivsuhe_parser()[6],
                "fozzy": parser.bagrationi_bile_napivsuhe_parser()[8]
            }},

            {'bagrationi_bile_brut': {
                "varus": parser.bagrationi_bile_brut_parser()[2],
                "silpo": parser.bagrationi_bile_brut_parser()[3],
                "novus": parser.bagrationi_bile_brut_parser()[5],
                "metro": parser.bagrationi_bile_brut_parser()[6],
                "fozzy": parser.bagrationi_bile_brut_parser()[8]
            }},

            {'bagrationi_roj_napivsolodke': {
                "fozzy": parser.bagrationi_roj_napivsolod_parser()[8]
            }},

            {'bagrationi_gold_napivsolodke': {
                "fozzy": parser.bagrationi_gold_napivsolodke_parser()[8]
            }},

            {'bolgrad_bile_brut': {
                "varus": parser.bolgrad_bile_brut_parser()[2],
                "silpo": parser.bolgrad_bile_brut_parser()[3],
                "fozzy": parser.bolgrad_bile_brut_parser()[8]
            }},

            {'bolgrad_bile_napivsolodke': {
                "atb": parser.bolgrad_bile_napivsolodke_parser()[0],
                "varus": parser.bolgrad_bile_napivsolodke_parser()[2],
                "silpo": parser.bolgrad_bile_napivsolodke_parser()[3],
                "fozzy": parser.bolgrad_bile_napivsolodke_parser()[8]
            }},

            {'bolgrad_nectar_bile_solodke': {
                "varus": parser.bolgrad_nektar_bile_solodke_parser()[2],
                "fozzy": parser.bolgrad_nektar_bile_solodke_parser()[8]
            }},

            {'fran_bulvar_bile_napivsuhe': {
                "eko": parser.fran_bulvar_bile_napivsuhe_parser()[1],
                "silpo": parser.fran_bulvar_bile_napivsuhe_parser()[3],
                "metro": parser.fran_bulvar_bile_napivsuhe_parser()[6],
                "fozzy": parser.fran_bulvar_bile_napivsuhe_parser()[8]
            }},

            {'fran_bulvar_bile_brut': {
                "eko": parser.fran_bulvar_bile_brut_parser()[1],
                "silpo": parser.fran_bulvar_bile_brut_parser()[3],
                "metro": parser.fran_bulvar_bile_brut_parser()[6],
                "fozzy": parser.fran_bulvar_bile_brut_parser()[8]
            }},

            {'fran_bulvar_bile_napivsolodke': {
                "eko": parser.fran_bulvar_bile_napivsolod_parser()[1],
                "silpo": parser.fran_bulvar_bile_napivsolod_parser()[3],
                "metro": parser.fran_bulvar_bile_napivsolod_parser()[6],
                "fozzy": parser.fran_bulvar_bile_napivsolod_parser()[8]
            }},

            {'stariy_kaheti_3': {
                "varus": parser.stariy_kaheti_3_parser()[2],
                "novus": parser.stariy_kaheti_3_parser()[5],
                "metro": parser.stariy_kaheti_3_parser()[6],
                "fozzy": parser.stariy_kaheti_3_parser()[8]
            }},

            {'stariy_kaheti_5': {
                "varus": parser.stariy_kaheti_5_parser()[2],
                "novus": parser.stariy_kaheti_5_parser()[5],
                "metro": parser.stariy_kaheti_5_parser()[6],
                "fozzy": parser.stariy_kaheti_5_parser()[8]
            }},

            {'stariy_kaheti_4': {
                "varus": parser.stariy_kaheti_4_parser()[2],
                "novus": parser.stariy_kaheti_4_parser()[5],
                "metro": parser.stariy_kaheti_4_parser()[6],
                "fozzy": parser.stariy_kaheti_4_parser()[8]
            }},

            {'koblevo_extra_old_8': {
                "eko": parser.koblevo_extra_old_8_parser()[1],
                "novus": parser.koblevo_extra_old_8_parser()[5],
                "fozzy": parser.koblevo_extra_old_8_parser()[8]
            }},

            {'shabo_vsop_5': {
                "atb": parser.shabo_vsop_5_parser()[0],
                "eko": parser.shabo_vsop_5_parser()[1],
                "varus": parser.shabo_vsop_5_parser()[2],
                "silpo": parser.shabo_vsop_5_parser()[3],
                "metro": parser.shabo_vsop_5_parser()[6],
                "nash_kray": parser.shabo_vsop_5_parser()[7],
                "fozzy": parser.shabo_vsop_5_parser()[8]
            }},

            {'shabo_vs_3': {
                "atb": parser.shabo_vs_3_parser()[0],
                "eko": parser.shabo_vs_3_parser()[1],
                "varus": parser.shabo_vs_3_parser()[2],
                "silpo": parser.shabo_vs_3_parser()[3],
                "novus": parser.shabo_vs_3_parser()[5],
                "metro": parser.shabo_vs_3_parser()[6],
                "nash_kray": parser.shabo_vs_3_parser()[7],
                "fozzy": parser.shabo_vs_3_parser()[8]
            }},

            {'shabo_1788_4': {
                "atb": parser.shabo_1788_4_parser()[0],
                "eko": parser.shabo_1788_4_parser()[1],
                "varus": parser.shabo_1788_4_parser()[2],
                "silpo": parser.shabo_1788_4_parser()[3],
                "novus": parser.shabo_1788_4_parser()[5],
                "metro": parser.shabo_1788_4_parser()[6],
                "fozzy": parser.shabo_1788_4_parser()[8]
            }},

            {'shabo_1788_reserv': {
                "fozzy": parser.shabo_1788_reserv_parser()[8]
            }},

            {'shabo_vs_reserv': {
                "varus": parser.shabo_vs_reserv_parser()[2],
                "silpo": parser.shabo_vs_reserv_parser()[3],
                "novus": parser.shabo_vs_reserv_parser()[5],
                "metro": parser.shabo_vs_reserv_parser()[6],
                "fozzy": parser.shabo_vs_reserv_parser()[8]
            }},

            {'shabo_vsop_reserv': {
                "atb": parser.shabo_vsop_reserv_parser()[0],
                "eko": parser.shabo_vsop_reserv_parser()[1],
                "silpo": parser.shabo_vsop_reserv_parser()[3],
                "novus": parser.shabo_vsop_reserv_parser()[5],
                "metro": parser.shabo_vsop_reserv_parser()[6],
                "fozzy": parser.shabo_vsop_reserv_parser()[8]
            }},

            {'aznauri_3': {
                "atb": parser.aznauri_3_parser()[0],
                "eko": parser.aznauri_3_parser()[1],
                "varus": parser.aznauri_3_parser()[2],
                "silpo": parser.aznauri_3_parser()[3],
                "ashan": parser.aznauri_3_parser()[4],
                "novus": parser.aznauri_3_parser()[5],
                "metro": parser.aznauri_3_parser()[6],
                "nash_kray": parser.aznauri_3_parser()[7],
                "fozzy": parser.aznauri_3_parser()[8]
            }},

            {'aznauri_5': {
                "atb": parser.aznauri_5_parser()[0],
                "eko": parser.aznauri_5_parser()[1],
                "varus": parser.aznauri_5_parser()[2],
                "silpo": parser.aznauri_5_parser()[3],
                "ashan": parser.aznauri_5_parser()[4],
                "novus": parser.aznauri_5_parser()[5],
                "nash_kray": parser.aznauri_5_parser()[7],
                "fozzy": parser.aznauri_5_parser()[8]
            }},

            {'aznauri_4': {
                "eko": parser.aznauri_4_parser()[1],
                "ashan": parser.aznauri_4_parser()[4],
                "novus": parser.aznauri_4_parser()[5],
                "metro": parser.aznauri_4_parser()[6],
                "fozzy": parser.aznauri_4_parser()[8]
            }},

            {'aznauri_black_barrel_5': {
                "atb": parser.aznauri_black_barrel_5_parser()[0],
                "eko": parser.aznauri_black_barrel_5_parser()[1],
                "varus": parser.aznauri_black_barrel_5_parser()[2],
                "silpo": parser.aznauri_black_barrel_5_parser()[3],
                "ashan": parser.aznauri_black_barrel_5_parser()[4],
                "novus": parser.aznauri_black_barrel_5_parser()[5],
                "fozzy": parser.aznauri_black_barrel_5_parser()[8]
            }},

            {'adjari_3': {
                "varus": parser.adjari_3_parser()[2],
                "silpo": parser.adjari_3_parser()[3],
                "ashan": parser.adjari_3_parser()[4],
                "metro": parser.adjari_3_parser()[6],
                "fozzy": parser.adjari_3_parser()[8]
            }},

            {'adjari_5': {
                "varus": parser.adjari_5_parser()[2],
                "silpo": parser.adjari_5_parser()[3],
                "ashan": parser.adjari_5_parser()[4],
                "metro": parser.adjari_5_parser()[6],
                "novus": parser.adjari_5_parser()[5],
                "fozzy": parser.adjari_5_parser()[8]
            }},

            {'adjari_4': {
                "ashan": parser.adjari_4_parser()[4],
                "fozzy": parser.adjari_4_parser()[8]
            }},

            {'hennesy_vs': {
                "atb": parser.hennesy_vs_parser()[0],
                "silpo": parser.hennesy_vs_parser()[3],
                "novus": parser.hennesy_vs_parser()[5],
                "metro": parser.hennesy_vs_parser()[6],
                "fozzy": parser.hennesy_vs_parser()[8]
            }},

            {'hennesy_vsop': {
                "silpo": parser.hennesy_vsop_parser()[3],
                "metro": parser.hennesy_vsop_parser()[6],
                "fozzy": parser.hennesy_vsop_parser()[8]
            }},

            {'alexx_gold_vsop': {
                "varus": parser.alexx_gold_vsop_parser()[2],
                "silpo": parser.alexx_gold_vsop_parser()[3],
                "novus": parser.alexx_gold_vsop_parser()[5],
                "metro": parser.alexx_gold_vsop_parser()[6],
                "fozzy": parser.alexx_gold_vsop_parser()[8]
            }},

            {'alexx_silver_vs': {
                "varus": parser.alexx_silver_vs_parser()[2],
                "silpo": parser.alexx_silver_vs_parser()[3],
                "metro": parser.alexx_silver_vs_parser()[6],
                "fozzy": parser.alexx_silver_vs_parser()[8]
            }},

            {'ararat_5': {
                "varus": parser.ararat_5_parser()[2],
                "silpo": parser.ararat_5_parser()[3],
                "ashan": parser.ararat_5_parser()[4],
                "metro": parser.ararat_5_parser()[6],
                "fozzy": parser.ararat_5_parser()[8]
            }},

            {'ararat_ahtamar_10': {
                "silpo": parser.ararat_ahtamar_10_parser()[3],
                "ashan": parser.ararat_ahtamar_10_parser()[4],
                "fozzy": parser.ararat_ahtamar_10_parser()[8]
            }},

            {'ararat_3': {
                "varus": parser.ararat_3_parser()[2],
                "silpo": parser.ararat_3_parser()[3],
                "ashan": parser.ararat_3_parser()[4],
                "metro": parser.ararat_3_parser()[6],
                "nash_kray": parser.ararat_3_parser()[7],
                "fozzy": parser.ararat_3_parser()[8]
            }},

            {'ararat_nairi_20': {
                "ashan": parser.ararat_nairi_20_parser()[4],
                "fozzy": parser.ararat_nairi_20_parser()[8]
            }},

            {'green_day_air_05l': {
                "fozzy": parser.green_day_air_05l_parser()[8]
            }},

            {'green_day_ultra_soft_05l': {
                "fozzy": parser.green_day_ultra_soft_05l_parser()[8]
            }},

            {'green_day_organic_life_05l': {
                "varus": parser.green_day_organic_life_05l_parser()[2],
                "ashan": parser.green_day_organic_life_05l_parser()[4],
                "fozzy": parser.green_day_organic_life_05l_parser()[8]
            }},

            {'green_day_crystal_05l': {
                "varus": parser.green_day_crystal_05l_parser()[2],
                "silpo": parser.green_day_crystal_05l_parser()[3],
                "ashan": parser.green_day_crystal_05l_parser()[4],
                "metro": parser.green_day_crystal_05l_parser()[6],
                "fozzy": parser.green_day_crystal_05l_parser()[8]
            }},

            {'green_day_05l': {
                "varus": parser.green_day_05l_parser()[2],
                "silpo": parser.green_day_05l_parser()[3],
                "ashan": parser.green_day_05l_parser()[4],
                "metro": parser.green_day_05l_parser()[6],
                "fozzy": parser.green_day_05l_parser()[8]
            }},

            {'medoff_classic_05l': {
                "eko": parser.medoff_classic_05l_parser()[1],
                "varus": parser.medoff_classic_05l_parser()[2],
                "silpo": parser.medoff_classic_05l_parser()[3],
                "nash_kray": parser.medoff_classic_05l_parser()[7],
                "fozzy": parser.medoff_classic_05l_parser()[8]
            }},

            {'smirnoff_red_05l': {
                "eko": parser.smirnoff_red_05l_parser()[1],
                "varus": parser.smirnoff_red_05l_parser()[2],
                "silpo": parser.smirnoff_red_05l_parser()[3],
                "fozzy": parser.smirnoff_red_05l_parser()[8]
            }},
        ]
        # далее записываем цены в json-файл
        write_prices_to_json(all_products_names_batch_4, batch_4_path, mode_type_first_write)

    # для 5-го батча
    elif batch_name == batch_name_5:
        all_products_names_batch_5 = [
            {'kozacka_rada_classic_05l': {
                "atb": parser.kozacka_rada_classic_05l_parser()[0],
                "eko": parser.kozacka_rada_classic_05l_parser()[1],
                "silpo": parser.kozacka_rada_classic_05l_parser()[3],
                "ashan": parser.kozacka_rada_classic_05l_parser()[4],
                "novus": parser.kozacka_rada_classic_05l_parser()[5],
                "metro": parser.kozacka_rada_classic_05l_parser()[6],
                "nash_kray": parser.kozacka_rada_classic_05l_parser()[7],
                "fozzy": parser.kozacka_rada_classic_05l_parser()[8]
            }},

            {'kozacka_rada_osobliva_05l': {
                "atb": parser.kozacka_rada_osobliva_05l_parser()[0],
                "eko": parser.kozacka_rada_osobliva_05l_parser()[1],
                "varus": parser.kozacka_rada_osobliva_05l_parser()[2],
                "silpo": parser.kozacka_rada_osobliva_05l_parser()[3],
                "novus": parser.kozacka_rada_osobliva_05l_parser()[5],
                "fozzy": parser.kozacka_rada_osobliva_05l_parser()[8]
            }},

            {'zubrowka_bison_grass_05l': {
                "atb": parser.zubrowka_bison_grass_05l_parser()[0],
                "eko": parser.zubrowka_bison_grass_05l_parser()[1],
                "ashan": parser.zubrowka_bison_grass_05l_parser()[4],
                "novus": parser.zubrowka_bison_grass_05l_parser()[5],
                "metro": parser.zubrowka_bison_grass_05l_parser()[6],
                "nash_kray": parser.zubrowka_bison_grass_05l_parser()[7],
                "fozzy": parser.zubrowka_bison_grass_05l_parser()[8]
            }},

            {'zubrowka_biala_05l': {
                "atb": parser.zubrowka_biala_05l_parser()[0],
                "eko": parser.zubrowka_biala_05l_parser()[1],
                "ashan": parser.zubrowka_biala_05l_parser()[4],
                "novus": parser.zubrowka_biala_05l_parser()[5],
                "metro": parser.zubrowka_biala_05l_parser()[6],
                "nash_kray": parser.zubrowka_biala_05l_parser()[7],
                "fozzy": parser.zubrowka_biala_05l_parser()[8]
            }},

            {'zubrowka_czarna_05l': {
                "eko": parser.zubrowka_czarna_05l_parser()[1],
                "ashan": parser.zubrowka_czarna_05l_parser()[4],
                "nash_kray": parser.zubrowka_czarna_05l_parser()[7],
                "fozzy": parser.zubrowka_czarna_05l_parser()[8]
            }},

            {'vozduh_legka_osobliva_05l': {
                "silpo": parser.vozduh_legka_osobliva_05l_parser()[3],
                "fozzy": parser.vozduh_legka_osobliva_05l_parser()[8]
            }},

            {'vozduh_legka_osobliva_05l': {
                "eko": parser.vozduh_alpha_05l_parser()[1],
                "fozzy": parser.vozduh_alpha_05l_parser()[8]
            }},

            {'persha_gildiya_verhovna_05l': {
                "ashan": parser.persha_gildiya_verhovna_05l_parser()[4],
                "novus": parser.persha_gildiya_verhovna_05l_parser()[5],
                "fozzy": parser.persha_gildiya_verhovna_05l_parser()[8]
            }},

            {'persha_gildiya_znatna_05l': {
                "silpo": parser.persha_gildiya_znatna_05l_parser()[3],
                "ashan": parser.persha_gildiya_znatna_05l_parser()[4],
                "fozzy": parser.persha_gildiya_znatna_05l_parser()[8]
            }},

            {'persha_gildiya_povajna_05l': {
                "silpo": parser.persha_gildiya_povajna_05l_parser()[3],
                "ashan": parser.persha_gildiya_povajna_05l_parser()[4],
                "novus": parser.persha_gildiya_povajna_05l_parser()[5],
                "metro": parser.persha_gildiya_povajna_05l_parser()[6],
                "fozzy": parser.persha_gildiya_povajna_05l_parser()[8]
            }},

            {'hlib_dar_classic_05l': {
                "atb": parser.hlib_dar_classic_05l_parser()[0],
                "eko": parser.hlib_dar_classic_05l_parser()[1],
                "silpo": parser.hlib_dar_classic_05l_parser()[3],
                "ashan": parser.hlib_dar_classic_05l_parser()[4],
                "metro": parser.hlib_dar_classic_05l_parser()[6],
                "fozzy": parser.hlib_dar_classic_05l_parser()[8]
            }},

            {'hlib_dar_pror_zerno_05l': {
                "eko": parser.hlib_dar_pror_zerno_05l_parser()[1],
                "silpo": parser.hlib_dar_pror_zerno_05l_parser()[3],
                "novus": parser.hlib_dar_pror_zerno_05l_parser()[5],
                "fozzy": parser.hlib_dar_pror_zerno_05l_parser()[8]
            }},

            {'hlib_dar_jitnya_05l': {
                "eko": parser.hlib_dar_jitnya_05l_parser()[1],
                "silpo": parser.hlib_dar_jitnya_05l_parser()[3],
                "fozzy": parser.hlib_dar_jitnya_05l_parser()[8]
            }},

            {'hlib_dar_pshenichna_05l': {
                "eko": parser.hlib_dar_pshenichna_05l_parser()[1],
                "silpo": parser.hlib_dar_pshenichna_05l_parser()[3],
                "novus": parser.hlib_dar_pshenichna_05l_parser()[5],
                "fozzy": parser.hlib_dar_pshenichna_05l_parser()[8]
            }},

            {'green_day_organic_life_07l': {
                "silpo": parser.green_day_organic_life_07l_parser()[3],
                "ashan": parser.green_day_organic_life_07l_parser()[4],
                "fozzy": parser.green_day_organic_life_07l_parser()[8]
            }},

            {'green_day_07l': {
                "varus": parser.green_day_07l_parser()[2],
                "silpo": parser.green_day_07l_parser()[3],
                "ashan": parser.green_day_07l_parser()[4],
                "fozzy": parser.green_day_07l_parser()[8]
            }},

            {'green_day_ultra_soft_07l': {
                "fozzy": parser.green_day_ultra_soft_07l_parser()[8]
            }},

            {'green_day_air_07l': {
                "fozzy": parser.green_day_air_07l_parser()[8]
            }},

            {'green_day_crystal_07l': {
                "varus": parser.green_day_crystal_07l_parser()[2],
                "silpo": parser.green_day_crystal_07l_parser()[3],
                "ashan": parser.green_day_crystal_07l_parser()[4],
                "novus": parser.green_day_crystal_07l_parser()[5],
                "fozzy": parser.green_day_crystal_07l_parser()[8]
            }},

            {'medoff_classic_07l': {
                "eko": parser.medoff_classic_07l_parser()[1],
                "varus": parser.medoff_classic_07l_parser()[2],
                "silpo": parser.medoff_classic_07l_parser()[3],
                "ashan": parser.medoff_classic_07l_parser()[4],
                "nash_kray": parser.medoff_classic_07l_parser()[7],
                "fozzy": parser.medoff_classic_07l_parser()[8]
            }},

            {'nemiroff_delikat_myaka_07l': {
                "eko": parser.nemiroff_delikat_myaka_07l_parser()[1],
                "varus": parser.nemiroff_delikat_myaka_07l_parser()[2],
                "silpo": parser.nemiroff_delikat_myaka_07l_parser()[3],
                "novus": parser.nemiroff_delikat_myaka_07l_parser()[5],
                "metro": parser.nemiroff_delikat_myaka_07l_parser()[6],
                "nash_kray": parser.nemiroff_delikat_myaka_07l_parser()[7],
                "fozzy": parser.nemiroff_delikat_myaka_07l_parser()[8]
            }},

            {'nemiroff_osob_shtof_07l': {
                "atb": parser.nemiroff_osob_shtof_07l_parser()[0],
                "silpo": parser.nemiroff_osob_shtof_07l_parser()[3],
                "metro": parser.nemiroff_osob_shtof_07l_parser()[6],
                "fozzy": parser.nemiroff_osob_shtof_07l_parser()[8]
            }},

            {'nemiroff_deluxe_07l': {
                "atb": parser.nemiroff_deluxe_07l_parser()[0],
                "eko": parser.nemiroff_deluxe_07l_parser()[1],
                "silpo": parser.nemiroff_deluxe_07l_parser()[3],
                "ashan": parser.nemiroff_deluxe_07l_parser()[4],
                "novus": parser.nemiroff_deluxe_07l_parser()[5],
                "metro": parser.nemiroff_deluxe_07l_parser()[6],
                "fozzy": parser.nemiroff_deluxe_07l_parser()[8]
            }},

            {'nemiroff_lex_07l': {
                "silpo": parser.nemiroff_lex_07l_parser()[3],
                "novus": parser.nemiroff_lex_07l_parser()[5],
                "metro": parser.nemiroff_lex_07l_parser()[6],
                "fozzy": parser.nemiroff_lex_07l_parser()[8]
            }},

            {'zubrowka_bison_grass_07l': {
                "atb": parser.zubrowka_bison_grass_07l_parser()[0],
                "eko": parser.zubrowka_bison_grass_07l_parser()[1],
                "ashan": parser.zubrowka_bison_grass_07l_parser()[4],
                "novus": parser.zubrowka_bison_grass_07l_parser()[5],
                "nash_kray": parser.zubrowka_bison_grass_07l_parser()[7],
                "fozzy": parser.zubrowka_bison_grass_07l_parser()[8]
            }},

            {'zubrowka_czarna_07l': {
                "eko": parser.zubrowka_czarna_07l_parser()[1],
                "ashan": parser.zubrowka_czarna_07l_parser()[4],
                "nash_kray": parser.zubrowka_czarna_07l_parser()[7],
                "fozzy": parser.zubrowka_czarna_07l_parser()[8]
            }},

            {'hetman_07l': {
                "varus": parser.hetman_07l_parser()[2],
                "silpo": parser.hetman_07l_parser()[3],
                "novus": parser.hetman_07l_parser()[5],
                "fozzy": parser.hetman_07l_parser()[8]
            }},

            {'kozacka_rada_classic_07l': {
                "atb": parser.kozacka_rada_classic_07l_parser()[0],
                "eko": parser.kozacka_rada_classic_07l_parser()[1],
                "silpo": parser.kozacka_rada_classic_07l_parser()[3],
                "ashan": parser.kozacka_rada_classic_07l_parser()[4],
                "novus": parser.kozacka_rada_classic_07l_parser()[5],
                "fozzy": parser.kozacka_rada_classic_07l_parser()[8]
            }},

            {'kozacka_rada_premium_07l': {
                "eko": parser.kozacka_rada_premium_07l_parser()[1],
                "ashan": parser.kozacka_rada_premium_07l_parser()[4],
                "fozzy": parser.kozacka_rada_premium_07l_parser()[8]
            }},

            {'kozacka_rada_osobliva_07l': {
                "eko": parser.kozacka_rada_osobliva_07l_parser()[1],
                "varus": parser.kozacka_rada_osobliva_07l_parser()[2],
                "ashan": parser.kozacka_rada_osobliva_07l_parser()[4],
                "novus": parser.kozacka_rada_osobliva_07l_parser()[5],
                "fozzy": parser.kozacka_rada_osobliva_07l_parser()[8]
            }},

            {'persha_gildiya_povajna_07l': {
                "eko": parser.persha_gildiya_povajna_07l_parser()[1],
                "silpo": parser.persha_gildiya_povajna_07l_parser()[3],
                "ashan": parser.persha_gildiya_povajna_07l_parser()[4],
                "fozzy": parser.persha_gildiya_povajna_07l_parser()[8]
            }},

            {'persha_gildiya_verhovna_07l': {
                "eko": parser.persha_gildiya_verhovna_07l_parser()[1],
                "silpo": parser.persha_gildiya_verhovna_07l_parser()[3],
                "ashan": parser.persha_gildiya_verhovna_07l_parser()[4],
                "novus": parser.persha_gildiya_verhovna_07l_parser()[5],
                "fozzy": parser.persha_gildiya_verhovna_07l_parser()[8]
            }},

            {'persha_gildiya_znatna_07l': {
                "eko": parser.persha_gildiya_znatna_07l_parser()[1],
                "silpo": parser.persha_gildiya_znatna_07l_parser()[3],
                "ashan": parser.persha_gildiya_znatna_07l_parser()[4],
                "fozzy": parser.persha_gildiya_znatna_07l_parser()[8]
            }},

            {'hlibniy_dar_classic_07l': {
                "atb": parser.hlib_dar_classic_07l_parser()[0],
                "eko": parser.hlib_dar_classic_07l_parser()[1],
                "silpo": parser.hlib_dar_classic_07l_parser()[3],
                "ashan": parser.hlib_dar_classic_07l_parser()[4],
                "novus": parser.hlib_dar_classic_07l_parser()[5],
                "metro": parser.hlib_dar_classic_07l_parser()[6],
                "nash_kray": parser.hlib_dar_classic_07l_parser()[7],
                "fozzy": parser.hlib_dar_classic_07l_parser()[8]
            }},

            {'medoff_classic_1l': {
                "nash_kray": parser.medoff_classic_1l_parser()[7],
                "fozzy": parser.medoff_classic_1l_parser()[8]
            }},

            {'nemiroff_shtof_1l': {
                "atb": parser.nemiroff_shtof_1l_parser()[0],
                "silpo": parser.nemiroff_shtof_1l_parser()[3],
                "nash_kray": parser.nemiroff_shtof_1l_parser()[7],
                "fozzy": parser.nemiroff_shtof_1l_parser()[8]
            }},

            {'nemiroff_delicat_1l': {
                "eko": parser.nemiroff_delicat_1l_parser()[1],
                "varus": parser.nemiroff_delicat_1l_parser()[2],
                "silpo": parser.nemiroff_delicat_1l_parser()[3],
                "ashan": parser.nemiroff_delicat_1l_parser()[4],
                "novus": parser.nemiroff_delicat_1l_parser()[5],
                "fozzy": parser.nemiroff_delicat_1l_parser()[8]
            }},

            {'zubrowka_bison_grass_1l': {
                "varus": parser.zubrowka_bison_grass_1l_parser()[2],
                "novus": parser.zubrowka_bison_grass_1l_parser()[5],
                "nash_kray": parser.zubrowka_bison_grass_1l_parser()[7],
                "fozzy": parser.zubrowka_bison_grass_1l_parser()[8]
            }},

            {'zubrowka_biala_1l': {
                "eko": parser.zubrowka_biala_1l_parser()[1],
                "varus": parser.zubrowka_biala_1l_parser()[2],
                "fozzy": parser.zubrowka_biala_1l_parser()[8]
            }},

            {'hetman_1l': {
                "varus": parser.hetman_1l_parser()[2],
                "silpo": parser.hetman_1l_parser()[3],
                "fozzy": parser.hetman_1l_parser()[8]
            }},

            {'kozacka_rada_osobliva_1l': {
                "eko": parser.kozacka_rada_osobliva_1l_parser()[1],
                "varus": parser.kozacka_rada_osobliva_1l_parser()[2],
                "ashan": parser.kozacka_rada_osobliva_1l_parser()[4],
                "novus": parser.kozacka_rada_osobliva_1l_parser()[5],
                "fozzy": parser.kozacka_rada_osobliva_1l_parser()[8]
            }},

            {'kozacka_rada_classic_1l': {
                "atb": parser.kozacka_rada_classic_1l_parser()[0],
                "eko": parser.kozacka_rada_classic_1l_parser()[1],
                "varus": parser.kozacka_rada_classic_1l_parser()[2],
                "silpo": parser.kozacka_rada_classic_1l_parser()[3],
                "ashan": parser.kozacka_rada_classic_1l_parser()[4],
                "novus": parser.kozacka_rada_classic_1l_parser()[5],
                "fozzy": parser.kozacka_rada_classic_1l_parser()[8]
            }},

            {'hlib_dar_classic_1l': {
                "eko": parser.hlib_dar_classic_1l_parser()[1],
                "varus": parser.hlib_dar_classic_1l_parser()[2],
                "silpo": parser.hlib_dar_classic_1l_parser()[3],
                "novus": parser.hlib_dar_classic_1l_parser()[5],
                "fozzy": parser.hlib_dar_classic_1l_parser()[8]
            }},

            {'svinne_rebro': {
                "eko": parser.svinne_rebro_parser()[1],
                "varus": parser.svinne_rebro_parser()[2],
                "silpo": parser.svinne_rebro_parser()[3] * mul_price_by_10,
                "novus": parser.svinne_rebro_parser()[5],
                "metro": parser.svinne_rebro_parser()[6],
                "nash_kray": parser.svinne_rebro_parser()[7] * mul_price_by_10,
                "fozzy": parser.svinne_rebro_parser()[8]
            }},

            {'salo': {
                "varus": parser.salo_parser()[2],
                "silpo": parser.salo_parser()[3] * mul_price_by_10,
                "novus": parser.salo_parser()[5],
                "nash_kray": parser.salo_parser()[7],
                "fozzy": parser.salo_parser()[8]
            }},

            {'svinna_gomilka': {
                "varus": parser.svinna_gomilka_parser()[2],
                "metro": parser.svinna_gomilka_parser()[6],
                "fozzy": parser.svinna_gomilka_parser()[8]
            }},

            {'svinna_pechinka': {
                "varus": parser.svin_pechinka_parser()[2],
                "nash_kray": parser.svin_pechinka_parser()[7],
                "fozzy": parser.svin_pechinka_parser()[8]
            }},

            {'svin_gulyash': {
                "silpo": parser.svin_gulyash_parser()[3] * mul_price_by_10,
                "fozzy": parser.svin_gulyash_parser()[8]
            }},

            {'svinna_pidjarka': {
                "varus": parser.svin_pidjarka_parser()[2],
                "fozzy": parser.svin_pidjarka_parser()[8]
            }},

            {'svin_koreyka': {
                "varus": parser.svin_koreyka_parser()[2],
                "silpo": parser.svin_koreyka_parser()[3] * mul_price_by_10,
                "novus": parser.svin_koreyka_parser()[5],
                "metro": parser.svin_koreyka_parser()[6],
                "nash_kray": parser.svin_koreyka_parser()[7],
            }},

            {'svin_virizka': {
                "eko": parser.svin_virizka_parser()[1],
                "varus": parser.svin_virizka_parser()[2],
                "silpo": parser.svin_virizka_parser()[3] * mul_price_by_10,
                "metro": parser.svin_virizka_parser()[6],
                "fozzy": parser.svin_virizka_parser()[8]
            }},

            {'svin_lopatka_bez_kistki': {
                "eko": parser.svin_lopatka_bez_kistki_parser()[1],
                "varus": parser.svin_lopatka_bez_kistki_parser()[2],
                "silpo": parser.svin_lopatka_bez_kistki_parser()[3] * mul_price_by_10,
                "metro": parser.svin_lopatka_bez_kistki_parser()[6],
                "fozzy": parser.svin_lopatka_bez_kistki_parser()[8]
            }},

            {'svin_okist_bez_kistki': {
                "silpo": parser.svin_okist_bez_kistki_parser()[3] * mul_price_by_10,
                "fozzy": parser.svin_okist_bez_kistki_parser()[8]
            }},

            {'svin_farsh': {
                "nash_kray": parser.svin_farsh_parser()[7] * mul_price_by_10,
                "fozzy": parser.svin_farsh_parser()[8]
            }},

            {'svin_bitok_bez_kosti': {
                "eko": parser.svin_bitok_bez_kosti_parser()[1],
                "varus": parser.svin_bitok_bez_kosti_parser()[2],
                "silpo": parser.svin_bitok_bez_kosti_parser()[3] * mul_price_by_10,
                "fozzy": parser.svin_bitok_bez_kosti_parser()[8]
            }},

            {'svin_ragu': {
                "silpo": parser.svin_ragu_parser()[3] * mul_price_by_10,
                "fozzy": parser.svin_ragu_parser()[8]
            }},

            {'svin_osheek_bez_kistki': {
                "eko": parser.svin_osheek_bez_kistki_parser()[1],
                "varus": parser.svin_osheek_bez_kistki_parser()[2],
                "silpo": parser.svin_osheek_bez_kistki_parser()[3] * mul_price_by_10,
                "novus": parser.svin_osheek_bez_kistki_parser()[5],
                "metro": parser.svin_osheek_bez_kistki_parser()[6],
                "fozzy": parser.svin_osheek_bez_kistki_parser()[8]
            }},

            {'kuryacha_chetvert': {
                "atb": parser.kuryacha_chetvert_parser()[0],
                "eko": parser.kuryacha_chetvert_parser()[1],
                "varus": parser.kuryacha_chetvert_parser()[2],
                "silpo": parser.kuryacha_chetvert_parser()[3] * mul_price_by_10,
                "nash_kray": parser.kuryacha_chetvert_parser()[7],
                "fozzy": parser.kuryacha_chetvert_parser()[8]
            }},

            {'kuryache_stegno': {
                "atb": parser.kuryache_stegno_parser()[0],
                "eko": parser.kuryache_stegno_parser()[1],
                "varus": parser.kuryache_stegno_parser()[2],
                "silpo": parser.kuryache_stegno_parser()[3] * mul_price_by_10,
                "novus": parser.kuryache_stegno_parser()[5],
                "metro": parser.kuryache_stegno_parser()[6],
                "nash_kray": parser.kuryache_stegno_parser()[7],
                "fozzy": parser.kuryache_stegno_parser()[8]
            }},

            {'kuryache_krilo': {
                "atb": parser.kuryache_krilo_parser()[0],
                "varus": parser.kuryache_krilo_parser()[2],
                "silpo": parser.kuryache_krilo_parser()[3] * mul_price_by_10,
                "novus": parser.kuryache_krilo_parser()[5],
                "metro": parser.kuryache_krilo_parser()[6],
                "nash_kray": parser.kuryache_krilo_parser()[7],
                "fozzy": parser.kuryache_krilo_parser()[8]
            }},

            {'kuryache_file': {
                "atb": parser.kuryache_file_parser()[0],
                "eko": parser.kuryache_file_parser()[1],
                "varus": parser.kuryache_file_parser()[2],
                "silpo": parser.kuryache_file_parser()[3] * mul_price_by_10,
                "novus": parser.kuryache_file_parser()[5],
                "metro": parser.kuryache_file_parser()[6],
                "nash_kray": parser.kuryache_file_parser()[7] * mul_price_by_10,
                "fozzy": parser.kuryache_file_parser()[8]
            }},

            {'kuryacha_gomilka': {
                "eko": parser.kuryacha_gomilka_parser()[1],
                "varus": parser.kuryacha_gomilka_parser()[2],
                "silpo": parser.kuryacha_gomilka_parser()[3] * mul_price_by_10,
                "novus": parser.kuryacha_gomilka_parser()[5],
                "metro": parser.kuryacha_gomilka_parser()[6],
                "nash_kray": parser.kuryacha_gomilka_parser()[7],
                "fozzy": parser.kuryacha_gomilka_parser()[8]
            }},

            {'coca_cola_original_033_jb': {
                "eko": parser.coca_cola_original_033_jb_parser()[1],
                "varus": parser.coca_cola_original_033_jb_parser()[2],
                "silpo": parser.coca_cola_original_033_jb_parser()[3],
                "ashan": parser.coca_cola_original_033_jb_parser()[4],
                "novus": parser.coca_cola_original_033_jb_parser()[5],
                "metro": parser.coca_cola_original_033_jb_parser()[6],
                "fozzy": parser.coca_cola_original_033_jb_parser()[8]
            }},

            {'coca_cola_zero_033_jb': {
                "eko": parser.coca_cola_zero_033_jb_parser()[1],
                "varus": parser.coca_cola_zero_033_jb_parser()[2],
                "silpo": parser.coca_cola_zero_033_jb_parser()[3],
                "novus": parser.coca_cola_zero_033_jb_parser()[5],
                "metro": parser.coca_cola_zero_033_jb_parser()[6],
                "fozzy": parser.coca_cola_zero_033_jb_parser()[8]
            }},

            {'fanta_orange_033_jb': {
                "eko": parser.fanta_orange_033_jb_parser()[1],
                "varus": parser.fanta_orange_033_jb_parser()[2],
                "silpo": parser.fanta_orange_033_jb_parser()[3],
                "ashan": parser.fanta_orange_033_jb_parser()[4],
                "novus": parser.fanta_orange_033_jb_parser()[5],
                "metro": parser.fanta_orange_033_jb_parser()[6],
                "fozzy": parser.fanta_orange_033_jb_parser()[8]
            }},

            {'fanta_pineapple_033_jb': {
                "silpo": parser.fanta_pineapple_033_jb_parser()[3],
                "fozzy": parser.fanta_pineapple_033_jb_parser()[8]
            }},

            {'sprite_033_jb': {
                "eko": parser.sprite_033_jb_parser()[1],
                "varus": parser.sprite_033_jb_parser()[2],
                "silpo": parser.sprite_033_jb_parser()[3],
                "ashan": parser.sprite_033_jb_parser()[4],
                "novus": parser.sprite_033_jb_parser()[5],
                "fozzy": parser.sprite_033_jb_parser()[8]
            }},

            {'coca_cola_original_025_gl': {
                "fozzy": parser.coca_cola_original_025_gl_parser()[8]
            }},

            {'coca_cola_zero_025_gl': {
                "fozzy": parser.coca_cola_zero_025_gl_parser()[8]
            }},

            {'coca_cola_original_05_pl': {
                "atb": parser.coca_cola_original_05_pl_parser()[0],
                "eko": parser.coca_cola_original_05_pl_parser()[1],
                "varus": parser.coca_cola_original_05_pl_parser()[2],
                "silpo": parser.coca_cola_original_05_pl_parser()[3],
                "ashan": parser.coca_cola_original_05_pl_parser()[4],
                "novus": parser.coca_cola_original_05_pl_parser()[5],
                "metro": parser.coca_cola_original_05_pl_parser()[6],
                "fozzy": parser.coca_cola_original_05_pl_parser()[8]
            }},

            {'coca_cola_zero_05_pl': {
                "atb": parser.coca_cola_zero_05_pl_parser()[0],
                "eko": parser.coca_cola_zero_05_pl_parser()[1],
                "varus": parser.coca_cola_zero_05_pl_parser()[2],
                "silpo": parser.coca_cola_zero_05_pl_parser()[3],
                "novus": parser.coca_cola_zero_05_pl_parser()[5],
                "fozzy": parser.coca_cola_zero_05_pl_parser()[8]
            }},

            {'fanta_orange_05_pl': {
                "atb": parser.fanta_orange_05_pl_parser()[0],
                "eko": parser.fanta_orange_05_pl_parser()[1],
                "varus": parser.fanta_orange_05_pl_parser()[2],
                "silpo": parser.fanta_orange_05_pl_parser()[3],
                "ashan": parser.fanta_orange_05_pl_parser()[4],
                "novus": parser.fanta_orange_05_pl_parser()[5],
                "metro": parser.fanta_orange_05_pl_parser()[6],
                "nash_kray": parser.fanta_orange_05_pl_parser()[7],
                "fozzy": parser.fanta_orange_05_pl_parser()[8]
            }},

            {'sprite_05_pl': {
                "atb": parser.sprite_05_pl_parser()[0],
                "eko": parser.sprite_05_pl_parser()[1],
                "varus": parser.sprite_05_pl_parser()[2],
                "silpo": parser.sprite_05_pl_parser()[3],
                "ashan": parser.sprite_05_pl_parser()[4],
                "novus": parser.sprite_05_pl_parser()[5],
                "fozzy": parser.sprite_05_pl_parser()[8]
            }},

            {'coca_cola_original_15_pl': {
                "eko": parser.coca_cola_original_15_pl_parser()[1],
                "varus": parser.coca_cola_original_15_pl_parser()[2],
                "silpo": parser.coca_cola_original_15_pl_parser()[3],
                "ashan": parser.coca_cola_original_15_pl_parser()[4],
                "novus": parser.coca_cola_original_15_pl_parser()[5],
                "fozzy": parser.coca_cola_original_15_pl_parser()[8]
            }},

            {'coca_cola_zero_15_pl': {
                "eko": parser.coca_cola_zero_15_pl_parser()[1],
                "varus": parser.coca_cola_zero_15_pl_parser()[2],
                "silpo": parser.coca_cola_zero_15_pl_parser()[3],
                "ashan": parser.coca_cola_zero_15_pl_parser()[4],
                "metro": parser.coca_cola_zero_15_pl_parser()[6],
                "fozzy": parser.coca_cola_zero_15_pl_parser()[8]
            }},

            {'sprite_15_pl': {
                "eko": parser.sprite_15_pl_parser()[1],
                "varus": parser.sprite_15_pl_parser()[2],
                "silpo": parser.sprite_15_pl_parser()[3],
                "ashan": parser.sprite_15_pl_parser()[4],
                "novus": parser.sprite_15_pl_parser()[5],
                "fozzy": parser.sprite_15_pl_parser()[8]
            }},

            {'fanta_orange_15_pl': {
                "eko": parser.fanta_orange_15_pl_parser()[1],
                "varus": parser.fanta_orange_15_pl_parser()[2],
                "silpo": parser.fanta_orange_15_pl_parser()[3],
                "novus": parser.fanta_orange_15_pl_parser()[5],
                "metro": parser.fanta_orange_15_pl_parser()[6],
                "nash_kray": parser.fanta_orange_15_pl_parser()[7],
                "fozzy": parser.fanta_orange_15_pl_parser()[8]
            }},

            {'fanta_shokata_15_pl': {
                "eko": parser.fanta_shokata_15_pl_parser()[1],
                "varus": parser.fanta_shokata_15_pl_parser()[2],
                "silpo": parser.fanta_shokata_15_pl_parser()[3],
                "ashan": parser.fanta_shokata_15_pl_parser()[4],
                "novus": parser.fanta_shokata_15_pl_parser()[5],
                "metro": parser.fanta_shokata_15_pl_parser()[6],
                "nash_kray": parser.fanta_shokata_15_pl_parser()[7],
                "fozzy": parser.fanta_shokata_15_pl_parser()[8]
            }},

            {'fanta_mandarin_15_pl': {
                "varus": parser.fanta_mandarin_15_pl_parser()[2],
                "silpo": parser.fanta_mandarin_15_pl_parser()[3],
                "novus": parser.fanta_mandarin_15_pl_parser()[5],
                "metro": parser.fanta_mandarin_15_pl_parser()[6],
                "fozzy": parser.fanta_mandarin_15_pl_parser()[8]
            }},

            {'chips_luxe_becon_133gr': {
                "eko": parser.chips_luxe_becon_133gr_parser()[1],
                "silpo": parser.chips_luxe_becon_133gr_parser()[3],
                "ashan": parser.chips_luxe_becon_133gr_parser()[4],
                "novus": parser.chips_luxe_becon_133gr_parser()[5],
                "metro": parser.chips_luxe_becon_133gr_parser()[6],
                "nash_kray": parser.chips_luxe_becon_133gr_parser()[7],
                "fozzy": parser.chips_luxe_becon_133gr_parser()[8]
            }},

            {'chips_luxe_paprika_133gr': {
                "atb": parser.chips_luxe_paprika_133gr_parser()[0],
                "eko": parser.chips_luxe_paprika_133gr_parser()[1],
                "silpo": parser.chips_luxe_paprika_133gr_parser()[3],
                "ashan": parser.chips_luxe_paprika_133gr_parser()[4],
                "novus": parser.chips_luxe_paprika_133gr_parser()[5],
                "metro": parser.chips_luxe_paprika_133gr_parser()[6],
                "nash_kray": parser.chips_luxe_paprika_133gr_parser()[7],
                "fozzy": parser.chips_luxe_paprika_133gr_parser()[8]
            }},

            {'chips_luxe_crab_133gr': {
                "atb": parser.chips_luxe_crab_133gr_parser()[0],
                "eko": parser.chips_luxe_crab_133gr_parser()[1],
                "silpo": parser.chips_luxe_crab_133gr_parser()[3],
                "ashan": parser.chips_luxe_crab_133gr_parser()[4],
                "novus": parser.chips_luxe_crab_133gr_parser()[5],
                "metro": parser.chips_luxe_crab_133gr_parser()[6],
                "nash_kray": parser.chips_luxe_crab_133gr_parser()[7],
                "fozzy": parser.chips_luxe_crab_133gr_parser()[8]
            }},

            {'chips_luxe_smetana_cibulya_133gr': {
                "atb": parser.chips_luxe_smetana_cibulya_133gr_parser()[0],
                "eko": parser.chips_luxe_smetana_cibulya_133gr_parser()[1],
                "silpo": parser.chips_luxe_smetana_cibulya_133gr_parser()[3],
                "novus": parser.chips_luxe_smetana_cibulya_133gr_parser()[5],
                "metro": parser.chips_luxe_smetana_cibulya_133gr_parser()[6],
                "nash_kray": parser.chips_luxe_smetana_cibulya_133gr_parser()[7],
                "fozzy": parser.chips_luxe_smetana_cibulya_133gr_parser()[8]
            }},

            {'chips_luxe_sir_133gr': {
                "atb": parser.chips_luxe_sir_133gr_parser()[0],
                "eko": parser.chips_luxe_sir_133gr_parser()[1],
                "silpo": parser.chips_luxe_sir_133gr_parser()[3],
                "ashan": parser.chips_luxe_sir_133gr_parser()[4],
                "novus": parser.chips_luxe_sir_133gr_parser()[5],
                "metro": parser.chips_luxe_sir_133gr_parser()[6],
                "nash_kray": parser.chips_luxe_sir_133gr_parser()[7],
                "fozzy": parser.chips_luxe_sir_133gr_parser()[8]
            }},

            {'chips_luxe_sir_71gr': {
                "eko": parser.chips_luxe_sir_71gr_parser()[1],
                "varus": parser.chips_luxe_sir_71gr_parser()[2],
                "silpo": parser.chips_luxe_sir_71gr_parser()[3],
                "novus": parser.chips_luxe_sir_71gr_parser()[5],
                "metro": parser.chips_luxe_sir_71gr_parser()[6],
                "fozzy": parser.chips_luxe_sir_71gr_parser()[8]
            }},

            {'chips_luxe_becon_71gr': {
                "eko": parser.chips_luxe_becon_71gr_parser()[1],
                "varus": parser.chips_luxe_becon_71gr_parser()[2],
                "silpo": parser.chips_luxe_becon_71gr_parser()[3],
                "metro": parser.chips_luxe_becon_71gr_parser()[6],
                "nash_kray": parser.chips_luxe_becon_71gr_parser()[7],
                "fozzy": parser.chips_luxe_becon_71gr_parser()[8]
            }},

            {'chips_luxe_paprika_71gr': {
                "varus": parser.chips_luxe_paprika_71gr_parser()[2],
                "silpo": parser.chips_luxe_paprika_71gr_parser()[3],
                "novus": parser.chips_luxe_paprika_71gr_parser()[5],
                "metro": parser.chips_luxe_paprika_71gr_parser()[6],
                "nash_kray": parser.chips_luxe_paprika_71gr_parser()[7],
                "fozzy": parser.chips_luxe_paprika_71gr_parser()[8]
            }},

            {'chips_luxe_crab_71gr': {
                "fozzy": parser.chips_luxe_crab_71gr_parser()[8]
            }},

            {'chips_luxe_smetana_cibulya_71gr': {
                "fozzy": parser.chips_luxe_smetana_cibulya_71gr_parser()[8]
            }},

            {'chips_luxe_hvil_lisichki_125gr': {
                "atb": parser.chips_luxe_hvil_lisichki_125gr_parser()[0],
                "eko": parser.chips_luxe_hvil_lisichki_125gr_parser()[1],
                "varus": parser.chips_luxe_hvil_lisichki_125gr_parser()[2],
                "silpo": parser.chips_luxe_hvil_lisichki_125gr_parser()[3],
                "ashan": parser.chips_luxe_hvil_lisichki_125gr_parser()[4],
                "novus": parser.chips_luxe_hvil_lisichki_125gr_parser()[5],
                "metro": parser.chips_luxe_hvil_lisichki_125gr_parser()[6],
                "nash_kray": parser.chips_luxe_hvil_lisichki_125gr_parser()[7],
                "fozzy": parser.chips_luxe_hvil_lisichki_125gr_parser()[8]
            }},

            {'chips_luxe_smetana_cibulya_183gr': {
                "silpo": parser.chips_luxe_smetana_cibulya_183gr_parser()[3],
                "ashan": parser.chips_luxe_smetana_cibulya_183gr_parser()[4],
                "novus": parser.chips_luxe_smetana_cibulya_183gr_parser()[5],
                "metro": parser.chips_luxe_smetana_cibulya_183gr_parser()[6],
                "nash_kray": parser.chips_luxe_smetana_cibulya_183gr_parser()[7],
                "fozzy": parser.chips_luxe_smetana_cibulya_183gr_parser()[8]
            }},

            {'chips_luxe_becon_183gr': {
                "silpo": parser.chips_luxe_becon_183gr_parser()[3],
                "ashan": parser.chips_luxe_becon_183gr_parser()[4],
                "novus": parser.chips_luxe_becon_183gr_parser()[5],
                "metro": parser.chips_luxe_becon_183gr_parser()[6],
                "nash_kray": parser.chips_luxe_becon_183gr_parser()[7],
                "fozzy": parser.chips_luxe_becon_183gr_parser()[8]
            }},

            {'chips_luxe_sir_183gr': {
                "silpo": parser.chips_luxe_sir_183gr_parser()[3],
                "ashan": parser.chips_luxe_sir_183gr_parser()[4],
                "novus": parser.chips_luxe_sir_183gr_parser()[5],
                "metro": parser.chips_luxe_sir_183gr_parser()[6],
                "nash_kray": parser.chips_luxe_sir_183gr_parser()[7],
                "fozzy": parser.chips_luxe_sir_183gr_parser()[8]
            }},

            {'chips_pringles_greece_souce_caciki_185gr': {
                "fozzy": parser.chips_pringles_greece_souce_caciki_185gr_parser()[8]
            }},

            {'chips_pringles_paprika_165gr': {
                "varus": parser.chips_pringles_paprika_165gr_parser()[2],
                "silpo": parser.chips_pringles_paprika_165gr_parser()[3],
                "ashan": parser.chips_pringles_paprika_165gr_parser()[4],
                "novus": parser.chips_pringles_paprika_165gr_parser()[5],
                "metro": parser.chips_pringles_paprika_165gr_parser()[6],
                "fozzy": parser.chips_pringles_paprika_165gr_parser()[8]
            }},

            {'chips_pringles_pizza_peperoni_185gr': {
                "fozzy": parser.chips_pringles_pizza_peperoni_185gr_parser()[8]
            }},

            {'chips_pringles_sir_cubylya_165gr': {
                "novus": parser.chips_pringles_sir_cubylya_165gr_parser()[5],
                "metro": parser.chips_pringles_sir_cubylya_165gr_parser()[6],
                "fozzy": parser.chips_pringles_sir_cubylya_165gr_parser()[8]
            }},

            {'chips_pringles_original_165gr': {
                "eko": parser.chips_pringles_original_165gr_parser()[1],
                "varus": parser.chips_pringles_original_165gr_parser()[2],
                "silpo": parser.chips_pringles_original_165gr_parser()[3],
                "ashan": parser.chips_pringles_original_165gr_parser()[4],
                "novus": parser.chips_pringles_original_165gr_parser()[5],
                "metro": parser.chips_pringles_original_165gr_parser()[6],
                "fozzy": parser.chips_pringles_original_165gr_parser()[8]
            }},

            {'chips_pringles_sir_165gr': {
                "atb": parser.chips_pringles_sir_165gr_parser()[0],
                "eko": parser.chips_pringles_sir_165gr_parser()[1],
                "varus": parser.chips_pringles_sir_165gr_parser()[2],
                "silpo": parser.chips_pringles_sir_165gr_parser()[3],
                "ashan": parser.chips_pringles_sir_165gr_parser()[4],
                "novus": parser.chips_pringles_sir_165gr_parser()[5],
                "metro": parser.chips_pringles_sir_165gr_parser()[6],
                "fozzy": parser.chips_pringles_sir_165gr_parser()[8]
            }},

            {'chips_lays_paprika_120gr': {
                "varus": parser.chips_lays_paprika_120gr_parser()[2],
                "silpo": parser.chips_lays_paprika_120gr_parser()[3],
                "novus": parser.chips_lays_paprika_120gr_parser()[5],
                "metro": parser.chips_lays_paprika_120gr_parser()[6],
                "fozzy": parser.chips_lays_paprika_120gr_parser()[8]
            }},

            {'chips_lays_crab_120gr': {
                "atb": parser.chips_lays_crab_120gr_parser()[0],
                "eko": parser.chips_lays_crab_120gr_parser()[1],
                "varus": parser.chips_lays_crab_120gr_parser()[2],
                "silpo": parser.chips_lays_crab_120gr_parser()[3],
                "novus": parser.chips_lays_crab_120gr_parser()[5],
                "metro": parser.chips_lays_crab_120gr_parser()[6],
                "fozzy": parser.chips_lays_crab_120gr_parser()[8]
            }}
        ]
        # далее записываем цены в json-файл
        write_prices_to_json(all_products_names_batch_5, batch_5_path, mode_type_first_write)

    # для 6-го батча
    elif batch_name == batch_name_6:
        all_products_names_batch_6 = [
            {'chips_lays_sir_60gr': {
                "eko": parser.chips_lays_sir_60gr_parser()[1],
                "varus": parser.chips_lays_sir_60gr_parser()[2],
                "silpo": parser.chips_lays_sir_60gr_parser()[3],
                "novus": parser.chips_lays_sir_60gr_parser()[5],
                "metro": parser.chips_lays_sir_60gr_parser()[6],
                "fozzy": parser.chips_lays_sir_60gr_parser()[8]
            }},

            {'sir_svet_feta_ukr_rozsil_45_1kg': {
                "fozzy": parser.sir_svet_feta_ukr_rozsil_45_1kg_parser()[8]
            }},

            {'olivki_extra_chorni_bez_kist_300gr': {
                "fozzy": parser.olivki_extra_chorni_bez_kist_300gr_parser()[8]
            }},

            {'oliv_oil_povna_chasha_913gr': {
                "fozzy": parser.oliv_oil_povna_chasha_913gr_parser()[8]
            }},

            {'basilik_chervoniy_svij': {
                "varus": parser.basilik_chervoniy_svij_parser()[2],
                "silpo": parser.basilik_chervoniy_svij_parser()[3],
                "novus": parser.basilik_chervoniy_svij_parser()[5],
                "metro": parser.basilik_chervoniy_svij_parser()[6],
                "fozzy": parser.basilik_chervoniy_svij_parser()[8]
            }},

            {'pelmeni_gerkules_firm_400gr': {
                "varus": parser.pelmeni_gerkules_firm_400gr_parser()[2],
                "silpo": parser.pelmeni_gerkules_firm_400gr_parser()[3],
                "novus": parser.pelmeni_gerkules_firm_400gr_parser()[5],
                "fozzy": parser.pelmeni_gerkules_firm_400gr_parser()[8]
            }},

            {'pelmeni_gerkules_firm_800gr': {
                "varus": parser.pelmeni_gerkules_firm_800gr_parser()[2],
                "silpo": parser.pelmeni_gerkules_firm_800gr_parser()[3],
                "novus": parser.pelmeni_gerkules_firm_800gr_parser()[5],
                "metro": parser.pelmeni_gerkules_firm_800gr_parser()[6],
                "fozzy": parser.pelmeni_gerkules_firm_800gr_parser()[8]
            }},

            {'pelmeni_gerkules_indeyka_400gr': {
                "varus": parser.pelmeni_gerkules_indeyka_400gr_parser()[2],
                "silpo": parser.pelmeni_gerkules_indeyka_400gr_parser()[3],
                "novus": parser.pelmeni_gerkules_indeyka_400gr_parser()[5],
                "fozzy": parser.pelmeni_gerkules_indeyka_400gr_parser()[8]
            }},

            {'pelmeni_tri_vedmedi_firm_800gr': {
                "atb": parser.pelmeni_tri_vedmedi_firm_800gr_parser()[0],
                "varus": parser.pelmeni_tri_vedmedi_firm_800gr_parser()[2],
                "silpo": parser.pelmeni_tri_vedmedi_firm_800gr_parser()[3],
                "novus": parser.pelmeni_tri_vedmedi_firm_800gr_parser()[5],
                "metro": parser.pelmeni_tri_vedmedi_firm_800gr_parser()[6],
                "fozzy": parser.pelmeni_tri_vedmedi_firm_800gr_parser()[8]
            }},

            {'pelmeni_tri_vedmedi_mishutka_400gr': {
                "atb": parser.pelmeni_tri_vedmedi_mishutka_400gr_parser()[0],
                "eko": parser.pelmeni_tri_vedmedi_mishutka_400gr_parser()[1],
                "varus": parser.pelmeni_tri_vedmedi_mishutka_400gr_parser()[2],
                "silpo": parser.pelmeni_tri_vedmedi_mishutka_400gr_parser()[3],
                "novus": parser.pelmeni_tri_vedmedi_mishutka_400gr_parser()[5],
                "metro": parser.pelmeni_tri_vedmedi_mishutka_400gr_parser()[6],
                "fozzy": parser.pelmeni_tri_vedmedi_mishutka_400gr_parser()[8]
            }},

            {'pelmeni_extra_firm_800gr': {
                "fozzy": parser.pelmeni_extra_firm_800gr_parser()[8]
            }},

            {'pelmeni_extra_sibir_500gr': {
                "fozzy": parser.pelmeni_extra_sibir_500gr_parser()[8]
            }},

            {'pelmeni_extra_ravioli_dom_800gr': {
                "fozzy": parser.pelmeni_extra_ravioli_dom_800gr_parser()[8]
            }},

            {'seven_up_033_jb': {
                "atb": parser.seven_up_033_jb_parser()[0],
                "eko": parser.seven_up_033_jb_parser()[1],
                "ashan": parser.seven_up_033_jb_parser()[4],
                "novus": parser.seven_up_033_jb_parser()[5],
                "metro": parser.seven_up_033_jb_parser()[6],
                "fozzy": parser.seven_up_033_jb_parser()[8]
            }},

            {'kavun': {
                "atb": parser.kavun_parser()[0],
                "eko": parser.kavun_parser()[1],
                "varus": parser.kavun_parser()[2],
                "silpo": parser.kavun_parser()[3] * mul_price_by_10,
                "novus": parser.kavun_parser()[5],
                "metro": parser.kavun_parser()[6]
            }},

            {'jivchik_apple_2l': {
                "atb": parser.jivchik_apple_2l_parser()[0],
                "eko": parser.jivchik_apple_2l_parser()[1],
                "silpo": parser.jivchik_apple_2l_parser()[3],
                "ashan": parser.jivchik_apple_2l_parser()[4],
                "novus": parser.jivchik_apple_2l_parser()[5],
                "metro": parser.jivchik_apple_2l_parser()[6],
                "fozzy": parser.jivchik_apple_2l_parser()[8]
            }},

            {'jivchik_apple_1l': {
                "atb": parser.jivchik_apple_1l_parser()[0],
                "eko": parser.jivchik_apple_1l_parser()[1],
                "varus": parser.jivchik_apple_1l_parser()[2],
                "silpo": parser.jivchik_apple_1l_parser()[3],
                "novus": parser.jivchik_apple_1l_parser()[5],
                "metro": parser.jivchik_apple_1l_parser()[6],
                "fozzy": parser.jivchik_apple_1l_parser()[8]
            }},

            {'jivchik_apple_05l': {
                "atb": parser.jivchik_apple_05l_parser()[0],
                "eko": parser.jivchik_apple_05l_parser()[1],
                "varus": parser.jivchik_apple_05l_parser()[2],
                "silpo": parser.jivchik_apple_05l_parser()[3],
                "novus": parser.jivchik_apple_05l_parser()[5],
                "fozzy": parser.jivchik_apple_05l_parser()[8]
            }},

            {'jivchik_grusha_1l': {
                "eko": parser.jivchik_grusha_1l_parser()[1],
                "varus": parser.jivchik_grusha_1l_parser()[2],
                "silpo": parser.jivchik_grusha_1l_parser()[3],
                "ashan": parser.jivchik_grusha_1l_parser()[4],
                "novus": parser.jivchik_grusha_1l_parser()[5],
                "fozzy": parser.jivchik_grusha_1l_parser()[8]
            }},

            {'jivchik_smart_cola_2l': {
                "eko": parser.jivchik_smart_cola_2l_parser()[1],
                "silpo": parser.jivchik_smart_cola_2l_parser()[3],
                "ashan": parser.jivchik_smart_cola_2l_parser()[4],
                "novus": parser.jivchik_smart_cola_2l_parser()[5],
                "fozzy": parser.jivchik_smart_cola_2l_parser()[8]
            }},

            {'jivchik_limon_2l': {
                "eko": parser.jivchik_limon_2l_parser()[1],
                "varus": parser.jivchik_limon_2l_parser()[2],
                "silpo": parser.jivchik_limon_2l_parser()[3],
                "ashan": parser.jivchik_limon_2l_parser()[4],
                "novus": parser.jivchik_limon_2l_parser()[5],
                "metro": parser.jivchik_limon_2l_parser()[6],
                "fozzy": parser.jivchik_limon_2l_parser()[8]
            }},

            {'jivchik_smart_cola_1l': {
                "eko": parser.jivchik_smart_cola_1l_parser()[1],
                "silpo": parser.jivchik_smart_cola_1l_parser()[3],
                "ashan": parser.jivchik_smart_cola_1l_parser()[4],
                "novus": parser.jivchik_smart_cola_1l_parser()[5],
                "fozzy": parser.jivchik_smart_cola_1l_parser()[8]
            }},

            {'biola_strawb_kiwi_2l': {
                "atb": parser.biola_strawb_kiwi_2l_parser()[0],
                "novus": parser.biola_strawb_kiwi_2l_parser()[5],
                "fozzy": parser.biola_strawb_kiwi_2l_parser()[8]
            }},

            {'biola_lemonad_2l': {
                "varus": parser.biola_lemonad_2l_parser()[2],
                "silpo": parser.biola_lemonad_2l_parser()[3],
                "novus": parser.biola_lemonad_2l_parser()[5],
                "fozzy": parser.biola_lemonad_2l_parser()[8]
            }},

            {'bon_boisson_limonad_1l': {
                "varus": parser.bon_boisson_limonad_1l_parser()[2],
                "silpo": parser.bon_boisson_limonad_1l_parser()[3],
                "ashan": parser.bon_boisson_limonad_1l_parser()[4],
                "novus": parser.bon_boisson_limonad_1l_parser()[5],
                "nash_kray": parser.bon_boisson_limonad_1l_parser()[7],
                "fozzy": parser.bon_boisson_limonad_1l_parser()[8]
            }},

            {'bon_boisson_limonad_2l': {
                "eko": parser.bon_boisson_limonad_2l_parser()[1],
                "varus": parser.bon_boisson_limonad_2l_parser()[2],
                "silpo": parser.bon_boisson_limonad_2l_parser()[3],
                "ashan": parser.bon_boisson_limonad_2l_parser()[4],
                "novus": parser.bon_boisson_limonad_2l_parser()[5],
                "metro": parser.bon_boisson_limonad_2l_parser()[6],
                "nash_kray": parser.bon_boisson_limonad_2l_parser()[7],
                "fozzy": parser.bon_boisson_limonad_2l_parser()[8]
            }},

            {'bon_boisson_lime_mint_2l': {
                "fozzy": parser.bon_boisson_lime_mint_2l_parser()[8]
            }},

            {'bon_boisson_baikal_2l': {
                "eko": parser.bon_boisson_baikal_2l_parser()[1],
                "varus": parser.bon_boisson_baikal_2l_parser()[2],
                "silpo": parser.bon_boisson_baikal_2l_parser()[3],
                "ashan": parser.bon_boisson_baikal_2l_parser()[4],
                "novus": parser.bon_boisson_baikal_2l_parser()[5],
                "metro": parser.bon_boisson_baikal_2l_parser()[6],
                "fozzy": parser.bon_boisson_baikal_2l_parser()[8]
            }},

            {'bon_boisson_tarhun_2l': {
                "atb": parser.bon_boisson_tarhun_2l_parser()[0],
                "eko": parser.bon_boisson_tarhun_2l_parser()[1],
                "varus": parser.bon_boisson_tarhun_2l_parser()[2],
                "silpo": parser.bon_boisson_tarhun_2l_parser()[3],
                "ashan": parser.bon_boisson_tarhun_2l_parser()[4],
                "novus": parser.bon_boisson_tarhun_2l_parser()[5],
                "metro": parser.bon_boisson_tarhun_2l_parser()[6],
                "nash_kray": parser.bon_boisson_tarhun_2l_parser()[7],
                "fozzy": parser.bon_boisson_tarhun_2l_parser()[8]
            }},

            {'bon_boisson_baikal_1l': {
                "silpo": parser.bon_boisson_baikal_1l_parser()[3],
                "ashan": parser.bon_boisson_baikal_1l_parser()[4],
                "novus": parser.bon_boisson_baikal_1l_parser()[5],
                "nash_kray": parser.bon_boisson_baikal_1l_parser()[7],
                "fozzy": parser.bon_boisson_baikal_1l_parser()[8]
            }},

            {'borsh_red': {
                "atb": ((parser.water_in_6l_bottle_parser()[0] / rate_3) + (
                        parser.pork_lopatka_parser()[0] * eighty_percent_price)
                        + (parser.potato_parser()[0] / double_price) + (parser.beet_parser()[0] / mul_price_by_10)
                        + (parser.carrot_parcer()[0] / mul_price_by_10) + (parser.onion_parcer()[0] * twenty_percent_price)
                        + (parser.cabbage_parcer()[0] * fourty_percent_rate)) / devide_by_6,

                "eko": ((parser.water_in_6l_bottle_parser()[1] / rate_3) + (
                        parser.pork_lopatka_parser()[1] * eighty_percent_price)
                        + (parser.potato_parser()[1] / double_price) + (parser.beet_parser()[1] / mul_price_by_10)
                        + (parser.carrot_parcer()[1] / mul_price_by_10) + (parser.onion_parcer()[1] * twenty_percent_price)
                        + (parser.cabbage_parcer()[1] * fourty_percent_rate)) / devide_by_6,

                "varus": ((parser.water_in_6l_bottle_parser()[2] / rate_3) + (
                        parser.pork_lopatka_parser()[2] * eighty_percent_price)
                          + (parser.potato_parser()[2] / double_price) + (parser.beet_parser()[2] / mul_price_by_10)
                          + (parser.carrot_parcer()[2] / mul_price_by_10) + (parser.onion_parcer()[2] * twenty_percent_price)
                          + (parser.cabbage_parcer()[2] * fourty_percent_rate)) / devide_by_6,

                "silpo": ((parser.water_in_6l_bottle_parser()[3] / rate_3)
                          + ((parser.pork_lopatka_parser()[3]) * eighty_percent_price)
                          + (parser.potato_parser()[3] / double_price) + (
                                  (parser.beet_parser()[3]) / mul_price_by_10)
                          + ((parser.carrot_parcer()[3]) / mul_price_by_10)
                          + ((parser.onion_parcer()[3]) * twenty_percent_price)
                          + ((parser.cabbage_parcer()[3]) * fourty_percent_rate)) / devide_by_6,

                "novus": ((parser.water_in_6l_bottle_parser()[5] / rate_3) + (
                        parser.pork_lopatka_parser()[5] * eighty_percent_price)
                          + (parser.potato_parser()[5] / double_price) + (parser.beet_parser()[5] / mul_price_by_10)
                          + (parser.carrot_parcer()[5] / mul_price_by_10) + (parser.onion_parcer()[5] * twenty_percent_price)
                          + (parser.cabbage_parcer()[5] * fourty_percent_rate)) / devide_by_6,

                "metro": ((parser.water_in_6l_bottle_parser()[6] / rate_3) + (
                        parser.pork_lopatka_parser()[6] * eighty_percent_price)
                          + (parser.potato_parser()[6] / double_price) + (parser.beet_parser()[6] / mul_price_by_10)
                          + (parser.carrot_parcer()[6] / mul_price_by_10) + (parser.onion_parcer()[6] * twenty_percent_price)
                          + (parser.cabbage_parcer()[6] * fourty_percent_rate)) / devide_by_6,

                "fozzy": ((parser.water_in_6l_bottle_parser()[8] / rate_3) + (
                        parser.pork_lopatka_parser()[8] * eighty_percent_price)
                          + (parser.potato_parser()[8] / double_price) + (parser.beet_parser()[8] / mul_price_by_10)
                          + (parser.carrot_parcer()[8] / mul_price_by_10) + (parser.onion_parcer()[8] * twenty_percent_price)
                          + (parser.cabbage_parcer()[8] * fourty_percent_rate)) / devide_by_6
            }},

            {'veriniki_potato': {
                "atb": ((parser.four_parser()[0] * fourty_percent_rate) + (parser.water_in_6l_bottle_parser()[0] * water_var)
                        + (parser.egg_parcer()[0] * ten_percent_price) + (parser.oil_for_dishes_parser()[0] * five_percent_price)
                        + (parser.onion_parcer()[0] * twenty_percent_price) + (parser.sour_cream_for_dishes_parser()[0])
                        + (parser.potato_parser()[0] * sixty_percent_price)) / devide_by_5,

                "eko": ((parser.four_parser()[1] * fourty_percent_rate) + (parser.water_in_6l_bottle_parser()[1] * water_var)
                        + ((parser.egg_parcer()[1] * mul_price_by_10) * ten_percent_price) + (
                                parser.oil_for_dishes_parser()[1] * five_percent_price)
                        + (parser.onion_parcer()[1] * twenty_percent_price) + (parser.sour_cream_for_dishes_parser()[1])
                        + (parser.potato_parser()[1] * sixty_percent_price)) / devide_by_5,

                "varus": ((parser.four_parser()[2] * fourty_percent_rate) + (parser.water_in_6l_bottle_parser()[2] * water_var)
                          + (parser.egg_parcer()[2] * ten_percent_price) + (parser.oil_for_dishes_parser()[2] * five_percent_price)
                          + (parser.onion_parcer()[2] * twenty_percent_price) + (parser.sour_cream_for_dishes_parser()[2])
                          + (parser.potato_parser()[2] * sixty_percent_price)) / devide_by_5,

                "silpo": ((parser.four_parser()[3] * fourty_percent_rate) + (parser.water_in_6l_bottle_parser()[3] * water_var)
                          + (parser.egg_parcer()[3] * ten_percent_price) + (parser.oil_shedriy_dar_850_parcer()[3] * five_percent_price)
                          + ((parser.onion_parcer()[3]) * twenty_percent_price) + (
                              parser.sour_cream_for_dishes_parser()[3])
                          + (parser.potato_parser()[3] * sixty_percent_price)) / devide_by_5,

                "novus": ((parser.four_parser()[5] * fourty_percent_rate) + (parser.water_in_6l_bottle_parser()[5] * water_var)
                          + (parser.egg_parcer()[5] * ten_percent_price) + (parser.oil_shedriy_dar_850_parcer()[5] * five_percent_price)
                          + (parser.onion_parcer()[5] * twenty_percent_price) + (parser.sour_cream_for_dishes_parser()[5])
                          + (parser.potato_parser()[5] * sixty_percent_price)) / devide_by_5,

                "metro": ((parser.four_parser()[6] * fourty_percent_rate) + (parser.water_in_6l_bottle_parser()[6] * water_var)
                          + (parser.egg_parcer()[6] * ten_percent_price) + (parser.oil_shedriy_dar_850_parcer()[6] * five_percent_price)
                          + (parser.onion_parcer()[6] * twenty_percent_price) + (parser.sour_cream_for_dishes_parser()[6])
                          + (parser.potato_parser()[6] * sixty_percent_price)) / devide_by_5,

                "fozzy": ((parser.four_parser()[8] * fourty_percent_rate) + (parser.water_in_6l_bottle_parser()[8] * water_var)
                          + ((parser.egg_parcer()[8] * mul_price_by_10) * ten_percent_price) + (
                                  parser.oil_shedriy_dar_850_parcer()[8] * five_percent_price)
                          + (parser.onion_parcer()[8] * twenty_percent_price) + (parser.sour_cream_for_dishes_parser()[8])
                          + (parser.potato_parser()[8] * sixty_percent_price)) / devide_by_5
            }},

            {'veriniki_kapusta': {
                "atb": ((parser.four_parser()[0] * fourty_percent_rate) + (parser.water_in_6l_bottle_parser()[0] * water_var)
                        + (parser.egg_parcer()[0] * ten_percent_price) + (parser.oil_for_dishes_parser()[0] * five_percent_price)
                        + (parser.onion_parcer()[0] * fourty_percent_rate) + (parser.sour_cream_for_dishes_parser()[0])
                        + (parser.cabbage_parcer()[0] * sixty_percent_price) + parser.carrot_parcer()[
                            0] * five_percent_price) / devide_by_5,

                "eko": ((parser.four_parser()[1] * fourty_percent_rate) + (parser.water_in_6l_bottle_parser()[1] * water_var)
                        + ((parser.egg_parcer()[1] * mul_price_by_10) * ten_percent_price) + (
                                parser.oil_for_dishes_parser()[1] * five_percent_price)
                        + (parser.onion_parcer()[1] * fourty_percent_rate) + (parser.sour_cream_for_dishes_parser()[1])
                        + (parser.cabbage_parcer()[1] * sixty_percent_price) + parser.carrot_parcer()[
                            1] * five_percent_price) / devide_by_5,

                "varus": ((parser.four_parser()[2] * fourty_percent_rate) + (parser.water_in_6l_bottle_parser()[2] * water_var)
                          + (parser.egg_parcer()[2] * ten_percent_price) + (parser.oil_for_dishes_parser()[2] * five_percent_price)
                          + (parser.onion_parcer()[2] * fourty_percent_rate) + (parser.sour_cream_for_dishes_parser()[2])
                          + (parser.cabbage_parcer()[2] * sixty_percent_price) + parser.carrot_parcer()[
                              2] * five_percent_price) / devide_by_5,

                "silpo": ((parser.four_parser()[3] * fourty_percent_rate) + (parser.water_in_6l_bottle_parser()[3] * water_var)
                          + (parser.egg_parcer()[3] * ten_percent_price) + (parser.oil_shedriy_dar_850_parcer()[3] * five_percent_price)
                          + ((parser.onion_parcer()[3]) * fourty_percent_rate) + (
                              parser.sour_cream_for_dishes_parser()[3])
                          + (parser.cabbage_parcer()[3] * sixty_percent_price) + parser.carrot_parcer()[
                              3] * five_percent_price) / devide_by_5,

                "novus": ((parser.four_parser()[5] * fourty_percent_rate) + (parser.water_in_6l_bottle_parser()[5] * water_var)
                          + (parser.egg_parcer()[5] * ten_percent_price) + (parser.oil_shedriy_dar_850_parcer()[5] * five_percent_price)
                          + (parser.onion_parcer()[5] * fourty_percent_rate) + (parser.sour_cream_for_dishes_parser()[5])
                          + (parser.cabbage_parcer()[5] * sixty_percent_price) + parser.carrot_parcer()[
                              5] * five_percent_price) / devide_by_5,

                "metro": ((parser.four_parser()[6] * fourty_percent_rate) + (parser.water_in_6l_bottle_parser()[6] * water_var)
                          + (parser.egg_parcer()[6] * ten_percent_price) + (parser.oil_shedriy_dar_850_parcer()[6] * five_percent_price)
                          + (parser.onion_parcer()[6] * fourty_percent_rate) + (parser.sour_cream_for_dishes_parser()[6])
                          + (parser.cabbage_parcer()[6] * sixty_percent_price) + parser.carrot_parcer()[
                              6] * five_percent_price) / devide_by_5,

                "fozzy": ((parser.four_parser()[8] * fourty_percent_rate) + (parser.water_in_6l_bottle_parser()[8] * water_var)
                          + ((parser.egg_parcer()[8] * mul_price_by_10) * ten_percent_price) + (
                                  parser.oil_shedriy_dar_850_parcer()[8] * five_percent_price)
                          + (parser.onion_parcer()[8] * fourty_percent_rate) + (parser.sour_cream_for_dishes_parser()[8])
                          + (parser.cabbage_parcer()[8] * sixty_percent_price) + parser.carrot_parcer()[
                              8] * five_percent_price) / devide_by_5
            }},

            {'grecheskiy_salat': {
                "fozzy": ((parser.tomato_parser()[8] * twenty_five_percent_price) + (parser.cucumber_parser()[8] * fifteen_percent_price)
                          + (parser.red_bolg_papper_parser()[8] * fifteen_percent_price) + (
                                  parser.onion_parcer()[8] * five_percent_price)
                          + (parser.onion_parcer()[8] * ninety_percent_price) + (
                                  parser.sir_svet_feta_ukr_rozsil_45_1kg_parser()[8] * fifteen_percent_price)
                          + (parser.olivki_extra_chorni_bez_kist_300gr_parser()[8] * oliv_var) +
                          (parser.oliv_oil_povna_chasha_913gr_parser()[
                               8] * five_percent_price) + parser.basilik_chervoniy_svij_parser()[
                              8] * half_price) / devide_by_4,
            }}
        ]
        # далее записываем цены в json-файл
        write_prices_to_json(all_products_names_batch_6, batch_6_path, mode_type_first_write)

    # для 7-го батча
    elif batch_name == batch_name_7:
        all_products_names_batch_7 = [

            {'bon_boisson_mult_sok_1l': {
                "varus": parser.bon_boisson_mult_sok_1l_parser()[2],
                "silpo": parser.bon_boisson_mult_sok_1l_parser()[3],
                "nash_kray": parser.bon_boisson_mult_sok_1l_parser()[7],
                "fozzy": parser.bon_boisson_mult_sok_1l_parser()[8]
            }},

            {'bon_boisson_mango_2l': {
                "varus": parser.bon_boisson_mango_2l_parser()[2],
                "silpo": parser.bon_boisson_mango_2l_parser()[3],
                "novus": parser.bon_boisson_mango_2l_parser()[5],
                "metro": parser.bon_boisson_mango_2l_parser()[6],
                "fozzy": parser.bon_boisson_mango_2l_parser()[8]
            }},

            {'bon_boisson_mohito_2l': {
                "varus": parser.bon_boisson_mohito_2l_parser()[2],
                "silpo": parser.bon_boisson_mohito_2l_parser()[3],
                "metro": parser.bon_boisson_mohito_2l_parser()[6],
                "nash_kray": parser.bon_boisson_mohito_2l_parser()[7],
                "fozzy": parser.bon_boisson_mohito_2l_parser()[8]
            }},

            {'bon_boisson_sitro_2l': {
                "varus": parser.bon_boisson_sitro_2l_parser()[2],
                "novus": parser.bon_boisson_sitro_2l_parser()[5],
                "metro": parser.bon_boisson_sitro_2l_parser()[6],
                "nash_kray": parser.bon_boisson_sitro_2l_parser()[7],
                "fozzy": parser.bon_boisson_sitro_2l_parser()[8]
            }},

            {'bon_boisson_krem_soda_2l': {
                "silpo": parser.bon_boisson_krem_soda_2l_parser()[3],
                "ashan": parser.bon_boisson_krem_soda_2l_parser()[4],
                "novus": parser.bon_boisson_krem_soda_2l_parser()[5],
                "metro": parser.bon_boisson_krem_soda_2l_parser()[6],
                "nash_kray": parser.bon_boisson_krem_soda_2l_parser()[7],
                "fozzy": parser.bon_boisson_krem_soda_2l_parser()[8]
            }},

            {'bon_boisson_mult_sok_2l': {
                "eko": parser.bon_boisson_mult_sok_2l_parser()[1],
                "novus": parser.bon_boisson_mult_sok_2l_parser()[5],
                "metro": parser.bon_boisson_mult_sok_2l_parser()[6],
                "nash_kray": parser.bon_boisson_mult_sok_2l_parser()[7],
                "fozzy": parser.bon_boisson_mult_sok_2l_parser()[8]
            }},

            {'mirinda_orange_033jb': {
                "atb": parser.mirinda_orange_033jb_parser()[0],
                "novus": parser.mirinda_orange_033jb_parser()[5],
                "metro": parser.mirinda_orange_033jb_parser()[6],
                "fozzy": parser.mirinda_orange_033jb_parser()[8]
            }},
            {'mirinda_orange_05l': {
                "eko": parser.mirinda_orange_05l_parser()[1],
                "varus": parser.mirinda_orange_05l_parser()[2],
                "novus": parser.mirinda_orange_05l_parser()[5],
                "fozzy": parser.mirinda_orange_05l_parser()[8]
            }},

            {'schweppes_granat_1l': {
                "silpo": parser.schweppes_granat_1l_parser()[3]
            }},
            {'schweppes_indian_tonic_033jb': {
                "eko": parser.schweppes_indian_tonic_033jb_parser()[1],
                "varus": parser.schweppes_indian_tonic_033jb_parser()[2],
                "silpo": parser.schweppes_indian_tonic_033jb_parser()[3],
                "ashan": parser.schweppes_indian_tonic_033jb_parser()[4],
                "novus": parser.schweppes_indian_tonic_033jb_parser()[5],
                "nash_kray": parser.schweppes_indian_tonic_033jb_parser()[7],
                "fozzy": parser.schweppes_indian_tonic_033jb_parser()[8]
            }},

            {'schweppes_original_bitter_lemon_033jb': {
                "eko": parser.schweppes_original_bitter_lemon_033jb_parser()[1],
                "silpo": parser.schweppes_original_bitter_lemon_033jb_parser()[3],
                "novus": parser.schweppes_original_bitter_lemon_033jb_parser()[5]
            }},

            {'schweppes_original_bitter_lemon_075l': {
                "atb": parser.schweppes_original_bitter_lemon_075l_parser()[0],
                "eko": parser.schweppes_original_bitter_lemon_075l_parser()[1],
                "silpo": parser.schweppes_original_bitter_lemon_075l_parser()[3],
                "novus": parser.schweppes_original_bitter_lemon_075l_parser()[5],
                "metro": parser.schweppes_original_bitter_lemon_075l_parser()[6],
                "fozzy": parser.schweppes_original_bitter_lemon_075l_parser()[8]
            }},

            {'schweppes_original_bitter_lemon_1l': {
                "silpo": parser.schweppes_original_bitter_lemon_1l_parser()[3]
            }},
            {'schweppes_classic_mojito_033jb': {
                "eko": parser.schweppes_classic_mojito_033jb_parser()[1],
                "varus": parser.schweppes_classic_mojito_033jb_parser()[2],
                "silpo": parser.schweppes_classic_mojito_033jb_parser()[3],
                "ashan": parser.schweppes_classic_mojito_033jb_parser()[4],
                "novus": parser.schweppes_classic_mojito_033jb_parser()[5],
                "metro": parser.schweppes_classic_mojito_033jb_parser()[6],
                "nash_kray": parser.schweppes_classic_mojito_033jb_parser()[7],
                "fozzy": parser.schweppes_classic_mojito_033jb_parser()[8]
            }},

            {'farsh_govyajiy': {
                "atb": parser.farsh_govyajiy_parser()[0] * double_price,
                "varus": parser.farsh_govyajiy_parser()[2],
                "ashan": parser.farsh_govyajiy_parser()[4] * double_price + 24.60,
                "novus": parser.farsh_govyajiy_parser()[5],
                "metro": parser.farsh_govyajiy_parser()[6] * double_price,
                "fozzy": parser.farsh_govyajiy_parser()[8]
            }},

            {'rice_extra_krugliy_1kg': {
                "fozzy": parser.rice_extra_krugl_1kg_parser()[8]
            }},

            {'golubci': {
                "fozzy": ((parser.cabbage_parcer()[8] * half_price) + (parser.sour_cream_for_dishes_parser()[8])
                          + (parser.farsh_govyajiy_parser()[8] * ten_percent_price) + (
                                      parser.svin_farsh_parser()[8] * ten_percent_price)
                          + (parser.tomato_parser()[8] * ten_percent_price) + (
                                      parser.rice_extra_krugl_1kg_parser()[8] * six_percent_price)
                          + (parser.carrot_parcer()[8] * five_percent_price) + (
                                      parser.onion_parcer()[8] * three_percent_price)) / devide_by_3
            }},

            {'classic_plov_v_kazane_na_plite_svinina': {
                "fozzy": ((parser.svin_osheek_bez_kistki_parser()[8] * 0.04)
                          + (parser.rice_extra_krugl_1kg_parser()[8] * 0.04) + (parser.onion_parcer()[8] * 0.03)
                          + (parser.carrot_parcer()[8] * 0.03) + 6)
            }},

            {'maslo_ferma_selyanske_73jir_180gr': {
                "atb": parser.maslo_sliv_ferma_selyanske_73jir_180gr_parser()[0],
                "eko": parser.maslo_sliv_ferma_selyanske_73jir_180gr_parser()[1],
                "varus": parser.maslo_sliv_ferma_selyanske_73jir_180gr_parser()[2],
                "silpo": parser.maslo_sliv_ferma_selyanske_73jir_180gr_parser()[3],
                "novus": parser.maslo_sliv_ferma_selyanske_73jir_180gr_parser()[5],
                "metro": parser.maslo_sliv_ferma_selyanske_73jir_180gr_parser()[6],
                "nash_kray": parser.maslo_sliv_ferma_selyanske_73jir_180gr_parser()[7],
                "fozzy": parser.maslo_sliv_ferma_selyanske_73jir_180gr_parser()[8]
            }},

            {'classic_cotleti_po_kievski': {
                "fozzy": ( (parser.kuryache_file_parser()[8] * 0.125)
                           + (parser.maslo_sliv_ferma_selyanske_73jir_180gr_parser()[8] * 0.025)
                           + (parser.egg_parcer()[8] * 0.08)
                           + (parser.oil_for_dishes_parser()[8] * 0.03) + 6)
            }},

            {'maslo_sliv_ferma_chocolat_62jir_180gr': {
                "varus": parser.maslo_sliv_ferma_chocolat_62jir_180gr_parser()[2],
                "silpo": parser.maslo_sliv_ferma_chocolat_62jir_180gr_parser()[3],
                "nash_kray": parser.maslo_sliv_ferma_chocolat_62jir_180gr_parser()[7],
                "fozzy": parser.maslo_sliv_ferma_chocolat_62jir_180gr_parser()[8]
            }},

            {'maslo_sliv_ferma_extra_82_5jir_180gr': {
                "eko": parser.maslo_sliv_ferma_extra_82_5jir_180gr_parser()[1],
                "varus": parser.maslo_sliv_ferma_extra_82_5jir_180gr_parser()[2],
                "silpo": parser.maslo_sliv_ferma_extra_82_5jir_180gr_parser()[3],
                "metro": parser.maslo_sliv_ferma_extra_82_5jir_180gr_parser()[6],
                "fozzy": parser.maslo_sliv_ferma_extra_82_5jir_180gr_parser()[8]
            }},

            {'maslo_sliv_ferma_buter_63jir_180gr': {
                "atb": parser.maslo_sliv_ferma_buter_63jir_180gr_parser()[0],
                "varus": parser.maslo_sliv_ferma_buter_63jir_180gr_parser()[2],
                "silpo": parser.maslo_sliv_ferma_buter_63jir_180gr_parser()[3],
                "nash_kray": parser.maslo_sliv_ferma_buter_63jir_180gr_parser()[7]
            }},
             {'maslo_ferma_selyanske_73jir_400gr': {
                "atb": parser.maslo_sliv_ferma_selyanske_73jir_400gr_parser()[0],
                "eko": parser.maslo_sliv_ferma_selyanske_73jir_400gr_parser()[1],
                "silpo": parser.maslo_sliv_ferma_selyanske_73jir_400gr_parser()[3],
                "nash_kray": parser.maslo_sliv_ferma_selyanske_73jir_400gr_parser()[7]
            }},

            {'maslo_sliv_jagotinske_extra_82_5_180gr': {
                "atb": parser.maslo_sliv_jagotinske_extra_82_5_180gr_parser()[0],
                "eko": parser.maslo_sliv_jagotinske_extra_82_5_180gr_parser()[1],
                "varus": parser.maslo_sliv_jagotinske_extra_82_5_180gr_parser()[2],
                "silpo": parser.maslo_sliv_jagotinske_extra_82_5_180gr_parser()[3],
                "novus": parser.maslo_sliv_jagotinske_extra_82_5_180gr_parser()[5],
                "metro": parser.maslo_sliv_jagotinske_extra_82_5_180gr_parser()[6],
                "nash_kray": parser.maslo_sliv_jagotinske_extra_82_5_180gr_parser()[7],
                "fozzy": parser.maslo_sliv_jagotinske_extra_82_5_180gr_parser()[8]
            }},

            {'maslo_sliv_jagotinske_buter_69_2_200gr': {
                "eko": parser.maslo_sliv_jagotinske_buter_69_2_200gr_parser()[1],
                "silpo": parser.maslo_sliv_jagotinske_buter_69_2_200gr_parser()[3],
                "fozzy": parser.maslo_sliv_jagotinske_buter_69_2_200gr_parser()[8]
            }},

            {'maslo_sliv_selyanske_extra_82_180gr': {
                "varus": parser.maslo_sliv_selyanske_extra_82_180gr_parser()[2],
                "silpo": parser.maslo_sliv_selyanske_extra_82_180gr_parser()[3],
                "novus": parser.maslo_sliv_selyanske_extra_82_180gr_parser()[5],
                "metro": parser.maslo_sliv_selyanske_extra_82_180gr_parser()[6],
                "fozzy": parser.maslo_sliv_selyanske_extra_82_180gr_parser()[8]
            }},

            {'maslo_sliv_selyanske_buter_63_180gr': {
                "silpo": parser.maslo_sliv_selyanske_buter_63_180gr_parser()[3],
                "fozzy": parser.maslo_sliv_selyanske_buter_63_180gr_parser()[8]
            }},

            {'maslo_sliv_selyanske_72_5_180gr': {
                "eko": parser.maslo_sliv_selyanske_72_5_180gr_parser()[1],
                "varus": parser.maslo_sliv_selyanske_72_5_180gr_parser()[2],
                "metro": parser.maslo_sliv_selyanske_72_5_180gr_parser()[6]
            }},

            {'maslo_sliv_globino_extra_82_500gr': {
                "fozzy": parser.maslo_sliv_globino_extra_82_500gr_parser()[8]
            }},

            {'maslo_sliv_globino_bezlaktoz_82_180gr': {
                "eko": parser.maslo_sliv_globino_bezlaktoz_82_180gr_parser()[1],
                "fozzy": parser.maslo_sliv_globino_bezlaktoz_82_180gr_parser()[8]
            }},

            {'maslo_sliv_galichina_82_5_180gr': {
                "atb": parser.maslo_sliv_galichina_82_5_180gr_parser()[0],
                "eko": parser.maslo_sliv_galichina_82_5_180gr_parser()[1],
                "varus": parser.maslo_sliv_galichina_82_5_180gr_parser()[2],
                "silpo": parser.maslo_sliv_galichina_82_5_180gr_parser()[3],
                "novus": parser.maslo_sliv_galichina_82_5_180gr_parser()[5],
                "nash_kray": parser.maslo_sliv_galichina_82_5_180gr_parser()[7],
                "fozzy": parser.maslo_sliv_galichina_82_5_180gr_parser()[8]
            }},

            {'maslo_sliv_galichina_selyanske_72_6_180gr': {
                "eko": parser.maslo_sliv_galichina_selyanske_72_6_180gr_parser()[1],
                "varus": parser.maslo_sliv_galichina_selyanske_72_6_180gr_parser()[2],
                "silpo": parser.maslo_sliv_galichina_selyanske_72_6_180gr_parser()[3],
                "novus": parser.maslo_sliv_galichina_selyanske_72_6_180gr_parser()[5],
                "nash_kray": parser.maslo_sliv_galichina_selyanske_72_6_180gr_parser()[7]
            }},

            {'maslo_sliv_malokiya_82_180gr': {
                "atb": parser.maslo_sliv_malokiya_82_180gr_parser()[0],
                "eko": parser.maslo_sliv_malokiya_82_180gr_parser()[1],
                "silpo": parser.maslo_sliv_malokiya_82_180gr_parser()[3],
                "novus": parser.maslo_sliv_malokiya_82_180gr_parser()[5],
                "metro": parser.maslo_sliv_malokiya_82_180gr_parser()[6],
                "nash_kray": parser.maslo_sliv_malokiya_82_180gr_parser()[7],
                "fozzy": parser.maslo_sliv_malokiya_82_180gr_parser()[8]
            }},

            {'maslo_sliv_farm_fresh_extra_82_180gr': {
                "fozzy": parser.maslo_sliv_farm_fresh_extra_82_180gr_parser()[8]
            }},
             {'maslo_sliv_farm_fresh_selyanske_73_180gr': {
                "fozzy": parser.maslo_sliv_farm_fresh_selyanske_73_180gr_parser()[8]
            }},
             {'maslo_sliv_president_82_200gr': {
                "varus": parser.maslo_sliv_president_82_200gr_parser()[2],
                "silpo": parser.maslo_sliv_president_82_200gr_parser()[3],
                "novus": parser.maslo_sliv_president_82_200gr_parser()[5],
                "metro": parser.maslo_sliv_president_82_200gr_parser()[6],
                "fozzy": parser.maslo_sliv_president_82_200gr_parser()[8]
            }},
             {'maslo_sliv_president_82_400gr': {
                "silpo": parser.maslo_sliv_president_82_400gr_parser()[3],
                "metro": parser.maslo_sliv_president_82_400gr_parser()[6],
                "fozzy": parser.maslo_sliv_president_82_400gr_parser()[8]
            }},
             {'maslo_sliv_president_solone_80_200gr': {
                "silpo": parser.maslo_sliv_president_solone_80_200gr_parser()[3],
                "fozzy": parser.maslo_sliv_president_solone_80_200gr_parser()[8]
            }},

            {'jacobs_monarch_banka_95gr': {
                "atb": parser.jacobs_monarch_banka_95gr_parser()[0],
                "eko": parser.jacobs_monarch_banka_95gr_parser()[1],
                "varus": parser.jacobs_monarch_banka_95gr_parser()[2],
                "silpo": parser.jacobs_monarch_banka_95gr_parser()[3],
                "ashan": parser.jacobs_monarch_banka_95gr_parser()[4],
                "novus": parser.jacobs_monarch_banka_95gr_parser()[5],
                "metro": parser.jacobs_monarch_banka_95gr_parser()[6],
                "nash_kray": parser.jacobs_monarch_banka_95gr_parser()[7],
                "fozzy": parser.jacobs_monarch_banka_95gr_parser()[8]
            }},

            {'jacobs_monarch_banka_190gr': {
                "atb": parser.jacobs_monarch_banka_190gr_parser()[0],
                "eko": parser.jacobs_monarch_banka_190gr_parser()[1],
                "varus": parser.jacobs_monarch_banka_190gr_parser()[2],
                "silpo": parser.jacobs_monarch_banka_190gr_parser()[3],
                "novus": parser.jacobs_monarch_banka_190gr_parser()[5],
                "nash_kray": parser.jacobs_monarch_banka_190gr_parser()[7]
            }},

            {'jacobs_monarch_banka_200gr': {
                "atb": parser.jacobs_monarch_banka_200gr_parser()[0],
                "eko": parser.jacobs_monarch_banka_200gr_parser()[1],
                "ashan": parser.jacobs_monarch_banka_200gr_parser()[4]
            }},
             {'jacobs_monarch_banka_100gr': {
                "eko": parser.jacobs_monarch_banka_100gr_parser()[1],
                "ashan": parser.jacobs_monarch_banka_100gr_parser()[4]
            }},
             {'jacobs_monarch_banka_50gr': {
                "ashan": parser.jacobs_monarch_banka_50gr_parser()[4],
                "novus": parser.jacobs_monarch_banka_50gr_parser()[5],
                "nash_kray": parser.jacobs_monarch_banka_50gr_parser()[7]
            }},

            {'jacobs_monarch_classico_pack_225gr': {
                "silpo": parser.jacobs_monarch_classico_pack_225gr_parser()[3],
                "ashan": parser.jacobs_monarch_classico_pack_225gr_parser()[4]
            }},

            {'jacobs_barista_strong_pack_225gr': {
                "silpo": parser.jacobs_barista_strong_pack_225gr_parser()[3],
                "ashan": parser.jacobs_barista_strong_pack_225gr_parser()[4],
                "nash_kray": parser.jacobs_barista_strong_pack_225gr_parser()[7]
            }},

            {'jacobs_kronung_500gr': {
                "silpo": parser.jacobs_kronung_500gr_parser()[3]
            }},

            {'jacobs_monarch_classico_pack_70gr': {
                "eko": parser.jacobs_monarch_classico_pack_70gr_parser()[1],
                "varus": parser.jacobs_monarch_classico_pack_70gr_parser()[2],
                "silpo": parser.jacobs_monarch_classico_pack_70gr_parser()[3],
                "novus": parser.jacobs_monarch_classico_pack_70gr_parser()[5]
            }},

             {'jacobs_monarch_intense_200gr': {
                "eko": parser.jacobs_monarch_intense_200gr_parser()[1],
                "silpo": parser.jacobs_monarch_intense_200gr_parser()[3],
                "novus": parser.jacobs_monarch_intense_200gr_parser()[5],
                "metro": parser.jacobs_monarch_intense_200gr_parser()[6],
                "nash_kray": parser.jacobs_monarch_intense_200gr_parser()[7]
            }},

            {'jacobs_espresso_230gr': {
                "atb": parser.jacobs_espresso_230gr_parser()[0],
                "eko": parser.jacobs_espresso_230gr_parser()[1],
                "varus": parser.jacobs_espresso_230gr_parser()[2],
                "silpo": parser.jacobs_espresso_230gr_parser()[3],
                "metro": parser.jacobs_espresso_230gr_parser()[6],
                "nash_kray": parser.jacobs_espresso_230gr_parser()[7]
            }},

             {'jacobs_barista_classic_pack_225gr': {
                "silpo": parser.jacobs_barista_classic_pack_225gr_parser()[3],
                "ashan": parser.jacobs_barista_classic_pack_225gr_parser()[4],
                "novus": parser.jacobs_barista_classic_pack_225gr_parser()[5],
                "metro": parser.jacobs_barista_classic_pack_225gr_parser()[6]
            }},
             {'jacobs_monarch_intense_400gr': {
                "eko": parser.jacobs_monarch_intense_400gr_parser()[1],
                "silpo": parser.jacobs_monarch_intense_400gr_parser()[3],
                "ashan": parser.jacobs_monarch_intense_400gr_parser()[4],
                "novus": parser.jacobs_monarch_intense_400gr_parser()[5],
                "metro": parser.jacobs_monarch_intense_400gr_parser()[6]
            }},
             {'jacobs_monarch_classico_pack_400gr': {
                "eko": parser.jacobs_monarch_classico_pack_400gr_parser()[1],
                "silpo": parser.jacobs_monarch_classico_pack_400gr_parser()[3],
                "ashan": parser.jacobs_monarch_classico_pack_400gr_parser()[4],
                "novus": parser.jacobs_monarch_classico_pack_400gr_parser()[5],
                "metro": parser.jacobs_monarch_classico_pack_400gr_parser()[6]
            }},

             {'jacobs_monarch_rozch_60gr': {
                "atb": parser.jacobs_monarch_rozch_60gr_parser()[0]
            }},

            {'jacobs_monarch_rozch_425gr': {
                "atb": parser.jacobs_monarch_rozch_425gr_parser()[0]
            }},

             {'nescafe_gold_rozch_pack_165gr': {
                "eko": parser.nescafe_gold_rozch_pack_165gr_parser()[1],
                "varus": parser.nescafe_gold_rozch_pack_165gr_parser()[2],
                "silpo": parser.nescafe_gold_rozch_pack_165gr_parser()[3],
                "ashan": parser.nescafe_gold_rozch_pack_165gr_parser()[4],
                "novus": parser.nescafe_gold_rozch_pack_165gr_parser()[5],
                "fozzy": parser.nescafe_gold_rozch_pack_165gr_parser()[8]
            }},

            {'nescafe_gold_rozch_pack_310gr': {
                "varus": parser.nescafe_gold_rozch_pack_310gr_parser()[2],
                "silpo": parser.nescafe_gold_rozch_pack_310gr_parser()[3],
                "novus": parser.nescafe_gold_rozch_pack_310gr_parser()[5]
            }},

            {'nescafe_classic_rozch_pack_170gr': {
                "silpo": parser.nescafe_classic_rozch_pack_170gr_parser()[3]
            }},

            {'nescafe_gold_rozch_pack_360gr': {
                "eko": parser.nescafe_gold_rozch_pack_360gr_parser()[1],
                "silpo": parser.nescafe_gold_rozch_pack_360gr_parser()[3]
            }},

             {'nescafe_classic_rozch_pack_30gr': {
                "silpo": parser.nescafe_classic_rozch_pack_30gr_parser()[3]
            }},

             {'nescafe_gold_rozch_pack_30gr': {
                "eko": parser.nescafe_gold_rozch_pack_30gr_parser()[1],
                "varus": parser.nescafe_gold_rozch_pack_30gr_parser()[2],
                "silpo": parser.nescafe_gold_rozch_pack_30gr_parser()[3],
                "ashan": parser.nescafe_gold_rozch_pack_30gr_parser()[4],
                "nash_kray": parser.nescafe_gold_rozch_pack_30gr_parser()[7],
                "fozzy": parser.nescafe_gold_rozch_pack_30gr_parser()[8]
            }},

             {'nescafe_gold_rozch_pack_60gr': {
                "eko": parser.nescafe_gold_rozch_pack_60gr_parser()[1],
                "varus": parser.nescafe_gold_rozch_pack_60gr_parser()[2],
                "silpo": parser.nescafe_gold_rozch_pack_60gr_parser()[3],
                "ashan": parser.nescafe_gold_rozch_pack_60gr_parser()[4],
                "novus": parser.nescafe_gold_rozch_pack_60gr_parser()[5],
                "nash_kray": parser.nescafe_gold_rozch_pack_60gr_parser()[7],
                "fozzy": parser.nescafe_gold_rozch_pack_60gr_parser()[8]
            }},

            {'nescafe_classic_rozch_pack_300gr': {
                "silpo": parser.nescafe_classic_rozch_pack_300gr_parser()[3]
            }},

            {'nescafe_gold_rozch_pack_260gr': {
                "eko": parser.nescafe_gold_rozch_pack_260gr_parser()[1],
                "varus": parser.nescafe_gold_rozch_pack_260gr_parser()[2],
                "silpo": parser.nescafe_gold_rozch_pack_260gr_parser()[3],
                "ashan": parser.nescafe_gold_rozch_pack_260gr_parser()[4],
                "fozzy": parser.nescafe_gold_rozch_pack_260gr_parser()[8]
            }},

            {'carte_noire_pack_rozch_140gr': {
                "atb": parser.carte_noire_pack_rozch_140gr_parser()[0],
                "eko": parser.carte_noire_pack_rozch_140gr_parser()[1],
                "varus": parser.carte_noire_pack_rozch_140gr_parser()[2],
                "silpo": parser.carte_noire_pack_rozch_140gr_parser()[3],
                "ashan": parser.carte_noire_pack_rozch_140gr_parser()[4],
                "novus": parser.carte_noire_pack_rozch_140gr_parser()[5],
                "metro": parser.carte_noire_pack_rozch_140gr_parser()[6]
            }},

            {'carte_noire_pack_rozch_70gr': {
                "atb": parser.carte_noire_pack_rozch_70gr_parser()[0],
                "eko": parser.carte_noire_pack_rozch_70gr_parser()[1],
                "silpo": parser.carte_noire_pack_rozch_70gr_parser()[3],
                "novus": parser.carte_noire_pack_rozch_70gr_parser()[5],
                "metro": parser.carte_noire_pack_rozch_70gr_parser()[6]
            }},

            {'carte_noire_caramel_pack_rozch_120gr': {
                "atb": parser.carte_noire_caramel_pack_rozch_120gr_parser()[0],
                "eko": parser.carte_noire_caramel_pack_rozch_120gr_parser()[1],
                "silpo": parser.carte_noire_caramel_pack_rozch_120gr_parser()[3],
                "novus": parser.carte_noire_caramel_pack_rozch_120gr_parser()[5],
                "metro": parser.carte_noire_caramel_pack_rozch_120gr_parser()[6]
            }},

            {'carte_noire_rozch_pack_210gr': {
                "varus": parser.carte_noire_rozch_pack_210gr_parser()[2],
                "silpo": parser.carte_noire_rozch_pack_210gr_parser()[3],
                "ashan": parser.carte_noire_rozch_pack_210gr_parser()[4],
                "novus": parser.carte_noire_rozch_pack_210gr_parser()[5]
            }},

            {'carte_noire_rozch_pack_280gr': {
                "silpo": parser.carte_noire_rozch_pack_280gr_parser()[3],
                "ashan": parser.carte_noire_rozch_pack_280gr_parser()[4],
                "metro": parser.carte_noire_rozch_pack_280gr_parser()[6]
            }},
             {'ambassador_premium_rozch_pack_50gr': {
                "varus": parser.ambassador_premium_rozch_pack_50gr_parser()[2],
                "silpo": parser.ambassador_premium_rozch_pack_50gr_parser()[3],
                "ashan": parser.ambassador_premium_rozch_pack_50gr_parser()[4],
                "novus": parser.ambassador_premium_rozch_pack_50gr_parser()[5]
            }},
             {'ambassador_premium_rozch_pack_100gr': {
                "eko": parser.ambassador_premium_rozch_pack_100gr_parser()[1],
                "varus": parser.ambassador_premium_rozch_pack_100gr_parser()[2],
                "silpo": parser.ambassador_premium_rozch_pack_100gr_parser()[3],
                "ashan": parser.ambassador_premium_rozch_pack_100gr_parser()[4],
                "metro": parser.ambassador_premium_rozch_pack_100gr_parser()[6]
            }},


        ]
        # далее записываем цены в json-файл
        write_prices_to_json(all_products_names_batch_7, batch_7_path, mode_type_first_write)

    # для первого батча
    elif batch_name == batch_name_8:
        all_products_names_batch_8 = [

            {'ambassador_premium_rozch_pack_250gr': {
                "varus": parser.ambassador_premium_rozch_pack_250gr_parser()[2],
                "silpo": parser.ambassador_premium_rozch_pack_250gr_parser()[3],
                "novus": parser.ambassador_premium_rozch_pack_250gr_parser()[5],
                "metro": parser.ambassador_premium_rozch_pack_250gr_parser()[6]
            }},

            {'ambassador_premium_rozch_pack_170gr': {
                "silpo": parser.ambassador_premium_rozch_pack_170gr_parser()[3],
                "ashan": parser.ambassador_premium_rozch_pack_170gr_parser()[4],
                "metro": parser.ambassador_premium_rozch_pack_170gr_parser()[6]
            }},

            {'ambassador_premium_rozch_pack_400gr': {
                "silpo": parser.ambassador_premium_rozch_pack_400gr_parser()[3],
                "ashan": parser.ambassador_premium_rozch_pack_400gr_parser()[4],
                "metro": parser.ambassador_premium_rozch_pack_400gr_parser()[6]
            }},

            {'ambassador_premium_rozch_pack_500gr': {
                "ashan": parser.ambassador_premium_rozch_pack_500gr_parser()[4],
                "metro": parser.ambassador_premium_rozch_pack_500gr_parser()[6]
            }},

            {'chorna_carta_gold_rozch_pack_200gr': {
                "silpo": parser.chorna_carta_gold_rozch_pack_200gr_parser()[3],
                "ashan": parser.chorna_carta_gold_rozch_pack_200gr_parser()[4],
                "metro": parser.chorna_carta_gold_rozch_pack_200gr_parser()[6]
            }},

             {'chorna_carta_gold_rozch_pack_100gr': {
                 "eko": parser.chorna_carta_gold_rozch_pack_100gr_parser()[1],
                "silpo": parser.chorna_carta_gold_rozch_pack_100gr_parser()[3],
                "ashan": parser.chorna_carta_gold_rozch_pack_100gr_parser()[4],
                "novus": parser.chorna_carta_gold_rozch_pack_100gr_parser()[5]
            }},

            {'tchibo_gold_selection_rozch_glass_jar_50gr': {
                "silpo": parser.tchibo_gold_selection_rozch_glass_jar_50gr_parser()[3],
                "ashan": parser.tchibo_gold_selection_rozch_glass_jar_50gr_parser()[4],
                "novus": parser.tchibo_gold_selection_rozch_glass_jar_50gr_parser()[5]
            }},

            {'tchibo_gold_selection_rozch_glass_jar_100gr': {
                "varus": parser.tchibo_gold_selection_rozch_glass_jar_100gr_parser()[2],
                "silpo": parser.tchibo_gold_selection_rozch_glass_jar_100gr_parser()[3],
                "ashan": parser.tchibo_gold_selection_rozch_glass_jar_100gr_parser()[4],
                "novus": parser.tchibo_gold_selection_rozch_glass_jar_100gr_parser()[5],
                "metro": parser.tchibo_gold_selection_rozch_glass_jar_100gr_parser()[6]
            }},

            {'tchibo_gold_selection_rozch_glass_jar_200gr': {
                "silpo": parser.tchibo_gold_selection_rozch_glass_jar_200gr_parser()[3],
                "ashan": parser.tchibo_gold_selection_rozch_glass_jar_200gr_parser()[4],
                "metro": parser.tchibo_gold_selection_rozch_glass_jar_200gr_parser()[6]
            }},

            {'tchibo_exclusive_rozch_glass_jar_200gr': {
                "silpo": parser.tchibo_exclusive_rozch_glass_jar_200gr_parser()[3],
                "ashan": parser.tchibo_exclusive_rozch_glass_jar_200gr_parser()[4]
            }},

            {'aroma_gold_decaff_rozch_glass_jar_100gr': {
                "silpo": parser.aroma_gold_decaff_rozch_glass_jar_100gr_parser()[3],
                "fozzy": parser.aroma_gold_decaff_rozch_glass_jar_100gr_parser()[8]
            }},

            {'aroma_gold_freeze_dried_rozch_glass_jar_100gr': {
                "silpo": parser.aroma_gold_freeze_dried_rozch_glass_jar_100gr_parser()[3],
                "novus": parser.aroma_gold_freeze_dried_rozch_glass_jar_100gr_parser()[5],
                "nash_kray": parser.aroma_gold_freeze_dried_rozch_glass_jar_100gr_parser()[7],
                "fozzy": parser.aroma_gold_freeze_dried_rozch_glass_jar_100gr_parser()[8]
            }},

            {'aroma_gold_freeze_dried_rozch_glass_jar_200gr': {
                "silpo": parser.aroma_gold_freeze_dried_rozch_glass_jar_200gr_parser()[3]
            }},

            {'maccoffee_arabica_rozch_glass_jar_120gr': {
                "silpo": parser.maccoffee_arabica_rozch_glass_jar_120gr_parser()[3],
                "ashan": parser.maccoffee_arabica_rozch_glass_jar_120gr_parser()[4],
                "novus": parser.maccoffee_arabica_rozch_glass_jar_120gr_parser()[5],
                "metro": parser.maccoffee_arabica_rozch_glass_jar_120gr_parser()[6]
            }},

            {'maxwell_house_instant_mild_blend_rozch_glass_jar_100gr': {
                "silpo": parser.maxwell_house_instant_mild_blend_rozch_glass_jar_100gr_parser()[3],
                "fozzy": parser.maxwell_house_instant_mild_blend_rozch_glass_jar_100gr_parser()[8]
            }},

            {'maxwell_house_instant_mild_blend_rozch_glass_jar_200gr': {
                "silpo": parser.maxwell_house_instant_mild_blend_rozch_glass_jar_200gr_parser()[3],
                "fozzy": parser.maxwell_house_instant_mild_blend_rozch_glass_jar_200gr_parser()[8]
            }},

            {'dallmayr_gold_rozch_glass_jar_100gr': {
                "silpo": parser.dallmayr_gold_rozch_glass_jar_100gr_parser()[3]
            }},

            {'dallmayr_gold_rozch_glass_jar_200gr': {
                "metro": parser.dallmayr_gold_rozch_glass_jar_200gr_parser()[6]
            }},

            {'aroma_platinum_fr_dr_rozch_glass_jar_200gr': {
                "fozzy": parser.aroma_platinum_fr_dr_rozch_glass_jar_200gr_parser()[8]
            }},

            {'aroma_platinum_fr_dr_rozch_glass_jar_100gr': {
                "fozzy": parser.aroma_platinum_fr_dr_rozch_glass_jar_100gr_parser()[8]
            }},

            {'beanies_mince_pie_rozch_glass_jar_50gr': {
                "fozzy": parser.beanies_mince_pie_rozch_glass_jar_50gr_parser()[8]
            }},

            {'beanies_cristmas_pudding_rozch_glass_jar_50gr': {
                "fozzy": parser.beanies_cristmas_pudding_rozch_glass_jar_50gr_parser()[8]
            }},

            {'beanies_double_chocolate_rozch_glass_jar_50gr': {
                "fozzy": parser.beanies_double_chocolate_rozch_glass_jar_50gr_parser()[8]
            }},

            {'beanies_cinder_toffee_rozch_glass_jar_50gr': {
                "fozzy": parser.beanies_cinder_toffee_rozch_glass_jar_50gr_parser()[8]
            }},

            {'bushido_kodo_rozch_glass_jar_95gr': {
                "fozzy": parser.bushido_kodo_rozch_glass_jar_95gr_parser()[8]
            }},

            {'davidoff_rich_aroma_rozch_glass_jar_100gr': {
                "ashan": parser.davidoff_rich_aroma_rozch_glass_jar_100gr_parser()[4],
                "novus": parser.davidoff_rich_aroma_rozch_glass_jar_100gr_parser()[5],
                "fozzy": parser.davidoff_rich_aroma_rozch_glass_jar_100gr_parser()[8]
            }},

            {'davidoff_fine_aroma_rozch_glass_jar_100gr': {
                "ashan": parser.davidoff_fine_aroma_rozch_glass_jar_100gr_parser()[4]
            }},

            {'ahmad_tea_eng_breakf_black_pack_100gr': {
                "silpo": parser.ahmad_tea_eng_breakf_black_pack_100gr_parser()[3]
            }},

            {'ahmad_tea_graf_grey_black_pack_100gr': {
                "silpo": parser.ahmad_tea_graf_grey_black_pack_100gr_parser()[3]
            }},

            {'ahmad_tea_london_black_pack_100gr': {
                "eko": parser.ahmad_tea_london_black_pack_100gr_parser()[1],
                "varus": parser.ahmad_tea_london_black_pack_100gr_parser()[2],
                "silpo": parser.ahmad_tea_london_black_pack_100gr_parser()[3]
            }},

            {'ahmad_tea_english_n1_black_pack_100gr': {
                "eko": parser.ahmad_tea_english_n1_black_pack_100gr_parser()[1],
                "varus": parser.ahmad_tea_english_n1_black_pack_100gr_parser()[2],
                "silpo": parser.ahmad_tea_english_n1_black_pack_100gr_parser()[3]
            }},

            {'ahmad_tea_eng_breakf_black_pack_200gr': {
                "eko": parser.ahmad_tea_eng_breakf_black_pack_200gr_parser()[1],
                "silpo": parser.ahmad_tea_eng_breakf_black_pack_200gr_parser()[3],
                "fozzy": parser.ahmad_tea_eng_breakf_black_pack_200gr_parser()[8]
            }},

            {'ahmad_tea_graf_grey_black_pack_200gr': {
                "eko": parser.ahmad_tea_graf_grey_black_pack_200gr_parser()[1],
                "silpo": parser.ahmad_tea_graf_grey_black_pack_200gr_parser()[3],
                "novus": parser.ahmad_tea_graf_grey_black_pack_200gr_parser()[5],
                "fozzy": parser.ahmad_tea_graf_grey_black_pack_200gr_parser()[8]
            }},

            {'ahmad_tea_london_black_pack_100pk': {
                "eko": parser.ahmad_tea_london_black_pack_100pk_parser()[1],
                "varus": parser.ahmad_tea_london_black_pack_100pk_parser()[2],
                "silpo": parser.ahmad_tea_london_black_pack_100pk_parser()[3],
                "fozzy": parser.ahmad_tea_london_black_pack_100pk_parser()[8]
            }},

            {'ahmad_tea_graf_grey_black_pack_40pk': {
                "silpo": parser.ahmad_tea_graf_grey_black_pack_40pk_parser()[3]
            }},

            {'ahmad_tea_london_black_pack_25pk': {
                "eko": parser.ahmad_tea_london_black_pack_25pk_parser()[1],
                "varus": parser.ahmad_tea_london_black_pack_25pk_parser()[2],
                "silpo": parser.ahmad_tea_london_black_pack_25pk_parser()[3]
            }},

            {'ahmad_tea_lavanda_bergamot_black_pack_20pk': {
                "silpo": parser.ahmad_tea_lavanda_bergamot_black_pack_20pk_parser()[3]
            }},

            {'ahmad_tea_eng_breakf_black_pack_25pk': {
                "eko": parser.ahmad_tea_eng_breakf_black_pack_25pk_parser()[1],
                "varus": parser.ahmad_tea_eng_breakf_black_pack_25pk_parser()[2],
                "silpo": parser.ahmad_tea_eng_breakf_black_pack_25pk_parser()[3],
                "ashan": parser.ahmad_tea_eng_breakf_black_pack_25pk_parser()[4],
                "novus": parser.ahmad_tea_eng_breakf_black_pack_25pk_parser()[5],
                "fozzy": parser.ahmad_tea_eng_breakf_black_pack_25pk_parser()[8]
            }},

            {'ahmad_tea_english_n1_black_pack_25pk': {
                "eko": parser.ahmad_tea_english_n1_black_pack_25pk_parser()[1],
                "varus": parser.ahmad_tea_english_n1_black_pack_25pk_parser()[2],
                "silpo": parser.ahmad_tea_english_n1_black_pack_25pk_parser()[3],
                "novus": parser.ahmad_tea_english_n1_black_pack_25pk_parser()[5],
                "fozzy": parser.ahmad_tea_english_n1_black_pack_25pk_parser()[8]
            }},

            {'ahmad_tea_graf_grey_black_pack_25pk': {
                "silpo": parser.ahmad_tea_graf_grey_black_pack_25pk_parser()[3],
                "fozzy": parser.ahmad_tea_graf_grey_black_pack_25pk_parser()[8]
            }},

            {'ahmad_tea_london_black_pack_40pk': {
                "eko": parser.ahmad_tea_london_black_pack_40pk_parser()[1],
                "silpo": parser.ahmad_tea_london_black_pack_40pk_parser()[3],
                "fozzy": parser.ahmad_tea_london_black_pack_40pk_parser()[8]
            }},

            {'ahmad_tea_eng_breakf_black_pack_40pk': {
                "atb": parser.ahmad_tea_eng_breakf_black_pack_40pk_parser()[0],
                "eko": parser.ahmad_tea_eng_breakf_black_pack_40pk_parser()[1],
                "varus": parser.ahmad_tea_eng_breakf_black_pack_40pk_parser()[2],
                "silpo": parser.ahmad_tea_eng_breakf_black_pack_40pk_parser()[3],
                "ashan": parser.ahmad_tea_eng_breakf_black_pack_40pk_parser()[4],
                "novus": parser.ahmad_tea_eng_breakf_black_pack_40pk_parser()[5]
            }},

            {'ahmad_tea_english_n1_black_pack_40pk': {
                "eko": parser.ahmad_tea_english_n1_black_pack_40pk_parser()[1],
                "silpo": parser.ahmad_tea_english_n1_black_pack_40pk_parser()[3],
                "fozzy": parser.ahmad_tea_english_n1_black_pack_40pk_parser()[8]
            }},

            {'ahmad_tea_eng_breakf_black_pack_100pk': {
                "eko": parser.ahmad_tea_eng_breakf_black_pack_100pk_parser()[1],
                "silpo": parser.ahmad_tea_eng_breakf_black_pack_100pk_parser()[3],
                "novus": parser.ahmad_tea_eng_breakf_black_pack_100pk_parser()[5],
                "fozzy": parser.ahmad_tea_eng_breakf_black_pack_100pk_parser()[8]
            }},

            {'ahmad_tea_graf_grey_black_pack_100pk': {
                "silpo": parser.ahmad_tea_graf_grey_black_pack_100pk_parser()[3],
                "fozzy": parser.ahmad_tea_graf_grey_black_pack_100pk_parser()[8]
            }},

            {'lipton_yellow_label_black_pack_25pk': {
                "varus": parser.lipton_yellow_label_black_pack_25pk_parser()[2],
                "silpo": parser.lipton_yellow_label_black_pack_25pk_parser()[3],
                "metro": parser.lipton_yellow_label_black_pack_25pk_parser()[6]
            }},

            {'lipton_earl_gray_black_pack_25pk': {
                "varus": parser.lipton_earl_gray_black_pack_25pk_parser()[2],
                "silpo": parser.lipton_earl_gray_black_pack_25pk_parser()[3],
                "metro": parser.lipton_earl_gray_black_pack_25pk_parser()[6]
            }},

            {'lipton_eng_breakf_black_pack_25pk': {
                "silpo": parser.lipton_eng_breakf_black_pack_25pk_parser()[3]
            }},

            {'lipton_gold_tea_black_pack_25pk': {
                "silpo": parser.lipton_gold_tea_black_pack_25pk_parser()[3]
            }},

            {'lipton_earl_grey_orange_black_pack_25pk': {
                "silpo": parser.lipton_earl_grey_orange_black_pack_25pk_parser()[3]
            }},

            {'lipton_forest_fruits_black_pack_20pk': {
                "varus": parser.lipton_forest_fruits_black_pack_20pk_parser()[2],
                "silpo": parser.lipton_forest_fruits_black_pack_20pk_parser()[3]
            }},

            {'lipton_intense_black_black_pack_25pk': {
                "silpo": parser.lipton_intense_black_black_pack_25pk_parser()[3],
                "metro": parser.lipton_intense_black_black_pack_25pk_parser()[6]
            }},

            {'lipton_peach_mango_black_black_pack_20pk': {
                "silpo": parser.lipton_peach_mango_black_black_pack_20pk_parser()[3]
            }},

            {'lipton_yellow_label_black_pack_50pk': {
                "silpo": parser.lipton_yellow_label_black_pack_50pk_parser()[3],
                "metro": parser.lipton_yellow_label_black_pack_50pk_parser()[6]
            }},

            {'lipton_intense_black_black_pack_92pk': {
                "silpo": parser.lipton_intense_black_black_pack_92pk_parser()[3]
            }},

            {'lipton_gold_tea_black_pack_92pk': {
                "silpo": parser.lipton_gold_tea_black_pack_92pk_parser()[3]
            }},

            {'lipton_yellow_label_black_pack_100pk': {
                "varus": parser.lipton_yellow_label_black_pack_100pk_parser()[2]
            }},

            {'lipton_earl_gray_black_pack_50pk': {
                "varus": parser.lipton_earl_gray_black_pack_50pk_parser()[2]
            }},

            {'lipton_intense_mint_green_pack_20pk': {
                "silpo": parser.lipton_intense_mint_green_pack_20pk_parser()[3]
            }},

            {'lipton_intense_raspb_pomegran_pack_20pk': {
                "silpo": parser.lipton_raspberry_pomegranate_green_pack_20pk_parser()[3]
            }},

            {'lipton_classic_green_pack_25pk': {
                "varus": parser.lipton_classic_green_pack_25pk_parser()[2],
                "silpo": parser.lipton_classic_green_pack_25pk_parser()[3]
            }},

            {'batik_korol_std_black_pack_25pk': {
                "eko": parser.batik_korol_std_black_pack_25pk_parser()[1],
                "silpo": parser.batik_korol_std_black_pack_25pk_parser()[3]
            }},

            {'batik_gold_earl_grey_black_pack_25pk': {
                "eko": parser.batik_gold_earl_grey_black_pack_25pk_parser()[1],
                "silpo": parser.batik_gold_earl_grey_black_pack_25pk_parser()[3]
            }},

            {'batik_chorniy_barhat_black_pack_25pk': {
                "eko": parser.batik_chorniy_barhat_black_pack_25pk_parser()[1],
                "silpo": parser.batik_chorniy_barhat_black_pack_25pk_parser()[3]
            }},

            {'batik_jagidniy_cilynok_black_pack_25pk': {
                "eko": parser.batik_jagidniy_cilynok_black_pack_25pk_parser()[1],
                "silpo": parser.batik_jagidniy_cilynok_black_pack_25pk_parser()[3],
                "ashan": parser.batik_jagidniy_cilynok_black_pack_25pk_parser()[4]
            }},

            {'batik_badyoriy_limon_black_pack_25pk': {
                "eko": parser.batik_badyoriy_limon_black_pack_25pk_parser()[1],
                "silpo": parser.batik_badyoriy_limon_black_pack_25pk_parser()[3],
                "ashan": parser.batik_badyoriy_limon_black_pack_25pk_parser()[4]
            }},

            {'batik_gold_ceylon_visokogir_black_pack_25pk': {
                "eko": parser.batik_gold_ceylon_visokogir_black_pack_25pk_parser()[1],
                "silpo": parser.batik_gold_ceylon_visokogir_black_pack_25pk_parser()[3]
            }},

            {'batik_black_granul_standart_sts_100gr': {
                "eko": parser.batik_black_granul_standart_sts_100gr_parser()[1],
                "silpo": parser.batik_black_granul_standart_sts_100gr_parser()[3]
            }},

            {'batik_korol_std_black_100gr': {
                "eko": parser.batik_korol_std_black_100gr_parser()[1],
                "silpo": parser.batik_korol_std_black_100gr_parser()[3]
            }},

            {'batik_chorniy_barhat_black_pack_60pk': {
                "silpo": parser.batik_chorniy_barhat_black_pack_60pk_parser()[3]
            }},

            {'batik_korol_std_black_pack_100pk': {
                "eko": parser.batik_korol_std_black_pack_100pk_parser()[1],
                "silpo": parser.batik_korol_std_black_pack_100pk_parser()[3],
                "ashan": parser.batik_korol_std_black_pack_100pk_parser()[4]
            }},

            {'akbar_gold_black_25pk': {
                "silpo": parser.akbar_gold_black_25pk_parser()[3],
                "ashan": parser.akbar_gold_black_25pk_parser()[4],
                "metro": parser.akbar_gold_black_25pk_parser()[6]
            }},

            {'akbar_limon_lime_twist_black_pack_20pk': {
                "silpo": parser.akbar_limon_lime_twist_black_pack_20pk_parser()[3],
                "ashan": parser.akbar_limon_lime_twist_black_pack_20pk_parser()[4]
            }},

            {'akbar_peach_passion_punch_black_pack_20pk': {
                "silpo": parser.akbar_peach_passion_punch_black_pack_20pk_parser()[3],
                "ashan": parser.akbar_peach_passion_punch_black_pack_20pk_parser()[4]
            }},

            {'akbar_strawberry_kiwi_black_pack_20pk': {
                "ashan": parser.akbar_strawberry_kiwi_black_pack_20pk_parser()[4]
            }},

            {'pickwick_english_black_pack_20pk': {
                "eko": parser.pickwick_english_black_pack_20pk_parser()[1],
                "silpo": parser.pickwick_english_black_pack_20pk_parser()[3],
                "ashan": parser.pickwick_english_black_pack_20pk_parser()[4],
                "novus": parser.pickwick_english_black_pack_20pk_parser()[5]
            }},

            {'pickwick_mango_black_pack_20pk': {
                "eko": parser.pickwick_mango_black_pack_20pk_parser()[1],
                "silpo": parser.pickwick_mango_black_pack_20pk_parser()[3],
                "ashan": parser.pickwick_mango_black_pack_20pk_parser()[4],
                "novus": parser.pickwick_mango_black_pack_20pk_parser()[5],
                "metro": parser.pickwick_mango_black_pack_20pk_parser()[6]
            }},

            {'pickwick_forest_fruit_black_pack_20pk': {
                "eko": parser.pickwick_forest_fruit_black_pack_20pk_parser()[1],
                "silpo": parser.pickwick_forest_fruit_black_pack_20pk_parser()[3],
                "ashan": parser.pickwick_forest_fruit_black_pack_20pk_parser()[4],
                "novus": parser.pickwick_forest_fruit_black_pack_20pk_parser()[5]
            }},

            {'pickwick_earl_grey_black_pack_20pk': {
                "eko": parser.pickwick_earl_grey_black_pack_20pk_parser()[1],
                "silpo": parser.pickwick_earl_grey_black_pack_20pk_parser()[3],
                "ashan": parser.pickwick_earl_grey_black_pack_20pk_parser()[4],
                "novus": parser.pickwick_earl_grey_black_pack_20pk_parser()[5]
            }},

            {'pickwick_strawberry_black_pack_20pk': {
                "eko": parser.pickwick_strawberry_black_pack_20pk_parser()[1],
                "varus": parser.pickwick_strawberry_black_pack_20pk_parser()[2],
                "silpo": parser.pickwick_strawberry_black_pack_20pk_parser()[3],
                "ashan": parser.pickwick_strawberry_black_pack_20pk_parser()[4],
                "novus": parser.pickwick_strawberry_black_pack_20pk_parser()[5]
            }},

            {'pickwick_green_pure_green_pack_20pk': {
                "ashan": parser.pickwick_green_pure_green_pack_20pk_parser()[4],
                "novus": parser.pickwick_green_pure_green_pack_20pk_parser()[5],
                "metro": parser.pickwick_green_pure_green_pack_20pk_parser()[6]
            }},

            {'pickwick_mint_green_pack_20pk': {
                "ashan": parser.pickwick_mint_green_pack_20pk_parser()[4],
                "novus": parser.pickwick_mint_green_pack_20pk_parser()[5],
                "metro": parser.pickwick_mint_green_pack_20pk_parser()[6]
            }},

            {'pickwick_romashka_green_pack_20pk': {
                "ashan": parser.pickwick_romashka_green_pack_20pk_parser()[4],
                "novus": parser.pickwick_romashka_green_pack_20pk_parser()[5],
                "metro": parser.pickwick_romashka_green_pack_20pk_parser()[6]
            }},

            {'pickwick_spicy_chai_trav_pack_15pk': {
                "eko": parser.pickwick_spicy_chai_trav_pack_15pk_parser()[1],
                "silpo": parser.pickwick_spicy_chai_trav_pack_15pk_parser()[3],
                "ashan": parser.pickwick_spicy_chai_trav_pack_15pk_parser()[4]
            }},

            {'pickwick_romashka_trav_pack_15pk': {
                "eko": parser.pickwick_romashka_trav_pack_15pk_parser()[1],
                "silpo": parser.pickwick_romashka_trav_pack_15pk_parser()[3],
                "ashan": parser.pickwick_romashka_trav_pack_15pk_parser()[4],
                "novus": parser.pickwick_romashka_trav_pack_15pk_parser()[5]
            }},

            {'pickwick_imbir_pryan_trav_pack_15pk': {
                "eko": parser.pickwick_imbir_pryan_trav_pack_15pk_parser()[1],
                "silpo": parser.pickwick_imbir_pryan_trav_pack_15pk_parser()[3],
                "ashan": parser.pickwick_imbir_pryan_trav_pack_15pk_parser()[4]
            }},

            {'pickwick_energy_trav_pack_15pk': {
                "eko": parser.pickwick_energy_trav_pack_15pk_parser()[1],
                "silpo": parser.pickwick_energy_trav_pack_15pk_parser()[3],
                "ashan": parser.pickwick_energy_trav_pack_15pk_parser()[4],
                "novus": parser.pickwick_energy_trav_pack_15pk_parser()[5]
            }},

            {'pickwick_immunity_trav_pack_15pk': {
                "eko": parser.pickwick_immunity_trav_pack_15pk_parser()[1],
                "silpo": parser.pickwick_immunity_trav_pack_15pk_parser()[3],
                "ashan": parser.pickwick_immunity_trav_pack_15pk_parser()[4],
                "novus": parser.pickwick_immunity_trav_pack_15pk_parser()[5]
            }},

            {'pickwick_earl_grey_citrus_trav_pack_15pk': {
                "eko": parser.pickwick_earl_grey_citrus_trav_pack_15pk_parser()[1],
                "novus": parser.pickwick_earl_grey_citrus_trav_pack_15pk_parser()[5]
            }},

            {'pickwick_citrus_buzina_trav_pack_20pk': {
                "silpo": parser.pickwick_citrus_buzina_trav_pack_20pk_parser()[3],
                "novus": parser.pickwick_citrus_buzina_trav_pack_20pk_parser()[5]
            }},

            {'pickwick_imbir_lemon_citrus_trav_pack_20pk': {
                "silpo": parser.pickwick_imbir_lemon_citrus_trav_pack_20pk_parser()[3]
            }},

            {'azerchay_bergamot_black_pack_25pk': {
                "silpo": parser.azerchay_bergamot_black_pack_25pk_parser()[3],
                "ashan": parser.azerchay_bergamot_black_pack_25pk_parser()[4],
                "novus": parser.azerchay_bergamot_black_pack_25pk_parser()[5],
                "metro": parser.azerchay_bergamot_black_pack_25pk_parser()[6]
            }},

            {'azerchay_buket_black_pack_25pk': {
                "silpo": parser.azerchay_buket_black_pack_25pk_parser()[3],
                "ashan": parser.azerchay_buket_black_pack_25pk_parser()[4],
                "novus": parser.azerchay_buket_black_pack_25pk_parser()[5],
                "fozzy": parser.azerchay_buket_black_pack_25pk_parser()[8]
            }},

            {'azerchay_chebrec_black_pack_30pk': {
                "atb": parser.azerchay_chebrec_black_pack_30pk_parser()[0]
            }},

            {'sir_plav_komo_druzba_40_75gr': {
                "varus": parser.sir_plav_komo_druzba_40_75gr_parser()[2],
                "silpo": parser.sir_plav_komo_druzba_40_75gr_parser()[3],
                "novus": parser.sir_plav_komo_druzba_40_75gr_parser()[5],
                "metro": parser.sir_plav_komo_druzba_40_75gr_parser()[6],
                "nash_kray": parser.sir_plav_komo_druzba_40_75gr_parser()[7],
                "fozzy": parser.sir_plav_komo_druzba_40_75gr_parser()[8]
            }},

            {'sir_plav_komo_vershk_40_75gr': {
                "eko": parser.sir_plav_komo_vershk_40_75gr_parser()[1],
                "silpo": parser.sir_plav_komo_vershk_40_75gr_parser()[3],
                "novus": parser.sir_plav_komo_vershk_40_75gr_parser()[5],
                "metro": parser.sir_plav_komo_vershk_40_75gr_parser()[6],
                "nash_kray": parser.sir_plav_komo_vershk_40_75gr_parser()[7],
                "fozzy": parser.sir_plav_komo_vershk_40_75gr_parser()[8]
            }},

            {'sir_plav_komo_zelen_chasnik_40_75gr': {
                "varus": parser.sir_plav_komo_zelen_chasnik_40_75gr_parser()[2],
                "silpo": parser.sir_plav_komo_zelen_chasnik_40_75gr_parser()[3],
                "nash_kray": parser.sir_plav_komo_zelen_chasnik_40_75gr_parser()[7],
                "fozzy": parser.sir_plav_komo_zelen_chasnik_40_75gr_parser()[8]
            }},

            {'sir_plav_komo_crab_pal_40_75gr': {
                "nash_kray": parser.sir_plav_komo_crab_pal_40_75gr_parser()[7],
            }},

            {'sir_plav_komo_grib_40_75gr': {
                "nash_kray": parser.sir_plav_komo_grib_40_75gr_parser()[7],
                "fozzy": parser.sir_plav_komo_grib_40_75gr_parser()[8]
            }},

        ]

        # далее записываем цены в json-файл
        write_prices_to_json(all_products_names_batch_8, batch_8_path, mode_type_first_write)

    else:
        print("Нет такого батча!")


#price_parcing("all_products_names_batch_1")
#price_parcing("all_products_names_batch_2")
#price_parcing("all_products_names_batch_3")
#price_parcing("all_products_names_batch_4")
#price_parcing("all_products_names_batch_5")
#price_parcing("all_products_names_batch_6")
#price_parcing("all_products_names_batch_7")
#price_parcing("all_products_names_batch_8")


def prepeare_json_data(path:str):
    '''Открытие и загрузка json-файлов'''

    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def merging_jsons():

    '''Метод, объединяющий json - файлы в один общий.'''

    data_1 = prepeare_json_data(batch_1_path)
    data_2 = prepeare_json_data(batch_2_path)
    data_3 = prepeare_json_data(batch_3_path)
    data_4 = prepeare_json_data(batch_4_path)
    data_5 = prepeare_json_data(batch_5_path)
    data_6 = prepeare_json_data(batch_6_path)
    data_7 = prepeare_json_data(batch_7_path)
    data_8 = prepeare_json_data(batch_8_path)

    df1 = pd.DataFrame([data_1])
    df2 = pd.DataFrame([data_2])
    df3 = pd.DataFrame([data_3])
    df4 = pd.DataFrame([data_4])
    df5 = pd.DataFrame([data_5])
    df6 = pd.DataFrame([data_6])
    df7 = pd.DataFrame([data_7])
    df8 = pd.DataFrame([data_8])

    merged_contents = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], axis=1)

    merged_contents.to_json('../overall_prices.json', orient='records')

merging_jsons()

