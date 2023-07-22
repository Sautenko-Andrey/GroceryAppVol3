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
    MAX_WORDS = 2000

    # определяем количество слов, к которому дуте приведен каждый запрос от пользователя
    MAX_LENGTH_TEXT = 10

    def prepearing_data(self):
        '''Подготавливаем текст'''
        get_text_data = RefersForRNN()
        #texts = get_text_data.get_text()[0]
        texts = get_text_data.get_text_from_DB()[0]
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

        #загружаем обученную модель НС для распознования товара по тексту (для образа включительно):
        #model = load_model('/code/my_model_text')
        #----------------------------------------

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
        elif np.argmax(result) == 241:
            return POTATO
        elif np.argmax(result) == 242:
            return TOMATO
        elif np.argmax(result) == 243:
            return CUCUMBER
        elif np.argmax(result) == 244:
            return KABACHKI
        elif np.argmax(result) == 245:
            return RED_BOLG_PAPPER
        elif np.argmax(result) == 246:
            return YELLOW_BOLG_PAPPER
        elif np.argmax(result) == 247:
            return ASPARAGUS
        elif np.argmax(result) == 248:
            return BROCCOLI
        elif np.argmax(result) == 249:
            return CAPTAIN_MORGAN_SPICED_GOLD_1L
        elif np.argmax(result) == 250:
            return BELLS_ORIGINAL_07L
        elif np.argmax(result) == 251:
            return MARTINI_ASTI_BILE_075L
        elif np.argmax(result) == 252:
            return JAMESON_IRISH_WHISKEY_07L
        elif np.argmax(result) == 253:
            return BELLS_ORIGINAL_1L
        elif np.argmax(result) == 254:
            return CAPTAIN_MORGAN_SPICED_GOLD_05L
        elif np.argmax(result) == 255:
            return JAMESON_IRISH_WHISKEY_05L
        elif np.argmax(result) == 256:
            return JW_RED_LABEL_05L
        elif np.argmax(result) == 257:
            return BELLS_SPICED_07L
        elif np.argmax(result) == 258:
            return BALLANTINES_FINEST_07L
        elif np.argmax(result) == 259:
            return JACK_DANILES_07L
        elif np.argmax(result) == 260:
            return JACK_DANILES_1L
        elif np.argmax(result) == 261:
            return JIM_BEAM_WHITE_07L
        elif np.argmax(result) == 262:
            return BORJOMI_SILNOGAZ_05L
        elif np.argmax(result) == 263:
            return MORSHINSKAYA_NEGAZ_15L
        elif np.argmax(result) == 264:
            return MORSHINSKAYA_LOW_GAZ_15L
        elif np.argmax(result) == 265:
            return MORSHINSKAYA_HIGH_GAZ_15L
        elif np.argmax(result) == 266:
            return NASH_SIK_APPLE_GRAPE_02L
        elif np.argmax(result) == 267:
            return NASH_SIK_APPLE_CARROT_02L
        elif np.argmax(result) == 268:
            return NASH_SIK_ORANGE_02L
        elif np.argmax(result) == 269:
            return NASH_SIK_MULTIFRUKT_02L
        elif np.argmax(result) == 270:
            return NASH_SIK_APPLE_PEACH_02L
        elif np.argmax(result) == 271:
            return NASH_SIK_PEAR_APPLE_02L
        elif np.argmax(result) == 272:
            return NASH_SIK_MULTIVITAMIN_02L
        elif np.argmax(result) == 273:
            return NASH_SIK_APPLE_02L
        elif np.argmax(result) == 274:
            return NASH_SIK_APPLE_STRAWBERRY_02L
        elif np.argmax(result) == 275:
            return NON_STOP_ORIGINAL_025L
        elif np.argmax(result) == 276:
            return NON_STOP_ORIGINAL_05L
        elif np.argmax(result) == 277:
            return NON_STOP_JUNGLE_025L
        elif np.argmax(result) == 278:
            return NON_STOP_BOOST_05L
        elif np.argmax(result) == 279:
            return NON_STOP_ULTRA_05L
        elif np.argmax(result) == 280:
            return NON_STOP_BOOST_025L
        elif np.argmax(result) == 281:
            return BURN_CLASSIC_025L
        elif np.argmax(result) == 282:
            return BURN_CLASSIC_05L
        elif np.argmax(result) == 283:
            return BURN_MANGO_025L
        elif np.argmax(result) == 284:
            return BURN_APPLE_KIWI_05L
        elif np.argmax(result) == 285:
            return BURN_DARK_ENERGY_025L
        elif np.argmax(result) == 286:
            return RED_BULL_025L
        elif np.argmax(result) == 287:
            return RED_BULL_0355L
        elif np.argmax(result) == 288:
            return RED_BULL_0473L
        elif np.argmax(result) == 289:
            return RED_BULL_0591L
        elif np.argmax(result) == 290:
            return RED_BULL_SUGAR_FREE_025L
        elif np.argmax(result) == 291:
            return RED_BULL_RED_EDITION_CAVUN_025L
        elif np.argmax(result) == 292:
            return RED_BULL_YELLOW_EDITION_TROPIC_FRUITS_025L
        elif np.argmax(result) == 293:
            return MONSTER_0355L
        elif np.argmax(result) == 294:
            return MONSTER_THE_DOCTOR_0355L
        elif np.argmax(result) == 295:
            return MONSTER_ULTRA_ZERO_0355L
        elif np.argmax(result) == 296:
            return MONSTER_JUICED_0355L
        elif np.argmax(result) == 297:
            return PIT_BULL_COFFEE_025L
        elif np.argmax(result) == 298:
            return PIT_BULL_POWER_025L
        elif np.argmax(result) == 299:
            return PIT_BULL_X_025L
        elif np.argmax(result) == 300:
            return PIT_BULL_EXTRA_VITAMIN_C_025L
        elif np.argmax(result) == 301:
            return PIT_BULL_025L
        elif np.argmax(result) == 302:
            return MACCOFFEE_GOLD_ROZCHIN_SOFT_PACK_60_GR
        elif np.argmax(result) == 303:
            return NESCAFE_GOLD_ROZCH_SOFT_PACK_120_GR
        elif np.argmax(result) == 304:
            return GRANO_DORADO_GOLD_SOFT_P_130GR
        elif np.argmax(result) == 305:
            return NESCAFE_CLASSIC_SOFT_P_60GR
        elif np.argmax(result) == 306:
            return CHORNA_CARTA_GOLD_SOFT_P_400GR
        elif np.argmax(result) == 307:
            return BOUNTY_SMALL
        elif np.argmax(result) == 308:
            return BOUNTY_BIG
        elif np.argmax(result) == 309:
            return MARS_SMALL
        elif np.argmax(result) == 310:
            return MARS_BIG
        elif np.argmax(result) == 311:
            return NUTS_STRAWBERRY
        elif np.argmax(result) == 312:
            return NUTS_SMALL
        elif np.argmax(result) == 313:
            return NUTS_KING_SIZE
        elif np.argmax(result) == 314:
            return SNICKERS_SMALL
        elif np.argmax(result) == 315:
            return SNICKERS_SUPER
        elif np.argmax(result) == 316:
            return SNICKERS_CREAMY_PEANUT_BUTTER
        elif np.argmax(result) == 317:
            return SNICKERS_CREAMY_PEANUT_BUTTER_SMALL
        elif np.argmax(result) == 318:
            return TWIX_PECHIVO_KARAMEL_50GR
        elif np.argmax(result) == 319:
            return TWIX_EXTRA_PECHIVO_KARAMEL_75GR
        elif np.argmax(result) == 320:
            return VODKA_ABSOLUT_05L
        elif np.argmax(result) == 321:
            return VODKA_ABSOLUT_1L
        elif np.argmax(result) == 322:
            return VODKA_ABSOLUT_07L
        elif np.argmax(result) == 323:
            return VODKA_ABSOLUT_LIME_07L
        elif np.argmax(result) == 324:
            return VODKA_ABSOLUT_GRAPEFRUIT_07L
        elif np.argmax(result) == 325:
            return VODKA_ABSOLUT_ELYX_07L
        elif np.argmax(result) == 326:
            return VODKA_ABSOLUT_CITRON_07L
        elif np.argmax(result) == 327:
            return VODKA_ABSOLUT_KURANT_07L
        elif np.argmax(result) == 328:
            return VODKA_ABSOLUT_WATERMELON_07L
        elif np.argmax(result) == 329:
            return VODKA_ABSOLUT_MANDARIN_07L
        elif np.argmax(result) == 330:
            return VODKA_FINLAND_05L
        elif np.argmax(result) == 331:
            return VODKA_FINLAND_07L
        elif np.argmax(result) == 332:
            return VODKA_FINLAND_1L
        elif np.argmax(result) == 333:
            return VODKA_FINLAND_REDBERRY_05L
        elif np.argmax(result) == 334:
            return VODKA_FINLAND_REDBERRY_1L
        elif np.argmax(result) == 335:
            return VODKA_FINLAND_CRANBERRY_05L
        elif np.argmax(result) == 336:
            return VODKA_FINLAND_CRANBERRY_1L
        elif np.argmax(result) == 337:
            return VODKA_FINLAND_GRAPEFRUIT_05L
        elif np.argmax(result) == 338:
            return VODKA_FINLAND_LIME_05L
        elif np.argmax(result) == 339:
            return VODKA_FINLAND_COCONUT_05L
        elif np.argmax(result) == 340:
            return VODKA_FINLAND_BLACKCURRANT_05L
        elif np.argmax(result) == 341:
            return VODKA_FINLAND_LIME_1L
        elif np.argmax(result) == 342:
            return VODKA_FINLAND_BLACKCURRANT_1L
        elif np.argmax(result) == 343:
            return VODKA_FINLAND_GRAPEFRUIT_1L
        elif np.argmax(result) == 344:
            return VODKA_FINLAND_WHITE_175L
        elif np.argmax(result) == 345:
            return VODKA_NEMIROFF_DELIKAT_SOFT_05L
        elif np.argmax(result) == 346:
            return VODKA_NEMIROFF_SHTOF_05L
        elif np.argmax(result) == 347:
            return VODKA_NEMIROFF_UKR_PSHEN_05L
        elif np.argmax(result) == 348:
            return VODKA_NEMIROFF_DELUX_05L
        elif np.argmax(result) == 349:
            return VODKA_NEMIROFF_LEX_05L
        elif np.argmax(result) == 350:
            return SHAMP_ARTEMIVSKE_BILE_NAPIVSOLOD
        elif np.argmax(result) == 351:
            return SHAMP_ARTEMIVSKE_ROJEVE_NAPIVSUHE
        elif np.argmax(result) == 352:
            return SHAMP_ARTEMIVSKE_BILE_BRUT
        elif np.argmax(result) == 353:
            return SHAMP_ARTEMIVSKE_COLLECT_NAPIVSUHE
        elif np.argmax(result) == 354:
            return SHAMP_ARTEMIVSKE_CHERVONE_NAPIVSOLOD
        elif np.argmax(result) == 355:
            return SHAMP_BAGRATIONI_BILE_NAPIVSOLOD
        elif np.argmax(result) == 356:
            return SHAMP_BAGRATIONI_BILE_NAPIVSUHE
        elif np.argmax(result) == 357:
            return SHAMP_BAGRATIONI_BILE_BRUT
        elif np.argmax(result) == 358:
            return SHAMP_BAGRATIONI_ROJ_NAPIVSOLOD
        elif np.argmax(result) == 359:
            return SHAMP_BAGRATIONI_GOLD_NAPIVSOLOD
        elif np.argmax(result) == 360:
            return SHAMP_BOLGRAD_BILE_BRUT
        elif np.argmax(result) == 361:
            return SHAMP_BOLGRAD_BILE_NAPIVSOLOD
        elif np.argmax(result) == 362:
            return SHAMP_BOLGRAD_NECTAR_BILE_SOLODKE
        elif np.argmax(result) == 363:
            return SHAMP_FRAN_BULV_BILE_NAPIVSUHE
        elif np.argmax(result) == 364:
            return SHAMP_FRAN_BULV_BILE_BRUT
        elif np.argmax(result) == 365:
            return SHAMP_FRAN_BULV_BILE_NAPIVSOLOD
        elif np.argmax(result) == 366:
            return STARIY_KOHETI_3
        elif np.argmax(result) == 367:
            return STARIY_KOHETI_5
        elif np.argmax(result) == 368:
            return STARIY_KOHETI_4
        elif np.argmax(result) == 369:
            return BRENDI_KOBLEVO_RESERVE_EXTRA_OLD_8_YEARS_05L
        elif np.argmax(result) == 370:
            return SHABO_VSOP_5
        elif np.argmax(result) == 371:
            return SHABO_VS_3
        elif np.argmax(result) == 372:
            return SHABO_1788_4
        elif np.argmax(result) == 373:
            return SHABO_1788_RESERV
        elif np.argmax(result) == 374:
            return SHABO_VS_RESERV
        elif np.argmax(result) == 375:
            return SHABO_VSOP_RESERV
        elif np.argmax(result) == 376:
            return AZNAURI_3
        elif np.argmax(result) == 377:
            return AZNAURI_5
        elif np.argmax(result) == 378:
            return AZNAURI_4
        elif np.argmax(result) == 379:
            return AZNAURI_BLACK_BARREL_5
        elif np.argmax(result) == 380:
            return ADJARI_3
        elif np.argmax(result) == 381:
            return ADJARI_5
        elif np.argmax(result) == 382:
            return ADJARI_4
        elif np.argmax(result) == 383:
            return HENNESY_VS
        elif np.argmax(result) == 384:
            return HENNESY_VSOP
        elif np.argmax(result) == 385:
            return ALEXX_GOLD_VSOP
        elif np.argmax(result) == 386:
            return ALEXX_SILVER_VS
        elif np.argmax(result) == 387:
            return ARARAT_5
        elif np.argmax(result) == 388:
            return ARARAT_AHTAMAR_10
        elif np.argmax(result) == 389:
            return ARARAT_3
        elif np.argmax(result) == 390:
            return ARARAT_NAIRI_20
        elif np.argmax(result) == 391:
            return GREEN_DAY_AIR_05L
        elif np.argmax(result) == 392:
            return GREEN_DAY_ULTRA_SOFT_05L
        elif np.argmax(result) == 393:
            return GREEN_DAY_ORGANIC_LIFE_05L
        elif np.argmax(result) == 394:
            return GREEN_DAY_CRYSTAL_05L
        elif np.argmax(result) == 395:
            return GREEN_DAY_05L
        elif np.argmax(result) == 396:
            return MEDOFF_CLASSIC_05L
        elif np.argmax(result) == 397:
            return SMIRNOFF_RED_05L
        elif np.argmax(result) == 398:
            return KOZACKA_RADA_CLASSIC_05L
        elif np.argmax(result) == 399:
            return KOZACKA_RADA_OSOBLIVA_05L
        elif np.argmax(result) == 400:
            return ZUBROWKA_BISON_GRASS_05L
        elif np.argmax(result) == 401:
            return ZUBROWKA_BIALA_05L
        elif np.argmax(result) == 402:
            return ZUBROWKA_CZARNA_05L
        elif np.argmax(result) == 403:
            return VOZDUH_LEGKA_05L
        elif np.argmax(result) == 404:
            return VOZDUH_ALPHA_05L
        elif np.argmax(result) == 405:
            return PERSHA_GILDIYA_VERHOVNA_05L
        elif np.argmax(result) == 406:
            return PERSHA_GILDIYA_ZNATNA_05L
        elif np.argmax(result) == 407:
            return PERSHA_GILDIYA_POVAJNA_05L
        elif np.argmax(result) == 408:
            return HLIB_DAR_CLASSIC_05L
        elif np.argmax(result) == 409:
            return HLIB_DAR_PROR_ZERNO_05L
        elif np.argmax(result) == 410:
            return HLIB_DAR_JITNYA_05L
        elif np.argmax(result) == 411:
            return HLIB_DAR_PSHENICHNA_05L
        elif np.argmax(result) == 412:
            return GREEN_DAY_ORGANIC_LIFE_07L
        elif np.argmax(result) == 413:
            return GREEN_DAY_07L
        elif np.argmax(result) == 414:
            return GREEN_DAY_ULTRA_SOFT_07L
        elif np.argmax(result) == 415:
            return GREEN_DAY_AIR_07L
        elif np.argmax(result) == 416:
            return GREEN_DAY_CRYSTAL_07L
        elif np.argmax(result) == 417:
            return MEDOFF_CLASSIC_07L
        elif np.argmax(result) == 418:
            return NEMIROFF_DELIKAT_MYAKA_07L
        elif np.argmax(result) == 419:
            return NEMIROFF_OSOBLIVA_SHTOF_07L
        elif np.argmax(result) == 420:
            return NEMIROFF_DELUXE_07L
        elif np.argmax(result) == 421:
            return NEMIROFF_LEX_07L
        elif np.argmax(result) == 422:
            return ZUBROWKA_07L
        elif np.argmax(result) == 423:
            return ZUBROWKA_CZARNA_07L
        elif np.argmax(result) == 424:
            return HETMAN_07L
        elif np.argmax(result) == 425:
            return KOZACKA_RADA_CLASSIC_07L
        elif np.argmax(result) == 426:
            return KOZACKA_RADA_PREMIUM_07L
        elif np.argmax(result) == 427:
            return KOZACKA_RADA_OSOBLIVA_07L
        elif np.argmax(result) == 428:
            return PERSHA_GILDIYA_POVAJNA_07L
        elif np.argmax(result) == 429:
            return PERSHA_GILDIYA_VERHOVNA_07L
        elif np.argmax(result) == 430:
            return PERSHA_GILDIYA_ZNATNA_07L
        elif np.argmax(result) == 431:
            return HLIB_DAR_CLASSIC_07L
        elif np.argmax(result) == 432:
            return MEDOFF_CLASSIC_1L
        elif np.argmax(result) == 433:
            return NEMIROFF_SHTOF_1L
        elif np.argmax(result) == 434:
            return NEMIROFF_DELICAT_SOFT_1L
        elif np.argmax(result) == 435:
            return ZUBROWKA_BISON_GRASS_1L
        elif np.argmax(result) == 436:
            return ZUBROWKA_BIALA_1L
        elif np.argmax(result) == 437:
            return HETMAN_1L
        elif np.argmax(result) == 438:
            return KOZACKA_RADA_OSOBLIVA_1L
        elif np.argmax(result) == 439:
            return KOZACKA_RADA_CLASSIC_1L
        elif np.argmax(result) == 440:
            return HLIB_DAR_CLASSIC_1L
        elif np.argmax(result) == 441:
            return SVINNE_REBRO
        elif np.argmax(result) == 442:
            return SALO
        elif np.argmax(result) == 443:
            return SVINNA_GOMILKA
        elif np.argmax(result) == 444:
            return SVIN_PECHINKA
        elif np.argmax(result) == 445:
            return SVIN_GULYASH
        elif np.argmax(result) == 446:
            return SVIN_PIDJARKA
        elif np.argmax(result) == 447:
            return SVIN_KOREYKA
        elif np.argmax(result) == 448:
            return SVIN_VIRIZKA
        elif np.argmax(result) == 449:
            return SVIN_LOPATKA_BEZ_KISTKI
        elif np.argmax(result) == 450:
            return SVIN_OKIST_BEZ_KISTKI
        elif np.argmax(result) == 451:
            return SVIN_FARSH
        elif np.argmax(result) == 452:
            return SVIN_BITOK_BEZ_KISTI
        elif np.argmax(result) == 453:
            return SVIN_RAGU
        elif np.argmax(result) == 454:
            return SVIN_OSHEYEK_BEZ_KISTKI
        elif np.argmax(result) == 455:
            return KURYACHA_CHETVERT
        elif np.argmax(result) == 456:
            return KURYACHE_STEGNO
        elif np.argmax(result) == 457:
            return KURYACHE_KRILO
        elif np.argmax(result) == 458:
            return KURYACHE_FILE
        elif np.argmax(result) == 459:
            return KURYACHA_GOMILKA
        elif np.argmax(result) == 460:
            return COCA_COLA_ORIGINAL_033_JB
        elif np.argmax(result) == 461:
            return COCA_COLA_ZERO_033_JB
        elif np.argmax(result) == 462:
            return FANTA_ORANGE_033_JB
        elif np.argmax(result) == 463:
            return FANTA_PINEAPPLE_033_JB
        elif np.argmax(result) == 464:
            return SPRITE_033_JB
        elif np.argmax(result) == 465:
            return COCA_COLA_ORIGINAL_025_GLASS
        elif np.argmax(result) == 466:
            return COCA_COLA_ZERO_025_GLASS
        elif np.argmax(result) == 467:
            return COCA_COLA_ORIGINAL_05_PL
        elif np.argmax(result) == 468:
            return COCA_COLA_ZERO_05_PL
        elif np.argmax(result) == 469:
            return FANTA_ORANGE_05_PL
        elif np.argmax(result) == 470:
            return SPRITE_05_PL
        elif np.argmax(result) == 471:
            return COCA_COLA_ORIGINAL_15_PL
        elif np.argmax(result) == 472:
            return COCA_COLA_ZERO_15_PL
        elif np.argmax(result) == 473:
            return SPRITE_15_PL
        elif np.argmax(result) == 474:
            return FANTA_ORANGE_15_PL
        elif np.argmax(result) == 475:
            return FANTA_SHOKATA_15_PL
        elif np.argmax(result) == 476:
            return FANTA_MANDARIN_15_PL
        elif np.argmax(result) == 477:
            return CHIPS_LUXE_BECON_133GR
        elif np.argmax(result) == 478:
            return CHIPS_LUXE_PAPRIKA_133GR
        elif np.argmax(result) == 479:
            return CHIPS_LUXE_CRAB_133GR
        elif np.argmax(result) == 480:
            return CHIPS_LUXE_SMETANA_CIBULYA_133GR
        elif np.argmax(result) == 481:
            return CHIPS_LUXE_SIR_133GR
        elif np.argmax(result) == 482:
            return CHIPS_LUXE_SIR_71GR
        elif np.argmax(result) == 483:
            return CHIPS_LUXE_BECON_71GR
        elif np.argmax(result) == 484:
            return CHIPS_LUXE_PAPRIKA_71GR
        elif np.argmax(result) == 485:
            return CHIPS_LUXE_CRAB_71GR
        elif np.argmax(result) == 486:
            return CHIPS_LUXE_SMETANA_CIBULYA_71GR
        elif np.argmax(result) == 487:
            return CHIPS_LUXE_HVIL_LISICHKI_125GR
        elif np.argmax(result) == 488:
            return CHIPS_LUXE_SMETANA_CIBULYA_183GR
        elif np.argmax(result) == 489:
            return CHIPS_LUXE_BECON_183GR
        elif np.argmax(result) == 490:
            return CHIPS_LUXE_SIR_183GR
        elif np.argmax(result) == 491:
            return CHIPS_PRINGLES_GREECE_SOUCE_CACIKI_185GR
        elif np.argmax(result) == 492:
            return CHIPS_PRINGLES_PAPRIKA_165GR
        elif np.argmax(result) == 493:
            return CHIPS_PRINGLES_PIZZA_PEPERONI_185GR
        elif np.argmax(result) == 494:
            return CHIPS_PRINGLES_SIR_CIBULYA_165GR
        elif np.argmax(result) == 495:
            return CHIPS_PRINGLES_ORIGINAL_165GR
        elif np.argmax(result) == 496:
            return CHIPS_PRINGLES_SIR_165GR
        elif np.argmax(result) == 497:
            return CHIPS_LAYS_PAPRIKA_120GR
        elif np.argmax(result) == 498:
            return CHIPS_LAYS_CRAB_120GR
        elif np.argmax(result) == 499:
            return CHIPS_LAYS_SIR_60GR
        elif np.argmax(result) == 500:
            return SIR_SVET_FETA_UKR_ROZSIL_45_1KG
        elif np.argmax(result) == 501:
            return OLIVKI_EXTRA_CHORNI_BEZ_KIST_300GR
        elif np.argmax(result) == 502:
            return OLIV_OIL_POVNA_CHASHA_913GR
        elif np.argmax(result) == 503:
            return BASILIK_CHERVONIY_SVIJIY
        elif np.argmax(result) == 504:
            return PELMENI_GERKULES_FIRM_400GR
        elif np.argmax(result) == 505:
            return PELMENI_GERKULES_FIRM_800GR
        elif np.argmax(result) == 506:
            return PELMENI_GERKULES_INDEYKA_400GR
        elif np.argmax(result) == 507:
            return PELMENI_TRI_VEDMEDI_FIRM_800GR
        elif np.argmax(result) == 508:
            return PELMENI_TRI_VEDMEDI_MISHUTKA_TELYATINA_400GR
        elif np.argmax(result) == 509:
            return PELMENI_EXTRA_FIRM_800GR
        elif np.argmax(result) == 510:
            return PELMENI_EXTRA_SIBIR_500GR
        elif np.argmax(result) == 511:
            return PELMENI_EXTRA_RAVIOLI_DOMASHNIE_800GR