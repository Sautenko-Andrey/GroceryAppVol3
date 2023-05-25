import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np

from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.models import load_model

from .items_full_names import *


class TesterForGroceryAppText:
    # опредедяем количество наиболее употребляемых слов в тексте запроса пользователя
    MAX_WORDS = 1000

    # определяем количество слов, к которому дуте приведен каждый запрос от пользователя
    MAX_LENGTH_TEXT = 10

    def add_new_item(self,path_tail: str):
        '''Функция для предвариетльной обработки обучающего текстового набора для НС'''

        # загрузка обучающего текста
        path = f'/home/andrey/grocery_data/ALL_TEXT_VARIANTS/{path_tail}'
        with open(path, 'r', encoding='utf-8') as f:
            item_text = f.readlines()
        # убираем первый невидимый символ
        item_text[0] = item_text[0].replace('\ufeff', '')
        return item_text

    def prepearing_data(self):

        #загрузка обучающего текста
        obolon_premium_extra_11_text=self.add_new_item('pivo_obolon_extra(1.1).txt')
        hetman_sagaydachniy_07_text=self.add_new_item('vodka_hetman(0.7).txt')
        coffee_aroma_gold_classic_100gr_text=self.add_new_item('coffee_aroma_gold_classic_100gr.txt')
        apple_golden_text=self.add_new_item('apple_golden.txt')
        coca_cola_2l_text=self.add_new_item('coca_cola.txt')
        KOMO_paprikash_text=self.add_new_item('furnaced_cheese_KOMO_paprikash.txt')
        garlik_text=self.add_new_item('garlik.txt')
        kent_8_text=self.add_new_item('kent_8.txt')
        tea_minutka_40_p_black_text=self.add_new_item('tea_minutka_40_packs_black.txt')
        oil_shedriy_dar_850_text=self.add_new_item('oil_shedriy_dar_850.txt')
        onion_text=self.add_new_item('onion.txt')
        fairy_text=self.add_new_item('fairy.txt')
        apple_black_prince_text=self.add_new_item('apple_black_prince.txt')
        gorchica_kolos_text=self.add_new_item('gorchica_kolos.txt')
        smetana_stolica_smaky_20_400_text=self.add_new_item('smetana_stolica_smaky_20jir_400g.txt')
        limon_text=self.add_new_item('limon.txt')
        oil_oleyna_neraf_850_text=self.add_new_item('oil_oleyna_neraf_850.txt')
        pivo_lvivske_svitle_24l_text = self.add_new_item('pivo_lvivske_svitle_24l.txt')
        pena_arko_cool_200_100_text = self.add_new_item('pena_arko_cool_200_bonus_100.txt')
        pena_arko_sensitive_200_100_text = self.add_new_item('pena_arko_sensitive_200_bonus_100.txt')
        carrot_text = self.add_new_item('carrot.txt')
        drojji_text = self.add_new_item('drojji.txt')
        eggs_text = self.add_new_item('eggs.txt')
        desodorant_garnier_magniy_text = self.add_new_item('desodorant_garnier_magniy_m.txt')
        cabbage_text = self.add_new_item('cabbage.txt')
        marlboro_red_text = self.add_new_item('marlboro_red.txt')
        mayonez_detsk_shedro_190_text = self.add_new_item('mayonez_dom_detsk_shedro.txt')
        rexona_aloe_vera_w_text = self.add_new_item('rexona_aloe_vera_w.txt')
        smetana_stolica_smaky_15jir_400gr_text = self.add_new_item('smetana_stolica_smaky_15jir_400g.txt')
        tea_monomah_kenya_90_text = self.add_new_item('tea_monomah-kenya_90.txt')
        toilet_papir_text = self.add_new_item('toilet_papir_kiev_63m.txt')
        coffee_aroma_gold_freeze_dried_70g_text = self.add_new_item('coffee_aroma_gold_freeze_dried_70g.txt')
        gorchica_veres_ukrainska_micna_120g_text = self.add_new_item('gorchica_veres_ukrainska_micna_120g.txt')
        tea_monomah_100_ceylon_original_black_krupn_list_90g_text = self.add_new_item('tea_monomah_100%_ceylon_original_black_krupn_list_90g.txt')
        tea_monomah_ceylon_black_text = self.add_new_item('tea_monomah_ceylon_black.txt')
        apple_gala_text = self.add_new_item('apple_gala.txt')
        desodorant_garnier_spring_spirit_text = self.add_new_item('desodorant_garnier_spring_spirit.txt')
        smetana_galichanska_15_370gr_text = self.add_new_item('smetana_galichanska_15_370gr.txt')
        chips_lays_with_salt_big_pack_text = self.add_new_item('chips_lays_with_salt_big_pack.txt')
        sprite_2l_text = self.add_new_item('sprite_2l.txt')
        fanta_2l_text=self.add_new_item('fanta_2l.txt')
        bond_street_blue_selection_text = self.add_new_item('bond_street_blue_selection.txt')
        camel_blue_text = self.add_new_item('camel_blue.txt')
        LD_red_text = self.add_new_item('LD_red.txt')
        marlboro_gold_text = self.add_new_item('marlboro_gold.txt')
        rotmans_demi_blue_exclusive_text = self.add_new_item('rotmans_demi_blue_exclusive.txt')
        rotmans_demi_click_purple_text = self.add_new_item('rotmans_demi_click_purple.txt')
        winston_caster_text = self.add_new_item('winston_caster.txt')
        parlament_aqua_blue_text = self.add_new_item('parlament_aqua_blue.txt')
        winston_blue_text = self.add_new_item('winston_blue.txt')
        bond_street_red_selection_text = self.add_new_item('bond_street_red_selection.txt')
        LD_blue_text = self.add_new_item('LD_blue.txt')
        kent_silver_text = self.add_new_item('kent_silver.txt')
        kent_navy_blue_new_text = self.add_new_item('kent_navy_blue_new.txt')
        beer_chernigivske_svitle_05_l_glass_text = self.add_new_item('beer_chernigivske_svitle_05_l_glass.txt')
        beer_stella_artois_05_l_glass_text = self.add_new_item('beer_stella_artois_05_l_glass.txt')
        beer_obolon_svitle_05_l_glass_text=self.add_new_item('beer_obolon_svitle_05_l_glass.txt')
        beer_jigulivske_svitle_05_l_glass_text = self.add_new_item('beer_jigulivske_svitle_05_l_glass.txt')
        beer_rogan_tradiciyne_svitle_05_l_glass_text = self.add_new_item('beer_rogan_tradiciyne_svitle_05_l_glass.txt')
        beer_corona_extra_svitle_033_l_glass_text = self.add_new_item('beer_corona_extra_svitle_033_l_glass.txt')
        beer_chernigivske_bile_nefilter_05_l_glass_text = self.add_new_item('beer_chernigivske_bile_nefilter_05_l_glass.txt')
        beer_yantar_svitle_05_l_glass_text = self.add_new_item('beer_yantar_svitle_05_l_glass.txt')
        beer_zibert_svitle_05_l_glass_text = self.add_new_item('beer_zibert_svitle_05_l_glass.txt')
        beer_arsenal_micne_05_l_glass_text = self.add_new_item('beer_arsenal_micne_05_l_glass.txt')
        beer_persha_brovarnya_zakarpatske_05_l_glass_text = self.add_new_item('beer_persha_brovarnya_zakarpatske_05_l_glass.txt')
        beer_lvivske_svitle_05_l_glass_text = self.add_new_item('beer_lvivske_svitle_05_l_glass.txt')
        beer_lvivske_1715_05_l_glass_text = self.add_new_item('beer_lvivske_1715_05_l_glass.txt')
        beer_zlata_praha_svitle_05_l_glass_text = self.add_new_item('beer_zlata_praha_svitle_05_l_glass.txt')
        beer_tuborg_green_05_l_glass_text = self.add_new_item('beer_tuborg_green_05_l_glass.txt')
        beer_slavutich_ice_mix_lime_svitle_05_l_glass_text = self.add_new_item('beer_slavutich_ice_mix_lime_svitle_05_l_glass.txt')
        beer_teteriv_svitle_05_l_glass_text = self.add_new_item('beer_teteriv_svitle_05_l_glass.txt')
        beer_krusovice_svitle_05_l_glass_text = self.add_new_item('beer_krusovice_svitle_05_l_glass.txt')
        beer_heineken_svitle_05_l_glass_text = self.add_new_item('beer_heineken_svitle_05_l_glass.txt')
        beer_amstel_svitle_05_l_glass_text = self.add_new_item('beer_amstel_svitle_05_l_glass.txt')
        beer_hike_premium_svitle_05_l_glass_text = self.add_new_item('beer_hike_premium_svitle_05_l_glass.txt')
        beer_bochkove_svitle_05_l_glass_text = self.add_new_item('beer_bochkove_svitle_05_l_glass.txt')
        beer_kronenbourg_1664_blanc_046_l_glass_text = self.add_new_item('beer_kronenbourg_1664_blanc_046_l_glass.txt')
        beer_opilla_nepasterizovane_05_l_glass_text = self.add_new_item('beer_opilla_nepasterizovane_05_l_glass.txt')
        beer_yachminniy_kolos_svitle_05_l_glass_text = self.add_new_item('beer_yachminniy_kolos_svitle_05_l_glass.txt')
        beer_opilla_korifey_05_l_glass_text = self.add_new_item('beer_opilla_korifey_05_l_glass.txt')
        beer_chayka_dniprovska_svitle_05_l_glass_text = self.add_new_item('beer_chayka_dniprovska_svitle_05_l_glass.txt')
        beer_chayka_chernomorska_svitle_05_l_glass_text = self.add_new_item('beer_chayka_chernomorska_svitle_05_l_glass.txt')
        beer_uman_pivo_waissburg_svitle_1l_plastic_text = self.add_new_item('beer_uman_pivo_waissburg_svitle_1l_plastic.txt')
        beer_uman_pivo_pshenichnoe_svitle_1l_plastic_text = self.add_new_item('beer_uman_pivo_pshenichnoe_svitle_1l_plastic.txt')
        beer_berdichevske_hmilne_svitle_1l_plastic_text = self.add_new_item('beer_berdichevske_hmilne_svitle_1l_plastic.txt')
        beer_berdichevske_lager_svitle_1l_plastic_text = self.add_new_item('beer_berdichevske_lager_svitle_1l_plastic.txt')
        beer_opilla_korifey_svitle_11l_plastic_text = self.add_new_item('beer_opilla_korifey_svitle_11l_plastic.txt')
        beer_obolon_jigulivske_exportne_svitle_1l_plastic_text = self.add_new_item('beer_obolon_jigulivske_exportne_svitle_1l_plastic.txt')
        beer_yantar_svitle_12l_plastic_text = self.add_new_item('beer_yantar_svitle_12l_plastic.txt')
        beer_jashkivske_pshenichne_nefilter_1l_plastic_text = self.add_new_item('beer_jashkivske_pshenichne_nefilter_1l_plastic.txt')
        beer_jashkivske_svitle_nefilter_1l_plastic_text = self.add_new_item('beer_jashkivske_svitle_nefilter_1l_plastic.txt')
        beer_jashkivske_jigulivske_nefilter_1l_plastic_text = self.add_new_item('beer_jashkivske_jigulivske_nefilter_1l_plastic.txt')
        beer_persha_privatna_brovarnya_bochkove_svitle_1l_plastic_text = self.add_new_item('beer_persha_privatna_brovarnya_bochkove_svitle_1l_plastic.txt')
        beer_chayka_dniprovska_svitle_1l_plastic_text = self.add_new_item('beer_chayka_dniprovska_svitle_1l_plastic.txt')
        ketchup_torchin_chasnik_270gr_text = self.add_new_item('ketchup_torchin_chasnik_270gr.txt')
        muka_zolote_zernyatko_pshen_2kg_text = self.add_new_item('muka_zolote_zernyatko_pshen_2kg.txt')
        mayonez_korolivskiy_smak_kororlivskiy_67_300gr_text = self.add_new_item('mayonez_korolivskiy_smak_kororlivskiy_67_300gr.txt')
        beer_chernigivske_bile_nefilter_1l_plastic_text = self.add_new_item('beer_chernigivske_bile_nefilter_1l_plastic.txt')
        beer_obolon_svitle_1l_plastic_text = self.add_new_item('beer_obolon_svitle_1l_plastic.txt')
        beer_rogan_svitle_tradiciyne_1l_plastic_text = self.add_new_item('beer_rogan_svitle_tradiciyne_1l_plastic.txt')
        sous_chumak_chesnochniy_200gr_text = self.add_new_item('sous_chumak_chesnochniy_200gr.txt')
        jvachka_orbit_clubnika_banan_text = self.add_new_item('jvachka_orbit_clubnika_banan.txt')
        LM_red_text = self.add_new_item('LM_red.txt')
        beer_jigulivske_svitle_2_l_plastic_text = self.add_new_item('beer_jigulivske_svitle_2_l_plastic.txt')
        beer_chayka_dniprovska_svitle_2l_plastic_text = self.add_new_item('beer_chayka_dniprovska_svitle_2l_plastic.txt')
        beer_piwny_kubek_svitle_2l_plastic_text = self.add_new_item('beer_piwny_kubek_svitle_2l_plastic.txt')
        ketchup_torchin_do_shasliky_270gr_test = self.add_new_item('ketchup_torchin_do_shasliky_270gr.txt')
        mayonez_chumak_appetitniy_50_300gr_text = self.add_new_item('mayonez_chumak_appetitniy_50_300gr.txt')
        kolbasa_persha_stolica_salyami_firmennaya_vs_text = self.add_new_item('kolbasa_persha_stolica_salyami_firmennaya_vs.txt')
        coffee_chorna_karta_gold_50gr_text = self.add_new_item('coffee_chorna_karta_gold_50gr.txt')
        beer_arsenal_micne_svitle_2l_plastic_text = self.add_new_item('beer_arsenal_micne_svitle_2l_plastic.txt')
        beer_ppb_bochkove_svitle_2l_plastic_text = self.add_new_item('beer_ppb_bochkove_svitle_2l_plastic.txt')
        beer_ppb_zakarpatske_originalne_svitle_2l_plastic_text = self.add_new_item('beer_ppb_zakarpatske_originalne_svitle_2l_plastic.txt')
        beer_zibert_svitle_05_l_banochnoe_text = self.add_new_item('beer_zibert_svitle_05_l_banochnoe.txt')
        yogurt_fanni_1_5_240gr_v_banke_text = self.add_new_item('yogurt_fanni_1_5_240gr_v_banke.txt')
        kefir_slviya_2_5_850gr_v_pakete_text = self.add_new_item('kefir_slviya_2_5_850gr_v_pakete.txt')
        beer_obolon_kievske_rozlivne_svitle_195l_plastic_text = self.add_new_item('beer_obolon_kievske_rozlivne_svitle_195l_plastic.txt')
        beer_chernigivske_light_svitle_2l_plastic_text = self.add_new_item('beer_chernigivske_light_svitle_2l_plastic.txt')
        beer_opilla_korifey_svitle_2l_plastic_text = self.add_new_item('beer_opilla_korifey_svitle_2l_plastic.txt')
        beer_yantar_svitle_2l_plastic_text = self.add_new_item('beer_yantar_svitle_2l_plastic.txt')
        beer_tuborg_green_05_4_banki_2litra_text = self.add_new_item('beer_tuborg_green_05_4_banki_2litra.txt')
        beer_ppb_zakarpatske_svitle_05_4_banki_2litra_text = self.add_new_item('beer_ppb_zakarpatske_svitle_05_4_banki_2litra.txt')
        beer_ppb_bochkove_svitle_05_4_banki_2litra_text = self.add_new_item('beer_ppb_bochkove_svitle_05_4_banki_2litra.txt')
        beer_budweiser_budvar_05_l_glass_text = self.add_new_item('beer_budweiser_budvar_05_l_glass.txt')
        beer_pilsner_urquell_05_l_glass_text = self.add_new_item('beer_pilsner_urquell_05_l_glass.txt')
        beer_robert_doms_belgiyskiy_svitle_nefilter_05_l_glass_text = self.add_new_item('beer_robert_doms_belgiyskiy_svitle_nefilter_05_l_glass.txt')
        beer_chernigivske_svitle_05_l_jb_text = self.add_new_item('beer_chernigivske_svitle_05_l_jb.txt')
        beer_chernigivske_bile_nefilter_05_l_jb_text = self.add_new_item('beer_chernigivske_bile_nefilter_05_l_jb.txt')
        beer_velkopopovicky_kozel_temne_05_l_jb_text = self.add_new_item('beer_velkopopovicky_kozel_temne_05_l_jb.txt')
        beer_edelmeister_pilsner_svitle_05_l_jb_text = self.add_new_item('beer_edelmeister_pilsner_svitle_05_l_jb.txt')
        beer_faxe_svitle_05_l_jb_text = self.add_new_item('beer_faxe_svitle_05_l_jb.txt')
        beer_livu_pilzenes_svitle_05_l_jb_text = self.add_new_item('beer_livu_pilzenes_svitle_05_l_jb.txt')
        beer_velkopopovicky_kozel_svitle_05_l_jb_text = self.add_new_item('beer_velkopopovicky_kozel_svitle_05_l_jb.txt')
        beer_obolon_beermix_limon_05_l_jb_text = self.add_new_item('beer_obolon_beermix_limon_05_l_jb.txt')
        beer_edelmeister_weizenbier_nefilter_svitle_05_l_jb_text = self.add_new_item('beer_edelmeister_weizenbier_nefilter_svitle_05_l_jb.txt')
        beer_edelmeister_schwarzbier_temnoe_05_l_jb_text = self.add_new_item('beer_edelmeister_schwarzbier_temnoe_05_l_jb.txt')
        beer_hike_blanche_svitle_nefilter_05_l_jb_text = self.add_new_item('beer_hike_blanche_svitle_nefilter_05_l_jb.txt')
        beer_zlata_praha_svitle_05_l_jb_text = self.add_new_item('beer_zlata_praha_svitle_05_l_jb.txt')
        beer_thuringer_premium_beer_svitle_05_l_jb_text = self.add_new_item('beer_thuringer_premium_beer_svitle_05_l_jb.txt')
        beer_livu_sencu_svitle_05_l_jb_text = self.add_new_item('beer_livu_sencu_svitle_05_l_jb.txt')
        beer_germanarich_svitle_05_l_jb_text = self.add_new_item('beer_germanarich_svitle_05_l_jb.txt')
        beer_hike_premium_svitle_05_l_jb_text = self.add_new_item('beer_hike_premium_svitle_05_l_jb.txt')
        beer_obolon_nonalcohol_svitle_nefilter_05_l_jb_text = self.add_new_item('beer_obolon_nonalcohol_svitle_nefilter_05_l_jb.txt')
        beer_zibert_bavarske_svitle_05_l_jb_text = self.add_new_item('beer_zibert_bavarske_svitle_05_l_jb.txt')
        beer_bavaria_liquid_apple_nonalcohol_svitle_05_l_jb_text = self.add_new_item('beer_bavaria_liquid_apple_nonalcohol_svitle_05_l_jb.txt')
        beer_heineken_svitle_05_l_jb_text = self.add_new_item('beer_heineken_svitle_05_l_jb.txt')
        beer_rychtar_grunt_11_svitle_05_l_jb_text = self.add_new_item('beer_rychtar_grunt_11_svitle_05_l_jb.txt')
        beer_amstel_svitle_05_l_jb_text = self.add_new_item('beer_amstel_svitle_05_l_jb.txt')
        beer_bavaria_svitle_05_l_jb_text = self.add_new_item('beer_bavaria_svitle_05_l_jb.txt')
        beer_bavaria_svitle_nonalcohol_05_l_jb_text = self.add_new_item('beer_bavaria_svitle_nonalcohol_05_l_jb.txt')
        beer_edelburg_lager_svitle_05_l_jb_text = self.add_new_item('beer_edelburg_lager_svitle_05_l_jb.txt')
        beer_donner_pills_svitle_05_l_jb_text = self.add_new_item('beer_donner_pills_svitle_05_l_jb.txt')
        beer_dutch_windmill_svitle_05_l_jb_text = self.add_new_item('beer_dutch_windmill_svitle_05_l_jb.txt')
        beer_edelberg_hefeweizen_svitle_nefilter_05_l_jb_text = self.add_new_item('beer_edelberg_hefeweizen_svitle_nefilter_05_l_jb.txt')
        beer_edelmeister_unfiltered_svitle_nefilter_05_l_jb_text = self.add_new_item('beer_edelmeister_unfiltered_svitle_nefilter_05_l_jb.txt')
        beer_estrella_damm_barcelona_svitle_05_l_jb_text = self.add_new_item('beer_estrella_damm_barcelona_svitle_05_l_jb.txt')
        beer_halne_jasne_pelne_05_l_jb_text = self.add_new_item('beer_halne_jasne_pelne_05_l_jb.txt')
        beer_eurotour_hefeweissbier_svitle_05_l_jb_text = self.add_new_item('beer_eurotour_hefeweissbier_svitle_05_l_jb.txt')
        beer_hollandia_strong_svitle_05_l_jb_text = self.add_new_item('beer_hollandia_strong_svitle_05_l_jb.txt')
        beer_lander_brau_premium_svitle_05_l_jb_text = self.add_new_item('beer_lander_brau_premium_svitle_05_l_jb.txt')
        beer_saku_kuld_05_l_jb_text = self.add_new_item('beer_saku_kuld_05_l_jb.txt')
        beer_saku_original_05_l_jb_text = self.add_new_item('beer_saku_original_05_l_jb.txt')
        beer_stangen_lager_svitle_05_l_jb_text = self.add_new_item('beer_stangen_lager_svitle_05_l_jb.txt')
        beer_van_pur_premium_svitle_05_l_jb_text = self.add_new_item('beer_van_pur_premium_svitle_05_l_jb.txt')
        beer_bavaria_mango_marakya_bezalkogol_svitle_05_l_jb_text = self.add_new_item('beer_bavaria_mango_marakya_bezalkogol_svitle_05_l_jb.txt')
        beer_bavaria_granat_bezalkogol_svitle_05_l_jb_text = self.add_new_item('beer_bavaria_granat_bezalkogol_svitle_05_l_jb.txt')
        beer_obolon_beermix_malina_05_l_jb_text = self.add_new_item('beer_obolon_beermix_malina_05_l_jb.txt')
        beer_obolon_beermix_vishnya_05_l_jb_text = self.add_new_item('beer_obolon_beermix_vishnya_05_l_jb.txt')
        beer_lomza_svitle_05_l_jb_text = self.add_new_item('beer_lomza_svitle_05_l_jb.txt')
        beer_paderborner_pilsener_svitle_05_l_jb_text = self.add_new_item('beer_paderborner_pilsener_svitle_05_l_jb.txt')
        beer_paderborner_export_05_l_jb_text = self.add_new_item('beer_paderborner_export_05_l_jb.txt')
        beer_clausthaler_greipfruit_nonalcohol_05_l_jb_text = self.add_new_item('beer_clausthaler_greipfruit_nonalcohol_05_l_jb.txt')
        beer_clausthaler_original_nonalcohol_05_l_jb_text = self.add_new_item('beer_clausthaler_original_nonalcohol_05_l_jb.txt')
        beer_clausthaler_lemon_nonalcohol_05_l_jb_text = self.add_new_item('beer_clausthaler_lemon_nonalcohol_05_l_jb.txt')
        beer_forever_rock_n_roll_svitle_nefilter_05_l_jb_text = self.add_new_item('beer_forever_rock_n_roll_svitle_nefilter_05_l_jb.txt')
        beer_forever_black_queen_temne_nefilter_05_l_jb_text = self.add_new_item('beer_forever_black_queen_temne_nefilter_05_l_jb.txt')
        beer_forever_kite_safari_svitle_nefilter_05_l_jb_text = self.add_new_item('beer_forever_kite_safari_svitle_nefilter_05_l_jb.txt')
        beer_forever_crazy_svitle_nefilter_05_l_jb_text = self.add_new_item('beer_forever_crazy_svitle_nefilter_05_l_jb.txt')
        beer_hike_light_svitle_05_l_jb_text = self.add_new_item('beer_hike_light_svitle_05_l_jb.txt')
        beer_hike_zero_nonalcohol_05_l_jb_text = self.add_new_item('beer_hike_zero_nonalcohol_05_l_jb.txt')
        beer_horn_disel_ice_pilsner_svitle_0568_l_jb_text = self.add_new_item('beer_horn_disel_ice_pilsner_svitle_0568_l_jb.txt')
        beer_horn_original_svitle_0568_l_jb_text = self.add_new_item('beer_horn_original_svitle_0568_l_jb.txt')
        beer_horn_traditional_svitle_0568_l_jb_text = self.add_new_item('beer_horn_traditional_svitle_0568_l_jb.txt')
        beer_horn_premium_svitle_05_l_jb_text = self.add_new_item('beer_horn_premium_svitle_05_l_jb.txt')
        beer_krusovice_cerne_temne_05_l_jb_text = self.add_new_item('beer_krusovice_cerne_temne_05_l_jb.txt')
        beer_lander_brau_micne_05_l_jb_text = self.add_new_item('beer_lander_brau_micne_05_l_jb.txt')
        beer_lander_brau_svitle_nefilter_05_l_jb_text = self.add_new_item('beer_lander_brau_svitle_nefilter_05_l_jb.txt')
        beer_padeborner_pilger_nefilter_svitle_05_l_jb_text = self.add_new_item('beer_padeborner_pilger_nefilter_svitle_05_l_jb.txt')
        beer_platan_jedenactka_05_l_jb_text = self.add_new_item('beer_platan_jedenactka_05_l_jb.txt')
        beer_praga_svitle_05_l_jb_text = self.add_new_item('beer_praga_svitle_05_l_jb.txt')
        beer_saku_rock_svitle_0568_l_jb_text = self.add_new_item('beer_saku_rock_svitle_0568_l_jb.txt')
        beer_sitnan_svitle_05_l_jb_text = self.add_new_item('beer_sitnan_svitle_05_l_jb.txt')
        beer_vienas_premium_golden_svitle_05_l_jb_text = self.add_new_item('beer_vienas_premium_golden_svitle_05_l_jb.txt')
        beer_vienas_premium_traditional_svitle_05_l_jb_text = self.add_new_item('beer_vienas_premium_traditional_svitle_05_l_jb.txt')
        beer_volynski_browar_forever_sweet_wit_pshen_nefilter_svitle_05_l_jb_text = self.add_new_item('beer_volynski_browar_forever_sweet_wit_pshen_nefilter_svitle_05_l_jb.txt')
        beer_zahringer_premium_svitle_05_l_jb_text = self.add_new_item('beer_zahringer_premium_svitle_05_l_jb.txt')
        beer_zahringer_hefeweizen_svitle_05_l_jb_text = self.add_new_item('beer_zahringer_hefeweizen_svitle_05_l_jb.txt')
        beer_jajkivske_svitle__nefilter_05_l_jb_text = self.add_new_item('beer_jajkivske_svitle__nefilter_05_l_jb.txt')
        beer_obolon_svitle_05_l_jb_text = self.add_new_item('beer_obolon_svitle_05_l_jb.txt')
        beer_pubster_svitle_05_l_jb_text = self.add_new_item('beer_pubster_svitle_05_l_jb.txt')
        beer_chaika_chernomorskaya_05_l_jb_text = self.add_new_item('beer_chaika_chernomorskaya_05_l_jb.txt')
        beer_ppb_zakarpatske_orig_svitle_05_l_jb_text = self.add_new_item('beer_ppb_zakarpatske_orig_svitle_05_l_jb.txt')
        beer_ppb_bochkove_nefilter_05_l_jb_text = self.add_new_item('beer_ppb_bochkove_nefilter_05_l_jb.txt')
        beer_ppb_nefilter_svitle_nonalco_05_l_jb_text = self.add_new_item('beer_ppb_nefilter_svitle_nonalco_05_l_jb.txt')
        beer_ppb_limon_lime_nonalco_nefilter_05_l_jb_text = self.add_new_item('beer_ppb_limon_lime_nonalco_nefilter_05_l_jb.txt')
        beer_chaika_dniprovskaya_05_l_jb_text = self.add_new_item('beer_chaika_dniprovskaya_05_l_jb.txt')
        beer_brok_export_svitle_05_l_jb_text = self.add_new_item('beer_brok_export_svitle_05_l_jb.txt')
        beer_carling_svitle_05_l_jb_text = self.add_new_item('beer_carling_svitle_05_l_jb.txt')
        beer_keten_brug_blanche_elegant_nefilter_05_l_jb_text = self.add_new_item('beer_keten_brug_blanche_elegant_nefilter_05_l_jb.txt')
        beer_budweiser_nonalco_svitle_05_l_jb_text = self.add_new_item('beer_budweiser_nonalco_svitle_05_l_jb.txt')
        beer_feldschlosschen_wheat_beer_svitle05_l_jb_text = self.add_new_item('beer_feldschlosschen_wheat_beer_svitle05_l_jb.txt')
        beer_teteriv_hmilna_vishnya_polutemne_05_l_jb_text = self.add_new_item('beer_teteriv_hmilna_vishnya_polutemne_05_l_jb.txt')
        beer_grotwerg_svitle_nonalco_05_l_jb_text = self.add_new_item('beer_grotwerg_svitle_nonalco_05_l_jb.txt')
        beer_holland_import_svitle_05_l_jb_text = self.add_new_item('beer_holland_import_svitle_05_l_jb.txt')
        beer_golden_castle_export_svitle_05_l_jb_text = self.add_new_item('beer_golden_castle_export_svitle_05_l_jb.txt')
        beer_5_0_origin_craft_beer_nefilter_svitle_05_l_jb_text = self.add_new_item('beer_5_0_origin_craft_beer_nefilter_svitle_05_l_jb.txt')
        beer_guinness_draught_temne_044_l_jb_text = self.add_new_item('beer_guinness_draught_temne_044_l_jb.txt')
        beer_grimbergenDoubleAmbree_napivtemne_05_l_jb_text = self.add_new_item('beer_grimbergenDoubleAmbree_napivtemne_05_l_jb.txt')
        beer_warsteinerPremiumVerum_svitle_05_l_jb_text = self.add_new_item('beer_warsteinerPremiumVerum_svitle_05_l_jb.txt')
        beer_dab_temne_05_l_jb_text = self.add_new_item('beer_dab_temne_05_l_jb.txt')
        beer_grimbergenBlanche_svitle_05_l_jb_text = self.add_new_item('beer_grimbergenBlanche_svitle_05_l_jb.txt')
        beer_klosterkellerWeissbierChina_svitle_nefilter_05_l_jb_text = self.add_new_item('beer_klosterkellerWeissbierChina_svitle_nefilter_05_l_jb.txt')
        beer_karpackiePils_svitle_05_l_jb_text = self.add_new_item('beer_karpackiePils_svitle_05_l_jb.txt')
        beer_5_0_OriginalPills_svitle_05_l_jb_text = self.add_new_item('beer_5_0_OriginalPills_svitle_05_l_jb.txt')
        beer_5_0_Original_Lager_svitle_05_l_jb_text = self.add_new_item('beer_5_0_Original_Lager_svitle_05_l_jb.txt')
        beer_5_0_Original_Weiss_svitle_nefilter_05_l_jb_text = self.add_new_item('beer_5_0_Original_Weiss_svitle_nefilter_05_l_jb.txt')
        beer_fahnen_brau_svitle_05_l_jb_text = self.add_new_item('beer_fahnen_brau_svitle_05_l_jb.txt')
        beer_gosser_light_svitle_05_l_jb_text = self.add_new_item('beer_gosser_light_svitle_05_l_jb.txt')
        beer_holland_import_svitle_033_l_jb_text = self.add_new_item('beer_holland_import_svitle_033_l_jb.txt')
        beer_holsten_pilsener_048_l_jb_text = self.add_new_item('beer_holsten_pilsener_048_l_jb.txt')
        beer_obolon_premium_extra_brew_svitle_05_l_jb_text = self.add_new_item('beer_obolon_premium_extra_brew_svitle_05_l_jb.txt')
        beer_lvivske__svitle_048_l_jb_text = self.add_new_item('beer_lvivske__svitle_048_l_jb.txt')
        beer_carlsberg_premium_pilsner_05_l_jb_text = self.add_new_item('beer_carlsberg_premium_pilsner_05_l_jb.txt')
        beer_carlsberg_pilsner_05_l_jb_text = self.add_new_item('beer_carlsberg_pilsner_05_l_jb.txt')



        # объединям обучающие выборки:
        texts = obolon_premium_extra_11_text+ hetman_sagaydachniy_07_text + coffee_aroma_gold_classic_100gr_text+ apple_golden_text\
                + coca_cola_2l_text + KOMO_paprikash_text+ garlik_text + kent_8_text+ tea_minutka_40_p_black_text\
                + oil_shedriy_dar_850_text+ onion_text+ fairy_text + apple_black_prince_text+ gorchica_kolos_text\
                + smetana_stolica_smaky_20_400_text+ limon_text + oil_oleyna_neraf_850_text+ pivo_lvivske_svitle_24l_text\
                + pena_arko_cool_200_100_text+ pena_arko_sensitive_200_100_text + carrot_text + drojji_text + eggs_text\
                + desodorant_garnier_magniy_text + cabbage_text + marlboro_red_text + mayonez_detsk_shedro_190_text\
                + rexona_aloe_vera_w_text + smetana_stolica_smaky_15jir_400gr_text + tea_monomah_kenya_90_text + toilet_papir_text\
                + coffee_aroma_gold_freeze_dried_70g_text + gorchica_veres_ukrainska_micna_120g_text\
                + tea_monomah_100_ceylon_original_black_krupn_list_90g_text + tea_monomah_ceylon_black_text + apple_gala_text\
                + desodorant_garnier_spring_spirit_text + smetana_galichanska_15_370gr_text\
                + chips_lays_with_salt_big_pack_text + sprite_2l_text\
                + fanta_2l_text + bond_street_blue_selection_text + camel_blue_text + LD_red_text\
                + marlboro_gold_text + rotmans_demi_blue_exclusive_text + rotmans_demi_click_purple_text\
                + winston_caster_text + parlament_aqua_blue_text + winston_blue_text\
                + bond_street_red_selection_text + LD_blue_text + kent_silver_text\
                + kent_navy_blue_new_text + beer_chernigivske_svitle_05_l_glass_text\
                + beer_stella_artois_05_l_glass_text + beer_obolon_svitle_05_l_glass_text\
                + beer_jigulivske_svitle_05_l_glass_text + beer_rogan_tradiciyne_svitle_05_l_glass_text\
                + beer_corona_extra_svitle_033_l_glass_text + beer_chernigivske_bile_nefilter_05_l_glass_text\
                + beer_yantar_svitle_05_l_glass_text + beer_zibert_svitle_05_l_glass_text\
                + beer_arsenal_micne_05_l_glass_text + beer_persha_brovarnya_zakarpatske_05_l_glass_text\
                + beer_lvivske_svitle_05_l_glass_text + beer_lvivske_1715_05_l_glass_text\
                + beer_zlata_praha_svitle_05_l_glass_text + beer_tuborg_green_05_l_glass_text\
                + beer_slavutich_ice_mix_lime_svitle_05_l_glass_text + beer_teteriv_svitle_05_l_glass_text\
                + beer_krusovice_svitle_05_l_glass_text + beer_heineken_svitle_05_l_glass_text\
                + beer_amstel_svitle_05_l_glass_text + beer_hike_premium_svitle_05_l_glass_text\
                + beer_bochkove_svitle_05_l_glass_text + beer_kronenbourg_1664_blanc_046_l_glass_text\
                + beer_opilla_nepasterizovane_05_l_glass_text + beer_yachminniy_kolos_svitle_05_l_glass_text\
                + beer_opilla_korifey_05_l_glass_text + beer_chayka_dniprovska_svitle_05_l_glass_text\
                + beer_chayka_chernomorska_svitle_05_l_glass_text + beer_uman_pivo_waissburg_svitle_1l_plastic_text\
                + beer_uman_pivo_pshenichnoe_svitle_1l_plastic_text + beer_berdichevske_hmilne_svitle_1l_plastic_text\
                + beer_berdichevske_lager_svitle_1l_plastic_text + beer_opilla_korifey_svitle_11l_plastic_text\
                + beer_obolon_jigulivske_exportne_svitle_1l_plastic_text + beer_yantar_svitle_12l_plastic_text\
                + beer_jashkivske_pshenichne_nefilter_1l_plastic_text + beer_jashkivske_svitle_nefilter_1l_plastic_text\
                + beer_jashkivske_jigulivske_nefilter_1l_plastic_text + beer_persha_privatna_brovarnya_bochkove_svitle_1l_plastic_text\
                + beer_chayka_dniprovska_svitle_1l_plastic_text + ketchup_torchin_chasnik_270gr_text\
                + muka_zolote_zernyatko_pshen_2kg_text + mayonez_korolivskiy_smak_kororlivskiy_67_300gr_text\
                + beer_chernigivske_bile_nefilter_1l_plastic_text + beer_obolon_svitle_1l_plastic_text\
                + beer_rogan_svitle_tradiciyne_1l_plastic_text + sous_chumak_chesnochniy_200gr_text + jvachka_orbit_clubnika_banan_text\
                + LM_red_text + beer_jigulivske_svitle_2_l_plastic_text + beer_chayka_dniprovska_svitle_2l_plastic_text\
                + beer_piwny_kubek_svitle_2l_plastic_text + ketchup_torchin_do_shasliky_270gr_test\
                + mayonez_chumak_appetitniy_50_300gr_text + kolbasa_persha_stolica_salyami_firmennaya_vs_text\
                + coffee_chorna_karta_gold_50gr_text + beer_arsenal_micne_svitle_2l_plastic_text\
                + beer_ppb_bochkove_svitle_2l_plastic_text + beer_ppb_zakarpatske_originalne_svitle_2l_plastic_text\
                + beer_zibert_svitle_05_l_banochnoe_text + yogurt_fanni_1_5_240gr_v_banke_text\
                + kefir_slviya_2_5_850gr_v_pakete_text + beer_obolon_kievske_rozlivne_svitle_195l_plastic_text\
                + beer_chernigivske_light_svitle_2l_plastic_text + beer_opilla_korifey_svitle_2l_plastic_text\
                + beer_yantar_svitle_2l_plastic_text + beer_tuborg_green_05_4_banki_2litra_text\
                + beer_ppb_zakarpatske_svitle_05_4_banki_2litra_text + beer_ppb_bochkove_svitle_05_4_banki_2litra_text\
                + beer_budweiser_budvar_05_l_glass_text + beer_pilsner_urquell_05_l_glass_text\
                + beer_robert_doms_belgiyskiy_svitle_nefilter_05_l_glass_text + beer_chernigivske_svitle_05_l_jb_text\
                + beer_chernigivske_bile_nefilter_05_l_jb_text + beer_velkopopovicky_kozel_temne_05_l_jb_text\
                + beer_edelmeister_pilsner_svitle_05_l_jb_text + beer_faxe_svitle_05_l_jb_text\
                + beer_livu_pilzenes_svitle_05_l_jb_text + beer_velkopopovicky_kozel_svitle_05_l_jb_text\
                + beer_obolon_beermix_limon_05_l_jb_text + beer_edelmeister_weizenbier_nefilter_svitle_05_l_jb_text\
                + beer_edelmeister_schwarzbier_temnoe_05_l_jb_text + beer_hike_blanche_svitle_nefilter_05_l_jb_text\
                + beer_zlata_praha_svitle_05_l_jb_text + beer_thuringer_premium_beer_svitle_05_l_jb_text\
                + beer_livu_sencu_svitle_05_l_jb_text + beer_germanarich_svitle_05_l_jb_text\
                + beer_hike_premium_svitle_05_l_jb_text + beer_obolon_nonalcohol_svitle_nefilter_05_l_jb_text\
                + beer_zibert_bavarske_svitle_05_l_jb_text + beer_bavaria_liquid_apple_nonalcohol_svitle_05_l_jb_text\
                + beer_heineken_svitle_05_l_jb_text + beer_rychtar_grunt_11_svitle_05_l_jb_text + beer_amstel_svitle_05_l_jb_text\
                + beer_bavaria_svitle_05_l_jb_text + beer_bavaria_svitle_nonalcohol_05_l_jb_text + beer_edelburg_lager_svitle_05_l_jb_text\
                + beer_donner_pills_svitle_05_l_jb_text + beer_dutch_windmill_svitle_05_l_jb_text + beer_edelberg_hefeweizen_svitle_nefilter_05_l_jb_text\
                + beer_edelmeister_unfiltered_svitle_nefilter_05_l_jb_text + beer_estrella_damm_barcelona_svitle_05_l_jb_text\
                + beer_halne_jasne_pelne_05_l_jb_text + beer_eurotour_hefeweissbier_svitle_05_l_jb_text + beer_hollandia_strong_svitle_05_l_jb_text\
                + beer_lander_brau_premium_svitle_05_l_jb_text + beer_saku_kuld_05_l_jb_text + beer_saku_original_05_l_jb_text\
                + beer_stangen_lager_svitle_05_l_jb_text + beer_van_pur_premium_svitle_05_l_jb_text + beer_bavaria_mango_marakya_bezalkogol_svitle_05_l_jb_text\
                + beer_bavaria_granat_bezalkogol_svitle_05_l_jb_text + beer_obolon_beermix_malina_05_l_jb_text + beer_obolon_beermix_vishnya_05_l_jb_text\
                + beer_lomza_svitle_05_l_jb_text + beer_paderborner_pilsener_svitle_05_l_jb_text + beer_paderborner_export_05_l_jb_text\
                + beer_clausthaler_greipfruit_nonalcohol_05_l_jb_text + beer_clausthaler_original_nonalcohol_05_l_jb_text\
                + beer_clausthaler_lemon_nonalcohol_05_l_jb_text + beer_forever_rock_n_roll_svitle_nefilter_05_l_jb_text\
                + beer_forever_black_queen_temne_nefilter_05_l_jb_text + beer_forever_kite_safari_svitle_nefilter_05_l_jb_text\
                + beer_forever_crazy_svitle_nefilter_05_l_jb_text + beer_hike_light_svitle_05_l_jb_text + beer_hike_zero_nonalcohol_05_l_jb_text\
                + beer_horn_disel_ice_pilsner_svitle_0568_l_jb_text + beer_horn_original_svitle_0568_l_jb_text + beer_horn_traditional_svitle_0568_l_jb_text\
                + beer_horn_premium_svitle_05_l_jb_text + beer_krusovice_cerne_temne_05_l_jb_text + beer_lander_brau_micne_05_l_jb_text\
                + beer_lander_brau_svitle_nefilter_05_l_jb_text + beer_padeborner_pilger_nefilter_svitle_05_l_jb_text + beer_platan_jedenactka_05_l_jb_text\
                + beer_praga_svitle_05_l_jb_text + beer_saku_rock_svitle_0568_l_jb_text + beer_sitnan_svitle_05_l_jb_text\
                + beer_vienas_premium_golden_svitle_05_l_jb_text + beer_vienas_premium_traditional_svitle_05_l_jb_text\
                + beer_volynski_browar_forever_sweet_wit_pshen_nefilter_svitle_05_l_jb_text + beer_zahringer_premium_svitle_05_l_jb_text\
                + beer_zahringer_hefeweizen_svitle_05_l_jb_text + beer_jajkivske_svitle__nefilter_05_l_jb_text + beer_obolon_svitle_05_l_jb_text\
                + beer_pubster_svitle_05_l_jb_text + beer_chaika_chernomorskaya_05_l_jb_text + beer_ppb_zakarpatske_orig_svitle_05_l_jb_text\
                + beer_ppb_bochkove_nefilter_05_l_jb_text + beer_ppb_nefilter_svitle_nonalco_05_l_jb_text + beer_ppb_limon_lime_nonalco_nefilter_05_l_jb_text\
                + beer_chaika_dniprovskaya_05_l_jb_text + beer_brok_export_svitle_05_l_jb_text + beer_carling_svitle_05_l_jb_text\
                + beer_keten_brug_blanche_elegant_nefilter_05_l_jb_text + beer_budweiser_nonalco_svitle_05_l_jb_text\
                + beer_feldschlosschen_wheat_beer_svitle05_l_jb_text + beer_teteriv_hmilna_vishnya_polutemne_05_l_jb_text\
                + beer_grotwerg_svitle_nonalco_05_l_jb_text + beer_holland_import_svitle_05_l_jb_text + beer_golden_castle_export_svitle_05_l_jb_text\
                + beer_5_0_origin_craft_beer_nefilter_svitle_05_l_jb_text + beer_guinness_draught_temne_044_l_jb_text\
                + beer_grimbergenDoubleAmbree_napivtemne_05_l_jb_text + beer_warsteinerPremiumVerum_svitle_05_l_jb_text\
                + beer_dab_temne_05_l_jb_text + beer_grimbergenBlanche_svitle_05_l_jb_text + beer_klosterkellerWeissbierChina_svitle_nefilter_05_l_jb_text\
                + beer_karpackiePils_svitle_05_l_jb_text + beer_5_0_OriginalPills_svitle_05_l_jb_text + beer_5_0_Original_Lager_svitle_05_l_jb_text\
                + beer_5_0_Original_Weiss_svitle_nefilter_05_l_jb_text + beer_fahnen_brau_svitle_05_l_jb_text + beer_gosser_light_svitle_05_l_jb_text\
                + beer_holland_import_svitle_033_l_jb_text + beer_holsten_pilsener_048_l_jb_text + beer_obolon_premium_extra_brew_svitle_05_l_jb_text\
                + beer_lvivske__svitle_048_l_jb_text + beer_carlsberg_premium_pilsner_05_l_jb_text + beer_carlsberg_pilsner_05_l_jb_text

        return texts

    def create_tokenizer(self):
        # создаем необходимый нам токенайзер:
        tokenizer = Tokenizer(num_words=self.MAX_WORDS,
                              filters='!"-#$%amp;()*+-/:;<=>?@[\\]^_`{|}~\t\n\r',
                              lower=True, split=' ', char_level=False)

        # пропускаем все нащи тексты через токенайзер:
        tokenizer.fit_on_texts(self.prepearing_data())
        return tokenizer

    def index_convert_to_text(self, indeces_list):
        '''Метод для преобразования индексов в слова'''
        reverse_word_map = dict(map(reversed, self.create_tokenizer().word_index.items()))
        normal_text = [reverse_word_map.get(x) for x in indeces_list]
        return (normal_text)

    def identify_item(self, user_text):

        # загружаем обученную модель НС для распознования товара по тексту:
        model = load_model('/home/andrey/GroceryAppVol3/FBApp/my_app/my_model_text')

        # переводим пользовательский запрос в нижний регистр:
        user_text = user_text.lower()

        # пропускам текст через созданный токенайзер и преобразовываем слова в числа(индексы):
        # загружаем токенайзер:
        tokenizer = self.create_tokenizer()

        # преобразовываем слова:
        data = tokenizer.texts_to_sequences([user_text])

        # преобразовываем в вектор нужной длины,
        # дополняя нулями или сокращая до 10 слов в тексте
        data_pad = pad_sequences(data, maxlen=self.MAX_LENGTH_TEXT)

        result = model.predict(data_pad)
        print(result, np.argmax(result), sep='\n')
        if np.argmax(result) == 0:
            return BEER_OBOLON_PREMIUM_EXTRA_1_1_L
        elif np.argmax(result)==1:
            return VODKA_HETMAN_ICE_07_L
        elif np.argmax(result)==2:
            return COFFEE_AROMA_GOLD_CLASSIC_100_GR
        elif np.argmax(result)==3:
            return APPLE_GOLDEN
        elif np.argmax(result)==4:
            return COCA_COLA_2_L
        elif np.argmax(result)==5:
            return SIROK_PLAVLENIY_KOMO_PAPRIKASH
        elif np.argmax(result)==6:
            return GARLIK
        elif np.argmax(result)==7:
            return KENT_8
        elif np.argmax(result)==8:
            return TEA_MINUTKA_40_BAGS
        elif np.argmax(result) == 9:
            return SUN_OIL_SHEDRIY_DAR_RAFINIR_580_GR
        elif np.argmax(result) == 10:
            return ONION
        elif np.argmax(result) == 11:
            return FAIRY_LIMON_500_GR
        elif np.argmax(result) == 12:
            return APPLE_BLACK_PRINCE
        elif np.argmax(result) == 13:
            return MUSTARD_KOLOS
        elif np.argmax(result) == 14:
            return SMETANA_STOLICA_SMAKY_20PER_400_GR
        elif np.argmax(result) == 15:
            return LEMON
        elif np.argmax(result) ==16:
            return SUN_OIL_OLEYNA_NERAF_850_GR
        elif np.argmax(result) == 17:
            return BEER_LVIVSKE_SVITLE_2_4_L
        elif np.argmax(result) == 18:
            return SHAVING_FOAM_ARKO_COOL_200_MLG
        elif np.argmax(result) == 19:
            return SHAVING_FOAM_ARKO_SENSITIVE_200_MLG
        elif np.argmax(result)==20:
            return CARROT
        elif np.argmax(result) ==21:
            return DROJJI_HARKOV_100_GR
        elif np.argmax(result) == 22:
            return EGGS
        elif np.argmax(result) == 23:
            return DESODORANT_GARNIER_MAGNIY_MEN
        elif np.argmax(result) == 24:
            return CABBAGE
        elif np.argmax(result)==25:
            return MARLBORO_RED
        elif np.argmax(result) == 26:
            return MAYONES_DETSKIY_SHEDRO_67
        elif np.argmax(result) == 27:
            return DESODORANT_REXONA_ALOE_VERA_WOMEN
        elif np.argmax(result) == 28:
            return SMETANA_STOLICA_SMAKY_15_400_GR
        elif np.argmax(result) == 29:
            return TEA_MONOMAH_KENYA_BLACK_90_GR
        elif np.argmax(result) == 30:
            return TOILET_PAPER_KIEV_63_M
        elif np.argmax(result) == 31:
            return COFFEE_AROMA_GOLD_FREEZE_FRIED_70_GR
        elif np.argmax(result) == 32:
            return MUSTARD_VERES_UKRAINSKA_MICNA_120_GR
        elif np.argmax(result) == 33:
            return TEA_MONOMAH_100_CEYLON_ORIGINAL_BLACK_KRUPNOLIST
        elif np.argmax(result) == 34:
            return DESODORANT_GARNIER_VESENNYA_SVEJEST
        elif np.argmax(result) == 35:
            return APPLE_GALA
        elif np.argmax(result) == 36:
            return DESODORANT_GARNIER_VESENNYA_SVEJEST
        elif np.argmax(result) == 37:
            return SMETANA_GALICHANSKAYA_15_370_GR
        elif np.argmax(result) == 38:
            return CHIPS_SALT_BIG_PACK_30_GR
        elif np.argmax(result) == 39:
            return SPRITE_2L
        elif np.argmax(result) == 40:
            return FANTA_2L
        elif np.argmax(result) == 41:
            return BOND_STREET_BLUE_SELECTION
        elif np.argmax(result) == 42:
            return CAMEL_BLUE
        elif np.argmax(result) == 43:
            return LD_RED
        elif np.argmax(result) == 44:
            return MARLBORO_GOLD
        elif np.argmax(result) == 45:
            return ROTHMANS_DEMI_BLUE_EXCLUSIVE
        elif np.argmax(result) == 46:
            return ROTHMANS_DEMI_CLICK_PURPLE
        elif np.argmax(result) == 47:
            return WINSTON_CASTER
        elif np.argmax(result) == 48:
            return PARLAMENT_AQUA_BLUE
        elif np.argmax(result) == 49:
            return WINSTON_BLUE
        elif np.argmax(result) == 50:
            return BOND_STREET_RED_SELECTION
        elif np.argmax(result) == 51:
            return LD_BLUE
        elif np.argmax(result) == 52:
            return KENT_SILVER
        elif np.argmax(result) == 53:
            return KENT_NAVY_BLUE_NEW
        elif np.argmax(result) == 54:
            return BEER_CHERNIGOVSKOE_SVITLE_05_L_GLASS
        elif np.argmax(result) == 55:
            return BEER_STELLA_ARTOIS_05_L_GLASS
        elif np.argmax(result) == 56:
            return BEER_OBOLON_SVITLE_05_L_GLASS
        elif np.argmax(result) == 57:
            return BEER_JIGULIVSKE_SVITLE_05_L_GLASS
        elif np.argmax(result) == 58:
            return BEER_ROGAN_TRADICIYNE_SVITLE_05_L_GLASS
        elif np.argmax(result) == 59:
            return BEER_CORONA_EXTRA_SVITLE_033_L_GLASS
        elif np.argmax(result) == 60:
            return BEER_CHERNIGIVSKE_BILE_NEFILTER_05_L_GLASS
        elif np.argmax(result) == 61:
            return BEER_YANTAR_SVITLE_05_L_GLASS
        elif np.argmax(result) == 62:
            return BEER_ZIBERT_SVITLE_05_L_GLASS
        elif np.argmax(result) == 63:
            return BEER_ARSENAL_MICNE_05_L_GLASS
        elif np.argmax(result) == 64:
            return BEER_PPB_ZAKARPATSKE_05_L_GLASS
        elif np.argmax(result) == 65:
            return BEER_LVIVSKE_SVITLE_05_L_GLASS
        elif np.argmax(result) == 66:
            return BEER_LVIVSKE_1715_05_L_GLASS
        elif np.argmax(result) == 67:
            return BEER_ZLATA_PRAHA_SVITLE_05_L_GLASS
        elif np.argmax(result) == 68:
            return BEER_TUBORG_GREEN_05_L_GLASS
        elif np.argmax(result) == 69:
            return BEER_SLAVUTICH_ICE_MIX_LIME_05_L_GLASS
        elif np.argmax(result) == 70:
            return BEER_TETEREV_05_L_GLASS
        elif np.argmax(result) == 71:
            return BEER_KRUSOVICE_SVITLE_05_L_GLASS
        elif np.argmax(result) == 72:
            return BEER_HEINEKEN_SVITLE_05_L_GLASS
        elif np.argmax(result) == 73:
            return BEER_AMSTEL_SVITLE_05_L_GLASS
        elif np.argmax(result) == 74:
            return BEER_HIKE_PREMIUM_SVITLE_05_L_GLASS
        elif np.argmax(result) == 75:
            return BEER_BOCHKOVE_SVITLE_05_L_GLASS
        elif np.argmax(result) == 76:
            return BEER_KRONENBOURG_1664_BLANC_SVITLE_05_L_GLASS
        elif np.argmax(result) == 77:
            return BEER_OPILLYA_FIRMENNOE_SVITLE_05_L_GLASS
        elif np.argmax(result) == 78:
            return BEER_YACHMENNIY_KOLOS_SVITLE_05_L_GLASS
        elif np.argmax(result) == 79:
            return BEER_OPILLYA_KORIFEY_SVITLE_05_L_GLASS
        elif np.argmax(result) == 80:
            return BEER_CHAYKA_DNIPROVSKAYA_05_L_GLASS
        elif np.argmax(result) == 81:
            return BEER_CHAYKA_CHERNOMORSKAYA_SVITLE_05_L_GLASS
        elif np.argmax(result) == 82:
            return BEER_UMAN_WAISSBURG_SVITLE_1_L
        elif np.argmax(result) == 83:
            return BEER_UMAN_PSHENICHNOE_SVITLE_1_L
        elif np.argmax(result) == 84:
            return BEER_BERDICHEVSKOE_HMELNOE_SVITLE_1_L
        elif np.argmax(result) == 85:
            return BEER_BERDICHEVSKOE_LAGER_SVITLE_1_L
        elif np.argmax(result) == 86:
            return BEER_OPILLYA_KORIFEY_11_L
        elif np.argmax(result) == 87:
            return BEER_OBOLON_JIGULIVSKE_EXPORTNE_15_L
        elif np.argmax(result) == 88:
            return BEER_YANTAR_SVITLE_12_L
        elif np.argmax(result) == 89:
            return BEER_JASHKOVSKOE_PSHENICHNOE_NEFILTER_1_L
        elif np.argmax(result) == 90:
            return BEER_JASHKOVSKOE_SVITLE_NEFILTER_1_L
        elif np.argmax(result) == 91:
            return BEER_JASHKOVSKOE_JIGULIVSKE_NEFILTER_1_L
        elif np.argmax(result) == 92:
            return BEER_PPB_BOCHKOVE_1_L
        elif np.argmax(result) == 93:
            return BEER_CHAYKA_DNIPROVSKAYA_1_L
        elif np.argmax(result) == 94:
            return KETCHUP_TORCHIN_CHESNOK_270_GR
        elif np.argmax(result) == 95:
            return MUKA_ZOLOTE_ZERNYATKO_PSHENICHNE_2_KG
        elif np.argmax(result) == 96:
            return MAYONES_KOROLIVSKIY_SMAK_KOROLIVSKIY_67_300_GR
        elif np.argmax(result) == 97:
            return BEER_CHERNIGOVSKOE_BELOE_NEFILTER_1_L
        elif np.argmax(result) == 98:
            return BEER_OBOLON_SVITLE_1_L
        elif np.argmax(result) == 99:
            return BEER_ROGAN_TRADICIYNE_SVITLE_1_L
        elif np.argmax(result) == 100:
            return SOUS_CHUMAK_CHESNOCHNIY_200_GR
        elif np.argmax(result) == 101:
            return ORBIT_POLYNICA_BANAN
        elif np.argmax(result) == 102:
            return LM_RED
        elif np.argmax(result) == 103:
            return BEER_JIGULIVSKE_SVITLE_2_L
        elif np.argmax(result) == 104:
            return BEER_CHAYKA_DNIPROVSKAYA_2_L
        elif np.argmax(result) == 105:
            return BEER_PIWNY_KEBEK_2_L
        elif np.argmax(result) == 106:
            return KETCHUP_TORCHIN_DO_SHASHLIKY_270_GR
        elif np.argmax(result) == 107:
            return MAYONES_CHUMAK_APPETITNIY_50_300_GR
        elif np.argmax(result) == 108:
            return KOLBASA_PERSHA_STOLICA_SALYAMI_FIRMENNAYA_VS
        elif np.argmax(result) == 109:
            return COFFEE_CHERNA_KARTA_GOLD_50_GR
        elif np.argmax(result) == 110:
            return BEER_ARSENAL_MICNE_SVITLE_2_L
        elif np.argmax(result) == 111:
            return BEER_PPB_BOCHKOVE_SVITLE_2_L
        elif np.argmax(result) == 112:
            return BEER_PPB_ZAKARPATSKE_ORIGINALNE_SVITLE_2_L
        elif np.argmax(result) == 113:
            return BEER_ZIBERT_SVITLE_05_L_JB
        elif np.argmax(result) == 114:
            return YOGURT_FANNI_240_GR_1_5_LESNIE_YAGODI
        elif np.argmax(result) == 115:
            return KEFIR_SLAVIYA_2_5_850_GR
        elif np.argmax(result) == 116:
            return BEER_OBOLON_KIEVSKOE_ROZLIVNOE_SVITLE_195_L
        elif np.argmax(result) == 117:
            return BEER_CHERNIGOVSKOE_LIGHT_SVITLE_2_L
        elif np.argmax(result) == 118:
            return BEER_OPILLYA_KORIFEY_2_L
        elif np.argmax(result) == 119:
            return BEER_YANTAR_SVITLE_2_L
        elif np.argmax(result) == 120:
            return BEER_TUBORG_GREEN_4_X_05_L
        elif np.argmax(result) == 121:
            return BEER_PPB_ZAKARPATSKE_4_X_05_L
        elif np.argmax(result) == 122:
            return BEER_PPB_BOCHKOVE_4_X_05_L
        elif np.argmax(result) == 123:
            return BEER_BUDWEISER_BUDVAR_SVITLE_05_L_GLASS
        elif np.argmax(result) == 124:
            return BEER_PILSNER_URQUELL_SVITLE_05_L_GLASS
        elif np.argmax(result) == 125:
            return BEER_ROBERT_DOMS_BELGIYSKIY_SVITLE_NEFILTER_05_L_GLASS
        elif np.argmax(result) == 126:
            return BEER_CHERNIGOVSKOE_SVITLE_05_L_JB
        elif np.argmax(result) == 127:
            return BEER_CHERNIGOVSKOE_BELOE_05_L_JB
        elif np.argmax(result) == 128:
            return BEER_VELKOPOPOVICKY_KOZEL_TEMNE_05_L_JB
        elif np.argmax(result) == 129:
            return BEER_EDELMEISTER_PILSNER_SVITLE_05_L_JB
        elif np.argmax(result) == 130:
            return BEER_FAXE_SVITLE_05_L_JB
        elif np.argmax(result) == 131:
            return BEER_LIVU_PILZENES_SVITLE_05_L_JB
        elif np.argmax(result) == 132:
            return BEER_VELKOPOPOVICKY_KOZEL_SVITLE_05_L_JB
        elif np.argmax(result) == 133:
            return BEER_OBOLON_BEERMIX_LIMON_05_L_JB
        elif np.argmax(result) == 134:
            return BEER_EDELMEISTER_WEIZENBIER_SVITLE_NEFILTER_05_L_JB
        elif np.argmax(result) == 135:
            return BEER_EDELMEISTER_SCHWARZBIER_TEMNE_05_L_JB
        elif np.argmax(result) == 136:
            return BEER_HIKE_BLANCHE_SVITLE_NEFILTER_05_L_JB
        elif np.argmax(result) == 137:
            return BEER_ZLATA_PRAHA_SVITLE_05_L_JB
        elif np.argmax(result) == 138:
            return BEER_THURINGER_PREMIUM_BEER_SVITLE_05_L_JB
        elif np.argmax(result) == 139:
            return BEER_LIVU_SENCU_SVITLE_05_L_JB
        elif np.argmax(result) == 140:
            return BEER_GERMANARICH_SVITLE_05_L_JB
        elif np.argmax(result) == 141:
            return BEER_HIKE_PREMIUM_SVITLE_05_L_JB
        elif np.argmax(result) == 142:
            return BEER_OBOLON_0_NONALCO_NEFILTER_SVITLE_05_L_JB
        elif np.argmax(result) == 143:
            return BEER_ZIBERT_BAVARSKOE_SVITLE_05_L_JB
        elif np.argmax(result) == 144:
            return BEER_BAVARIYA_LIQUID_APPLE_NONALCO_SVITLE_05_L_JB
        elif np.argmax(result) == 145:
            return BEER_HEINEKEN_SVITLE_05_L_JB
        elif np.argmax(result) == 146:
            return BEER_RYCHTAR_GRANT_11_SVITLE_05_L_JB
        elif np.argmax(result) == 147:
            return BEER_AMSTEL_SVITLE_05_L_JB
        elif np.argmax(result) == 148:
            return BEER_BAVARIA_SVITLE_05_L_JB
        elif np.argmax(result) == 149:
            return BEER_BAVARIA_SVITLE_NONALCO_05_L_JB
        elif np.argmax(result) == 150:
            return BEER_EDELBURG_LAGER_SVITLE_05_L_JB
        elif np.argmax(result) == 151:
            return BEER_DONNER_PILS_SVITLE_05_L_JB
        elif np.argmax(result) == 152:
            return BEER_DUTCH_WINDMILL_SVITLE_05_L_JB
        elif np.argmax(result) == 153:
            return BEER_EDELBURG_HEFEWEIZEN_SVITLE_NEFILTER_05_L_JB
        elif np.argmax(result) == 154:
            return BEER_EDELMEISTER_UNFILTERED_SVITLE_NEFILTER_05_L_JB
        elif np.argmax(result) == 155:
            return BEER_ESTRELLA_DAMM_BARCELONA_SVITLE_05_L_JB
        elif np.argmax(result) == 156:
            return BEER_HALNE_JASNE_PELNE_05_L_JB
        elif np.argmax(result) == 157:
            return BEER_EUROTOUR_HEFEWEISSBIER_SVITLE_05_L_JB
        elif np.argmax(result) == 158:
            return BEER_HOLLANDIA_STRONG_SVITLE_05_L_JB
        elif np.argmax(result) == 159:
            return BEER_LANDER_BRAU_PREMIUM_SVITLE_05_L_JB
        elif np.argmax(result) == 160:
            return BEER_SAKU_KULD_05_L_JB
        elif np.argmax(result) == 161:
            return BEER_SAKU_ORIGINAAL_05_L_JB
        elif np.argmax(result) == 162:
            return BEER_STANGEN_LAGER_SVITLE_05_L_JB
        elif np.argmax(result) == 163:
            return BEER_VAN_PUR_PREMIUM_SVITLE_05_L_JB
        elif np.argmax(result) == 164:
            return BEER_BAVARIA_MANGO_MARAKUYA_SVITLE_NONALCO_05_L_JB
        elif np.argmax(result) == 165:
            return BEER_BAVARIA_GRANAT_NONALCO_05_L_JB
        elif np.argmax(result) == 166:
            return BEER_OBOLON_BEERMIX_MALINA_SVITLE_05_L_JB
        elif np.argmax(result) == 167:
            return BEER_OBOLON_BEERMIX_VISHNYA_SPECIALNE_SVITLE_05_L_JB
        elif np.argmax(result) == 168:
            return BEER_LOMZA_SVITLE_05_L_JB
        elif np.argmax(result) == 169:
            return BEER_PADERBORNER_PILSENER_SVITLE_05_L_JB
        elif np.argmax(result) == 170:
            return BEER_PADERBORNER_EXPORT_SVITLE_05_L_JB
        elif np.argmax(result) == 171:
            return BEER_CLAUSTHALER_GRAPEFRUIT_NONALCO_05_L_JB
        elif np.argmax(result) == 172:
            return BEER_CLAUSTHALER_ORIGINAL_NONALCO_05_L_JB
        elif np.argmax(result) == 173:
            return BEER_CLAUSTHALER_LEMON_NONALCO_05_L_JB
        elif np.argmax(result) == 174:
            return BEER_FOREVER_ROCK_N_ROLL_SVITLE_NEFILTER_05_L_JB
        elif np.argmax(result) == 175:
            return BEER_FOREVER_BLACK_QUEEN_TEMNE_NEFILTER_05_L_JB
        elif np.argmax(result) == 176:
            return BEER_FOREVER_KITE_SAFARI_SVITLE_NEFILTER_05_L_JB
        elif np.argmax(result) == 177:
            return BEER_FOREVER_CRAZY_SVITLE_NEFILTER_05_L_JB
        elif np.argmax(result) == 178:
            return BEER_HIKE_LIGHT_SVITLE_05_L_JB
        elif np.argmax(result) == 179:
            return BEER_HIKE_ZERO_NONALCO_05_L_JB
        elif np.argmax(result) == 180:
            return BEER_HORN_DISEL_ICE_PILSNER_SVITLE_0568_L_JB
        elif np.argmax(result) == 181:
            return BEER_HORN_DISEL_ORIGINAL_0568_L_JB
        elif np.argmax(result) == 182:
            return BEER_HORN_DISEL_TRADITIONAL_SVITLE_0568_L_JB
        elif np.argmax(result) == 183:
            return BEER_HORN_PREMIUM_DIESEL_SVITLE_05_L_JB
        elif np.argmax(result) == 184:
            return BEER_KRUSOVICE_CERNE_TEMNE_05_L_JB
        elif np.argmax(result) == 185:
            return BEER_LANDER_BRAU_MICNE_05_L_JB
        elif np.argmax(result) == 186:
            return BEER_LANDER_BRAU_SVITLE_NEFILTER_05_L_JB
        elif np.argmax(result) == 187:
            return BEER_PADERBORNER_PILGER_SVITLE_NEFILTER_05_L_JB
        elif np.argmax(result) == 188:
            return BEER_PLATAN_JEDENACTKA_11_SVITLE_05_L_JB
        elif np.argmax(result) == 189:
            return BEER_PRAGA_SVITLE_05_L_JB
        elif np.argmax(result) == 190:
            return BEER_SAKU_ROCK_SVITLE_0568_L_JB
        elif np.argmax(result) == 191:
            return BEER_SITNAN_SVITLE_05_L_JB
        elif np.argmax(result) == 192:
            return BEER_VIENAS_PREMIUM_GOLDEN_SVITLE_0568_L_JB
        elif np.argmax(result) == 193:
            return BEER_VIENAS_PREMIUM_TRADITIONAL_SVITLE_0568_L_JB
        elif np.argmax(result) == 194:
            return BEER_VLYNSKI_BROWAR_FOREVER_SWEET_WIT_SVITLE_NEFILTER_05_L_JB
        elif np.argmax(result) == 195:
            return BEER_ZAHRINGER_PREMIUM_SVITLE_05_L_JB
        elif np.argmax(result) == 196:
            return BEER_ZAHRINGER_HEFEWEIZEN_SVITLE_05_L_JB
        elif np.argmax(result) == 197:
            return BEER_JASHKOVSKOE_SVITLE_NEFILTER_05_L_JB
        elif np.argmax(result) == 198:
            return BEER_OBOLON_SVITLE_05_L_JB
        elif np.argmax(result) == 199:
            return BEER_PUBSTER_SVITLE_05_L_JB
        elif np.argmax(result) == 200:
            return BEER_CHAYKA_CHERNOMORSKAYA_SVITLE_05_L_JB
        elif np.argmax(result) == 201:
            return BEER_PPB_ZAKARPATSKE_ORIGINALNE_SVITLE_05_L_JB
        elif np.argmax(result) == 202:
            return BEER_PPB_BOCHKOVE_NEFILTER_05_L_JB
        elif np.argmax(result) == 203:
            return BEER_PPB_NEFILTROVANE_SVITLE_NONALCO_05_L_JB
        elif np.argmax(result) == 204:
            return BEER_PPB_LIMON_LIME_NONALCO_NEFILTER_05_L_JB
        elif np.argmax(result) == 205:
            return BEER_CHAYKA_DNIPROVSKAYA_05_L_JB
        elif np.argmax(result) == 206:
            return BEER_BROK_EXPORT_SVITLE_05_L_JB
        elif np.argmax(result) == 207:
            return BEER_CARLING_SVITLE_05_L_JB
        elif np.argmax(result) == 208:
            return BEER_KETEN_BRUG_BLANCHE_ELEGANT_05_L_JB
        elif np.argmax(result) == 209:
            return BEER_BUDWEISER_NONALCO_05_L_JB
        elif np.argmax(result) == 210:
            return BEER_FELDSCHLOSSCHEN_WHEAT_BEER_SVITLE_NEFILTER_05_L_JB
        elif np.argmax(result) == 211:
            return BEER_TETERIV_HMILNA_VISHNYA_NAPIVTEMNE_05_L_JB
        elif np.argmax(result) == 212:
            return BEER_GROTWERG_SVITLE_NONALCO_05_L_JB
        elif np.argmax(result) == 213:
            return BEER_HOLLAND_IMPORT_SVITLE_05_L_JB
        elif np.argmax(result) == 214:
            return BEER_GOLDEN_CASTLE_EXPORT_SVITLE_05_L_JB
        elif np.argmax(result) == 215:
            return BEER_5_0_ORIGINAL_CRAFT_BEER_SVITLE_NEFILTER_05_L_JB
        elif np.argmax(result) == 216:
            return BEER_GUINESS_DRAUGHT_TEMNE_044_L_JB
        elif np.argmax(result) == 217:
            return BEER_GRIMBERGEN_DOUBLE_AMBREE_NAPIVTEMNE_05_L_JB
        elif np.argmax(result) == 218:
            return BEER_WARSTEINER_PREMIUM_VERUM_SVITLE_05_L_JB
        elif np.argmax(result) == 219:
            return BEER_DAB_TEMNE_05_L_JB
        elif np.argmax(result) == 220:
            return BEER_GRIMBERGEN_BLANCHE_SVITLE_05_L_JB
        elif np.argmax(result) == 221:
            return BEER_KLOSTERKELLER_WEISSBIER_CHINA_SVITLE_NEFILTER_05_L_JB
        elif np.argmax(result) == 222:
            return BEER_KARPACKIE_PILS_SVITLE_05_L_JB
        elif np.argmax(result) == 223:
            return BEER_5_0_ORIGINAL_PILLS_SVITLE_05_L_JB
        elif np.argmax(result) == 224:
            return BEER_5_0_ORIGINAL_LAGER_SVITLE_05_L_JB
        elif np.argmax(result) == 225:
            return BEER_5_0_ORIGINAL_WEISS_BEER_SVITLE__NEFILTER_05_L_JB
        elif np.argmax(result) == 226:
            return BEER_FAHNEN_BRAU_SVITLE_05_L_JB
        elif np.argmax(result) == 227:
            return BEER_GOSSER_LIGHT_SVITLE_05_L_JB
        elif np.argmax(result) == 228:
            return BEER_HOLLANDIA_IMPORT_SVITLE_033_L_JB
        elif np.argmax(result) == 229:
            return BEER_HOLSTEN_PILSENER_048_L_JB
        elif np.argmax(result) == 230:
            return BEER_OBOLON_PREMIUM_EXTRA_BREW_SVITLE_05_L_JB
        elif np.argmax(result) == 231:
            return BEER_LVIVSKE_SVITLE_048_L_JB
        elif np.argmax(result) == 232:
            return BEER_CARLSBERG_PREMIUM_PILSNER_SVITLE_05_L_JB
        elif np.argmax(result) == 233:
            return BEER_CARLSBERG_PILSNER_05_L_JB


