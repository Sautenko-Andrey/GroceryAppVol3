import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FBApp.settings")

import django
django.setup()

from django.core.management import call_command
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


import numpy as np

import keras
from tensorflow import keras

from keras.layers import Dense, Embedding, LSTM
from keras.optimizers import Adam
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences

from my_app.utils import make_list


class GroceryAppText:
    # опредедяем количество наиболее употребляемых слов в тексте запроса пользователя
    MAX_WORDS = 1000

    # определяем количество слов, к которому дуте приведен каждый запрос от пользователя
    MAX_LENGTH_TEXT = 10

    def __init__(self):
        '''Инициализация модели НС и ее подготовка к обучению'''

        self.model = keras.Sequential([
            Embedding(self.MAX_WORDS, 234, input_length=self.MAX_LENGTH_TEXT),
            LSTM(234, return_sequences=True),  # 128
            LSTM(100),  # 64
            Dense(234, activation='softmax')
        ])

        self.model.compile(optimizer=Adam(0.0001), loss='categorical_crossentropy',
                           metrics=['accuracy'])

    def training_NN(self):
        '''Метод обучения НС'''

        # загружаем подготовленные данные для обучения:
        TRAIN_DATA, TARGET_DATA, tokenizer = self.converted_data()

        # запускаем тренировку:
        history = self.model.fit(TRAIN_DATA, TARGET_DATA, epochs=30, batch_size=50)

        reverse_word_map = dict(map(reversed, self.converted_data()[2].word_index.items()))

        # сохраняем модель обученной НС:
        self.model.save('my_model_text')
        print('Обучение нейронной сети успешно завершено.')

        return history, reverse_word_map

    def add_new_item(self, path_tail: str):
        '''Функция для предвариетльной обработки обучающего текстового набора для НС'''

        # загрузка обучающего текста
        path = f'/home/andrey/grocery_data/ALL_TEXT_VARIANTS/{path_tail}'
        with open(path, 'r', encoding='utf-8') as f:
            item_text = f.readlines()
        # убираем первый невидимый символ
        item_text[0] = item_text[0].replace('\ufeff', '')
        return item_text

    def upload_data(self):
        """Функция загрузки обучающей выборки для каждой позиции товара"""

        # загрузка обучающего текста
        obolon_premium_extra_11_text = self.add_new_item('pivo_obolon_extra(1.1).txt')
        hetman_sagaydachniy_07_text = self.add_new_item('vodka_hetman(0.7).txt')
        coffee_aroma_gold_classic_100gr_text = self.add_new_item('coffee_aroma_gold_classic_100gr.txt')
        apple_golden_text = self.add_new_item('apple_golden.txt')
        coca_cola_2l_text = self.add_new_item('coca_cola.txt')
        KOMO_paprikash_text = self.add_new_item('furnaced_cheese_KOMO_paprikash.txt')
        garlik_text = self.add_new_item('garlik.txt')
        kent_8_text = self.add_new_item('kent_8.txt')
        tea_minutka_40_p_black_text = self.add_new_item('tea_minutka_40_packs_black.txt')
        oil_shedriy_dar_850_text = self.add_new_item('oil_shedriy_dar_850.txt')
        onion_text = self.add_new_item('onion.txt')
        fairy_text = self.add_new_item('fairy.txt')
        apple_black_prince_text = self.add_new_item('apple_black_prince.txt')
        gorchica_kolos_text = self.add_new_item('gorchica_kolos.txt')
        smetana_stolica_smaky_20_400_text = self.add_new_item('smetana_stolica_smaky_20jir_400g.txt')
        limon_text = self.add_new_item('limon.txt')
        oil_oleyna_neraf_850_text = self.add_new_item('oil_oleyna_neraf_850.txt')
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
        fanta_2l_text = self.add_new_item('fanta_2l.txt')
        bond_street_blue_selection_text=self.add_new_item('bond_street_blue_selection.txt')
        camel_blue_text=self.add_new_item('camel_blue.txt')
        LD_red_text=self.add_new_item('LD_red.txt')
        marlboro_gold_text=self.add_new_item('marlboro_gold.txt')
        rotmans_demi_blue_exclusive_text=self.add_new_item('rotmans_demi_blue_exclusive.txt')
        rotmans_demi_click_purple_text=self.add_new_item('rotmans_demi_click_purple.txt')
        winston_caster_text=self.add_new_item('winston_caster.txt')
        parlament_aqua_blue_text=self.add_new_item('parlament_aqua_blue.txt')
        winston_blue_text=self.add_new_item('winston_blue.txt')
        bond_street_red_selection_text=self.add_new_item('bond_street_red_selection.txt')
        LD_blue_text=self.add_new_item('LD_blue.txt')
        kent_silver_text=self.add_new_item('kent_silver.txt')
        kent_navy_blue_new_text=self.add_new_item('kent_navy_blue_new.txt')
        beer_chernigivske_svitle_05_l_glass_text=self.add_new_item('beer_chernigivske_svitle_05_l_glass.txt')
        beer_stella_artois_05_l_glass_text = self.add_new_item('beer_stella_artois_05_l_glass.txt')
        beer_obolon_svitle_05_l_glass_text=self.add_new_item('beer_obolon_svitle_05_l_glass.txt')
        beer_jigulivske_svitle_05_l_glass_text=self.add_new_item('beer_jigulivske_svitle_05_l_glass.txt')
        beer_rogan_tradiciyne_svitle_05_l_glass_text=self.add_new_item('beer_rogan_tradiciyne_svitle_05_l_glass.txt')
        beer_corona_extra_svitle_033_l_glass_text=self.add_new_item('beer_corona_extra_svitle_033_l_glass.txt')
        beer_chernigivske_bile_nefilter_05_l_glass_text=self.add_new_item('beer_chernigivske_bile_nefilter_05_l_glass.txt')
        beer_yantar_svitle_05_l_glass_text=self.add_new_item('beer_yantar_svitle_05_l_glass.txt')
        beer_zibert_svitle_05_l_glass_text=self.add_new_item('beer_zibert_svitle_05_l_glass.txt')
        beer_arsenal_micne_05_l_glass_text=self.add_new_item('beer_arsenal_micne_05_l_glass.txt')
        beer_persha_brovarnya_zakarpatske_05_l_glass_text=self.add_new_item('beer_persha_brovarnya_zakarpatske_05_l_glass.txt')
        beer_lvivske_svitle_05_l_glass_text=self.add_new_item('beer_lvivske_svitle_05_l_glass.txt')
        beer_lvivske_1715_05_l_glass_text=self.add_new_item('beer_lvivske_1715_05_l_glass.txt')
        beer_zlata_praha_svitle_05_l_glass_text=self.add_new_item('beer_zlata_praha_svitle_05_l_glass.txt')
        beer_tuborg_green_05_l_glass_text=self.add_new_item('beer_tuborg_green_05_l_glass.txt')
        beer_slavutich_ice_mix_lime_svitle_05_l_glass_text=self.add_new_item('beer_slavutich_ice_mix_lime_svitle_05_l_glass.txt')
        beer_teteriv_svitle_05_l_glass_text=self.add_new_item('beer_teteriv_svitle_05_l_glass.txt')
        beer_krusovice_svitle_05_l_glass_text=self.add_new_item('beer_krusovice_svitle_05_l_glass.txt')
        beer_heineken_svitle_05_l_glass_text=self.add_new_item('beer_heineken_svitle_05_l_glass.txt')
        beer_amstel_svitle_05_l_glass_text=self.add_new_item('beer_amstel_svitle_05_l_glass.txt')
        beer_hike_premium_svitle_05_l_glass_text=self.add_new_item('beer_hike_premium_svitle_05_l_glass.txt')
        beer_bochkove_svitle_05_l_glass_text=self.add_new_item('beer_bochkove_svitle_05_l_glass.txt')
        beer_kronenbourg_1664_blanc_046_l_glass_text=self.add_new_item('beer_kronenbourg_1664_blanc_046_l_glass.txt')
        beer_opilla_nepasterizovane_05_l_glass_text=self.add_new_item('beer_opilla_nepasterizovane_05_l_glass.txt')
        beer_yachminniy_kolos_svitle_05_l_glass_text=self.add_new_item('beer_yachminniy_kolos_svitle_05_l_glass.txt')
        beer_opilla_korifey_05_l_glass_text=self.add_new_item('beer_opilla_korifey_05_l_glass.txt')
        beer_chayka_dniprovska_svitle_05_l_glass_text=self.add_new_item('beer_chayka_dniprovska_svitle_05_l_glass.txt')
        beer_chayka_chernomorska_svitle_05_l_glass_text=self.add_new_item('beer_chayka_chernomorska_svitle_05_l_glass.txt')
        beer_uman_pivo_waissburg_svitle_1l_plastic_text=self.add_new_item('beer_uman_pivo_waissburg_svitle_1l_plastic.txt')
        beer_uman_pivo_pshenichnoe_svitle_1l_plastic_text=self.add_new_item('beer_uman_pivo_pshenichnoe_svitle_1l_plastic.txt')
        beer_berdichevske_hmilne_svitle_1l_plastic_text=self.add_new_item('beer_berdichevske_hmilne_svitle_1l_plastic.txt')
        beer_berdichevske_lager_svitle_1l_plastic_text=self.add_new_item('beer_berdichevske_lager_svitle_1l_plastic.txt')
        beer_opilla_korifey_svitle_11l_plastic_text=self.add_new_item('beer_opilla_korifey_svitle_11l_plastic.txt')
        beer_obolon_jigulivske_exportne_svitle_1l_plastic_text=self.add_new_item('beer_obolon_jigulivske_exportne_svitle_1l_plastic.txt')
        beer_yantar_svitle_12l_plastic_text=self.add_new_item('beer_yantar_svitle_12l_plastic.txt')
        beer_jashkivske_pshenichne_nefilter_1l_plastic_text=self.add_new_item('beer_jashkivske_pshenichne_nefilter_1l_plastic.txt')
        beer_jashkivske_svitle_nefilter_1l_plastic_text=self.add_new_item('beer_jashkivske_svitle_nefilter_1l_plastic.txt')
        beer_jashkivske_jigulivske_nefilter_1l_plastic_text=self.add_new_item('beer_jashkivske_jigulivske_nefilter_1l_plastic.txt')
        beer_persha_privatna_brovarnya_bochkove_svitle_1l_plastic_text=self.add_new_item('beer_persha_privatna_brovarnya_bochkove_svitle_1l_plastic.txt')
        beer_chayka_dniprovska_svitle_1l_plastic_text=self.add_new_item('beer_chayka_dniprovska_svitle_1l_plastic.txt')
        ketchup_torchin_chasnik_270gr_text=self.add_new_item('ketchup_torchin_chasnik_270gr.txt')
        muka_zolote_zernyatko_pshen_2kg_text=self.add_new_item('muka_zolote_zernyatko_pshen_2kg.txt')
        mayonez_korolivskiy_smak_kororlivskiy_67_300gr_text=self.add_new_item('mayonez_korolivskiy_smak_kororlivskiy_67_300gr.txt')
        beer_chernigivske_bile_nefilter_1l_plastic_text=self.add_new_item('beer_chernigivske_bile_nefilter_1l_plastic.txt')
        beer_obolon_svitle_1l_plastic_text=self.add_new_item('beer_obolon_svitle_1l_plastic.txt')
        beer_rogan_svitle_tradiciyne_1l_plastic_text=self.add_new_item('beer_rogan_svitle_tradiciyne_1l_plastic.txt')
        sous_chumak_chesnochniy_200gr_text=self.add_new_item('sous_chumak_chesnochniy_200gr.txt')
        jvachka_orbit_clubnika_banan_text=self.add_new_item('jvachka_orbit_clubnika_banan.txt')
        LM_red_text=self.add_new_item('LM_red.txt')
        beer_jigulivske_svitle_2_l_plastic_text=self.add_new_item('beer_jigulivske_svitle_2_l_plastic.txt')
        beer_chayka_dniprovska_svitle_2l_plastic_text=self.add_new_item('beer_chayka_dniprovska_svitle_2l_plastic.txt')
        beer_piwny_kubek_svitle_2l_plastic_text=self.add_new_item('beer_piwny_kubek_svitle_2l_plastic.txt')
        ketchup_torchin_do_shasliky_270gr_test=self.add_new_item('ketchup_torchin_do_shasliky_270gr.txt')
        mayonez_chumak_appetitniy_50_300gr_text=self.add_new_item('mayonez_chumak_appetitniy_50_300gr.txt')
        kolbasa_persha_stolica_salyami_firmennaya_vs_text=self.add_new_item('kolbasa_persha_stolica_salyami_firmennaya_vs.txt')
        coffee_chorna_karta_gold_50gr_text=self.add_new_item('coffee_chorna_karta_gold_50gr.txt')
        beer_arsenal_micne_svitle_2l_plastic_text=self.add_new_item('beer_arsenal_micne_svitle_2l_plastic.txt')
        beer_ppb_bochkove_svitle_2l_plastic_text=self.add_new_item('beer_ppb_bochkove_svitle_2l_plastic.txt')
        beer_ppb_zakarpatske_originalne_svitle_2l_plastic_text=self.add_new_item('beer_ppb_zakarpatske_originalne_svitle_2l_plastic.txt')
        beer_zibert_svitle_05_l_banochnoe_text=self.add_new_item('beer_zibert_svitle_05_l_banochnoe.txt')
        yogurt_fanni_1_5_240gr_v_banke_text=self.add_new_item('yogurt_fanni_1_5_240gr_v_banke.txt')
        kefir_slviya_2_5_850gr_v_pakete_text=self.add_new_item('kefir_slviya_2_5_850gr_v_pakete.txt')
        beer_obolon_kievske_rozlivne_svitle_195l_plastic_text=self.add_new_item('beer_obolon_kievske_rozlivne_svitle_195l_plastic.txt')
        beer_chernigivske_light_svitle_2l_plastic_text=self.add_new_item('beer_chernigivske_light_svitle_2l_plastic.txt')
        beer_opilla_korifey_svitle_2l_plastic_text=self.add_new_item('beer_opilla_korifey_svitle_2l_plastic.txt')
        beer_yantar_svitle_2l_plastic_text=self.add_new_item('beer_yantar_svitle_2l_plastic.txt')
        beer_tuborg_green_05_4_banki_2litra_text=self.add_new_item('beer_tuborg_green_05_4_banki_2litra.txt')
        beer_ppb_zakarpatske_svitle_05_4_banki_2litra_text=self.add_new_item('beer_ppb_zakarpatske_svitle_05_4_banki_2litra.txt')
        beer_ppb_bochkove_svitle_05_4_banki_2litra_text=self.add_new_item('beer_ppb_bochkove_svitle_05_4_banki_2litra.txt')
        beer_budweiser_budvar_05_l_glass_text=self.add_new_item('beer_budweiser_budvar_05_l_glass.txt')
        beer_pilsner_urquell_05_l_glass_text=self.add_new_item('beer_pilsner_urquell_05_l_glass.txt')
        beer_robert_doms_belgiyskiy_svitle_nefilter_05_l_glass_text=self.add_new_item('beer_robert_doms_belgiyskiy_svitle_nefilter_05_l_glass.txt')
        beer_chernigivske_svitle_05_l_jb_text=self.add_new_item('beer_chernigivske_svitle_05_l_jb.txt')
        beer_chernigivske_bile_nefilter_05_l_jb_text=self.add_new_item('beer_chernigivske_bile_nefilter_05_l_jb.txt')
        beer_velkopopovicky_kozel_temne_05_l_jb_text=self.add_new_item('beer_velkopopovicky_kozel_temne_05_l_jb.txt')
        beer_edelmeister_pilsner_svitle_05_l_jb_text=self.add_new_item('beer_edelmeister_pilsner_svitle_05_l_jb.txt')
        beer_faxe_svitle_05_l_jb_text=self.add_new_item('beer_faxe_svitle_05_l_jb.txt')
        beer_livu_pilzenes_svitle_05_l_jb_text=self.add_new_item('beer_livu_pilzenes_svitle_05_l_jb.txt')
        beer_velkopopovicky_kozel_svitle_05_l_jb_text=self.add_new_item('beer_velkopopovicky_kozel_svitle_05_l_jb.txt')
        beer_obolon_beermix_limon_05_l_jb_text=self.add_new_item('beer_obolon_beermix_limon_05_l_jb.txt')
        beer_edelmeister_weizenbier_nefilter_svitle_05_l_jb_text=self.add_new_item('beer_edelmeister_weizenbier_nefilter_svitle_05_l_jb.txt')
        beer_edelmeister_schwarzbier_temnoe_05_l_jb_text=self.add_new_item('beer_edelmeister_schwarzbier_temnoe_05_l_jb.txt')
        beer_hike_blanche_svitle_nefilter_05_l_jb_text=self.add_new_item('beer_hike_blanche_svitle_nefilter_05_l_jb.txt')
        beer_zlata_praha_svitle_05_l_jb_text=self.add_new_item('beer_zlata_praha_svitle_05_l_jb.txt')
        beer_thuringer_premium_beer_svitle_05_l_jb_text=self.add_new_item('beer_thuringer_premium_beer_svitle_05_l_jb.txt')
        beer_livu_sencu_svitle_05_l_jb_text=self.add_new_item('beer_livu_sencu_svitle_05_l_jb.txt')
        beer_germanarich_svitle_05_l_jb_text=self.add_new_item('beer_germanarich_svitle_05_l_jb.txt')
        beer_hike_premium_svitle_05_l_jb_text=self.add_new_item('beer_hike_premium_svitle_05_l_jb.txt')
        beer_obolon_nonalcohol_svitle_nefilter_05_l_jb_text=self.add_new_item('beer_obolon_nonalcohol_svitle_nefilter_05_l_jb.txt')
        beer_zibert_bavarske_svitle_05_l_jb_text=self.add_new_item('beer_zibert_bavarske_svitle_05_l_jb.txt')
        beer_bavaria_liquid_apple_nonalcohol_svitle_05_l_jb_text = self.add_new_item('beer_bavaria_liquid_apple_nonalcohol_svitle_05_l_jb.txt')
        beer_heineken_svitle_05_l_jb_text=self.add_new_item('beer_heineken_svitle_05_l_jb.txt')
        beer_rychtar_grunt_11_svitle_05_l_jb_text=self.add_new_item('beer_rychtar_grunt_11_svitle_05_l_jb.txt')
        beer_amstel_svitle_05_l_jb_text=self.add_new_item('beer_amstel_svitle_05_l_jb.txt')
        beer_bavaria_svitle_05_l_jb_text=self.add_new_item('beer_bavaria_svitle_05_l_jb.txt')
        beer_bavaria_svitle_nonalcohol_05_l_jb_text=self.add_new_item('beer_bavaria_svitle_nonalcohol_05_l_jb.txt')
        beer_edelburg_lager_svitle_05_l_jb_text=self.add_new_item('beer_edelburg_lager_svitle_05_l_jb.txt')
        beer_donner_pills_svitle_05_l_jb_text=self.add_new_item('beer_donner_pills_svitle_05_l_jb.txt')
        beer_dutch_windmill_svitle_05_l_jb_text=self.add_new_item('beer_dutch_windmill_svitle_05_l_jb.txt')
        beer_edelberg_hefeweizen_svitle_nefilter_05_l_jb_text=self.add_new_item('beer_edelberg_hefeweizen_svitle_nefilter_05_l_jb.txt')
        beer_edelmeister_unfiltered_svitle_nefilter_05_l_jb_text=self.add_new_item('beer_edelmeister_unfiltered_svitle_nefilter_05_l_jb.txt')
        beer_estrella_damm_barcelona_svitle_05_l_jb_text=self.add_new_item('beer_estrella_damm_barcelona_svitle_05_l_jb.txt')
        beer_halne_jasne_pelne_05_l_jb_text=self.add_new_item('beer_halne_jasne_pelne_05_l_jb.txt')
        beer_eurotour_hefeweissbier_svitle_05_l_jb_text=self.add_new_item('beer_eurotour_hefeweissbier_svitle_05_l_jb.txt')
        beer_hollandia_strong_svitle_05_l_jb_text=self.add_new_item('beer_hollandia_strong_svitle_05_l_jb.txt')
        beer_lander_brau_premium_svitle_05_l_jb_text=self.add_new_item('beer_lander_brau_premium_svitle_05_l_jb.txt')
        beer_saku_kuld_05_l_jb_text=self.add_new_item('beer_saku_kuld_05_l_jb.txt')
        beer_saku_original_05_l_jb_text = self.add_new_item('beer_saku_original_05_l_jb.txt')
        beer_stangen_lager_svitle_05_l_jb_text=self.add_new_item('beer_stangen_lager_svitle_05_l_jb.txt')
        beer_van_pur_premium_svitle_05_l_jb_text=self.add_new_item('beer_van_pur_premium_svitle_05_l_jb.txt')
        beer_bavaria_mango_marakya_bezalkogol_svitle_05_l_jb_text=self.add_new_item('beer_bavaria_mango_marakya_bezalkogol_svitle_05_l_jb.txt')
        beer_bavaria_granat_bezalkogol_svitle_05_l_jb_text=self.add_new_item('beer_bavaria_granat_bezalkogol_svitle_05_l_jb.txt')
        beer_obolon_beermix_malina_05_l_jb_text=self.add_new_item('beer_obolon_beermix_malina_05_l_jb.txt')
        beer_obolon_beermix_vishnya_05_l_jb_text=self.add_new_item('beer_obolon_beermix_vishnya_05_l_jb.txt')
        beer_lomza_svitle_05_l_jb_text=self.add_new_item('beer_lomza_svitle_05_l_jb.txt')
        beer_paderborner_pilsener_svitle_05_l_jb_text=self.add_new_item('beer_paderborner_pilsener_svitle_05_l_jb.txt')
        beer_paderborner_export_05_l_jb_text=self.add_new_item('beer_paderborner_export_05_l_jb.txt')
        beer_clausthaler_greipfruit_nonalcohol_05_l_jb_text=self.add_new_item('beer_clausthaler_greipfruit_nonalcohol_05_l_jb.txt')
        beer_clausthaler_original_nonalcohol_05_l_jb_text=self.add_new_item('beer_clausthaler_original_nonalcohol_05_l_jb.txt')
        beer_clausthaler_lemon_nonalcohol_05_l_jb_text=self.add_new_item('beer_clausthaler_lemon_nonalcohol_05_l_jb.txt')
        beer_forever_rock_n_roll_svitle_nefilter_05_l_jb_text=self.add_new_item('beer_forever_rock_n_roll_svitle_nefilter_05_l_jb.txt')
        beer_forever_black_queen_temne_nefilter_05_l_jb_text=self.add_new_item('beer_forever_black_queen_temne_nefilter_05_l_jb.txt')
        beer_forever_kite_safari_svitle_nefilter_05_l_jb_text=self.add_new_item('beer_forever_kite_safari_svitle_nefilter_05_l_jb.txt')
        beer_forever_crazy_svitle_nefilter_05_l_jb_text=self.add_new_item('beer_forever_crazy_svitle_nefilter_05_l_jb.txt')
        beer_hike_light_svitle_05_l_jb_text=self.add_new_item('beer_hike_light_svitle_05_l_jb.txt')
        beer_hike_zero_nonalcohol_05_l_jb_text=self.add_new_item('beer_hike_zero_nonalcohol_05_l_jb.txt')
        beer_horn_disel_ice_pilsner_svitle_0568_l_jb_text=self.add_new_item('beer_horn_disel_ice_pilsner_svitle_0568_l_jb.txt')
        beer_horn_original_svitle_0568_l_jb_text=self.add_new_item('beer_horn_original_svitle_0568_l_jb.txt')
        beer_horn_traditional_svitle_0568_l_jb_text=self.add_new_item('beer_horn_traditional_svitle_0568_l_jb.txt')
        beer_horn_premium_svitle_05_l_jb_text=self.add_new_item('beer_horn_premium_svitle_05_l_jb.txt')
        beer_krusovice_cerne_temne_05_l_jb_text=self.add_new_item('beer_krusovice_cerne_temne_05_l_jb.txt')
        beer_lander_brau_micne_05_l_jb_text=self.add_new_item('beer_lander_brau_micne_05_l_jb.txt')
        beer_lander_brau_svitle_nefilter_05_l_jb_text=self.add_new_item('beer_lander_brau_svitle_nefilter_05_l_jb.txt')
        beer_padeborner_pilger_nefilter_svitle_05_l_jb_text=self.add_new_item('beer_padeborner_pilger_nefilter_svitle_05_l_jb.txt')
        beer_platan_jedenactka_05_l_jb_text=self.add_new_item('beer_platan_jedenactka_05_l_jb.txt')
        beer_praga_svitle_05_l_jb_text=self.add_new_item('beer_praga_svitle_05_l_jb.txt')
        beer_saku_rock_svitle_0568_l_jb_text=self.add_new_item('beer_saku_rock_svitle_0568_l_jb.txt')
        beer_sitnan_svitle_05_l_jb_text=self.add_new_item('beer_sitnan_svitle_05_l_jb.txt')
        beer_vienas_premium_golden_svitle_05_l_jb_text=self.add_new_item('beer_vienas_premium_golden_svitle_05_l_jb.txt')
        beer_vienas_premium_traditional_svitle_05_l_jb_text=self.add_new_item('beer_vienas_premium_traditional_svitle_05_l_jb.txt')
        beer_volynski_browar_forever_sweet_wit_pshen_nefilter_svitle_05_l_jb_text=self.add_new_item('beer_volynski_browar_forever_sweet_wit_pshen_nefilter_svitle_05_l_jb.txt')
        beer_zahringer_premium_svitle_05_l_jb_text=self.add_new_item('beer_zahringer_premium_svitle_05_l_jb.txt')
        beer_zahringer_hefeweizen_svitle_05_l_jb_text=self.add_new_item('beer_zahringer_hefeweizen_svitle_05_l_jb.txt')
        beer_jajkivske_svitle__nefilter_05_l_jb_text=self.add_new_item('beer_jajkivske_svitle__nefilter_05_l_jb.txt')
        beer_obolon_svitle_05_l_jb_text=self.add_new_item('beer_obolon_svitle_05_l_jb.txt')
        beer_pubster_svitle_05_l_jb_text=self.add_new_item('beer_pubster_svitle_05_l_jb.txt')
        beer_chaika_chernomorskaya_05_l_jb_text=self.add_new_item('beer_chaika_chernomorskaya_05_l_jb.txt')
        beer_ppb_zakarpatske_orig_svitle_05_l_jb_text=self.add_new_item('beer_ppb_zakarpatske_orig_svitle_05_l_jb.txt')
        beer_ppb_bochkove_nefilter_05_l_jb_text=self.add_new_item('beer_ppb_bochkove_nefilter_05_l_jb.txt')
        beer_ppb_nefilter_svitle_nonalco_05_l_jb_text=self.add_new_item('beer_ppb_nefilter_svitle_nonalco_05_l_jb.txt')
        beer_ppb_limon_lime_nonalco_nefilter_05_l_jb_text=self.add_new_item('beer_ppb_limon_lime_nonalco_nefilter_05_l_jb.txt')
        beer_chaika_dniprovskaya_05_l_jb_text=self.add_new_item('beer_chaika_dniprovskaya_05_l_jb.txt')
        beer_brok_export_svitle_05_l_jb_text=self.add_new_item('beer_brok_export_svitle_05_l_jb.txt')
        beer_carling_svitle_05_l_jb_text=self.add_new_item('beer_carling_svitle_05_l_jb.txt')
        beer_keten_brug_blanche_elegant_nefilter_05_l_jb_text=self.add_new_item('beer_keten_brug_blanche_elegant_nefilter_05_l_jb.txt')
        beer_budweiser_nonalco_svitle_05_l_jb_text=self.add_new_item('beer_budweiser_nonalco_svitle_05_l_jb.txt')
        beer_feldschlosschen_wheat_beer_svitle05_l_jb_text=self.add_new_item('beer_feldschlosschen_wheat_beer_svitle05_l_jb.txt')
        beer_teteriv_hmilna_vishnya_polutemne_05_l_jb_text=self.add_new_item('beer_teteriv_hmilna_vishnya_polutemne_05_l_jb.txt')
        beer_grotwerg_svitle_nonalco_05_l_jb_text=self.add_new_item('beer_grotwerg_svitle_nonalco_05_l_jb.txt')
        beer_holland_import_svitle_05_l_jb_text = self.add_new_item('beer_holland_import_svitle_05_l_jb.txt')
        beer_golden_castle_export_svitle_05_l_jb_text=self.add_new_item('beer_golden_castle_export_svitle_05_l_jb.txt')
        beer_5_0_origin_craft_beer_nefilter_svitle_05_l_jb_text=self.add_new_item('beer_5_0_origin_craft_beer_nefilter_svitle_05_l_jb.txt')
        beer_guinness_draught_temne_044_l_jb_text=self.add_new_item('beer_guinness_draught_temne_044_l_jb.txt')
        beer_grimbergenDoubleAmbree_napivtemne_05_l_jb_text=self.add_new_item('beer_grimbergenDoubleAmbree_napivtemne_05_l_jb.txt')
        beer_warsteinerPremiumVerum_svitle_05_l_jb_text=self.add_new_item('beer_warsteinerPremiumVerum_svitle_05_l_jb.txt')
        beer_dab_temne_05_l_jb_text=self.add_new_item('beer_dab_temne_05_l_jb.txt')
        beer_grimbergenBlanche_svitle_05_l_jb_text=self.add_new_item('beer_grimbergenBlanche_svitle_05_l_jb.txt')
        beer_klosterkellerWeissbierChina_svitle_nefilter_05_l_jb_text=self.add_new_item('beer_klosterkellerWeissbierChina_svitle_nefilter_05_l_jb.txt')
        beer_karpackiePils_svitle_05_l_jb_text=self.add_new_item('beer_karpackiePils_svitle_05_l_jb.txt')
        beer_5_0_OriginalPills_svitle_05_l_jb_text=self.add_new_item('beer_5_0_OriginalPills_svitle_05_l_jb.txt')
        beer_5_0_Original_Lager_svitle_05_l_jb_text=self.add_new_item('beer_5_0_Original_Lager_svitle_05_l_jb.txt')
        beer_5_0_Original_Weiss_svitle_nefilter_05_l_jb_text = self.add_new_item('beer_5_0_Original_Weiss_svitle_nefilter_05_l_jb.txt')
        beer_fahnen_brau_svitle_05_l_jb_text=self.add_new_item('beer_fahnen_brau_svitle_05_l_jb.txt')
        beer_gosser_light_svitle_05_l_jb_text=self.add_new_item('beer_gosser_light_svitle_05_l_jb.txt')
        beer_holland_import_svitle_033_l_jb_text=self.add_new_item('beer_holland_import_svitle_033_l_jb.txt')
        beer_holsten_pilsener_048_l_jb_text=self.add_new_item('beer_holsten_pilsener_048_l_jb.txt')
        beer_obolon_premium_extra_brew_svitle_05_l_jb_text=self.add_new_item('beer_obolon_premium_extra_brew_svitle_05_l_jb.txt')
        beer_lvivske__svitle_048_l_jb_text=self.add_new_item('beer_lvivske__svitle_048_l_jb.txt')
        beer_carlsberg_premium_pilsner_05_l_jb_text=self.add_new_item('beer_carlsberg_premium_pilsner_05_l_jb.txt')
        beer_carlsberg_pilsner_05_l_jb_text=self.add_new_item('beer_carlsberg_pilsner_05_l_jb.txt')


        # объед. обучающие выборки:
        texts = obolon_premium_extra_11_text + hetman_sagaydachniy_07_text \
                + coffee_aroma_gold_classic_100gr_text + apple_golden_text \
                + coca_cola_2l_text + KOMO_paprikash_text + garlik_text \
                + kent_8_text + tea_minutka_40_p_black_text + oil_shedriy_dar_850_text \
                + onion_text + fairy_text + apple_black_prince_text + gorchica_kolos_text \
                + smetana_stolica_smaky_20_400_text + limon_text + oil_oleyna_neraf_850_text \
                + pivo_lvivske_svitle_24l_text + pena_arko_cool_200_100_text \
                + pena_arko_sensitive_200_100_text + carrot_text + drojji_text + eggs_text \
                + desodorant_garnier_magniy_text + cabbage_text \
                + marlboro_red_text + mayonez_detsk_shedro_190_text \
                + rexona_aloe_vera_w_text + smetana_stolica_smaky_15jir_400gr_text \
                + tea_monomah_kenya_90_text + toilet_papir_text + coffee_aroma_gold_freeze_dried_70g_text \
                + gorchica_veres_ukrainska_micna_120g_text \
                + tea_monomah_100_ceylon_original_black_krupn_list_90g_text \
                + tea_monomah_ceylon_black_text + apple_gala_text \
                + desodorant_garnier_spring_spirit_text + smetana_galichanska_15_370gr_text \
                + chips_lays_with_salt_big_pack_text + sprite_2l_text + fanta_2l_text\
                + bond_street_blue_selection_text + camel_blue_text + LD_red_text\
                + marlboro_gold_text + rotmans_demi_blue_exclusive_text+rotmans_demi_click_purple_text\
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
                + beer_rogan_svitle_tradiciyne_1l_plastic_text + sous_chumak_chesnochniy_200gr_text\
                + jvachka_orbit_clubnika_banan_text + LM_red_text + beer_jigulivske_svitle_2_l_plastic_text\
                + beer_chayka_dniprovska_svitle_2l_plastic_text + beer_piwny_kubek_svitle_2l_plastic_text\
                + ketchup_torchin_do_shasliky_270gr_test + mayonez_chumak_appetitniy_50_300gr_text\
                + kolbasa_persha_stolica_salyami_firmennaya_vs_text + coffee_chorna_karta_gold_50gr_text\
                + beer_arsenal_micne_svitle_2l_plastic_text + beer_ppb_bochkove_svitle_2l_plastic_text\
                + beer_ppb_zakarpatske_originalne_svitle_2l_plastic_text + beer_zibert_svitle_05_l_banochnoe_text\
                + yogurt_fanni_1_5_240gr_v_banke_text + kefir_slviya_2_5_850gr_v_pakete_text\
                + beer_obolon_kievske_rozlivne_svitle_195l_plastic_text + beer_chernigivske_light_svitle_2l_plastic_text\
                + beer_opilla_korifey_svitle_2l_plastic_text + beer_yantar_svitle_2l_plastic_text + beer_tuborg_green_05_4_banki_2litra_text\
                + beer_ppb_zakarpatske_svitle_05_4_banki_2litra_text + beer_ppb_bochkove_svitle_05_4_banki_2litra_text\
                + beer_budweiser_budvar_05_l_glass_text + beer_pilsner_urquell_05_l_glass_text\
                + beer_robert_doms_belgiyskiy_svitle_nefilter_05_l_glass_text + beer_chernigivske_svitle_05_l_jb_text\
                + beer_chernigivske_bile_nefilter_05_l_jb_text + beer_velkopopovicky_kozel_temne_05_l_jb_text\
                + beer_edelmeister_pilsner_svitle_05_l_jb_text + beer_faxe_svitle_05_l_jb_text + beer_livu_pilzenes_svitle_05_l_jb_text\
                + beer_velkopopovicky_kozel_svitle_05_l_jb_text + beer_obolon_beermix_limon_05_l_jb_text\
                + beer_edelmeister_weizenbier_nefilter_svitle_05_l_jb_text + beer_edelmeister_schwarzbier_temnoe_05_l_jb_text\
                + beer_hike_blanche_svitle_nefilter_05_l_jb_text + beer_zlata_praha_svitle_05_l_jb_text\
                + beer_thuringer_premium_beer_svitle_05_l_jb_text + beer_livu_sencu_svitle_05_l_jb_text\
                + beer_germanarich_svitle_05_l_jb_text + beer_hike_premium_svitle_05_l_jb_text\
                + beer_obolon_nonalcohol_svitle_nefilter_05_l_jb_text + beer_zibert_bavarske_svitle_05_l_jb_text\
                + beer_bavaria_liquid_apple_nonalcohol_svitle_05_l_jb_text + beer_heineken_svitle_05_l_jb_text\
                + beer_rychtar_grunt_11_svitle_05_l_jb_text + beer_amstel_svitle_05_l_jb_text + beer_bavaria_svitle_05_l_jb_text\
                + beer_bavaria_svitle_nonalcohol_05_l_jb_text + beer_edelburg_lager_svitle_05_l_jb_text + beer_donner_pills_svitle_05_l_jb_text\
                + beer_dutch_windmill_svitle_05_l_jb_text + beer_edelberg_hefeweizen_svitle_nefilter_05_l_jb_text\
                + beer_edelmeister_unfiltered_svitle_nefilter_05_l_jb_text + beer_estrella_damm_barcelona_svitle_05_l_jb_text\
                + beer_halne_jasne_pelne_05_l_jb_text + beer_eurotour_hefeweissbier_svitle_05_l_jb_text\
                +  beer_hollandia_strong_svitle_05_l_jb_text + beer_lander_brau_premium_svitle_05_l_jb_text + beer_saku_kuld_05_l_jb_text\
                + beer_saku_original_05_l_jb_text + beer_stangen_lager_svitle_05_l_jb_text + beer_van_pur_premium_svitle_05_l_jb_text\
                + beer_bavaria_mango_marakya_bezalkogol_svitle_05_l_jb_text + beer_bavaria_granat_bezalkogol_svitle_05_l_jb_text\
                + beer_obolon_beermix_malina_05_l_jb_text + beer_obolon_beermix_vishnya_05_l_jb_text + beer_lomza_svitle_05_l_jb_text\
                + beer_paderborner_pilsener_svitle_05_l_jb_text + beer_paderborner_export_05_l_jb_text + beer_clausthaler_greipfruit_nonalcohol_05_l_jb_text\
                + beer_clausthaler_original_nonalcohol_05_l_jb_text + beer_clausthaler_lemon_nonalcohol_05_l_jb_text\
                + beer_forever_rock_n_roll_svitle_nefilter_05_l_jb_text + beer_forever_black_queen_temne_nefilter_05_l_jb_text\
                + beer_forever_kite_safari_svitle_nefilter_05_l_jb_text + beer_forever_crazy_svitle_nefilter_05_l_jb_text\
                + beer_hike_light_svitle_05_l_jb_text + beer_hike_zero_nonalcohol_05_l_jb_text + beer_horn_disel_ice_pilsner_svitle_0568_l_jb_text\
                + beer_horn_original_svitle_0568_l_jb_text + beer_horn_traditional_svitle_0568_l_jb_text + beer_horn_premium_svitle_05_l_jb_text\
                + beer_krusovice_cerne_temne_05_l_jb_text + beer_lander_brau_micne_05_l_jb_text + beer_lander_brau_svitle_nefilter_05_l_jb_text\
                + beer_padeborner_pilger_nefilter_svitle_05_l_jb_text + beer_platan_jedenactka_05_l_jb_text + beer_praga_svitle_05_l_jb_text\
                + beer_saku_rock_svitle_0568_l_jb_text + beer_sitnan_svitle_05_l_jb_text + beer_vienas_premium_golden_svitle_05_l_jb_text\
                + beer_vienas_premium_traditional_svitle_05_l_jb_text + beer_volynski_browar_forever_sweet_wit_pshen_nefilter_svitle_05_l_jb_text\
                + beer_zahringer_premium_svitle_05_l_jb_text + beer_zahringer_hefeweizen_svitle_05_l_jb_text + beer_jajkivske_svitle__nefilter_05_l_jb_text\
                + beer_obolon_svitle_05_l_jb_text + beer_pubster_svitle_05_l_jb_text + beer_chaika_chernomorskaya_05_l_jb_text\
                + beer_ppb_zakarpatske_orig_svitle_05_l_jb_text + beer_ppb_bochkove_nefilter_05_l_jb_text + beer_ppb_nefilter_svitle_nonalco_05_l_jb_text\
                + beer_ppb_limon_lime_nonalco_nefilter_05_l_jb_text + beer_chaika_dniprovskaya_05_l_jb_text + beer_brok_export_svitle_05_l_jb_text\
                + beer_carling_svitle_05_l_jb_text + beer_keten_brug_blanche_elegant_nefilter_05_l_jb_text + beer_budweiser_nonalco_svitle_05_l_jb_text\
                + beer_feldschlosschen_wheat_beer_svitle05_l_jb_text + beer_teteriv_hmilna_vishnya_polutemne_05_l_jb_text\
                + beer_grotwerg_svitle_nonalco_05_l_jb_text + beer_holland_import_svitle_05_l_jb_text + beer_golden_castle_export_svitle_05_l_jb_text\
                + beer_5_0_origin_craft_beer_nefilter_svitle_05_l_jb_text + beer_guinness_draught_temne_044_l_jb_text + beer_grimbergenDoubleAmbree_napivtemne_05_l_jb_text\
                + beer_warsteinerPremiumVerum_svitle_05_l_jb_text + beer_dab_temne_05_l_jb_text + beer_grimbergenBlanche_svitle_05_l_jb_text\
                + beer_klosterkellerWeissbierChina_svitle_nefilter_05_l_jb_text + beer_karpackiePils_svitle_05_l_jb_text\
                + beer_5_0_OriginalPills_svitle_05_l_jb_text + beer_5_0_Original_Lager_svitle_05_l_jb_text + beer_5_0_Original_Weiss_svitle_nefilter_05_l_jb_text\
                + beer_fahnen_brau_svitle_05_l_jb_text + beer_gosser_light_svitle_05_l_jb_text + beer_holland_import_svitle_033_l_jb_text\
                + beer_holsten_pilsener_048_l_jb_text + beer_obolon_premium_extra_brew_svitle_05_l_jb_text + beer_lvivske__svitle_048_l_jb_text\
                + beer_carlsberg_premium_pilsner_05_l_jb_text + beer_carlsberg_pilsner_05_l_jb_text

        # подсчитываем кол-во выборок
        count_obolon_premium_extra_11_text = len(obolon_premium_extra_11_text)
        count_hetman_sagaydachniy_07_text = len(hetman_sagaydachniy_07_text)
        count_coffee_aroma_gold_classic_100gr_text = len(coffee_aroma_gold_classic_100gr_text)
        count_apple_golden_text = len(apple_golden_text)
        count_coca_cola_2l_text = len(coca_cola_2l_text)
        count_KOMO_paprikash_text = len(KOMO_paprikash_text)
        count_garlik_text = len(garlik_text)
        count_kent_8_text = len(kent_8_text)
        count_tea_minutka_40_p_black_text = len(tea_minutka_40_p_black_text)
        count_oil_shedriy_dar_850_text = len(oil_shedriy_dar_850_text)
        count_onion_text = len(onion_text)
        count_fairy_text = len(fairy_text)
        count_apple_black_prince_text = len(apple_black_prince_text)
        count_gorchica_kolos_text = len(gorchica_kolos_text)
        count_smetana_stolica_smaky_20_400_text = len(smetana_stolica_smaky_20_400_text)
        count_limon_text = len(limon_text)
        count_oil_oleyna_neraf_850_text = len(oil_oleyna_neraf_850_text)
        count_pivo_lvivske_svitle_24l_text = len(pivo_lvivske_svitle_24l_text)
        count_pena_arko_cool_200_100_text = len(pena_arko_cool_200_100_text)
        count_pena_arko_sensitive_200_100_text = len(pena_arko_sensitive_200_100_text)
        count_carrot_text = len(carrot_text)
        count_drojji_text = len(drojji_text)
        count_eggs_text = len(eggs_text)
        count_desodorant_garnier_magniy_text = len(desodorant_garnier_magniy_text)
        count_cabbage_text = len(cabbage_text)
        count_marlboro_red_text = len(marlboro_red_text)
        count_mayonez_detsk_shedro_190_text = len(mayonez_detsk_shedro_190_text)
        count_rexona_aloe_vera_w_text = len(rexona_aloe_vera_w_text)
        count_smetana_stolica_smaky_15jir_400gr_text = len(smetana_stolica_smaky_15jir_400gr_text)
        count_tea_monomah_kenya_90_text = len(tea_monomah_kenya_90_text)
        count_toilet_papir_text = len(toilet_papir_text)
        count_coffee_aroma_gold_freeze_dried_70g_text = len(coffee_aroma_gold_freeze_dried_70g_text)
        count_gorchica_veres_ukrainska_micna_120g_text = len(gorchica_veres_ukrainska_micna_120g_text)
        count_tea_monomah_100_ceylon_original_black_krupn_list_90g_text = len(tea_monomah_100_ceylon_original_black_krupn_list_90g_text)
        count_tea_monomah_ceylon_black_text = len(tea_monomah_ceylon_black_text)
        count_apple_gala_text = len(apple_gala_text)
        count_desodorant_garnier_spring_spirit_text = len(desodorant_garnier_spring_spirit_text)
        count_smetana_galichanska_15_370gr_text = len(smetana_galichanska_15_370gr_text)
        count_chips_lays_with_salt_big_pack_text = len(chips_lays_with_salt_big_pack_text)
        count_sprite_2l_text = len(sprite_2l_text)
        count_fanta_2l_text = len(fanta_2l_text)
        count_bond_street_blue_selection_text=len(bond_street_blue_selection_text)
        count_camel_blue_text=len(camel_blue_text)
        count_LD_red_text=len(LD_red_text)
        count_marlboro_gold_text=len(marlboro_gold_text)
        count_rotmans_demi_blue_exclusive_text=len(rotmans_demi_blue_exclusive_text)
        count_rotmans_demi_click_purple_text=len(rotmans_demi_click_purple_text)
        count_winston_caster_text=len(winston_caster_text)
        count_parlament_aqua_blue_text=len(parlament_aqua_blue_text)
        count_winston_blue_text=len(winston_blue_text)
        count_bond_street_red_selection_text=len(bond_street_red_selection_text)
        count_LD_blue_text=len(LD_blue_text)
        count_kent_silver_text=len(kent_silver_text)
        count_kent_navy_blue_new_text=len(kent_navy_blue_new_text)
        count_beer_chernigivske_svitle_05_l_glass_text=len(beer_chernigivske_svitle_05_l_glass_text)
        count_beer_stella_artois_05_l_glass_text=len(beer_stella_artois_05_l_glass_text)
        count_beer_obolon_svitle_05_l_glass_text=len(beer_obolon_svitle_05_l_glass_text)
        count_beer_jigulivske_svitle_05_l_glass_text=len(beer_jigulivske_svitle_05_l_glass_text)
        count_beer_rogan_tradiciyne_svitle_05_l_glass_text=len(beer_rogan_tradiciyne_svitle_05_l_glass_text)
        count_beer_corona_extra_svitle_033_l_glass_text=len(beer_corona_extra_svitle_033_l_glass_text)
        count_beer_chernigivske_bile_nefilter_05_l_glass_text=len(beer_chernigivske_bile_nefilter_05_l_glass_text)
        count_beer_yantar_svitle_05_l_glass_text=len(beer_yantar_svitle_05_l_glass_text)
        count_beer_zibert_svitle_05_l_glass_text=len(beer_zibert_svitle_05_l_glass_text)
        count_beer_arsenal_micne_05_l_glass_text=len(beer_arsenal_micne_05_l_glass_text)
        count_beer_persha_brovarnya_zakarpatske_05_l_glass_text=len(beer_persha_brovarnya_zakarpatske_05_l_glass_text)
        count_beer_lvivske_svitle_05_l_glass_text=len(beer_lvivske_svitle_05_l_glass_text)
        count_beer_lvivske_1715_05_l_glass_text=len(beer_lvivske_1715_05_l_glass_text)
        count_beer_zlata_praha_svitle_05_l_glass_text=len(beer_zlata_praha_svitle_05_l_glass_text)
        count_beer_tuborg_green_05_l_glass_text=len(beer_tuborg_green_05_l_glass_text)
        count_beer_slavutich_ice_mix_lime_svitle_05_l_glass_text=len(beer_slavutich_ice_mix_lime_svitle_05_l_glass_text)
        count_beer_teteriv_svitle_05_l_glass_text=len(beer_teteriv_svitle_05_l_glass_text)
        count_beer_krusovice_svitle_05_l_glass_text=len(beer_krusovice_svitle_05_l_glass_text)
        count_beer_heineken_svitle_05_l_glass_text=len(beer_heineken_svitle_05_l_glass_text)
        count_beer_amstel_svitle_05_l_glass_text=len(beer_amstel_svitle_05_l_glass_text)
        count_beer_hike_premium_svitle_05_l_glass_text=len(beer_hike_premium_svitle_05_l_glass_text)
        count_beer_bochkove_svitle_05_l_glass_text=len(beer_bochkove_svitle_05_l_glass_text)
        count_beer_kronenbourg_1664_blanc_046_l_glass_text=len(beer_kronenbourg_1664_blanc_046_l_glass_text)
        count_beer_opilla_nepasterizovane_05_l_glass_text=len(beer_opilla_nepasterizovane_05_l_glass_text)
        count_beer_yachminniy_kolos_svitle_05_l_glass_text=len(beer_yachminniy_kolos_svitle_05_l_glass_text)
        count_beer_opilla_korifey_05_l_glass_text=len(beer_opilla_korifey_05_l_glass_text)
        count_beer_chayka_dniprovska_svitle_05_l_glass_text=len(beer_chayka_dniprovska_svitle_05_l_glass_text)
        count_beer_chayka_chernomorska_svitle_05_l_glass_text=len(beer_chayka_chernomorska_svitle_05_l_glass_text)
        count_beer_uman_pivo_waissburg_svitle_1l_plastic_text=len(beer_uman_pivo_waissburg_svitle_1l_plastic_text)
        count_beer_uman_pivo_pshenichnoe_svitle_1l_plastic_text=len(beer_uman_pivo_pshenichnoe_svitle_1l_plastic_text)
        count_beer_berdichevske_hmilne_svitle_1l_plastic_text=len(beer_berdichevske_hmilne_svitle_1l_plastic_text)
        count_beer_berdichevske_lager_svitle_1l_plastic_text=len(beer_berdichevske_lager_svitle_1l_plastic_text)
        count_beer_opilla_korifey_svitle_11l_plastic_text=len(beer_opilla_korifey_svitle_11l_plastic_text)
        count_beer_obolon_jigulivske_exportne_svitle_1l_plastic_text=len(beer_obolon_jigulivske_exportne_svitle_1l_plastic_text)
        count_beer_yantar_svitle_12l_plastic_text=len(beer_yantar_svitle_12l_plastic_text)
        count_beer_jashkivske_pshenichne_nefilter_1l_plastic_text=len(beer_jashkivske_pshenichne_nefilter_1l_plastic_text)
        count_beer_jashkivske_svitle_nefilter_1l_plastic_text=len(beer_jashkivske_svitle_nefilter_1l_plastic_text)
        count_beer_jashkivske_jigulivske_nefilter_1l_plastic_text=len(beer_jashkivske_jigulivske_nefilter_1l_plastic_text)
        count_beer_persha_privatna_brovarnya_bochkove_svitle_1l_plastic_text=len(beer_persha_privatna_brovarnya_bochkove_svitle_1l_plastic_text)
        count_beer_chayka_dniprovska_svitle_1l_plastic_text=len(beer_chayka_dniprovska_svitle_1l_plastic_text)
        count_ketchup_torchin_chasnik_270gr_text=len(ketchup_torchin_chasnik_270gr_text)
        count_muka_zolote_zernyatko_pshen_2kg_text=len(muka_zolote_zernyatko_pshen_2kg_text)
        count_mayonez_korolivskiy_smak_kororlivskiy_67_300gr_text=len(mayonez_korolivskiy_smak_kororlivskiy_67_300gr_text)
        count_beer_chernigivske_bile_nefilter_1l_plastic_text=len(beer_chernigivske_bile_nefilter_1l_plastic_text)
        count_beer_obolon_svitle_1l_plastic_text=len(beer_obolon_svitle_1l_plastic_text)
        count_beer_rogan_svitle_tradiciyne_1l_plastic_text=len(beer_rogan_svitle_tradiciyne_1l_plastic_text)
        count_sous_chumak_chesnochniy_200gr_text=len(sous_chumak_chesnochniy_200gr_text)
        count_jvachka_orbit_clubnika_banan_text=len(jvachka_orbit_clubnika_banan_text)
        count_LM_red_text=len(LM_red_text)
        count_beer_jigulivske_svitle_2_l_plastic_text=len(beer_jigulivske_svitle_2_l_plastic_text)
        count_beer_chayka_dniprovska_svitle_2l_plastic_text=len(beer_chayka_dniprovska_svitle_2l_plastic_text)
        count_beer_piwny_kubek_svitle_2l_plastic_text=len(beer_piwny_kubek_svitle_2l_plastic_text)
        count_ketchup_torchin_do_shasliky_270gr_test=len(ketchup_torchin_do_shasliky_270gr_test)
        count_mayonez_chumak_appetitniy_50_300gr_text=len(mayonez_chumak_appetitniy_50_300gr_text)
        count_kolbasa_persha_stolica_salyami_firmennaya_vs_text=len(kolbasa_persha_stolica_salyami_firmennaya_vs_text)
        count_coffee_chorna_karta_gold_50gr_text=len(coffee_chorna_karta_gold_50gr_text)
        count_beer_arsenal_micne_svitle_2l_plastic_text=len(beer_arsenal_micne_svitle_2l_plastic_text)
        count_beer_ppb_bochkove_svitle_2l_plastic_text=len(beer_ppb_bochkove_svitle_2l_plastic_text)
        count_beer_ppb_zakarpatske_originalne_svitle_2l_plastic_text=len(beer_ppb_zakarpatske_originalne_svitle_2l_plastic_text)
        count_beer_zibert_svitle_05_l_banochnoe_text=len(beer_zibert_svitle_05_l_banochnoe_text)
        count_yogurt_fanni_1_5_240gr_v_banke_text=len(yogurt_fanni_1_5_240gr_v_banke_text)
        count_kefir_slviya_2_5_850gr_v_pakete_text=len(kefir_slviya_2_5_850gr_v_pakete_text)
        count_beer_obolon_kievske_rozlivne_svitle_195l_plastic_text=len(beer_obolon_kievske_rozlivne_svitle_195l_plastic_text)
        count_beer_chernigivske_light_svitle_2l_plastic_text=len(beer_chernigivske_light_svitle_2l_plastic_text)
        count_beer_opilla_korifey_svitle_2l_plastic_text=len(beer_opilla_korifey_svitle_2l_plastic_text)
        count_beer_yantar_svitle_2l_plastic_text=len(beer_yantar_svitle_2l_plastic_text)
        count_beer_tuborg_green_05_4_banki_2litra_text=len(beer_tuborg_green_05_4_banki_2litra_text)
        count_beer_ppb_zakarpatske_svitle_05_4_banki_2litra_text=len(beer_ppb_zakarpatske_svitle_05_4_banki_2litra_text)
        count_beer_ppb_bochkove_svitle_05_4_banki_2litra_text=len(beer_ppb_bochkove_svitle_05_4_banki_2litra_text)
        count_beer_budweiser_budvar_05_l_glass_text=len(beer_budweiser_budvar_05_l_glass_text)
        count_beer_pilsner_urquell_05_l_glass_text=len(beer_pilsner_urquell_05_l_glass_text)
        count_beer_robert_doms_belgiyskiy_svitle_nefilter_05_l_glass_text=len(beer_robert_doms_belgiyskiy_svitle_nefilter_05_l_glass_text)
        count_beer_chernigivske_svitle_05_l_jb_text=len(beer_chernigivske_svitle_05_l_jb_text)
        count_beer_chernigivske_bile_nefilter_05_l_jb_text=len(beer_chernigivske_bile_nefilter_05_l_jb_text)
        count_beer_velkopopovicky_kozel_temne_05_l_jb_text=len(beer_velkopopovicky_kozel_temne_05_l_jb_text)
        count_beer_edelmeister_pilsner_svitle_05_l_jb_text=len(beer_edelmeister_pilsner_svitle_05_l_jb_text)
        count_beer_faxe_svitle_05_l_jb_text=len(beer_faxe_svitle_05_l_jb_text)
        count_beer_livu_pilzenes_svitle_05_l_jb_text=len(beer_livu_pilzenes_svitle_05_l_jb_text)
        count_beer_velkopopovicky_kozel_svitle_05_l_jb_text=len(beer_velkopopovicky_kozel_svitle_05_l_jb_text)
        count_beer_obolon_beermix_limon_05_l_jb_text=len(beer_obolon_beermix_limon_05_l_jb_text)
        count_beer_edelmeister_weizenbier_nefilter_svitle_05_l_jb_text=len(beer_edelmeister_weizenbier_nefilter_svitle_05_l_jb_text)
        count_beer_edelmeister_schwarzbier_temnoe_05_l_jb_text=len(beer_edelmeister_schwarzbier_temnoe_05_l_jb_text)
        count_beer_hike_blanche_svitle_nefilter_05_l_jb_text=len(beer_hike_blanche_svitle_nefilter_05_l_jb_text)
        count_beer_zlata_praha_svitle_05_l_jb_text=len(beer_zlata_praha_svitle_05_l_jb_text)
        count_beer_thuringer_premium_beer_svitle_05_l_jb_text=len(beer_thuringer_premium_beer_svitle_05_l_jb_text)
        count_beer_livu_sencu_svitle_05_l_jb_text=len(beer_livu_sencu_svitle_05_l_jb_text)
        count_beer_germanarich_svitle_05_l_jb_text=len(beer_germanarich_svitle_05_l_jb_text)
        count_beer_hike_premium_svitle_05_l_jb_text=len(beer_hike_premium_svitle_05_l_jb_text)
        count_beer_obolon_nonalcohol_svitle_nefilter_05_l_jb_text=len(beer_obolon_nonalcohol_svitle_nefilter_05_l_jb_text)
        count_beer_zibert_bavarske_svitle_05_l_jb_text=len(beer_zibert_bavarske_svitle_05_l_jb_text)
        count_beer_bavaria_liquid_apple_nonalcohol_svitle_05_l_jb_text=len(beer_bavaria_liquid_apple_nonalcohol_svitle_05_l_jb_text)
        count_beer_heineken_svitle_05_l_jb_text=len(beer_heineken_svitle_05_l_jb_text)
        count_beer_rychtar_grunt_11_svitle_05_l_jb_text=len(beer_rychtar_grunt_11_svitle_05_l_jb_text)
        count_beer_amstel_svitle_05_l_jb_text=len(beer_amstel_svitle_05_l_jb_text)
        count_beer_bavaria_svitle_05_l_jb_text=len(beer_bavaria_svitle_05_l_jb_text)
        count_beer_bavaria_svitle_nonalcohol_05_l_jb_text=len(beer_bavaria_svitle_nonalcohol_05_l_jb_text)
        count_beer_edelburg_lager_svitle_05_l_jb_text=len(beer_edelburg_lager_svitle_05_l_jb_text)
        count_beer_donner_pills_svitle_05_l_jb_text=len(beer_donner_pills_svitle_05_l_jb_text)
        count_beer_dutch_windmill_svitle_05_l_jb_text=len(beer_dutch_windmill_svitle_05_l_jb_text)
        count_beer_edelberg_hefeweizen_svitle_nefilter_05_l_jb_text=len(beer_edelberg_hefeweizen_svitle_nefilter_05_l_jb_text)
        count_beer_edelmeister_unfiltered_svitle_nefilter_05_l_jb_text=len(beer_edelmeister_unfiltered_svitle_nefilter_05_l_jb_text)
        count_beer_estrella_damm_barcelona_svitle_05_l_jb_text=len(beer_estrella_damm_barcelona_svitle_05_l_jb_text)
        count_beer_halne_jasne_pelne_05_l_jb_text=len(beer_halne_jasne_pelne_05_l_jb_text)
        count_beer_eurotour_hefeweissbier_svitle_05_l_jb_text=len(beer_eurotour_hefeweissbier_svitle_05_l_jb_text)
        count_beer_hollandia_strong_svitle_05_l_jb_text=len( beer_hollandia_strong_svitle_05_l_jb_text)
        count_beer_lander_brau_premium_svitle_05_l_jb_text=len(beer_lander_brau_premium_svitle_05_l_jb_text)
        count_beer_saku_kuld_05_l_jb_text=len(beer_saku_kuld_05_l_jb_text)
        count_beer_saku_original_05_l_jb_text=len(beer_saku_original_05_l_jb_text)
        count_beer_stangen_lager_svitle_05_l_jb_text=len(beer_stangen_lager_svitle_05_l_jb_text)
        count_beer_van_pur_premium_svitle_05_l_jb_text=len(beer_van_pur_premium_svitle_05_l_jb_text)
        count_beer_bavaria_mango_marakya_bezalkogol_svitle_05_l_jb_text=len(beer_bavaria_mango_marakya_bezalkogol_svitle_05_l_jb_text)
        count_beer_bavaria_granat_bezalkogol_svitle_05_l_jb_text=len(beer_bavaria_granat_bezalkogol_svitle_05_l_jb_text)
        count_beer_obolon_beermix_malina_05_l_jb_text=len(beer_obolon_beermix_malina_05_l_jb_text)
        count_beer_obolon_beermix_vishnya_05_l_jb_text=len(beer_obolon_beermix_vishnya_05_l_jb_text)
        count_beer_lomza_svitle_05_l_jb_text=len(beer_lomza_svitle_05_l_jb_text)
        count_beer_paderborner_pilsener_svitle_05_l_jb_text=len(beer_paderborner_pilsener_svitle_05_l_jb_text)
        count_beer_paderborner_export_05_l_jb_text=len(beer_paderborner_export_05_l_jb_text)
        count_beer_clausthaler_greipfruit_nonalcohol_05_l_jb_text=len(beer_clausthaler_greipfruit_nonalcohol_05_l_jb_text)
        count_beer_clausthaler_original_nonalcohol_05_l_jb_text=len(beer_clausthaler_original_nonalcohol_05_l_jb_text)
        count_beer_clausthaler_lemon_nonalcohol_05_l_jb_text=len(beer_clausthaler_lemon_nonalcohol_05_l_jb_text)
        count_beer_forever_rock_n_roll_svitle_nefilter_05_l_jb_text=len(beer_forever_rock_n_roll_svitle_nefilter_05_l_jb_text)
        count_beer_forever_black_queen_temne_nefilter_05_l_jb_text=len(beer_forever_black_queen_temne_nefilter_05_l_jb_text)
        count_beer_forever_kite_safari_svitle_nefilter_05_l_jb_text=len(beer_forever_kite_safari_svitle_nefilter_05_l_jb_text)
        count_beer_forever_crazy_svitle_nefilter_05_l_jb_text=len(beer_forever_crazy_svitle_nefilter_05_l_jb_text)
        count_beer_hike_light_svitle_05_l_jb_text=len(beer_hike_light_svitle_05_l_jb_text)
        count_beer_hike_zero_nonalcohol_05_l_jb_text=len(beer_hike_zero_nonalcohol_05_l_jb_text)
        count_beer_horn_disel_ice_pilsner_svitle_0568_l_jb_text=len(beer_horn_disel_ice_pilsner_svitle_0568_l_jb_text)
        count_beer_horn_original_svitle_0568_l_jb_text=len(beer_horn_original_svitle_0568_l_jb_text)
        count_beer_horn_traditional_svitle_0568_l_jb_text=len(beer_horn_traditional_svitle_0568_l_jb_text)
        count_beer_horn_premium_svitle_05_l_jb_text=len(beer_horn_premium_svitle_05_l_jb_text)
        count_beer_krusovice_cerne_temne_05_l_jb_text=len(beer_krusovice_cerne_temne_05_l_jb_text)
        count_beer_lander_brau_micne_05_l_jb_text=len(beer_lander_brau_micne_05_l_jb_text)
        count_beer_lander_brau_svitle_nefilter_05_l_jb_text=len(beer_lander_brau_svitle_nefilter_05_l_jb_text)
        count_beer_padeborner_pilger_nefilter_svitle_05_l_jb_text=len(beer_padeborner_pilger_nefilter_svitle_05_l_jb_text)
        count_beer_platan_jedenactka_05_l_jb_text=len(beer_platan_jedenactka_05_l_jb_text)
        count_beer_praga_svitle_05_l_jb_text=len(beer_praga_svitle_05_l_jb_text)
        count_beer_saku_rock_svitle_0568_l_jb_text=len(beer_saku_rock_svitle_0568_l_jb_text)
        count_beer_sitnan_svitle_05_l_jb_text=len(beer_sitnan_svitle_05_l_jb_text)
        count_beer_vienas_premium_golden_svitle_05_l_jb_text=len(beer_vienas_premium_golden_svitle_05_l_jb_text)
        count_beer_vienas_premium_traditional_svitle_05_l_jb_text=len(beer_vienas_premium_traditional_svitle_05_l_jb_text)
        count_beer_volynski_browar_forever_sweet_wit_pshen_nefilter_svitle_05_l_jb_text=len(beer_volynski_browar_forever_sweet_wit_pshen_nefilter_svitle_05_l_jb_text)
        count_beer_zahringer_premium_svitle_05_l_jb_text=len(beer_zahringer_premium_svitle_05_l_jb_text)
        count_beer_zahringer_hefeweizen_svitle_05_l_jb_text=len(beer_zahringer_hefeweizen_svitle_05_l_jb_text)
        count_beer_jajkivske_svitle__nefilter_05_l_jb_text=len(beer_jajkivske_svitle__nefilter_05_l_jb_text)
        count_beer_obolon_svitle_05_l_jb_text=len(beer_obolon_svitle_05_l_jb_text)
        count_beer_pubster_svitle_05_l_jb_text=len(beer_pubster_svitle_05_l_jb_text)
        count_beer_chaika_chernomorskaya_05_l_jb_text=len(beer_chaika_chernomorskaya_05_l_jb_text)
        count_beer_ppb_zakarpatske_orig_svitle_05_l_jb_text=len(beer_ppb_zakarpatske_orig_svitle_05_l_jb_text)
        count_beer_ppb_bochkove_nefilter_05_l_jb_text=len(beer_ppb_bochkove_nefilter_05_l_jb_text)
        count_beer_ppb_nefilter_svitle_nonalco_05_l_jb_text=len(beer_ppb_nefilter_svitle_nonalco_05_l_jb_text)
        count_beer_ppb_limon_lime_nonalco_nefilter_05_l_jb_text=len(beer_ppb_limon_lime_nonalco_nefilter_05_l_jb_text)
        count_beer_chaika_dniprovskaya_05_l_jb_text=len(beer_chaika_dniprovskaya_05_l_jb_text)
        count_beer_brok_export_svitle_05_l_jb_text=len(beer_brok_export_svitle_05_l_jb_text)
        count_beer_carling_svitle_05_l_jb_text=len(beer_carling_svitle_05_l_jb_text)
        count_beer_keten_brug_blanche_elegant_nefilter_05_l_jb_text=len(beer_keten_brug_blanche_elegant_nefilter_05_l_jb_text)
        count_beer_budweiser_nonalco_svitle_05_l_jb_text=len(beer_budweiser_nonalco_svitle_05_l_jb_text)
        count_beer_feldschlosschen_wheat_beer_svitle05_l_jb_text=len(beer_feldschlosschen_wheat_beer_svitle05_l_jb_text)
        count_beer_teteriv_hmilna_vishnya_polutemne_05_l_jb_text=len(beer_teteriv_hmilna_vishnya_polutemne_05_l_jb_text)
        count_beer_grotwerg_svitle_nonalco_05_l_jb_text=len(beer_grotwerg_svitle_nonalco_05_l_jb_text)
        count_beer_holland_import_svitle_05_l_jb_text=len(beer_holland_import_svitle_05_l_jb_text)
        count_beer_golden_castle_export_svitle_05_l_jb_text=len(beer_golden_castle_export_svitle_05_l_jb_text)
        count_beer_5_0_origin_craft_beer_nefilter_svitle_05_l_jb_text=len(beer_5_0_origin_craft_beer_nefilter_svitle_05_l_jb_text)
        count_beer_guinness_draught_temne_044_l_jb_text=len(beer_guinness_draught_temne_044_l_jb_text)
        count_beer_grimbergenDoubleAmbree_napivtemne_05_l_jb_text=len(beer_grimbergenDoubleAmbree_napivtemne_05_l_jb_text)
        count_beer_warsteinerPremiumVerum_svitle_05_l_jb_text=len(beer_warsteinerPremiumVerum_svitle_05_l_jb_text)
        count_beer_dab_temne_05_l_jb_text=len(beer_dab_temne_05_l_jb_text)
        count_beer_grimbergenBlanche_svitle_05_l_jb_text=len(beer_grimbergenBlanche_svitle_05_l_jb_text)
        count_beer_klosterkellerWeissbierChina_svitle_nefilter_05_l_jb_text=len(beer_klosterkellerWeissbierChina_svitle_nefilter_05_l_jb_text)
        count_beer_karpackiePils_svitle_05_l_jb_text=len(beer_karpackiePils_svitle_05_l_jb_text)
        count_beer_5_0_OriginalPills_svitle_05_l_jb_text=len(beer_5_0_OriginalPills_svitle_05_l_jb_text)
        count_beer_5_0_Original_Lager_svitle_05_l_jb_text=len(beer_5_0_Original_Lager_svitle_05_l_jb_text)
        count_beer_5_0_Original_Weiss_svitle_nefilter_05_l_jb_text=len(beer_5_0_Original_Weiss_svitle_nefilter_05_l_jb_text)
        count_beer_fahnen_brau_svitle_05_l_jb_text=len(beer_fahnen_brau_svitle_05_l_jb_text)
        count_beer_gosser_light_svitle_05_l_jb_text=len(beer_gosser_light_svitle_05_l_jb_text)
        count_beer_holland_import_svitle_033_l_jb_text=len(beer_holland_import_svitle_033_l_jb_text)
        count_beer_holsten_pilsener_048_l_jb_text=len(beer_holsten_pilsener_048_l_jb_text)
        count_beer_obolon_premium_extra_brew_svitle_05_l_jb_text=len(beer_obolon_premium_extra_brew_svitle_05_l_jb_text)
        count_beer_lvivske__svitle_048_l_jb_text=len(beer_lvivske__svitle_048_l_jb_text)
        count_beer_carlsberg_premium_pilsner_05_l_jb_text=len(beer_carlsberg_premium_pilsner_05_l_jb_text)
        count_beer_carlsberg_pilsner_05_l_jb_text=len(beer_carlsberg_pilsner_05_l_jb_text)

        return texts, count_obolon_premium_extra_11_text, count_hetman_sagaydachniy_07_text, \
               count_coffee_aroma_gold_classic_100gr_text, count_apple_golden_text, count_coca_cola_2l_text, \
               count_KOMO_paprikash_text, count_garlik_text, count_kent_8_text, count_tea_minutka_40_p_black_text, \
               count_oil_shedriy_dar_850_text, count_onion_text, count_fairy_text, count_apple_black_prince_text, \
               count_gorchica_kolos_text, count_smetana_stolica_smaky_20_400_text, count_limon_text, count_oil_oleyna_neraf_850_text, \
               count_pivo_lvivske_svitle_24l_text, count_pena_arko_cool_200_100_text, count_pena_arko_sensitive_200_100_text, \
               count_carrot_text, count_drojji_text, count_eggs_text, count_desodorant_garnier_magniy_text, \
               count_cabbage_text, count_marlboro_red_text, count_mayonez_detsk_shedro_190_text, \
               count_rexona_aloe_vera_w_text, count_smetana_stolica_smaky_15jir_400gr_text, \
               count_tea_monomah_kenya_90_text, count_toilet_papir_text, count_coffee_aroma_gold_freeze_dried_70g_text, \
               count_gorchica_veres_ukrainska_micna_120g_text, count_tea_monomah_100_ceylon_original_black_krupn_list_90g_text, \
               count_tea_monomah_ceylon_black_text, count_apple_gala_text, count_desodorant_garnier_spring_spirit_text, \
               count_smetana_galichanska_15_370gr_text, count_chips_lays_with_salt_big_pack_text, count_sprite_2l_text, \
               count_fanta_2l_text,count_bond_street_blue_selection_text,count_camel_blue_text,count_LD_red_text,\
               count_marlboro_gold_text,count_rotmans_demi_blue_exclusive_text,count_rotmans_demi_click_purple_text,\
               count_winston_caster_text,count_parlament_aqua_blue_text,count_winston_blue_text,\
               count_bond_street_red_selection_text,count_LD_blue_text,count_kent_silver_text,\
               count_kent_navy_blue_new_text,count_beer_chernigivske_svitle_05_l_glass_text,\
               count_beer_stella_artois_05_l_glass_text,count_beer_obolon_svitle_05_l_glass_text,\
               count_beer_jigulivske_svitle_05_l_glass_text,count_beer_rogan_tradiciyne_svitle_05_l_glass_text,\
               count_beer_corona_extra_svitle_033_l_glass_text,count_beer_chernigivske_bile_nefilter_05_l_glass_text,\
               count_beer_yantar_svitle_05_l_glass_text,count_beer_zibert_svitle_05_l_glass_text,\
               count_beer_arsenal_micne_05_l_glass_text,count_beer_persha_brovarnya_zakarpatske_05_l_glass_text,\
               count_beer_lvivske_svitle_05_l_glass_text,count_beer_lvivske_1715_05_l_glass_text,count_beer_zlata_praha_svitle_05_l_glass_text,\
               count_beer_tuborg_green_05_l_glass_text,count_beer_slavutich_ice_mix_lime_svitle_05_l_glass_text,\
               count_beer_teteriv_svitle_05_l_glass_text,count_beer_krusovice_svitle_05_l_glass_text,\
               count_beer_heineken_svitle_05_l_glass_text,count_beer_amstel_svitle_05_l_glass_text,\
               count_beer_hike_premium_svitle_05_l_glass_text,count_beer_bochkove_svitle_05_l_glass_text,\
               count_beer_kronenbourg_1664_blanc_046_l_glass_text,count_beer_opilla_nepasterizovane_05_l_glass_text,\
               count_beer_yachminniy_kolos_svitle_05_l_glass_text,count_beer_opilla_korifey_05_l_glass_text,\
               count_beer_chayka_dniprovska_svitle_05_l_glass_text,count_beer_chayka_chernomorska_svitle_05_l_glass_text,\
               count_beer_uman_pivo_waissburg_svitle_1l_plastic_text,count_beer_uman_pivo_pshenichnoe_svitle_1l_plastic_text,\
               count_beer_berdichevske_hmilne_svitle_1l_plastic_text,count_beer_berdichevske_lager_svitle_1l_plastic_text,\
               count_beer_opilla_korifey_svitle_11l_plastic_text,count_beer_obolon_jigulivske_exportne_svitle_1l_plastic_text,\
               count_beer_yantar_svitle_12l_plastic_text,count_beer_jashkivske_pshenichne_nefilter_1l_plastic_text,\
               count_beer_jashkivske_svitle_nefilter_1l_plastic_text,count_beer_jashkivske_jigulivske_nefilter_1l_plastic_text,\
               count_beer_persha_privatna_brovarnya_bochkove_svitle_1l_plastic_text,count_beer_chayka_dniprovska_svitle_1l_plastic_text,\
               count_ketchup_torchin_chasnik_270gr_text,count_muka_zolote_zernyatko_pshen_2kg_text,\
               count_mayonez_korolivskiy_smak_kororlivskiy_67_300gr_text,count_beer_chernigivske_bile_nefilter_1l_plastic_text,\
               count_beer_obolon_svitle_1l_plastic_text,count_beer_rogan_svitle_tradiciyne_1l_plastic_text,count_sous_chumak_chesnochniy_200gr_text,\
               count_jvachka_orbit_clubnika_banan_text,count_LM_red_text,count_beer_jigulivske_svitle_2_l_plastic_text,\
               count_beer_chayka_dniprovska_svitle_2l_plastic_text,count_beer_piwny_kubek_svitle_2l_plastic_text,\
               count_ketchup_torchin_do_shasliky_270gr_test,count_mayonez_chumak_appetitniy_50_300gr_text,\
               count_kolbasa_persha_stolica_salyami_firmennaya_vs_text,count_coffee_chorna_karta_gold_50gr_text,\
               count_beer_arsenal_micne_svitle_2l_plastic_text,count_beer_ppb_bochkove_svitle_2l_plastic_text,\
               count_beer_ppb_zakarpatske_originalne_svitle_2l_plastic_text,count_beer_zibert_svitle_05_l_banochnoe_text,\
               count_yogurt_fanni_1_5_240gr_v_banke_text,count_kefir_slviya_2_5_850gr_v_pakete_text,\
               count_beer_obolon_kievske_rozlivne_svitle_195l_plastic_text,count_beer_chernigivske_light_svitle_2l_plastic_text,\
               count_beer_opilla_korifey_svitle_2l_plastic_text,count_beer_yantar_svitle_2l_plastic_text,count_beer_tuborg_green_05_4_banki_2litra_text,\
               count_beer_ppb_zakarpatske_svitle_05_4_banki_2litra_text,count_beer_ppb_bochkove_svitle_05_4_banki_2litra_text,\
               count_beer_budweiser_budvar_05_l_glass_text,count_beer_pilsner_urquell_05_l_glass_text,\
               count_beer_robert_doms_belgiyskiy_svitle_nefilter_05_l_glass_text,count_beer_chernigivske_svitle_05_l_jb_text,\
               count_beer_chernigivske_bile_nefilter_05_l_jb_text,count_beer_velkopopovicky_kozel_temne_05_l_jb_text,\
               count_beer_edelmeister_pilsner_svitle_05_l_jb_text,count_beer_faxe_svitle_05_l_jb_text,\
               count_beer_livu_pilzenes_svitle_05_l_jb_text,count_beer_velkopopovicky_kozel_svitle_05_l_jb_text,\
               count_beer_obolon_beermix_limon_05_l_jb_text,count_beer_edelmeister_weizenbier_nefilter_svitle_05_l_jb_text,\
               count_beer_edelmeister_schwarzbier_temnoe_05_l_jb_text,count_beer_hike_blanche_svitle_nefilter_05_l_jb_text,\
               count_beer_zlata_praha_svitle_05_l_jb_text,count_beer_thuringer_premium_beer_svitle_05_l_jb_text,\
               count_beer_livu_sencu_svitle_05_l_jb_text,count_beer_germanarich_svitle_05_l_jb_text,\
               count_beer_hike_premium_svitle_05_l_jb_text,count_beer_obolon_nonalcohol_svitle_nefilter_05_l_jb_text,\
               count_beer_zibert_bavarske_svitle_05_l_jb_text,count_beer_bavaria_liquid_apple_nonalcohol_svitle_05_l_jb_text,\
               count_beer_heineken_svitle_05_l_jb_text,count_beer_rychtar_grunt_11_svitle_05_l_jb_text,\
               count_beer_amstel_svitle_05_l_jb_text,count_beer_bavaria_svitle_05_l_jb_text,count_beer_bavaria_svitle_nonalcohol_05_l_jb_text,\
               count_beer_edelburg_lager_svitle_05_l_jb_text,count_beer_donner_pills_svitle_05_l_jb_text,\
               count_beer_dutch_windmill_svitle_05_l_jb_text,count_beer_edelberg_hefeweizen_svitle_nefilter_05_l_jb_text,\
               count_beer_edelmeister_unfiltered_svitle_nefilter_05_l_jb_text,count_beer_estrella_damm_barcelona_svitle_05_l_jb_text,\
               count_beer_halne_jasne_pelne_05_l_jb_text,count_beer_eurotour_hefeweissbier_svitle_05_l_jb_text,\
               count_beer_hollandia_strong_svitle_05_l_jb_text,count_beer_lander_brau_premium_svitle_05_l_jb_text,\
               count_beer_saku_kuld_05_l_jb_text,\
               count_beer_saku_original_05_l_jb_text,count_beer_stangen_lager_svitle_05_l_jb_text,count_beer_van_pur_premium_svitle_05_l_jb_text,\
               count_beer_bavaria_mango_marakya_bezalkogol_svitle_05_l_jb_text,count_beer_bavaria_granat_bezalkogol_svitle_05_l_jb_text,\
               count_beer_obolon_beermix_malina_05_l_jb_text,count_beer_obolon_beermix_vishnya_05_l_jb_text,count_beer_lomza_svitle_05_l_jb_text,\
               count_beer_paderborner_pilsener_svitle_05_l_jb_text,count_beer_paderborner_export_05_l_jb_text,count_beer_clausthaler_greipfruit_nonalcohol_05_l_jb_text,\
               count_beer_clausthaler_original_nonalcohol_05_l_jb_text,count_beer_clausthaler_lemon_nonalcohol_05_l_jb_text,\
               count_beer_forever_rock_n_roll_svitle_nefilter_05_l_jb_text,count_beer_forever_black_queen_temne_nefilter_05_l_jb_text,\
               count_beer_forever_kite_safari_svitle_nefilter_05_l_jb_text,count_beer_forever_crazy_svitle_nefilter_05_l_jb_text,\
               count_beer_hike_light_svitle_05_l_jb_text,count_beer_hike_zero_nonalcohol_05_l_jb_text,count_beer_horn_disel_ice_pilsner_svitle_0568_l_jb_text,\
               count_beer_horn_original_svitle_0568_l_jb_text,count_beer_horn_traditional_svitle_0568_l_jb_text,count_beer_horn_premium_svitle_05_l_jb_text,\
               count_beer_krusovice_cerne_temne_05_l_jb_text,count_beer_lander_brau_micne_05_l_jb_text,count_beer_lander_brau_svitle_nefilter_05_l_jb_text,\
               count_beer_padeborner_pilger_nefilter_svitle_05_l_jb_text,count_beer_platan_jedenactka_05_l_jb_text,count_beer_praga_svitle_05_l_jb_text,\
               count_beer_saku_rock_svitle_0568_l_jb_text,count_beer_sitnan_svitle_05_l_jb_text,count_beer_vienas_premium_golden_svitle_05_l_jb_text,\
               count_beer_vienas_premium_traditional_svitle_05_l_jb_text,count_beer_volynski_browar_forever_sweet_wit_pshen_nefilter_svitle_05_l_jb_text,\
               count_beer_zahringer_premium_svitle_05_l_jb_text,count_beer_zahringer_hefeweizen_svitle_05_l_jb_text,count_beer_jajkivske_svitle__nefilter_05_l_jb_text,\
               count_beer_obolon_svitle_05_l_jb_text,count_beer_pubster_svitle_05_l_jb_text,count_beer_chaika_chernomorskaya_05_l_jb_text,\
               count_beer_ppb_zakarpatske_orig_svitle_05_l_jb_text,count_beer_ppb_bochkove_nefilter_05_l_jb_text,count_beer_ppb_nefilter_svitle_nonalco_05_l_jb_text,\
               count_beer_ppb_limon_lime_nonalco_nefilter_05_l_jb_text,count_beer_chaika_dniprovskaya_05_l_jb_text,count_beer_brok_export_svitle_05_l_jb_text,\
               count_beer_carling_svitle_05_l_jb_text,count_beer_keten_brug_blanche_elegant_nefilter_05_l_jb_text,count_beer_budweiser_nonalco_svitle_05_l_jb_text,\
               count_beer_feldschlosschen_wheat_beer_svitle05_l_jb_text,count_beer_teteriv_hmilna_vishnya_polutemne_05_l_jb_text,\
               count_beer_grotwerg_svitle_nonalco_05_l_jb_text,count_beer_holland_import_svitle_05_l_jb_text,count_beer_golden_castle_export_svitle_05_l_jb_text,\
               count_beer_5_0_origin_craft_beer_nefilter_svitle_05_l_jb_text,count_beer_guinness_draught_temne_044_l_jb_text,\
               count_beer_grimbergenDoubleAmbree_napivtemne_05_l_jb_text,count_beer_warsteinerPremiumVerum_svitle_05_l_jb_text,\
               count_beer_dab_temne_05_l_jb_text,count_beer_grimbergenBlanche_svitle_05_l_jb_text,count_beer_klosterkellerWeissbierChina_svitle_nefilter_05_l_jb_text,\
               count_beer_karpackiePils_svitle_05_l_jb_text,count_beer_5_0_OriginalPills_svitle_05_l_jb_text,count_beer_5_0_Original_Lager_svitle_05_l_jb_text,\
               count_beer_5_0_Original_Weiss_svitle_nefilter_05_l_jb_text,count_beer_fahnen_brau_svitle_05_l_jb_text,count_beer_gosser_light_svitle_05_l_jb_text,\
               count_beer_holland_import_svitle_033_l_jb_text,count_beer_holsten_pilsener_048_l_jb_text,count_beer_obolon_premium_extra_brew_svitle_05_l_jb_text,\
               count_beer_lvivske__svitle_048_l_jb_text,count_beer_carlsberg_premium_pilsner_05_l_jb_text,count_beer_carlsberg_pilsner_05_l_jb_text


    def converted_data(self):
        '''Подготовка обучающих данных'''

        # загружаем общую папку с текстами для обработки:
        texts = self.upload_data()[0]

        # создаем необходимый нам токенайзер:
        tokenizer = Tokenizer(num_words=self.MAX_WORDS,
                              filters='!"-#$%amp;()*+-/:;<=>?@[\\]^_`{|}~\t\n\r',
                              lower=True, split=' ', char_level=False)

        # пропускаем все нащи тексты через токенайзер:
        tokenizer.fit_on_texts(texts)

        # формируем последовательность из чисел вместо слов
        # (будут индексы каждых слов вместо слов)
        data = tokenizer.texts_to_sequences(texts)

        # короткие тексты дополняем нулями, а длинные урезаем до 10 слов:
        data_pad = pad_sequences(data, maxlen=self.MAX_LENGTH_TEXT)

        # окончательно формируем обучающую выборку:
        TRAIN_SAMPLE = data_pad
        items = 234
        TARGET_SAMPLE = np.array(
            make_list(items, 0) *
            self.upload_data()[1] + make_list(items, 1) * self.upload_data()[2] + make_list(items, 2) *
            self.upload_data()[3] + make_list(items, 3) * self.upload_data()[4] + make_list(items, 4) *
            self.upload_data()[5] + make_list(items, 5) * self.upload_data()[6] + make_list(items, 6) *
            self.upload_data()[7] + make_list(items, 7) * self.upload_data()[8] + make_list(items, 8) *
            self.upload_data()[9] + make_list(items, 9) * self.upload_data()[10] + make_list(items, 10) *
            self.upload_data()[11] + make_list(items, 11) * self.upload_data()[12] + make_list(items, 12) *
            self.upload_data()[13] + make_list(items, 13) * self.upload_data()[14] + make_list(items, 14) *
            self.upload_data()[15] + make_list(items, 15) * self.upload_data()[16] + make_list(items, 16) *
            self.upload_data()[17] + make_list(items, 17) * self.upload_data()[18] + make_list(items, 18) *
            self.upload_data()[19] + make_list(items, 19) * self.upload_data()[20] + make_list(items, 20) *
            self.upload_data()[21] + make_list(items, 21) * self.upload_data()[22] + make_list(items, 22) *
            self.upload_data()[23] + make_list(items, 23) * self.upload_data()[24] + make_list(items, 24) *
            self.upload_data()[25] + make_list(items, 25) * self.upload_data()[26] + make_list(items, 26) *
            self.upload_data()[27] + make_list(items, 27) * self.upload_data()[28] + make_list(items, 28) *
            self.upload_data()[29] + make_list(items, 29) * self.upload_data()[30] + make_list(items, 30) *
            self.upload_data()[31] + make_list(items, 31) * self.upload_data()[32] + make_list(items, 32) *
            self.upload_data()[33] + make_list(items, 33) * self.upload_data()[34] + make_list(items, 34) *
            self.upload_data()[35] + make_list(items, 35) * self.upload_data()[36] + make_list(items, 36) *
            self.upload_data()[37] + make_list(items, 37) * self.upload_data()[38] + make_list(items, 38) *
            self.upload_data()[39] + make_list(items, 39) *self.upload_data()[40] + make_list(items, 40) *
            self.upload_data()[41] + make_list(items, 41) *self.upload_data()[42] + make_list(items, 42) *
            self.upload_data()[43]+ make_list(items, 43) *self.upload_data()[44]+ make_list(items, 44) *
            self.upload_data()[45]+ make_list(items, 45) *self.upload_data()[46]+ make_list(items, 46) *
            self.upload_data()[47] + make_list(items, 47) *self.upload_data()[48]+ make_list(items, 48) *
            self.upload_data()[49]+ make_list(items, 49) *self.upload_data()[50]+ make_list(items, 50) *
            self.upload_data()[51]+ make_list(items, 51) *self.upload_data()[52]+ make_list(items, 52) *
            self.upload_data()[53]+ make_list(items, 53) *self.upload_data()[54]+ make_list(items, 54) *
            self.upload_data()[55]+ make_list(items, 55) *self.upload_data()[56]+ make_list(items, 56) *
            self.upload_data()[57]+ make_list(items, 57) *self.upload_data()[58]+ make_list(items, 58) *
            self.upload_data()[59]+ make_list(items, 59) *self.upload_data()[60]+ make_list(items, 60) *
            self.upload_data()[61]+ make_list(items, 61) *self.upload_data()[62]+ make_list(items, 62) *
            self.upload_data()[63]+ make_list(items, 63) *self.upload_data()[64]+ make_list(items, 64) *
            self.upload_data()[65]+ make_list(items, 65) *self.upload_data()[66]+ make_list(items, 66) *
            self.upload_data()[67]+ make_list(items, 67) *self.upload_data()[68]+ make_list(items, 68) *
            self.upload_data()[69]+ make_list(items, 69) *self.upload_data()[70]+ make_list(items, 70) *
            self.upload_data()[71]+ make_list(items, 71) *self.upload_data()[72]+ make_list(items, 72) *
            self.upload_data()[73]+ make_list(items, 73) *self.upload_data()[74]+ make_list(items, 74) *
            self.upload_data()[75]+ make_list(items, 75) *self.upload_data()[76]+ make_list(items, 76) *
            self.upload_data()[77]+ make_list(items, 77) *self.upload_data()[78]+ make_list(items, 78) *
            self.upload_data()[79]+ make_list(items, 79) *self.upload_data()[80]+ make_list(items, 80) *
            self.upload_data()[81]+ make_list(items, 81) *self.upload_data()[82]+ make_list(items, 82) *
            self.upload_data()[83]+ make_list(items, 83) *self.upload_data()[84]+ make_list(items, 84) *
            self.upload_data()[85]+ make_list(items, 85) *self.upload_data()[86]+ make_list(items, 86) *
            self.upload_data()[87]+ make_list(items, 87) *self.upload_data()[88]+ make_list(items, 88) *
            self.upload_data()[89]+ make_list(items, 89) *self.upload_data()[90]+ make_list(items, 90) *
            self.upload_data()[91]+ make_list(items, 91) *self.upload_data()[92]+ make_list(items, 92) *
            self.upload_data()[93]+ make_list(items, 93) *self.upload_data()[94]+ make_list(items, 94) *
            self.upload_data()[95]+ make_list(items, 95) *self.upload_data()[96]+ make_list(items, 96) *
            self.upload_data()[97]+ make_list(items, 97) *self.upload_data()[98]+ make_list(items, 98) *
            self.upload_data()[99]+ make_list(items, 99) *self.upload_data()[100]+ make_list(items, 100) *
            self.upload_data()[101]+ make_list(items, 101) *self.upload_data()[102]+ make_list(items, 102) *
            self.upload_data()[103]+ make_list(items, 103) *self.upload_data()[104]+ make_list(items, 104) *
            self.upload_data()[105]+ make_list(items, 105) *self.upload_data()[106]+ make_list(items, 106) *
            self.upload_data()[107]+ make_list(items, 107) *self.upload_data()[108]+ make_list(items, 108) *
            self.upload_data()[109]+ make_list(items, 109) *self.upload_data()[110]+ make_list(items, 110) *
            self.upload_data()[111]+ make_list(items, 111) *self.upload_data()[112]+ make_list(items, 112) *
            self.upload_data()[113]+ make_list(items, 113) *self.upload_data()[114]+ make_list(items, 114) *
            self.upload_data()[115]+ make_list(items, 115) *self.upload_data()[116]+ make_list(items, 116) *
            self.upload_data()[117]+ make_list(items, 117) *self.upload_data()[118]+ make_list(items, 118) *
            self.upload_data()[119]+ make_list(items, 119) *self.upload_data()[120]+ make_list(items, 120) *
            self.upload_data()[121]+ make_list(items, 121) *self.upload_data()[122]+ make_list(items, 122) *
            self.upload_data()[123]+ make_list(items, 123) *self.upload_data()[124]+ make_list(items, 124) *
            self.upload_data()[125]+ make_list(items, 125) *self.upload_data()[126]+ make_list(items, 126) *
            self.upload_data()[127]+ make_list(items, 127) *self.upload_data()[128]+ make_list(items, 128) *
            self.upload_data()[129]+ make_list(items, 129) *self.upload_data()[130]+ make_list(items, 130) *
            self.upload_data()[131]+ make_list(items, 131) *self.upload_data()[132]+ make_list(items, 132) *
            self.upload_data()[133]+ make_list(items, 133) *self.upload_data()[134]+ make_list(items, 134) *
            self.upload_data()[135]+ make_list(items, 135) *self.upload_data()[136]+ make_list(items, 136) *
            self.upload_data()[137]+ make_list(items, 137) *self.upload_data()[138]+ make_list(items, 138) *
            self.upload_data()[139]+ make_list(items, 139) *self.upload_data()[140]+ make_list(items, 140) *
            self.upload_data()[141]+ make_list(items, 141) *self.upload_data()[142]+ make_list(items, 142) *
            self.upload_data()[143]+ make_list(items, 143) *self.upload_data()[144]+ make_list(items, 144) *
            self.upload_data()[145]+ make_list(items, 145) *self.upload_data()[146]+ make_list(items, 146) *
            self.upload_data()[147]+ make_list(items, 147) *self.upload_data()[148]+ make_list(items, 148) *
            self.upload_data()[149]+ make_list(items, 149) *self.upload_data()[150]+ make_list(items, 150) *
            self.upload_data()[151]+ make_list(items, 151) *self.upload_data()[152]+ make_list(items, 152) *
            self.upload_data()[153]+ make_list(items, 153) *self.upload_data()[154]+ make_list(items, 154) *
            self.upload_data()[155]+ make_list(items, 155) *self.upload_data()[156]+ make_list(items, 156) *
            self.upload_data()[157]+ make_list(items, 157) *self.upload_data()[158]+ make_list(items, 158) *
            self.upload_data()[159]+ make_list(items, 159) *self.upload_data()[160]+ make_list(items, 160) *
            self.upload_data()[161]+ make_list(items, 161) *self.upload_data()[162]+ make_list(items, 162) *
            self.upload_data()[163]+ make_list(items, 163) *self.upload_data()[164]+ make_list(items, 164) *
            self.upload_data()[165]+ make_list(items, 165) *self.upload_data()[166]+ make_list(items, 166) *
            self.upload_data()[167]+ make_list(items, 167) *self.upload_data()[168]+ make_list(items, 168) *
            self.upload_data()[169]+ make_list(items, 169) *self.upload_data()[170]+ make_list(items, 170) *
            self.upload_data()[171]+ make_list(items, 171) *self.upload_data()[172]+ make_list(items, 172) *
            self.upload_data()[173]+ make_list(items, 173) *self.upload_data()[174]+ make_list(items, 174) *
            self.upload_data()[175]+ make_list(items, 175) *self.upload_data()[176]+ make_list(items, 176) *
            self.upload_data()[177]+ make_list(items, 177) *self.upload_data()[178]+ make_list(items, 178) *
            self.upload_data()[179]+ make_list(items, 179) *self.upload_data()[180]+ make_list(items, 180) *
            self.upload_data()[181]+ make_list(items, 181) *self.upload_data()[182]+ make_list(items, 182) *
            self.upload_data()[183]+ make_list(items, 183) *self.upload_data()[184]+ make_list(items, 184) *
            self.upload_data()[185]+ make_list(items, 185) *self.upload_data()[186]+ make_list(items, 186) *
            self.upload_data()[187]+ make_list(items, 187) *self.upload_data()[188]+ make_list(items, 188) *
            self.upload_data()[189]+ make_list(items, 189) *self.upload_data()[190]+ make_list(items, 190) *
            self.upload_data()[191]+ make_list(items, 191) *self.upload_data()[192]+ make_list(items, 192) *
            self.upload_data()[193]+ make_list(items, 193) *self.upload_data()[194]+ make_list(items, 194) *
            self.upload_data()[195]+ make_list(items, 195) *self.upload_data()[196]+ make_list(items, 196) *
            self.upload_data()[197]+ make_list(items, 197) *self.upload_data()[198]+ make_list(items, 198) *
            self.upload_data()[199]+ make_list(items, 199) *self.upload_data()[200]+ make_list(items, 200) *
            self.upload_data()[201]+ make_list(items, 201) *self.upload_data()[202]+ make_list(items, 202) *
            self.upload_data()[203]+ make_list(items, 203) *self.upload_data()[204]+ make_list(items, 204) *
            self.upload_data()[205]+ make_list(items, 205) *self.upload_data()[206]+ make_list(items, 206) *
            self.upload_data()[207]+ make_list(items, 207) *self.upload_data()[208]+ make_list(items, 208) *
            self.upload_data()[209]+ make_list(items, 209) *self.upload_data()[210]+ make_list(items, 210) *
            self.upload_data()[211]+ make_list(items, 211) *self.upload_data()[212]+ make_list(items, 212) *
            self.upload_data()[213]+ make_list(items, 213) *self.upload_data()[214]+ make_list(items, 214) *
            self.upload_data()[215]+ make_list(items, 215) *self.upload_data()[216]+ make_list(items, 216) *
            self.upload_data()[217]+ make_list(items, 217) *self.upload_data()[218]+ make_list(items, 218) *
            self.upload_data()[219]+ make_list(items, 219) *self.upload_data()[220]+ make_list(items, 220) *
            self.upload_data()[221]+ make_list(items, 221) *self.upload_data()[222]+ make_list(items, 222) *
            self.upload_data()[223]+ make_list(items, 223) *self.upload_data()[224]+ make_list(items, 224) *
            self.upload_data()[225]+ make_list(items, 225) *self.upload_data()[226]+ make_list(items, 226) *
            self.upload_data()[227]+ make_list(items, 227) *self.upload_data()[228]+ make_list(items, 228) *
            self.upload_data()[229]+ make_list(items, 229) *self.upload_data()[230]+ make_list(items, 230) *
            self.upload_data()[231]+ make_list(items, 231) *self.upload_data()[232]+ make_list(items, 232) *
            self.upload_data()[233]+ make_list(items, 233) *self.upload_data()[234])

        # перемешиваем обучающую выборку для лучшей тренированности НС:
        # создаем рандомные индексы:
        indeces = np.random.choice(TRAIN_SAMPLE.shape[0], size=TRAIN_SAMPLE.shape[0],
                                   replace=False)

        # перемешиаем обучающую и целевую выборки:
        TRAIN_SAMPLE = TRAIN_SAMPLE[indeces]
        TARGET_SAMPLE = TARGET_SAMPLE[indeces]

        return TRAIN_SAMPLE, TARGET_SAMPLE, tokenizer

    def index_convert_to_text(self, indeces_list):
        '''Метод для преобразования индексов в слова'''
        reverse_word_map = self.training_NN()[1]
        normal_text = [reverse_word_map.get(x) for x in indeces_list]
        return (normal_text)

    def defining_item(self, user_text):
        '''Метод определения товара по тексту, который запрашивает пользователь '''

        # переводим пользовательский запрос в нижний регистр:
        user_text = user_text.lower()

        # пропускам текст через созданный токенайзер и преобразовываем слова в числа(индексы):
        # загружаем токенайзер:
        tokenizer = self.converted_data()[2]
        # преобразовываем слова:
        data = tokenizer.texts_to_sequences([user_text])

        # преобразовываем в вектор нужной длины,
        # дополняя нулями или сокращая до 10 слов в тексте
        data_pad = pad_sequences(data, maxlen=self.MAX_LENGTH_TEXT)

        # смотрим какую на самом деле фразу мы анализируем(т.к. некоторых слов у нас может не быть в словаре)
        print(self.index_convert_to_text(data[0]))

        # получаем прогноз. если перменная argmax принимает значение 0 ( 0 - это первый нейрон,
        # отвечающий за пиво "Оболонь Премиум Экстра 1,1 л"),то пользователь ищет пиво "Оболонь Премиум Экстра 1,1 л",
        # если 1 , то пользователь ищет водку "Гетьман Сагайдачный 0,7 л"

        result = self.model.predict(data_pad)
        print(result, np.argmax(result), sep='\n')



user = GroceryAppText()
user.training_NN()
