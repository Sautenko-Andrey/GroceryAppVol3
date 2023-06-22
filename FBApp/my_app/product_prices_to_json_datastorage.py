import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FBApp.settings")

import django

django.setup()

from django.core.management import call_command

import json
from parsers import ProductParserVol2

# коэфициенты для борща красного
water_rate = 3
meat_rate = 0.8
potato_rate = 2
beet_rate = 10
carrot_rate = 10
onion_rate = 0.2
cabbage_rate = 0.4
borsh_mututal_devider = 6

# коэфициенты для вареников с картошкой
sour_var = 0.4
water_var = 0.033
egg_var = 0.1
oil_var = 0.05
onion_var = 0.2
potato_var = 0.6
vareniki_mutual_devider = 5

silpo_correct_price = 10

egg_correct_price = 10

parser = ProductParserVol2()

all_products_names = [
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
        "silpo": parser.garlik_parcer()[3],
        "novus": parser.garlik_parcer()[5],
        "nash_kray": parser.garlik_parcer()[7],
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
        "silpo": parser.apple_golden_parcer()[3] * silpo_correct_price,
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
        "silpo": parser.onion_parcer()[3] * silpo_correct_price,
        "novus": parser.onion_parcer()[5],
        "metro": parser.onion_parcer()[6],
        "nash_kray": parser.onion_parcer()[7],
        "fozzy": parser.onion_parcer()[8]
    }},
    {'apple_black_prince': {
        "atb": parser.apple_black_prince_parcer()[0],
        "eko": parser.apple_black_prince_parcer()[1],
        "varus": parser.apple_black_prince_parcer()[2],
        "silpo": parser.apple_black_prince_parcer()[3] * silpo_correct_price,
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
        "silpo": parser.limon_parcer()[3] * silpo_correct_price,
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
        "silpo": parser.carrot_parcer()[3] * silpo_correct_price,
        "novus": parser.carrot_parcer()[5],
        "metro": parser.carrot_parcer()[6],
        "nash_kray": parser.carrot_parcer()[7],
        "fozzy": parser.carrot_parcer()[8]
    }},
    {'cabbage': {
        "atb": parser.cabbage_parcer()[0],
        "eko": parser.cabbage_parcer()[1],
        "varus": parser.cabbage_parcer()[2],
        "silpo": parser.cabbage_parcer()[3] * silpo_correct_price,
        "novus": parser.cabbage_parcer()[5],
        "metro": parser.cabbage_parcer()[6],
        "nash_kray": parser.cabbage_parcer()[7],
        "fozzy": parser.cabbage_parcer()[8]
    }},
    {'eggs': {
        "atb": parser.egg_parcer()[0],
        "eko": parser.egg_parcer()[1],
        "varus": parser.egg_parcer()[2],
        "silpo": parser.egg_parcer()[3] * silpo_correct_price,
        "ashan": parser.egg_parcer()[4],
        "novus": parser.egg_parcer()[5],
        "metro": parser.egg_parcer()[6],
        "nash_kray": parser.egg_parcer()[7],
        "fozzy": parser.egg_parcer()[8]
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
        "silpo": parser.pork_lopatka_parser()[3] * silpo_correct_price,
        "novus": parser.pork_lopatka_parser()[5],
        "metro": parser.pork_lopatka_parser()[6],
        "nash_kray": parser.pork_lopatka_parser()[7],
        "fozzy": parser.pork_lopatka_parser()[8]
    }},
    {'potato': {
        "atb": parser.potato_parser()[0],
        "eko": parser.potato_parser()[1],
        "varus": parser.potato_parser()[2],
        "silpo": parser.pork_lopatka_parser()[3] * silpo_correct_price,
        "novus": parser.potato_parser()[5],
        "metro": parser.potato_parser()[6],
        "fozzy": parser.potato_parser()[8]
    }},
    {'beet': {
        "atb": parser.beet_parser()[0],
        "eko": parser.beet_parser()[1],
        "varus": parser.beet_parser()[2],
        "silpo": parser.beet_parser()[3] * silpo_correct_price,
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
        "silpo":parser.sour_cream_for_dishes_parser()[3],
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
        "silpo": parser.apple_gala_parser()[3] * silpo_correct_price,
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
    }},
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
    }},
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
        "silpo": parser.banana_parser()[3] * silpo_correct_price,
        "novus": parser.banana_parser()[5],
        "metro": parser.banana_parser()[6],
        "nash_kray": parser.banana_parser()[7],
        "fozzy": parser.banana_parser()[8]
    }},

    {'orange': {
        "atb": parser.orange_parser()[0],
        "eko": parser.orange_parser()[1],
        "varus": parser.orange_parser()[2],
        "silpo": parser.orange_parser()[3] * silpo_correct_price,
        "novus": parser.orange_parser()[5],
        "metro": parser.orange_parser()[6],
        "nash_kray": parser.orange_parser()[7],
        "fozzy": parser.orange_parser()[8]
    }},

    {'kiwi': {
        "atb": parser.kiwi_parser()[0],
        "eko": parser.kiwi_parser()[1],
        "varus": parser.kiwi_parser()[2],
        "silpo": parser.kiwi_parser()[3] * silpo_correct_price,
        "metro": parser.kiwi_parser()[6],
        "nash_kray": parser.kiwi_parser()[7],
        "fozzy": parser.kiwi_parser()[8]
    }},

    {'coconut': {
        "atb": parser.coconut_parser()[0],
        "varus": parser.coconut_parser()[2],
        "silpo": parser.coconut_parser()[3] * silpo_correct_price,
        "metro": parser.coconut_parser()[6],
        "nash_kray": parser.coconut_parser()[7],
        "fozzy": parser.coconut_parser()[8]
    }},

    {'grapefruit': {
        "atb": parser.grapefruit_parser()[0],
        "eko": parser.grapefruit_parser()[1],
        "varus": parser.grapefruit_parser()[2],
        "silpo": parser.grapefruit_parser()[3] * silpo_correct_price,
        "novus": parser.grapefruit_parser()[5],
        "metro": parser.grapefruit_parser()[6],
        "nash_kray": parser.grapefruit_parser()[7],
        "fozzy": parser.grapefruit_parser()[8]
    }},

    {'pomegranate': {
        "atb": parser.pomegranate_parser()[0],
        "eko": parser.pomegranate_parser()[1],
        "varus": parser.pomegranate_parser()[2],
        "silpo": parser.pomegranate_parser()[3] * silpo_correct_price,
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
        "silpo": parser.cucumber_parser()[3] * silpo_correct_price,
        "novus": parser.cucumber_parser()[5],
        "metro": parser.cucumber_parser()[6],
        "nash_kray": parser.cucumber_parser()[7],
        "fozzy": parser.cucumber_parser()[8]
    }},

    {'kabachki': {
        "atb": parser.kabachki_parser()[0],
        "eko": parser.kabachki_parser()[1],
        "varus": parser.kabachki_parser()[2],
        "silpo": parser.kabachki_parser()[3] * silpo_correct_price,
        "novus": parser.kabachki_parser()[5],
        "metro": parser.kabachki_parser()[6],
        "nash_kray": parser.kabachki_parser()[7],
        "fozzy": parser.kabachki_parser()[8]
    }},

    {'red_bolgar_papper': {
        "atb": parser.red_bolg_papper_parser()[0],
        "eko": parser.red_bolg_papper_parser()[1],
        "silpo": parser.red_bolg_papper_parser()[3] * silpo_correct_price,
        "novus": parser.red_bolg_papper_parser()[5],
        "metro": parser.red_bolg_papper_parser()[6],
        "nash_kray": parser.red_bolg_papper_parser()[7],
        "fozzy": parser.red_bolg_papper_parser()[8]
    }},

    {'yellow_bolgar_papper': {
        "atb": parser.yellow_bolg_papper_parser()[0],
        "silpo": parser.yellow_bolg_papper_parser()[3] * silpo_correct_price,
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
        "silpo": parser.brokoli_parser()[3],
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
    }},

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






    {'borsh_red': {
        "atb": ((parser.water_in_6l_bottle_parser()[0] / water_rate) + (parser.pork_lopatka_parser()[0] * meat_rate)
                + (parser.potato_parser()[0] / potato_rate) + (parser.beet_parser()[0] / beet_rate)
                + (parser.carrot_parcer()[0] / carrot_rate) + (parser.onion_parcer()[0] * onion_rate)
                + (parser.cabbage_parcer()[0] * cabbage_rate)) / borsh_mututal_devider,

        "eko": ((parser.water_in_6l_bottle_parser()[1] / water_rate) + (parser.pork_lopatka_parser()[1] * meat_rate)
                + (parser.potato_parser()[1] / potato_rate) + (parser.beet_parser()[1] / beet_rate)
                + (parser.carrot_parcer()[1] / carrot_rate) + (parser.onion_parcer()[1] * onion_rate)
                + (parser.cabbage_parcer()[1] * cabbage_rate)) / borsh_mututal_devider,

        "varus": ((parser.water_in_6l_bottle_parser()[2] / water_rate) + (parser.pork_lopatka_parser()[2] * meat_rate)
                  + (parser.potato_parser()[2] / potato_rate) + (parser.beet_parser()[2] / beet_rate)
                  + (parser.carrot_parcer()[2] / carrot_rate) + (parser.onion_parcer()[2] * onion_rate)
                  + (parser.cabbage_parcer()[2] * cabbage_rate)) / borsh_mututal_devider,

        "silpo": ((parser.water_in_6l_bottle_parser()[3] / water_rate)
                  + ((parser.pork_lopatka_parser()[3]*silpo_correct_price) * meat_rate)
                  + (parser.potato_parser()[3] / potato_rate) + ((parser.beet_parser()[3] * silpo_correct_price) / beet_rate)
                  + ((parser.carrot_parcer()[3] * silpo_correct_price) / carrot_rate)
                  + ((parser.onion_parcer()[3] * silpo_correct_price) * onion_rate)
                  + ((parser.cabbage_parcer()[3] * silpo_correct_price) * cabbage_rate)) / borsh_mututal_devider,

        "novus": ((parser.water_in_6l_bottle_parser()[5] / water_rate) + (parser.pork_lopatka_parser()[5] * meat_rate)
                  + (parser.potato_parser()[5] / potato_rate) + (parser.beet_parser()[5] / beet_rate)
                  + (parser.carrot_parcer()[5] / carrot_rate) + (parser.onion_parcer()[5] * onion_rate)
                  + (parser.cabbage_parcer()[5] * cabbage_rate)) / borsh_mututal_devider,

        "metro": ((parser.water_in_6l_bottle_parser()[6] / water_rate) + (parser.pork_lopatka_parser()[6] * meat_rate)
                  + (parser.potato_parser()[6] / potato_rate) + (parser.beet_parser()[6] / beet_rate)
                  + (parser.carrot_parcer()[6] / carrot_rate) + (parser.onion_parcer()[6] * onion_rate)
                  + (parser.cabbage_parcer()[6] * cabbage_rate)) / borsh_mututal_devider,

        "fozzy": ((parser.water_in_6l_bottle_parser()[8] / water_rate) + (parser.pork_lopatka_parser()[8] * meat_rate)
                  + (parser.potato_parser()[8] / potato_rate) + (parser.beet_parser()[8] / beet_rate)
                  + (parser.carrot_parcer()[8] / carrot_rate) + (parser.onion_parcer()[8] * onion_rate)
                  + (parser.cabbage_parcer()[8] * cabbage_rate)) / borsh_mututal_devider,
    }},

    {'veriniki_potato': {
        "atb": ((parser.four_parser()[0] * sour_var) + (parser.water_in_6l_bottle_parser()[0] * sour_var)
                + (parser.egg_parcer()[0] * egg_var) + (parser.oil_for_dishes_parser()[0] * oil_var)
                + (parser.onion_parcer()[0] * onion_var) + (parser.sour_cream_for_dishes_parser()[0])
                + (parser.potato_parser()[0] * potato_var)) / vareniki_mutual_devider,

        "eko": ((parser.four_parser()[1] * sour_var) + (parser.water_in_6l_bottle_parser()[1] * sour_var)
                + ((parser.egg_parcer()[1] * egg_correct_price) * egg_var) + (parser.oil_for_dishes_parser()[1] * oil_var)
                + (parser.onion_parcer()[1] * onion_var) + (parser.sour_cream_for_dishes_parser()[1])
                + (parser.potato_parser()[1] * potato_var)) / vareniki_mutual_devider,

        "varus": ((parser.four_parser()[2] * sour_var) + (parser.water_in_6l_bottle_parser()[2] * sour_var)
                + (parser.egg_parcer()[2] * egg_var) + (parser.oil_for_dishes_parser()[2] * oil_var)
                + (parser.onion_parcer()[2] * onion_var) + (parser.sour_cream_for_dishes_parser()[2])
                + (parser.potato_parser()[2] * potato_var)) / vareniki_mutual_devider,

        "silpo": ((parser.four_parser()[3] * sour_var) + (parser.water_in_6l_bottle_parser()[3] * sour_var)
                + (parser.egg_parcer()[3] * egg_var) + (parser.oil_shedriy_dar_850_parcer()[3] * oil_var)
                + ((parser.onion_parcer()[3] * silpo_correct_price) * onion_var) + (parser.sour_cream_for_dishes_parser()[3])
                + (parser.potato_parser()[3] * potato_var)) / vareniki_mutual_devider,

        "novus": ((parser.four_parser()[5] * sour_var) + (parser.water_in_6l_bottle_parser()[5] * sour_var)
                + (parser.egg_parcer()[5] * egg_var) + (parser.oil_shedriy_dar_850_parcer()[5] * oil_var)
                + (parser.onion_parcer()[5] * onion_var) + (parser.sour_cream_for_dishes_parser()[5])
                + (parser.potato_parser()[5] * potato_var)) / vareniki_mutual_devider,

        "metro": ((parser.four_parser()[6] * sour_var) + (parser.water_in_6l_bottle_parser()[6] * sour_var)
                + (parser.egg_parcer()[6] * egg_var) + (parser.oil_shedriy_dar_850_parcer()[6] * oil_var)
                + (parser.onion_parcer()[6] * onion_var) + (parser.sour_cream_for_dishes_parser()[6])
                + (parser.potato_parser()[6] * potato_var)) / vareniki_mutual_devider,

        "fozzy": ((parser.four_parser()[8] * sour_var) + (parser.water_in_6l_bottle_parser()[8] * sour_var)
                + ((parser.egg_parcer()[8] * egg_correct_price) * egg_var) + (parser.oil_shedriy_dar_850_parcer()[8] * oil_var)
                + (parser.onion_parcer()[8] * onion_var) + (parser.sour_cream_for_dishes_parser()[8])
                + (parser.potato_parser()[8] * potato_var)) / vareniki_mutual_devider,
    }},
]


def get_all_prices():
    to_json = dict()
    for item in all_products_names:
        for product, values in item.items():
            to_json[product] = values
    with open('/home/andrey/GroceryAppVol3/FBApp/my_app/prices_store.json', 'w') as f:
        json.dump(to_json, f, sort_keys=False, indent=len(all_products_names))
        print('Все продукты и их цены добавлены в базу данных!')


get_all_prices()
