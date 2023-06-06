import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np

from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.models import load_model

from .items_full_names import *
from my_app.utils import RefersForRNN


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
        '''Подготавливаем текст'''
        get_text_data = RefersForRNN()
        texts = get_text_data.get_text()[0]
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
        elif np.argmax(result) == 234:
            return BANANA
        elif np.argmax(result) == 235:
            return ORANGE
        elif np.argmax(result) == 236:
            return KIWI
        elif np.argmax(result) == 237:
            return COCONUT
        elif np.argmax(result) == 238:
            return GRAPEFRUIT
        elif np.argmax(result) == 239:
            return POMEGRANATE
        elif np.argmax(result) == 240:
            return MANGO


