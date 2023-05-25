import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from keras import optimizers
import matplotlib.pyplot as plt

import keras
from tensorflow import keras
from keras.layers import Flatten, Dense
from keras.applications import VGG16
from keras.preprocessing.image import ImageDataGenerator


class GroceryAppPhoto:
    '''Класс для обучения сверточной НС, которая распознает товар на изображениях пользователя,
     которые он загружает на сайт GroceryApp.
     Использована комбинация: предобученная сверточная НС VGG-16 на данных ImageNet в связке
     с обученным с нуля классификатором (полносвязная НС прямого распределения).
     Так же применен метод выделения признаков и расширения, т.к. обучающая выборка невелика.'''

    # загружаем данные:
    base_dir = '/home/andrey/grocery_data'
    train_dir = os.path.join(base_dir, 'train')
    validation_dir = os.path.join(base_dir, 'validation')
    test_dir = os.path.join(base_dir, 'test')

    def prepearing_data(self):
        '''Метод для подготовки данных перед обучением НС'''

        # создание генераторов, преобразующих изображения в нужные тензоры:
        train_datagen = ImageDataGenerator(
            rescale=1. / 255,
            rotation_range=40,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            fill_mode='nearest'
        )

        test_datagen = ImageDataGenerator(rescale=1. / 255)

        train_generator = train_datagen.flow_from_directory(
            self.train_dir,
            target_size=(150, 150),
            batch_size=20,
            class_mode='categorical'
        )

        validation_generator = test_datagen.flow_from_directory(
            self.validation_dir,
            target_size=(150, 150),
            batch_size=20,
            class_mode='categorical'
        )

        test_generator = test_datagen.flow_from_directory(
            self.test_dir,
            target_size=(150, 150),
            batch_size=20,
            class_mode='categorical'
        )

        return train_generator, validation_generator, test_generator

    def __init__(self):
        '''Инициализация НС, ее компиляция и обучение.'''

        # создадим сверточную базу на основе vgg16:
        self.conv_base = VGG16(
            weights='imagenet',
            include_top=False,
            input_shape=(150, 150, 3)
        )

        # создадим нашу модель НС со сверточной базой vgg16:

        self.model = keras.Sequential([
            self.conv_base,
            Flatten(),
            Dense(512, activation='relu'),      #было 256 слоев
            Dense(54, activation='softmax')
        ])

        # заморозим сверточную базу:
        self.conv_base.trainable = True

        # добавленный кусок кода для дообучения
        set_trainable = False
        for layer in self.conv_base.layers:
            if layer.name == 'block5_conv1':
                set_trainable = True
        if set_trainable:
            layer.trainable = True
        else:
            layer.trainable = False
        # конец куска кода

        # настраиваем модель НС перед обучением:
        self.model.compile(
            loss='categorical_crossentropy',
            optimizer=optimizers.RMSprop(learning_rate=1e-5),
            metrics=['accuracy']
        )

        train_generator, validation_generator, test_generation = self.prepearing_data()

        # обучаем НС:
        self.history = self.model.fit(
            train_generator,
            steps_per_epoch=25,
            epochs=35,             #было 25 эпох
            validation_data=validation_generator,
            validation_steps=10
        )

        #сохраняем модель обученной НС:
        self.model.save('my_model_photo')           #сохранил не как h5!!!
        print('Обучение НС успешно завершено.')

    def model_value(self):
        '''Метод, выводящий на экран точность и потери НС на тестовых данных'''

        train_generator, validation_generator, test_generator = self.prepearing_data()
        test_loss, test_acc = self.model.evaluate(test_generator, steps=5)
        print("Точность и потери модели на тестовых изображениях")
        print('---------------------------------------------------')
        print(f'Точость модели: {test_acc * 100}')
        print(f'Потери модели: {test_loss * 100}')

    def show_loss_acc_graphics(self):
        '''Метод, строящий графики точности и потерь при обучении НС.'''

        acc = self.history.history['accuracy']
        val_acc = self.history.history['val_accuracy']
        loss = self.history.history['loss']
        val_loss = self.history.history['val_loss']
        epochs = range(1, len(acc) + 1)
        plt.plot(epochs, acc, 'bo', label='Training acc')
        plt.plot(epochs, val_acc, 'b', label='Validation acc')
        plt.title('Training and validation accuracy')
        plt.legend()
        plt.figure()
        plt.plot(epochs, loss, 'bo', label='Training loss')
        plt.plot(epochs, val_loss, 'b', label='Validation loss')
        plt.title('Training and validation loss')
        plt.legend()
        plt.show()

    def show_model_architecture(self):
        '''Метод, выводящий в консоль архитектуру модели НС.'''

        print(self.model.summary())

    def identify_item(self, item_path):
        '''Метод, распознающий товар на изображении пользователя.'''

        # создадим генератор и преобразовываем изображение в нужный тензор:
        user_pic_datagen = ImageDataGenerator(rescale=1. / 255)

        user_pic_generator = user_pic_datagen.flow_from_directory(
            item_path,
            target_size=(150, 150),
            batch_size=2,
            class_mode='categorical'
        )

        for data_batch, labels_batch in user_pic_generator:
            print(f'data batch shape :{data_batch.shape}')
            print(f'labels batch shape :{labels_batch.shape}')
            break

        result = self.model.predict(user_pic_generator)
        print(result)
        # if result > 0.5:
        #     print('На изображении пиво "Оболонь Премиум 1.1 л"')
        # else:
        #     print('На изображении водка "Гетьман Сагайдачний 0,7"')


user_Andrey = GroceryAppPhoto()

