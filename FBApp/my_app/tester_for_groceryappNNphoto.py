import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model


class TesterForGroceryAppPhoto:

    def identify_item(self, item_path):
        '''Класс для тестирования обученной на моих фото продуктов и сохраненной НС.
        Повторяет все тоже без процесса обучения (заново).'''

        #загружаем мою обученную модель НС:
        model = load_model('/home/andrey/GroceryAppVol3/FBApp/my_app/my_model_photo')

        # создадим генератор и преобразовываем изображение в нужный тензор
        user_pic_datagen = ImageDataGenerator(rescale=1. / 255)

        user_pic_generator = user_pic_datagen.flow_from_directory(
            item_path,
            target_size=(150, 150),
            batch_size=2,
            class_mode='categorical'
        )


        result = model.predict(user_pic_generator)
        # if result >0.5:
        #     return 'Пиво "Оболонь Премиум 1.1 л"'
        # else:
        #     return 'Водка "Гетьман ICE 0,7 л"'

        if np.argmax(result) == 1:
            return 'Водка "Гетьман ICE 0,7 л"'
        elif np.argmax(result) == 2:
            return 'Пиво "Львовское светлое", 2.4 литра'
        elif np.argmax(result) == 5:
            return 'Яблоко "Черный принц"'
        elif np.argmax(result) == 3:
            return 'Пиво "Оболонь Премиум Экстра 1.1 л"'
        elif np.argmax(result) == 4:
            return 'Масло подсолнечное "Щедрый Дар" 0,85 л'
        elif np.argmax(result) == 0:
            return 'Напиток безалкогольный "Coca-Cola" 2 л'
        elif np.argmax(result) == 6:
            return 'Яблоко Гала, кг'
        elif np.argmax(result) == 9:
            return 'Пена для бритья "Arko Sensitive" 300 гр+100'
        elif np.argmax(result) == 8:
            return 'Пена для бритья "Arko Cool" 300 гр+100'
        elif np.argmax(result) == 11:
            return "Морковь, кг"
        elif np.argmax(result) == 10:
            return 'Кофе растворимый "Aroma Gold Classic 100 грамм"'
        elif np.argmax(result) == 7:
            return 'Яблоко Голден, 1 кг'
        elif np.argmax(result) == 12:
            return 'Сырок плавленный "Комо Паприкаш"'
        elif np.argmax(result) == 13:
            return 'Чипсы Lays с солью большая пачка 30 грамм'
        elif np.argmax(result) == 14:
            return 'Кофе Арома Голд Freeze Dried 70 грамм'
        elif np.argmax(result) == 15:
            return 'Дезодорант Garnier весенняя свежесть'
        elif np.argmax(result) ==16:
            return 'Дрожжи "Харьковские", 100 гр'
        elif np.argmax(result) == 17:
            return 'Яйца куринные, 10 шт'
        elif np.argmax(result) ==18:
            return 'Моющее средство Fairy'
        elif np.argmax(result)==19:
            return 'Напиток Fanta 2 литра'
        elif np.argmax(result)==20:
            return 'Капуста белокачанная, кг'
        elif np.argmax(result)==21:
            return 'Дезодорант Garnier Магний мужской'
        elif np.argmax(result)==22:
            return 'Горчица "Колос"'
        elif np.argmax(result)==23:
            return 'Горчица Верес украинска мицна 120 грамм'
        elif np.argmax(result) == 24:
            return 'Чеснок, кг'
        elif np.argmax(result) == 25:
            return 'Сигареты "Kent 8"'
        elif np.argmax(result) == 26:
            return 'Кетчуп Торчин с чесноком 270 гр'
        elif np.argmax(result) == 27:
            return 'Лимон, кг'
        elif np.argmax(result) == 28:
            return 'Сигареты Marlboro red'
        elif np.argmax(result) == 29:
            return 'Майонез Королевский Смак королевский 67 % 300 гр'
        elif np.argmax(result) == 30:
            return 'Майонез домашний детский "Щедро" 67%'
        elif np.argmax(result) == 31:
            return 'Мука ЗОЛОТЕ ЗЕРНЯТКО пшеничное 2 кг'
        elif np.argmax(result) == 32:
            return 'Масло подсолнечное "Олейна" нерафинированное, 850 гр'
        elif np.argmax(result) == 33:
            return 'Лук, 1 кг'
        elif np.argmax(result) == 34:
            return 'Дезодорант "Rexona Aloe Vera" женский'
        elif np.argmax(result) == 35:
            return 'Сметана Галичанская 15% 370 грамм'
        elif np.argmax(result) == 36:
            return 'Сметана Столица Смаку 400 гр 15% жирности'
        elif np.argmax(result) == 37:
            return 'Сметана "Столица Смаку" 20% 400 гр'
        elif np.argmax(result) == 38:
            return 'Напиток Sprite 2 литра'
        elif np.argmax(result) == 39:
            return 'Чай черный "Мономах Кения", 90 гр'
        elif np.argmax(result) == 40:
            return 'Чай "Минутка" черный, 40 пакетиков'
        elif np.argmax(result) == 41:
            return 'Чай Мономах 100% Цейлон Original черный крупнолистовой'
        elif np.argmax(result) == 42:
            return 'Чай Мономах Цейлон черный'
        elif np.argmax(result) == 43:
            return 'Туалетная бумага "Киев" 63 м'
        elif np.argmax(result) == 44:
            return 'Соус Чумак чесночный 200 грамм'
        elif np.argmax(result) == 45:
            return 'Жвачка Orbit полуниця-банан'
        elif np.argmax(result) == 46:
            return 'Сигареты LM красные'
        elif np.argmax(result) == 47:
            return 'Кетчуп Торчин до шашлику 270 грамм'
        elif np.argmax(result) == 48:
            return 'Майонез Чумак аппетитный 50% 300 грамм'
        elif np.argmax(result) == 49:
            return 'Колбаса Перша Столиця Салями Фирменная высший сорт'
        elif np.argmax(result) == 50:
            return 'Кофе Чорна Карта GOLD 50 грамм'
        elif np.argmax(result) == 51:
            return 'Пиво Zibert светлое 0,5 л в банке'
        elif np.argmax(result) == 52:
            return 'Йогурт Фанни 240 грамм 1.5% лесовые ягоды'
        elif np.argmax(result) == 53:
            return 'Кефир Славия 2,5% 850 грамм'


# user_Andrey = TesterForGroceryAppPhoto()
# item_image = '/home/andrey/grocery_data/predicts'
# user_Andrey.identify_item(item_image)