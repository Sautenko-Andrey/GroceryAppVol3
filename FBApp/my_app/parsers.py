import undetected_chromedriver
from selenium.webdriver.common.by import By
from my_app.utils import price_updating_data


class ProductParserVol2:
    '''Класс для парсинга цен с сайтов с приминением Selenium'''

    # количество досуипных маркетов
    COUNT_MARKETS = 3

    SELECTOR = By.CSS_SELECTOR
    ATB_REGULAR_DIV_CLASS = '[class="product-price__top"]'

    # старые div у эко
    # EKO_REGULAR_DIV_CLASS = '[class="jsx-2be52a4b5bdfcc8a Price__value_title"]'
    # EKO_DISCOUNT_DIV_CLASS = '[class="jsx-2be52a4b5bdfcc8a Price__value_title Price__value_discount"]'

    # новые div у эко
    EKO_NEW_REGULAR_DIV = '[class="jsx-906554f8658dceda Price__value_title"]'
    EKO_NEW_DISCOUNT_DIV = '[class="jsx-906554f8658dceda Price__value_title Price__value_discount"]'

    VARUS_REGULAR_DIV_CLASS = '[class="sf-price__regular"]'
    VARUS_SPECIAL_DIV_CLASS = '[class="sf-price__special"]'
    VARUS_DISCOUNT_DIV_CLASS = '[class="jsx-161433026 Price__value_title Price__value_discount"]'
    VARUS_REGULAR_SPAN_CLASS = '[class="jsx-2be52a4b5bdfcc8a Price__value_title"]'
    SILPO_REGULAR_DIV_CLASS = '[class="current-integer"]'
    ASHAN_DIV_CLASS = '[class="productDetails_price_actual__12u8E"]'
    NOVUS_DIV_CLASS = '[class="product-card__price-current h4"]'
    NOVUS_SPECIAL_DIV_CLASS = '[class="product-card__price-current h4 product-card__price-current_red"]'

    # старый div метро
    # METRO_REGULAR_DIV_CLASS='[class="jsx-2be52a4b5bdfcc8a Price__value_title"]'
    # новый div метро
    NEW_METRO_REGULEAR_DIV = '[class="jsx-906554f8658dceda Price__value_title"]'

    NASH_KRAY_DIV_CLASS = '[class="nice_price"]'
    FOZZY_REGULAR_DIV_CLASS = '[class="current-price"]'

    __slots__ = ("options", "driver", "atb_price", "eko_price", "varus_price",
                 "silpo_price", "ashan_price", "novus_price", "metro_price",
                 "nash_kray_price", "fozzy_price")

    def __init__(self):
        '''Инииализация драйвера Chrome со всеми нужными параметрами,
        а именно включение режима работы браузера в фоновом режиме'''

        self.options = undetected_chromedriver.ChromeOptions()
        # self.options.add_argument('enable-features=NetworkServiceInProcess')
        self.options.add_argument("disable-features=NetworkService")  # если верхнее не работает,то включаем это
        # last arguments
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--dns-prefetch-disable")
        # end last arguments
        self.options.add_argument('--headless')
        # новая опция из-за ошибки при парсинге
        self.options.add_argument("--disable-site-isolation-trials")
        # конец новой опции
        self.driver = undetected_chromedriver.Chrome(options=self.options)

    def check_comma(self, text: str):
        price = text[:5]
        price = float(price.replace(',', '.'))
        return price

    def prices_parsing(self, urls: list) -> list:

        # задаем изначальный список с ценами во всех маркетах по нулям
        results = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        # части(начала) адресов страниц магазинов (url)
        atb_url_name_short = 'https://www.atb'
        atb_url_name_long = 'https://atbmarket'
        eko_url_name = 'https://eko'
        varus_url_name = 'https://varus'
        silpo_url_name = 'https://shop.silpo'
        ashan_url_name = 'https://auchan'
        novus_url_name = 'https://novus.online'
        metro_url_name = 'https://metro.zakaz.ua'
        nk_url_name = 'https://shop.nashkraj.ua'
        fozzy_url_name = 'https://fozzyshop.ua'

        # срезы для адресов магазинов
        atb_url_slice_short = slice(0, 15)  # ранвосильно срезу[:15]
        atb_url_slice_long = slice(0, 17)  # ранвосильно срезу[:17]
        eko_url_slice = slice(0, 11)
        varus_url_slice = slice(0, 13)
        silpo_url_slice = slice(0, 18)
        ashan_url_slice = slice(0, 14)
        novus_url_slice = slice(0, 20)
        metro_url_slice = slice(0, 22)
        nk_url_slice = slice(0, 24)
        fozzy_url_slice = slice(0, 20)

        # время задержки при парсинге 5 секунд
        waiting_time = 5
        long_waiting_time = 15

        # номера индексов магазинов в списке с ценами по порядку
        atb_index = 0
        eko_index = 1
        varus_index = 2
        silpo_index = 3
        ashan_index = 4
        novus_index = 5
        metro_index = 6
        nk_index = 7
        fozzy_index = 8

        '''Парсинг цен для продукта сразу со всех досутпных маркетов.'''
        for url in urls:
            if url[atb_url_slice_short] == atb_url_name_short or url[atb_url_slice_long] == atb_url_name_long:
                # парсим цену АТБ
                self.driver.get(url)
                try:
                    self.atb_price = self.driver.find_element(self.SELECTOR, self.ATB_REGULAR_DIV_CLASS).text
                    self.driver.implicitly_wait(waiting_time)
                    self.atb_price = price_updating_data(self.atb_price)
                    results[atb_index] = self.atb_price
                except Exception as ex:
                    print(ex)
            elif url[eko_url_slice] == eko_url_name:
                # парсим цену ЭКО
                self.driver.get(url)
                try:
                    self.eko_price = self.driver.find_element(self.SELECTOR, self.EKO_NEW_REGULAR_DIV).text
                    # self.driver.implicitly_wait(5)
                    results[eko_index] = float(self.eko_price[:5])  # берем только первые 5 символов включая точку
                except Exception as ex:
                    print(ex)
                    if ex:
                        try:
                            self.eko_price = self.driver.find_element(self.SELECTOR, self.EKO_NEW_DISCOUNT_DIV).text
                            self.driver.implicitly_wait(waiting_time)
                            results[eko_index] = float(
                                self.eko_price[:5])  # берем только первые 5 символов включая точку
                        except Exception as ex:
                            print(ex)
            elif url[varus_url_slice] == varus_url_name:
                # парсим цену Varus
                self.driver.get(url)
                try:
                    self.varus_price = self.driver.find_element(self.SELECTOR, self.VARUS_REGULAR_DIV_CLASS).text
                    self.driver.implicitly_wait(waiting_time)
                    results[varus_index] = float(self.varus_price[:5])  # берем только первые 5 символов включая точку
                except Exception as ex:
                    print(ex)
                    if ex:
                        try:
                            self.varus_price = self.driver.find_element(self.SELECTOR,
                                                                        self.VARUS_SPECIAL_DIV_CLASS).text
                            self.driver.implicitly_wait(waiting_time)
                            results[varus_index] = float(
                                self.varus_price[:5])  # берем только первые 5 символов включая точку
                        except Exception as ex:
                            print(ex)
                            if ex:
                                try:
                                    self.varus_price = self.driver.find_element(self.SELECTOR,
                                                                                self.VARUS_DISCOUNT_DIV_CLASS).text
                                    self.driver.implicitly_wait(waiting_time)
                                    results[varus_index] = float(self.varus_price[:5])
                                except Exception as ex:
                                    print(ex)
                                    if ex:
                                        try:
                                            self.varus_price = self.driver.find_element(self.SELECTOR,
                                                                                        self.VARUS_REGULAR_SPAN_CLASS).text
                                            self.driver.implicitly_wait(waiting_time)
                                            results[varus_index] = float(self.varus_price[:5])
                                        except Exception as ex:
                                            print(ex)
            elif url[silpo_url_slice] == silpo_url_name:
                # парсим цену Сильпо
                self.driver.get(url)
                try:
                    self.silpo_price = self.driver.find_element(self.SELECTOR, self.SILPO_REGULAR_DIV_CLASS).text
                    self.driver.implicitly_wait(waiting_time)
                    results[silpo_index] = float(self.silpo_price[:5])  # берем только первые 5 символов включая точку
                except Exception as ex:
                    print(ex)
            elif url[ashan_url_slice] == ashan_url_name:
                # парсим цену Ашан
                self.driver.get(url)
                try:
                    self.ashan_price = self.driver.find_element(self.SELECTOR, self.ASHAN_DIV_CLASS).text
                    self.driver.implicitly_wait(waiting_time)
                    self.ashan_price = price_updating_data(self.ashan_price)
                    results[ashan_index] = self.ashan_price
                except Exception as ex:
                    print(ex)
            elif url[novus_url_slice] == novus_url_name:
                # парсим цену Novus
                self.driver.get(url)
                try:
                    self.novus_price = self.driver.find_element(self.SELECTOR, self.NOVUS_DIV_CLASS).text
                    self.driver.implicitly_wait(waiting_time)
                    results[novus_index] = float(self.novus_price[:5])
                except Exception as ex:
                    print(ex)
                    if ex:
                        try:
                            self.novus_price = self.driver.find_element(self.SELECTOR,
                                                                        self.NOVUS_SPECIAL_DIV_CLASS).text
                            self.driver.implicitly_wait(waiting_time)
                            results[novus_index] = float(self.novus_price[:5])
                        except Exception as ex:
                            print(ex)
            elif url[metro_url_slice] == metro_url_name:
                # парсим цену Метро
                self.driver.get(url)
                try:
                    self.metro_price = self.driver.find_element(self.SELECTOR, self.NEW_METRO_REGULEAR_DIV).text
                    self.driver.implicitly_wait(waiting_time)
                    results[metro_index] = float(self.metro_price[:5])
                except Exception as ex:
                    print(ex)
            elif url[nk_url_slice] == nk_url_name:
                # парсим цену Наш Край
                self.driver.get(url)
                try:
                    self.nash_kray_price = self.driver.find_element(self.SELECTOR, self.NASH_KRAY_DIV_CLASS).text
                    self.driver.implicitly_wait(waiting_time)
                    self.nash_kray_price = price_updating_data(self.nash_kray_price)
                    results[nk_index] = self.nash_kray_price
                except Exception as ex:
                    print(ex)
            elif url[fozzy_url_slice] == fozzy_url_name:
                # парсим цену Fozzy
                self.driver.get(url)
                try:
                    self.fozzy_price = self.driver.find_element(self.SELECTOR, self.FOZZY_REGULAR_DIV_CLASS).text
                    self.driver.implicitly_wait(waiting_time)
                    self.fozzy_price = price_updating_data(self.fozzy_price)
                    results[fozzy_index] = self.fozzy_price
                except Exception as ex:
                    print(ex)

        return results

    def obolon_premium_parser(self):
        '''Парсер для сбора данных о цене продукта "Оболонь Премиум Экстра 1.1 л"'''
        return self.prices_parsing(
            ['https://www.atbmarket.com/product/pivo-11l-obolon-premium-extra-brew-svitle-alk-46',
             'https://eko.zakaz.ua/uk/products/pivo-obolon-1100ml-ukrayina--04820000190008/'])

    def vodka_getman_ICE_parcer(self):
        '''Парсер для сбора данных о цене продукта "Водка Гетьман ICE 0,7 л"'''
        return self.prices_parsing(['https://www.atbmarket.com/product/gorilka-05l-getman-ice-40'])

    def coca_cola_2l_parcer(self):
        '''Парсер для сбора данных о цене продукта "напиток Coca-Cola 2 л"'''
        return self.prices_parsing(
            ['https://www.atbmarket.com/product/napij-225-l-coca-cola-bezalkogolnij-silnogazovanij',
             'https://eko.zakaz.ua/uk/products/napii-koka-kola-2000ml--05449000009067/',
             'https://varus.ua/napiy-coca-cola-silnogazovaniy-2-l',
             'https://shop.silpo.ua/product/napii-coca-cola-117',
             'https://auchan.ua/ua/napitok-bezalkogol-nyj-sil-nogazirovannyj-coca-cola-p-but-2l-688465/',
             'https://novus.online/product/napij-gazovanij-coca-cola-2l',
             'https://metro.zakaz.ua/uk/products/napii-koka-kola-2000ml--05449000009067/',
             'https://shop.nashkraj.ua/kovel/product/7588-napiy-koka-kola-2l',
             'https://fozzyshop.ua/ru/voda-sladkaya-gazirovannaya/12865-napitok-coca-cola-5449000009067.html'])

    def garlik_parcer(self):
        '''Парсер для сбора данных о цене продукта "Чеснок, кг" '''
        return self.prices_parsing(['https://www.atbmarket.com/product/casnik-import-1-gat',
                                    'https://eko.zakaz.ua/uk/products/ovochi-chasnik--ekomarket00000000640012/',
                                    'https://varus.ua/chasnik-vag',
                                    'https://shop.silpo.ua/product/chasnyk-32595',
                                    'https://novus.online/product/casnik-vag',
                                    'https://shop.nashkraj.ua/kovel/product/40072-chasnik-vag',
                                    'https://fozzyshop.ua/ru/ovoshhi/11587-chesnok-6925307588881.html'])

    def tea_minutka_black_40_b_parcer(self):
        '''Парсер для сбора данных о цене продукта "Чай Минутка, 40 п, черный"'''
        return self.prices_parsing(
            ['https://www.atbmarket.com/product/caj-40-fp-h-14-g-minutka-black-tea-cornij-z-bergamotom-polsa',
             'https://eko.zakaz.ua/uk/products/chai-56g--05900396000972/',
             'https://metro.zakaz.ua/uk/products/chai-56g--05900396000972/'])

    def apple_golden_parcer(self):
        '''Парсер для сбора данных о цене продукта яблоко Голден'''
        return self.prices_parsing(['https://www.atbmarket.com/product/abluko-golden-1-gat',
                                    'https://eko.zakaz.ua/uk/products/frukt-iabluka--ekomarket00000000641182/',
                                    'https://varus.ua/yabluko-golden-1-gatunok-vag',
                                    'https://shop.silpo.ua/product/yabluko-golden-zakarpattia-516860',
                                    'https://metro.zakaz.ua/uk/products/frukt-iabluka--metro28417100000000/',
                                    'https://shop.nashkraj.ua/kovel/product/170200-yabluka-golden-vag',
                                    'https://fozzyshop.ua/ru/frukty-i-yagody/11814-yabloko-golden-0250005543877.html'])

    def kent_8_parcer(self):
        '''Парсер для сбора данных о цене продукта сигареты Кент 8'''
        return self.prices_parsing(['https://www.atbmarket.com/product/sigareti-kent-silver-25',
                                    'https://eko.zakaz.ua/uk/products/tsigarki-kent--04820192683371/',
                                    'https://varus.ua/cigarki-kent-navy-blue-4-0-8-08',
                                    'https://shop.silpo.ua/product/tsygarky-kent-nd-navy-blue-907151',
                                    'https://auchan.ua/ua/sigarety-kent-blue-20-sht-917269/',
                                    'https://novus.online/product/cigarki-kent-blue-futura-8',
                                    'https://fozzyshop.ua/ru/sigarety/98899-sigarety-kent-navy-blue-0250014852113.html'])

    def coffee_aroma_gold_parcer(self):
        '''Парсер для сбора данных о цене продукта кофе растовримый Арома Голд'''
        return self.prices_parsing(['https://eko.zakaz.ua/uk/products/kava--04771632312880/'])

    def oil_shedriy_dar_850_parcer(self):
        '''Парсер для сбора данных о цене продукта
         "Масло подсолнечное рафинированное Щедрый Дар 850 мл"'''
        return self.prices_parsing(['https://www.atbmarket.com/product/olia-085l-sedrij-dar-sonasnikova-rafinovana',
                                    'https://eko.zakaz.ua/uk/products/oliia-shchedrii-dar-850ml--04820078575769/',
                                    'https://shop.silpo.ua/product/oliia-soniashnykova-shchedryi-dar-rafinovana-dezodorovana-890082',
                                    'https://auchan.ua/ua/maslo-podsolnechnoe-schedrij-dar-rafinirovannoe-850-ml-934363/',
                                    'https://novus.online/product/olia-sonasnikova-rafinovana-dezodarovana-sedrij-dar-087l-pet',
                                    'https://metro.zakaz.ua/uk/products/oliia-shchedrii-dar-850ml--04820078575769/',
                                    'https://fozzyshop.ua/ru/maslo-podsolnechnoe/94784-maslo-podsolnechnoe-shhedrij-dar-rafinirovannoe-dezodorirovannoe-4820078575776.html'])

    def fairy_limon_500_parcer(self):
        '''Парсер для сбора данных о цене продукта "Fairy лимон, 500 млг"'''
        return self.prices_parsing(
            ['https://www.atbmarket.com/product/zasib-miucij-dla-posudu-05l-fairy-sokovitij-limon',
             'https://eko.zakaz.ua/uk/products/zasib-feiri-500ml-ukrayina--05413149313842/',
             'https://varus.ua/zasib-d-posudu-sokovit-limon-fairy-500ml',
             'https://shop.silpo.ua/product/zasib-dlia-myttia-posudu-fairy-sokovytyi-lymon-48923',
             'https://novus.online/product/zasib-dla-mitta-posudu-fairy-plus-limon-500ml',
             'https://metro.zakaz.ua/uk/products/zasib-feiri-500ml-ukrayina--05413149313842/',
             'https://fozzyshop.ua/ru/dlya-ruchnogo-mytya-posudy/15384-sredstvo-dlya-mytya-posudy-fairy-plus-limon-5413149313842.html'])

    def onion_parcer(self):
        '''Парсер для сбора данных о цене продукта лук'''
        return self.prices_parsing(['https://www.atbmarket.com/product/cibula-ripcasta-1-gat',
                                    'https://eko.zakaz.ua/uk/products/ovochi-tsibulia--ekomarket00000000647281/',
                                    'https://varus.ua/cibulya-ripchasta-1-gatunok-vag',
                                    'https://shop.silpo.ua/product/tsybulia-ripchasta-zhovta-32573',
                                    'https://novus.online/product/cibula-vag',
                                    'https://metro.zakaz.ua/uk/products/ovochi-tsibulia--metro28960000000000/',
                                    'https://shop.nashkraj.ua/kovel/product/13435-tsibulya-ripchasta-vag',
                                    'https://fozzyshop.ua/ru/ovoshhi/11520-luk-repchatyj-zheltyj-2732573.html'])

    def apple_black_prince_parcer(self):
        '''Парсер для сбора данных о цене продукта "Яблоко Черный Принц"'''
        return self.prices_parsing(['https://www.atbmarket.com/product/abluko-red-princ-1gat',
                                    'https://eko.zakaz.ua/uk/products/frukt-iabluka-bez-tm--ekomarket00000000645795/',
                                    'https://varus.ua/yabloko-princ-vag',
                                    'https://shop.silpo.ua/product/yabluko-red-prynts-523750',
                                    'https://metro.zakaz.ua/uk/products/frukt-iabluka--metro28632200000000/',
                                    'https://fozzyshop.ua/ru/frukty-i-yagody/22864-yabloko-red-princ-2778989.html'])

    def smetana_stolica_smaky_400_20(self):
        '''Парсер для сбора данных о цене продукта "Сметана Столиця Смаку 400 гр 20% жирности"'''
        return self.prices_parsing(['https://varus.zakaz.ua/uk/products/ukrayina--04820194043531/'])

    def limon_parcer(self):
        '''Парсер для сбора данных о цене продукта лимон'''
        return self.prices_parsing(['https://atbmarket.com/product/limon-1-gat',
                                    'https://eko.zakaz.ua/uk/products/frukt-tsitrus--ekomarket00000000650210/',
                                    'https://varus.ua/limon-vag',
                                    'https://shop.silpo.ua/product/lymon-32550',
                                    'https://novus.online/product/limon-majer-vag',
                                    'https://metro.zakaz.ua/uk/products/frukt-tsitrus--metro28255100000000/',
                                    'https://shop.nashkraj.ua/kovel/product/20991-limon-vag',
                                    'https://fozzyshop.ua/ru/frukty-i-yagody/11775-limon-2732550.html'])

    def oil_oleyna_neraf_850_parcer(self):
        '''Парсер для сбора данных о цене продукта
        "Масло подсолнечное Олейна нерафинированное 850 гр"'''
        return self.prices_parsing(['https://eko.zakaz.ua/uk/products/oliia-oleina-900ml--04820077083500/',
                                    'https://auchan.ua/ua/maslo-podsolnechnoe-olejna-dushistoe-850-ml-665297/'])

    def tea_monomah_black_kenya_90_parcer(self):
        '''Парсер для сбора данных о цене продукта
         "Чай черный листовой Мономах Кения 90 гр"'''
        return self.prices_parsing(['https://eko.zakaz.ua/uk/products/chai-monomakh-90g--04820097812197/'])

    def arko_cool_200_bonus100_parcer(self):
        '''Парсер для сбора данных о цене продукта
        "Пена для бритья ARKO Cool 300 млг+100млг бонус"'''
        return self.prices_parsing(['https://atbmarket.com/product/pina-dla-golinna-200100-ml-arko-men-cool',
                                    'https://eko.zakaz.ua/uk/products/pina-arko-200ml--08690506090029/',
                                    'https://varus.ua/pina-dlya-golinnya-kul-arko-200ml',
                                    'https://shop.silpo.ua/product/pina-dlia-golinnia-arko-prokholoda-166950',
                                    'https://auchan.ua/ua/pena-dlja-brit-ja-arko-men-cool-200-ml-253128/',
                                    'https://novus.online/product/pina-dla-golinna-arco-proholoda-200ml',
                                    'https://metro.zakaz.ua/uk/products/pina-arko-200ml--08690506090029/',
                                    'https://fozzyshop.ua/ru/muzhskie-sredstva-dlya-britya-i-kosmetika/39096-pena-dlya-britya-arko-prokhlada-8690506090029.html'])

    def arko_sensitive_200_bonus100_parcer(self):
        '''Парсер для сбора данных о цене продукта
        "Пена для бритья ARKO Cool 300 млг+100млг бонус"'''
        return self.prices_parsing(
            ['https://www.atbmarket.com/product/pina-dla-golinna-200100-ml-arko-men-sensitive-promo',
             'https://eko.zakaz.ua/uk/products/pina-arko-200ml--08690506090043/',
             'https://varus.ua/pina-dlya-golinnya-ekstra-sensitiv-arko-200ml',
             'https://shop.silpo.ua/product/pina-dlia-golinnia-arko-dlia-chutlyvoi-shkiry-44192',
             'https://auchan.ua/ua/pena-dlja-brit-ja-arko-sensitive-200-ml-253127/',
             'https://novus.online/product/pina-dla-golinna-arco-dla-cutlivoi-skiri-200ml',
             'https://metro.zakaz.ua/uk/products/pina-arko-200ml--08690506090043/',
             'https://shop.nashkraj.ua/kovel/product/3475-pina-arko-d-g-200ml-ekstra-sensetiv',
             'https://fozzyshop.ua/ru/muzhskie-sredstva-dlya-britya-i-kosmetika/39097-pena-dlya-britya-arko-dlya-chuvstvitelnoj-kozhi-8690506090043.html'])

    def carrot_parcer(self):
        '''Парсер для сбора данных о цене продукта морковь'''
        return self.prices_parsing(['https://www.atbmarket.com/product/morkva-1gat',
                                    'https://eko.zakaz.ua/uk/products/ovochi-morkva--ekomarket00000000640007/',
                                    'https://varus.ua/morkva-1-gatunok-vag',
                                    'https://shop.silpo.ua/product/morkva-myta-367056',
                                    'https://novus.online/product/morkva-vag',
                                    'https://metro.zakaz.ua/uk/products/ovochi-morkva--metro28941500000000/',
                                    'https://shop.nashkraj.ua/kovel/product/12819-morkva-vag',
                                    'https://fozzyshop.ua/ru/ovoshhi/11524-morkov-2736546.html'])

    def cabbage_parcer(self):
        '''Парсер для сбора данных о цене продукта капуста'''
        return self.prices_parsing(['https://www.atbmarket.com/product/kapusta-1-gat',
                                    'https://eko.zakaz.ua/uk/products/ovochi-kapusta--ekomarket00000000667930/',
                                    'https://varus.ua/kapusta-1-gatunok-vag',
                                    'https://shop.silpo.ua/product/kapusta-bilogolova-32572',
                                    'https://novus.online/product/kapusta-vag',
                                    'https://metro.zakaz.ua/uk/products/ovochi-kapusta--metro28284700000000/',
                                    'https://shop.nashkraj.ua/kovel/product/869-kapusta-bilokachanna-vag',
                                    'https://fozzyshop.ua/ru/ovoshhi/11498-kapusta-belokachannaya-2732572.html'])

    def egg_parcer(self):
        '''Парсер для сбора данных о цене продукта яйца куринные'''
        return self.prices_parsing(['https://www.atbmarket.com/product/ajce-kurace-10-st-ukraina-1-kategoria-fas',
                                    'https://eko.zakaz.ua/uk/products/iaitse--ekomarket00000026102825/',
                                    'https://varus.ua/yayce-kuryache-1sht',
                                    'https://shop.silpo.ua/product/yaitsia-kuriachi-povna-chasha-1-kategoriia-435227',
                                    'https://auchan.ua/ua/jajca-kurinye-organicheskie-organic-eggs-s-1-10-sht-971455/',
                                    'https://novus.online/product/ajce-kurace-s1-harcove-marka-promo-10st',
                                    'https://metro.zakaz.ua/uk/products/iaitse-iasensvit-530g-ukrayina--04820147580830/',
                                    'https://shop.nashkraj.ua/kovel/product/301886-yaytse-kvochka-10sht-xl',
                                    'https://fozzyshop.ua/ru/yajca-kurinye/87720-yajco-kurinoe-s1-s0-4820215480079.html'])

    def mayonez_detsk_shedro_67_parcer(self):
        '''Парсер для сбора данных о цене продукта "Майонез детский Щедро 67%"'''
        return self.prices_parsing(['https://www.atbmarket.com/product/majonez-190g-sedro-domasnij-dla-ditej-67',
                                    'https://eko.zakaz.ua/uk/products/maionez-shchedro-190g--04820184020054/',
                                    'https://varus.ua/mayonez-domashniy-dlya-ditey-67-schedro-190g-d-p-ukraina',
                                    'https://shop.silpo.ua/product/maionez-shchedro-domashnii-dlia-ditei-67-685628',
                                    'https://metro.zakaz.ua/uk/products/maionez-shchedro-190g--04820184020054/',
                                    'https://fozzyshop.ua/ru/majonez/52017-majonez-shhedro-domashnij-dlya-detej-67-d-p-4823097402375.html'])

    def rexona_aloe_vera_w_parcer(self):
        '''Парсер для сбора данных о цене продукта "Дезодорант Rexona Aloe Vera женский"'''
        return self.prices_parsing(
            ['https://eko.zakaz.ua/uk/products/dezodorant-reksona-150ml-velikobritaniia--08712561844338/',
             'https://auchan.ua/ua/dezodorant-sprej-rexona-motionsense-aloe-vera-150-ml-256005/'])

    def marloboro_red_parcer(self):
        '''Парсер для сбора данных о цене продукта сигареты Мальборо красные'''
        return self.prices_parsing(['https://www.atbmarket.com/product/sigareti-marlboro-27',
                                    'https://eko.zakaz.ua/uk/products/tsigarki-malboro-25g--04823003205557/',
                                    'https://varus.ua/cigarki-marlboro',
                                    'https://shop.silpo.ua/product/sygarety-marlboro-red-911500',
                                    'https://auchan.ua/ua/sigarety-marlboro-20-sht-916786/',
                                    'https://novus.online/product/cigarki-marlboro-red',
                                    'https://fozzyshop.ua/ru/sigarety/98990-sigarety-marlboro-red-4823003205557.html'])

    def beer_lvivske_svitle_24l(self):
        '''Парсер для сбора данных о цене продукта "Пиво ЛЬвовское светлое 2,4 литра"'''
        return self.prices_parsing(
            ['https://varus.ua/pivo-2-4l-4-5-svitle-pasteriz-lvivske',
             'https://shop.silpo.ua/product/pyvo-lvivske-svitle-812957',
             'https://auchan.ua/ua/pivo-l-vivs-ke-svetloe-fil-trovannoe-4-5-2-4-l-1031963/',
             'https://fozzyshop.ua/ru/pivo-svetloe/74710-pivo-lvivske-svetloe-4820000455350.html'])

    def smetana_stolica_smaky_400_15_parcer(self):
        '''Парсер для сбора данных о цене продукта сметана "Столица Смаку 400 гр 15%"'''
        return self.prices_parsing(['https://varus.zakaz.ua/ru/products/ukrayina--04820194043517/'])

    def water_in_6l_bottle_parser(self):
        '''Парсер для сбора данных о цене продукта вода питьевая в 6 литровой бутылке'''
        return self.prices_parsing(['https://www.atbmarket.com/product/voda-6-l-karpatska-dzerelna-negazovana',
                                    'https://eko.zakaz.ua/uk/products/voda-karpatska-dzherelna-6000ml--04820051240240/',
                                    'https://varus.ua/voda-vygoda-negazirovannaya-vygoda-6-l',
                                    'https://shop.silpo.ua/product/voda-mineralna-karpatska-dzherelna-negazovana-440815',
                                    'https://auchan.ua/ua/voda-karpats-ka-dzherel-na-6-l-775207/',
                                    'https://novus.online/product/voda-pitna-dzerelna-negazovana-marka-promo-6l',
                                    'https://metro.zakaz.ua/ru/products/voda-karpatska-dzherelna-6000ml--04820051240240/',
                                    'https://shop.nashkraj.ua/kovel/product/19345-min-voda-prozora-6l-vershina-yakosti',
                                    'https://fozzyshop.ua/ru/voda-mineralnaya-negazirovannaya/12847-voda-pitevaya-prozora-artezianskaya-n-gaz-4820029431014.html'])

    def pork_lopatka_parser(self):
        '''Парсер для сбора данных о цене продукта свинина лопатка/на кости, кг'''
        return self.prices_parsing(['https://www.atbmarket.com/product/okist-lembergmit-svinacij-oholodzenij-vakupak',
                                    'https://eko.zakaz.ua/uk/products/m-iaso--ekomarket00000000535086/',
                                    'https://varus.ua/lopatka-svinaya-vesovaya',
                                    'https://shop.silpo.ua/product/svyniacha-lopatka-fermerska-757767',
                                    'https://novus.online/product/lopatka-svinna-na-kistocci-vag',
                                    'https://metro.zakaz.ua/uk/products/m-iaso--metro28500400000000/',
                                    'https://shop.nashkraj.ua/kovel/product/28508-svinina-okholodzhena-lopatka',
                                    'https://fozzyshop.ua/ru/svinina/11242-svinaya-lopatka-bez-kosti-2732700.html'])

    def potato_parser(self):
        '''Парсер для сбора данных о цене продукта картошка обыкновенная, кг'''
        return self.prices_parsing(['https://www.atbmarket.com/product/kartopla-1-gat',
                                    'https://eko.zakaz.ua/uk/products/ovochi-kartoplia--ekomarket00000000667970/',
                                    'https://varus.ua/kartoplya-1-gatunok-vag',
                                    'https://shop.silpo.ua/product/kartoplia-bila-myta-460748',
                                    'https://novus.online/product/kartopla-rozeva-vag',
                                    'https://metro.zakaz.ua/uk/products/ovochi-kartoplia--metro28013500000000/',
                                    'https://fozzyshop.ua/ru/ovoshhi/64754-kartoshka-belaya-2782970.html'])

    def beet_parser(self):
        '''Парсер для сбора данных о цене продукта буряк обыкновенный, кг'''
        return self.prices_parsing(['https://www.atbmarket.com/product/burak-1-gat',
                                    'https://eko.zakaz.ua/uk/products/ovochi-buriak--ekomarket00000000646097/',
                                    'https://varus.ua/buryak-1-gatunok-vag',
                                    'https://shop.silpo.ua/product/buriak-32570',
                                    'https://novus.online/product/burak-vag',
                                    'https://metro.zakaz.ua/uk/products/ovochi-buriak--metro28165800000000/',
                                    'https://fozzyshop.ua/ru/ovoshhi/11573-svekla-0101190394549.html'])

    def four_parser(self):
        '''Парсер для сбора данных о цене продукта муки, кг'''
        return self.prices_parsing(['https://www.atbmarket.com/product/borosno-1-kg-hutorok-psenicne-visij-gatunok',
                                    'https://eko.zakaz.ua/uk/products/boroshno-khutorok-1000g-ukrayina--04820101710204/',
                                    'https://varus.ua/boroshno-pshenichne-vigoda-1-kg',
                                    'https://shop.silpo.ua/product/boroshno-kyivmlyn-v-g-210259',
                                    'https://novus.online/product/borosno-psenicne-marka-promo-1kg',
                                    'https://metro.zakaz.ua/uk/products/boroshno-metro-shef-1000g--04820019601656/',
                                    'https://shop.nashkraj.ua/kovel/product/57341-boroshno-pshenichne-v-g',
                                    'https://fozzyshop.ua/ru/muka-pshenichnaya/19053-muka-pshenichnaya-extra-v-s-4824034039036.html'])

    def oil_for_dishes_parser(self):
        '''Парсер масла для приготовки блюд(самое популярное) '''
        return self.prices_parsing(
            ['https://www.atbmarket.com/product/olia-085l-olejna-tradicijna-sonasnikova-rafinovana',
             'https://eko.zakaz.ua/uk/products/oliia-oleina-850ml--04820001115567/',
             'https://varus.ua/maslo-podsolnechnoe-oleyna-tradicionnaya-rafinirovannoe-850-ml',
             'https://novus.online/product/olia-sonasna-rafinovana-dezodorovana-vimorozena-marki-p-olejnatradicijna-0850l',
             'https://metro.zakaz.ua/uk/products/oliia-aro-870ml--04820060041050/',
             'https://shop.nashkraj.ua/kovel/product/253258-oliya-oleyna-850ml-rafinovana',
             'https://fozzyshop.ua/ru/maslo-podsolnechnoe/56884-maslo-podsolnechnoe-shhedrij-dar-pervyj-otzhim-4820078575745.html'])

    def sour_cream_for_dishes_parser(self):
        '''Парсер для самой популярной сметаны к блюдам (вареники, борщ, т.д.)'''
        return self.prices_parsing(['https://www.atbmarket.com/product/smetana-300-g-agotinska-15-pstakan',
                                    'https://eko.zakaz.ua/uk/products/smetana-iagotin-300g--04823005209584/',
                                    'https://varus.ua/smetana-yagotinska-15-450g',
                                    'https://shop.silpo.ua/product/smetana-yagotynska-15-908738',
                                    'https://novus.online/product/smetana-15-yahotyn-stakan-300h',
                                    'https://metro.zakaz.ua/uk/products/smetana-iagotin-300g--04823005209584/',
                                    'https://fozzyshop.ua/ru/smetana/98665-smetana-yagotinske-15-stakan-0250014899583.html'])

    def desodorant_garnier_magniy_man_parser(self):
        '''Парсер для дезодоранта "Garnier Магний мужской"'''
        return self.prices_parsing(
            ['https://shop.silpo.ua/product/dezodorant-sprei-garnier-men-magnii-ultrasukhist-813133',
             'https://fozzyshop.ua/ru/dezodoranty/84270-dezodorant-sprej-garnier-men-magnij-ultrasukhost-3600542310369.html'])

    def coffee_aroma_gold_freeze_dried_70g_parser(self):
        '''Парсер для растворимого кофе "Арома Голд freeze dried 70 грамм"'''
        return self.prices_parsing(['https://eko.zakaz.ua/uk/products/kava-aroma-gold-70g--04771632088167/',
                                    'https://shop.silpo.ua/product/kava-aroma-gold-rozchynna-895284',
                                    'https://shop.nashkraj.ua/kovel/product/494322-kava-aroma-gold-70g-natur-rozch-subl-gran'])

    def gorchica_veres_ukrainska_micna_120g_parser(self):
        '''Парсер для горчицы "Верес украинская крепкая 120 грамм"'''
        return self.prices_parsing(['https://shop.silpo.ua/product/girchytsia-veres-ukrainska-mitsna-d-p-722177',
                                    'https://novus.online/product/gircica-ukrainska-micna-veres-120g-dp',
                                    'https://metro.zakaz.ua/uk/products/girchitsia-veres-120g-ukrayina--04823084600661/'])

    def tea_monomah_100_ceylon_original_black_krupn_list_90g_parser(self):
        '''Парсер для чая "Мономах 100% оригинал цейлонский черный крупнолистовой"'''
        pass  # нет нигде этого чая

    def tea_monomah_ceylon_black_parser(self):
        '''Парсер для чая "Мономах Цейлон черный 90 гр"'''
        pass  # нет нигде этого чая

    def sir_plavlenniy_komo_paprikash_parser(self):
        '''Парсер для сырка плавленного "Комо Паприкаш"'''
        return self.prices_parsing(['https://novus.online/product/sir-plavlenij-55-paprikas-komo-75g',
                                    'https://metro.zakaz.ua/uk/products/sir-komo-75g-ukrayina--04820039807908/',
                                    'https://shop.nashkraj.ua/kovel/product/455686-sir-komo-pl-40-75g-paprikash',
                                    'https://fozzyshop.ua/plavlenyj/98306-syr-plavlenyj-komo-paprikash-40-4820039807908.html'])

    def apple_gala_parser(self):
        '''Парсер для яблока сорта Гала'''
        return self.prices_parsing(['https://www.atbmarket.com/product/abluko-gala-1-gat',
                                    'https://eko.zakaz.ua/uk/products/frukt-iabluka--ekomarket00000000648329/',
                                    'https://varus.ua/yabluko-gala-premium-vag',
                                    'https://shop.silpo.ua/product/yabluko-gala-142571',
                                    'https://novus.online/product/abluko-ukraina-60-70-vag',
                                    'https://metro.zakaz.ua/uk/products/frukt-iabluka--metro28034800000000/',
                                    'https://fozzyshop.ua/frukty-i-yagody/23103-yabloko-gala.html'])

    def smetana_galichanska_15_370g_parser(self):
        '''Прасер для сметаны "Галичанська 15% 370 грамм"'''
        return self.prices_parsing(['https://www.atbmarket.com/product/smetana-400g-galicanska-15',
                                    'https://eko.zakaz.ua/uk/products/smetana-galichanska-400g--04820038494246/',
                                    'https://novus.online/product/smetana-15-halychanska-pe-370h',
                                    'https://metro.zakaz.ua/uk/products/smetana-galichanska-400g--04820038494246/',
                                    'https://fozzyshop.ua/smetana/90114-smetana-galichanska-15-p-e-4820038494246.html'])

    def desodorant_garnier_spring_spirit_parser(self):
        '''Парсер для дезодоранта "Garnier весенняя свежесть"'''
        return self.prices_parsing(['https://shop.silpo.ua/product/dezodorant-sprei-garnier-vesniana-svizhist-569230',
                                    'https://novus.online/product/dezodorant-antiperspirant-dla-tila-zahist-5-vesnana-svizist-garnier-150ml',
                                    'https://metro.zakaz.ua/uk/products/dezodorant-garner-150ml--03600541466180/',
                                    'https://fozzyshop.ua/ru/dezodoranty/23572-dezodorant-sprej-garnier-mineral-vesennyaya-svezhest-3600541466180.html'])

    def chips_lays_with_salt_parser(self):
        '''Парсер для чипсов "Lays с солью " большая пачка 30 грамм'''
        return self.prices_parsing(['https://eko.zakaz.ua/uk/products/chipsi-leiz-140g--05941000025639/',
                                    'https://metro.zakaz.ua/uk/products/dezodorant-garner-150ml--03600541466180/',
                                    'https://fozzyshop.ua/dezodoranty/23572-dezodorant-sprej-garnier-mineral-vesennyaya-svezhest-3600541466180.html'])

    def sprite_2l_parser(self):
        '''Парсер для "Sprite 2 литра"'''
        return self.prices_parsing(['https://eko.zakaz.ua/uk/products/napii-sprait-2000ml--05449000004864/',
                                    'https://varus.ua/napiy-sprite-silnogazovaniy-2-l',
                                    'https://shop.silpo.ua/product/napii-sprite-119',
                                    'https://auchan.ua/ua/napitok-bezalkogol-nyj-sil-nogazirovanyj-na-aromatizatorah-sprite-p-but-2l-688892/',
                                    'https://novus.online/product/napij-gazovanij-sprite-2l',
                                    'https://metro.zakaz.ua/uk/products/napii-sprait-2000ml--05449000004864/',
                                    'https://shop.nashkraj.ua/kovel/product/7677-napiy-sprayt-2l',
                                    'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/12914-napitok-sprite-5449000004864.html'])

    def fanta_2l_parser(self):
        '''Парсер для "Fanta 2 литра"'''
        return self.prices_parsing(['https://eko.zakaz.ua/uk/products/napii-fanta-2000ml--05449000004840/',
                                    'https://varus.ua/napiy-fanta-apelsin-silnogazovaniy-sokovmisniy-2-l',
                                    'https://shop.silpo.ua/product/napii-fanta-orange-118',
                                    'https://auchan.ua/ua/napitok-bezalkogol-nyj-sil-nogazirovannyj-s-apel-sinovym-sokom-fanta-p-but-2l-688689/',
                                    'https://novus.online/product/napij-gazovanij-fanta-apelsin-2l',
                                    'https://metro.zakaz.ua/uk/products/napii-fanta-2000ml--05449000004840/',
                                    'https://shop.nashkraj.ua/kovel/product/7697-napiy-fanta-2l-apelsin',
                                    'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/12851-napitok-fanta-orange-5449000004840.html'])

    def bond_street_blue_selection_parser(self):
        '''Парсер для сигарет "Bond Street Blue Selection"'''
        return self.prices_parsing(
            ['https://www.atbmarket.com/product/sigareti-bond-street-blue-selection-24?search=bond',
             'https://eko.zakaz.ua/uk/products/tsigarki-bond-25g--04823003208107/',
             'https://varus.ua/cigarki-bond-street-blue-selection',
             'https://shop.silpo.ua/product/tsygarky-bond-street-blue-selection-908565',
             'https://auchan.ua/ua/sigarety-bond-street-blue-selection-20-sht-916723/',
             'https://novus.online/product/cigarki-bond-street-blue',
             'https://fozzyshop.ua/ru/sigarety/98982-sigarety-bond-street-blue-selection-0250014886927.html'])

    def camel_blue_parser(self):
        '''Парсер для сигарет "Camel Blue"'''
        return self.prices_parsing(['https://atbmarket.com/product/sigareti-camel-blue-30',
                                    'https://eko.zakaz.ua/uk/products/tsigarki-kemel-25g--04820000531733/',
                                    'https://varus.ua/cigarki-camel-blue-20-sht',
                                    'https://shop.silpo.ua/product/tsygarky-camel-blue-907446',
                                    'https://auchan.ua/ua/sigarety-camel-blue-20-sht-1029520/',
                                    'https://novus.online/product/cigarki-camel-sf-blue',
                                    'https://fozzyshop.ua/ru/sigarety/98925-sigarety-camel-blue-0250014861030.html'])

    def ld_red_parser(self):
        '''Парсер для сигарет "LD RED"'''
        return self.prices_parsing(['https://atbmarket.com/product/sigareti-ld-red-26',
                                    'https://eko.zakaz.ua/uk/products/tsigarki-ld--04820000535243/',
                                    'https://shop.silpo.ua/product/tsygarky-ld-red-907420',
                                    'https://fozzyshop.ua/ru/sigarety/38439-sigarety-ld-red-4820000534628.html'])

    def marlboro_gold_parser(self):
        '''Парсер для сигарет "Marlboro Gold"'''
        return self.prices_parsing(['https://atbmarket.com/product/sigareti-marlboro-gold-28?search=marlboro',
                                    'https://eko.zakaz.ua/uk/products/tsigarki-malboro-25g--04823003210070/',
                                    'https://varus.ua/cigarki-marlboro-gold-z-filtrom-20-sht',
                                    'https://shop.silpo.ua/product/sygarety-marlboro-gold-908561',
                                    'https://auchan.ua/ua/sigarety-marlboro-gold-20-sht-916800/',
                                    'https://novus.online/product/cigarki-marlboro-gold-original',
                                    'https://fozzyshop.ua/ru/sigarety/98980-sigarety-marlboro-gold-0250014886880.html'])

    def rothmans_demi_blue_exclusive_parser(self):
        '''Парсер для сигарет "Rothmans Demi Blue Exclusive"'''
        return self.prices_parsing(
            ['https://atbmarket.com/product/sigareti-rothmans-demi-blue-exclusive-8?search=rothmans%20demi%20blue',
             'https://eko.zakaz.ua/uk/products/tsigarki-rotmans--04820192681995/',
             'https://varus.ua/cigarki-rothmans-royals-blue',
             'https://shop.silpo.ua/product/tsygarky-rothmans-royals-blue-907160',
             'https://auchan.ua/ua/sigarety-rothmans-royals-blue-exclusive-20-sht-917101/',
             'https://novus.online/product/cigarki-rothmans-royals-blue-exclusive'])

    def rothmans_demi_click_purple_parser(self):
        '''Парсер для сигарет "Rothmans Demi Click Purple"'''
        return self.prices_parsing(['https://atbmarket.com/product/sigareti-rothmans-demi-click-purple-28',
                                    'https://eko.zakaz.ua/uk/products/tsigarki-rotmans--00000048210218/',
                                    'https://auchan.ua/ua/sigarety-rothmans-demi-click-purple-20-sht-917136/'])

    def winston_caster_parser(self):
        '''Парсер для сигарет "Winston Caster"'''
        return self.prices_parsing(['https://atbmarket.com/product/sigareti-winston-caster-29'])

    def parlament_aqua_blue_parser(self):
        ''' Парсер для сигарет "Parlament Aqua Blue"'''
        return self.prices_parsing([
            'https://atbmarket.com/product/sigareti-parliament-aqua-blue-27',
            'https://eko.zakaz.ua/uk/products/tsigarki-parlament-25g--00000048207775/',
            'https://varus.ua/cigarki-parliament-aqua',
            'https://shop.silpo.ua/product/tsygarky-parliament-aqua-blue-908567',
            'https://auchan.ua/ua/sigarety-parliament-aqua-blue-20-sht-916807/',
            'https://novus.online/product/cigarki-parliament-aqua-blue',
            'https://fozzyshop.ua/sigarety/98983-sigarety-parliament-aqua-blue-0250014886941.html'
        ])

    def winston_blue_parser(self):
        ''' Парсер для сигарет "Winston Blue"'''
        return self.prices_parsing([
            'https://atbmarket.com/product/sigareti-winston-blue-28',
            'https://eko.zakaz.ua/uk/products/tsigarki-vinston-25g--04820000531351/',
            'https://varus.ua/cigarki-winston-blue',
            'https://shop.silpo.ua/product/sygarety-winston-blue-907419',
            'https://auchan.ua/ua/sigarety-winston-blue-20-sht-1029560/',
            'https://novus.online/product/cigarki-winston-blue',
            'https://fozzyshop.ua/sigarety/3227-sigarety-winston-blue-4820000531351.html'
        ])

    def bond_street_red_selection_parser(self):
        ''' Парсер для сигарет "Bond Street Red Selection"'''
        return self.prices_parsing([
            'https://atbmarket.com/product/sigareti-bond-street-red-selection-23',
            'https://varus.ua/cigarki-bond-street-red-selection',
            'https://shop.silpo.ua/product/sygarety-bond-street-red-selection-908566',
            'https://auchan.ua/ua/sigarety-bond-street-red-selection-20-sht-916702/'
        ])

    def ld_blue_parser(self):
        ''' Парсер для сигарет "LD Blue"'''
        return self.prices_parsing([
            'https://atbmarket.com/product/sigareti-ld-blue-23',
            'https://shop.silpo.ua/product/tsygarky-ld-blue-907421',
            'https://fozzyshop.ua/sigarety/56861-sigarety-ld-blue-4820000534642.html'
        ])

    def kent_silver_parser(self):
        ''' Парсер для сигарет "KENT Silver"'''
        return self.prices_parsing([
            'https://atbmarket.com/product/sigareti-kent-silver-27',
            'https://eko.zakaz.ua/uk/products/tsigarki-kent--04820192683340/',
            'https://varus.ua/cigarki-kent-silver-4-0-4-0-4',
            'https://auchan.ua/ua/sigarety-kent-silver-20-sht-917283/',
            'https://novus.online/product/cigarki-kent-siiver-neo-4',
            'https://fozzyshop.ua/sigarety/98898-sigarety-kent-nd-silver-0250014852106.html'
        ])

    def kent_navy_blue_new_parser(self):
        ''' Парсер для сигарет "KENT Navy Blue"'''
        return self.prices_parsing([
            'https://atbmarket.com/product/sigareti-kent-navy-blue-new-23',
            'https://eko.zakaz.ua/uk/products/tsigarki-kent--04820192683364/',
            'https://varus.ua/cigarki-kent-navy-blue-4-0-8-08',
            'https://shop.silpo.ua/product/tsygarky-kent-nd-navy-blue-907151',
            'https://auchan.ua/ua/sigarety-kent-navy-blue-20-sht-917276/',
            'https://novus.online/product/cigarki-kent-blue-futura-8',
            'https://fozzyshop.ua/sigarety/98899-sigarety-kent-navy-blue-0250014852113.html'
        ])

    def beer_chernigivske_svitle_05_l_glass_parser(self):
        ''' Парсер для пива "Черниговское светлое" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/pivo-05l-cernigivske-svitle',
            'https://shop.silpo.ua/product/pyvo-chernigivske-svitle-10503',
            'https://auchan.ua/ua/pivo-chernigivs-ke-svetloe-4-8-500-ml-1021029/',
            'https://novus.online/product/pivo-svitle-cernigivske-48-05l-sklpl',
            'https://metro.zakaz.ua/uk/products/pivo-chernigivske-500ml-ukrayina--04820034920077/',
            'https://shop.nashkraj.ua/kovel/product/6883-pivo-chernigivske-0-5l-svitle-sb-4-8',
            'https://fozzyshop.ua/pivo-svetloe/3001-pivo-chernigivske-svetloe-4820000380065.html'
        ])

    def beer_stella_artois_05_l_glass_parser(self):
        ''' Парсер для пива "Stella Artois" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05l-stella-artoisut',
            'https://shop.silpo.ua/product/pyvo-stella-artois-17332',
            'https://auchan.ua/ua/pivo-stella-artois-svetloe-5-500-ml-1021059/',
            'https://novus.online/product/pivo-svitle-stella-artois-50-05l-sklpl',
            'https://metro.zakaz.ua/ru/products/pivo-stella-artua-500ml-belgiia--04820000380348/',
            'https://fozzyshop.ua/ru/pivo-svetloe/2815-pivo-stella-artois-svetloe-4820034921500.html'
        ])

    def beer_obolon_svitle_05_l_glass_parser(self):
        ''' Парсер для пива "Оболонь Светлое" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05-l-obolon-svitle',
            'https://eko.zakaz.ua/uk/products/pivo-obolon-500ml-ukrayina--04670001497428/',
            'https://varus.ua/pivo-0-5l-svitle-obolon-sb',
            'https://novus.online/product/pivo-svitle-obolon-45-05l-sklpl',
            'https://metro.zakaz.ua/uk/products/pivo-obolon-500ml-ukrayina--04820000191708/',
            'https://shop.nashkraj.ua/kovel/product/6759-pivo-obolon-0-5l-svitle-4-5',
            'https://fozzyshop.ua/ru/pivo-svetloe/2919-pivo-obolon-svitle-svetloe-4820000191708.html'
        ])

    def beer_jugulivske_svitle_05_l_glass_parser(self):
        ''' Парсер для пива "Жигулевское светлое" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/pivo-05-l-zigulivske-svitle',
            'https://eko.zakaz.ua/uk/products/pivo-obolon-500ml-ukrayina--04820000195843/',
            'https://varus.ua/pivo-0-5l-4-2-svitle-zhigulivske-pl',
            'https://novus.online/product/pivo-svitle-obolon-zigulivske-42-05l-sklpl',
            'https://metro.zakaz.ua/ru/products/pivo-obolon-500ml-ukrayina--04820000195843/',
            'https://fozzyshop.ua/ru/pivo-svetloe/2937-pivo-obolon-zhigulivske-svetloe-4820000195843.html',
        ])

    def beer_rogan_tradicionnoe_svitle_05_l_glass_parser(self):
        ''' Парсер для пива "Рогань традиционное светлое" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05-l-rogan-tradicijne-svitle-skbut',
            'https://shop.silpo.ua/product/pyvo-rogan-tradytsiine-svitle-36278',
            'https://novus.online/product/pivo-svitle-rogan-tradicijne-48-05l-sklpl',
            'https://metro.zakaz.ua/ru/products/pivo-rogan-500ml-ukrayina--04820034921616/',
            'https://shop.nashkraj.ua/kovel/product/6789-pivo-rogan-0-5l-traditsiyne-svit-sb-4-8',
            'https://fozzyshop.ua/ru/pivo-svetloe/2988-pivo-rogan-tradicijne-svetloe-4820034921616.html'
        ])

    def beer_corona_extra_svitle_033_l_glass_parser(self):
        ''' Парсер для пива "Corona Extra светлое" 0,33 л в стекле'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-330-ml-corona-extra-svitle',
            'https://eko.zakaz.ua/uk/products/pivo-korona-ekstra--ekomarket00000026229294/',
            'https://varus.ua/pivo-4-5-0-355l-svitle-corona-extra-s-b',
            'https://shop.silpo.ua/product/pyvo-corona-extra-svitle-839544',
            'https://auchan.ua/ua/pivo-corona-extra-svetloe-4-5-330-ml-1021862/',
            'https://novus.online/product/pivo-svitle-corona-extra-45-033-sp',
            'https://metro.zakaz.ua/ru/products/pivo-korona-ekstra-330ml-meksika--07501064199844/',
            'https://fozzyshop.ua/ru/pivo-svetloe/81812-pivo-corona-extra-svetloe-7501064199844.html'
        ])

    def beer_chernigibske_bile_nefilter_05_l_glass_parser(self):
        ''' Парсер для пива "Черниговское белок нефильтрованное" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05l-cernigivske-bile-nefiltrovane',
            'https://shop.silpo.ua/product/pyvo-chernigivske-bile-18109',
            'https://novus.online/product/pivo-svitle-nefiltrovane-cernigivske-bile-50-05l-sklpl',
            'https://metro.zakaz.ua/ru/products/pivo-chernigivske-500ml-ukrayina--04820034920312/',
            'https://shop.nashkraj.ua/kovel/product/6876-pivo-chernigivske-0-5l-bile-4-8-s-b',
            'https://fozzyshop.ua/ru/pivo-svetloe/2983-pivo-chernigivske-bile-nefiltrovannoe-4820000750615.html'
        ])

    def beer_yantar_svitle_05_l_glass_parser(self):
        ''' Парсер для пива "Янтарь светлое" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05l-antar-svitle',
            'https://auchan.ua/ua/pivo-jantar-svetloe-4-5-500-ml-1021035/',
            'https://metro.zakaz.ua/ru/products/pivo-iantar-500ml-ukrayina--04820034920602/',
            'https://fozzyshop.ua/ru/pivo-svetloe/42648-pivo-yantar-svetloe-4820034920602.html'
        ])

    def beer_zlata_praha_svitle_05_l_glass_parser(self):
        ''' Парсер для пива "Zlata Praha светлое" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-zlata-praga-500ml-ukrayina--04820000196130/',
            'https://varus.ua/pivo-0-5l-5-0-svitle-zlata-praha-pl',
            'https://shop.silpo.ua/product/pyvo-zlata-praha-svitle-473045',
            'https://novus.online/product/pivo-svitle-zlata-praha-svetle-50-05l-sklpl',
            'https://fozzyshop.ua/ru/pivo-svetloe/46789-pivo-zlata-praha-svetloe-4820000196130.html'
        ])

    def beer_zibert_svitle_05_l_glass_parser(self):
        ''' Парсер для пива "Zibert светлое" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05-zibert-lager-beer-svitle-skbut',
            'https://eko.zakaz.ua/uk/products/pivo-zibert-500ml--04820000197472/',
            'https://varus.ua/pivo-svitle-zibert-0-5l-ukraina',
            'https://novus.online/product/pivo-svitle-zibert-legerbier-49-05l',
            'https://fozzyshop.ua/ru/pivo-svetloe/2842-pivo-zibert-svitle-svetloe-4820000197472.html'
        ])

    def beer_arsenal_micne_05_l_glass_parser(self):
        ''' Парсер для пива "Арсенал мицне" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://novus.online/product/pivo-svitle-arsenal-micne-8-05l-sklpl',
            'https://metro.zakaz.ua/ru/products/pivo-arsenal-500ml-ukrayina--04820000451420/',
            'https://shop.nashkraj.ua/kovel/product/6692-pivo-arsenal-0-5l-mitsne-8',
            'https://fozzyshop.ua/ru/pivo-svetloe/2829-pivo-arsenal-micne-svetloe-4820000451420.html'
        ])

    def beer_persha_brovarna_zakarpatske_05_l_glass_parser(self):
        ''' Парсер для пива "Перша Броварня Закарпатське" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-persha-privatna-brovarnia-500ml-ukrayina--04820046961242/',
            'https://varus.ua/pivo-zakarpatske-persha-privatna-brovarnya-0-5l',
            'https://shop.silpo.ua/product/pyvo-persha-pryvatna-brovarnia-zakarpatske-oryginalne-svitle-660937',
            'https://auchan.ua/ua/pivo-persha-privatna-brovarnja-zakarpatskoe-svetloe-fil-trovannoe-4-4-0-5-l-1031778/',
            'https://novus.online/product/pivo-zakarpatske-svitle-s-b-05l',
            'https://metro.zakaz.ua/ru/products/pivo-persha-privatna-brovarnia-500ml-ukrayina--04820046961242/',
            'https://shop.nashkraj.ua/kovel/product/223912-pivo-privatna-brovarnya-0-5l-zakarp-4-4',
            'https://fozzyshop.ua/ru/pivo-svetloe/27045-pivo-ppb-zakarpatskoe-originalnoe-svetloe-4820046961242.html'
        ])

    def beer_lvivske_svitle_05_l_glass_parser(self):
        ''' Парсер для пива "Львовское светлое" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://metro.zakaz.ua/ru/products/pivo-lvivske-500ml-ukrayina--04823005000150/',
            'https://shop.nashkraj.ua/kovel/product/6740-pivo-lvivske-0-5l-svitle-4-5',
            'https://fozzyshop.ua/ru/pivo-svetloe/2873-pivo-lvivske-svitle-svetloe-4823005000150.html'
        ])

    def beer_lvivske_1715_05_l_glass_parser(self):
        ''' Парсер для пива "Львовское 1715" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://varus.ua/pivo-lvivske-1715-0-5-svitle-pasterizovane-bezalkogolne-0-45-l',
            'https://shop.silpo.ua/product/pyvo-lvivske-1715-604163',
            'https://auchan.ua/ua/pivo-l-vivs-ke-1715-svetloe-fil-trovannoe-4-7-0-45-l-1031958/',
            'https://metro.zakaz.ua/ru/products/pivo-lvivske-450ml-ukrayina--04820250942068/',
            'https://shop.nashkraj.ua/kovel/product/213085-pivo-lvivske-0-45l-1715-4-7',
            'https://fozzyshop.ua/ru/pivo-svetloe/27028-pivo-lvivske-1715-4820000455732.html'
        ])

    def beer_tuborg_green_05_l_glass_parser(self):
        ''' Парсер для пива "Tuborg Green" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://varus.ua/pivo-0-5l-4-6-svitle-pasterizovane-green-tuborg-pl',
            'https://shop.silpo.ua/product/pyvo-tuborg-green-181028',
            'https://auchan.ua/ua/pivo-tuborg-green-svetloe-4-6-0-5-l-1032003/',
            'https://metro.zakaz.ua/ru/products/pivo-tuborg-500ml-ukrayina--04820000451178/',
            'https://shop.nashkraj.ua/kovel/product/6863-pivo-tuborg-grin-0-5l-4-6',
            'https://fozzyshop.ua/ru/pivo-svetloe/2687-pivo-tuborg-green-svetloe-4820000451178.html'
        ])

    def beer_slavutich_ice_mix_lime_05_l_glass_parser(self):
        ''' Парсер для пива "Славутич ICE MIX Lime" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://varus.ua/pivo-ays-birmiks-laym-slavutich-0-5l',
            'https://shop.silpo.ua/product/pyvo-slavutych-ice-mix-lime-363714',
            'https://metro.zakaz.ua/ru/products/pivo-slavutich-500ml-ukrayina--04820000454759/',
            'https://shop.nashkraj.ua/kovel/product/177507-pivo-slavutich-0-5lays-miks-smak-laym3-5',
        ])

    def beer_teteriv_svitle_05_l_glass_parser(self):
        ''' Парсер для пива "Тетерев светлое" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-persha-privatna-brovarnia-500ml-ukrayina--04820022692658/',
            'https://shop.silpo.ua/product/pyvo-persha-pryvatna-brovarnia-teteriv-svitle-584239',
            'https://novus.online/product/pivo-8-svitle-teterev-sklana-plaska-05l',
            'https://shop.nashkraj.ua/kovel/product/220894-pivo-privatna-brovarnya-0-5l-teteriv-8',
            'https://fozzyshop.ua/ru/pivo-svetloe/27071-pivo-ppb-teteriv-svetloe-4820022692658.html'
        ])

    def beer_krusovice_svitle_05_l_glass_parser(self):
        ''' Парсер для пива "Krusovice светлое" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-krushovitse-500ml--04820046961761/',
            'https://varus.ua/pivo-0-5l-4-2-svitle-filtrovane-pasterizovane-krusovice-pl',
            'https://shop.silpo.ua/product/pyvo-krusovice-svitle-s-p-714651',
            'https://auchan.ua/ua/pivo-krusovice-svetle-svetloe-fil-trovannoe-4-2-0-5-l-539974-1031768/',
            'https://novus.online/product/pivo-svitle-krusovice-svetle-42-05l-sklpl',
            'https://metro.zakaz.ua/ru/products/pivo-krushovitse-500ml--04820046961761/',
            'https://shop.nashkraj.ua/kovel/product/243764-pivo-krusovice-0-5l-svitle-4-2',
            'https://fozzyshop.ua/ru/pivo-svetloe/46786-pivo-krusovice-svetloe-c-b-4820046961761.html'
        ])

    def beer_heineken_svitle_05_l_glass_parser(self):
        ''' Парсер для пива "Heineken светлое" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-khaineken-500ml--04820022692832/',
            'https://shop.silpo.ua/product/pyvo-heineken-svitle-655372',
            'https://auchan.ua/ua/pivo-heineken-svetloe-fil-trovannoe-5-0-5-l-1031798/',
            'https://novus.online/product/pivo-svitle-heineken-5-05l-sklpl',
            'https://metro.zakaz.ua/ru/products/pivo-khaineken-500ml--04820022692832/',
            'https://shop.nashkraj.ua/kovel/product/38289-pivo-heineken-0-5l-svitle-5',
            'https://fozzyshop.ua/ru/pivo-svetloe/26962-pivo-heineken-svetloe-4820022692832.html'
        ])

    def beer_amstel_svitle_05_l_glass_parser(self):
        ''' Парсер для пива "Amstel светлое" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-amstel-500ml-ukrayina--04820046963086/',
            'https://shop.silpo.ua/product/pyvo-amstel-svitle-783828',
            'https://auchan.ua/ua/pivo-amstel-svetloe-fil-trovannoe-5-0-5-l-1031728/',
            'https://novus.online/product/pivo-svitle-amstel-lager-5-05l-sklpl',
            'https://metro.zakaz.ua/ru/products/pivo-amstel-500ml-ukrayina--04820046963086/',
            'https://shop.nashkraj.ua/kovel/product/309059-pivo-amstel-0-5l-5-sklo',
            'https://fozzyshop.ua/ru/pivo-svetloe/63280-pivo-amstel-svetloe-4820046963086.html'
        ])

    def beer_hike_premium_svitle_05_l_glass_parser(self):
        ''' Парсер для пива "Hike Premium светлое" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-khaik-500ml-ukrayina--04820000192439/',
            'https://varus.ua/pivo-0-5l-4-8-svitle-pasterizovane-premium-hike-pl',
            'https://shop.silpo.ua/product/pyvo-hike-premium-131590',
            'https://auchan.ua/ua/pivo-hike-svetloe-4-8-0-5-l-1032043/',
            'https://novus.online/product/pivo-svitle-hike-premium-5-05l',
            'https://metro.zakaz.ua/ru/products/pivo-khaik-500ml-ukrayina--04820000192439/',
            'https://shop.nashkraj.ua/kovel/product/6867-pivo-hike-0-5l-premium',
            'https://fozzyshop.ua/ru/pivo-svetloe/2750-pivo-hike-premium-4820000192439.html'
        ])

    def beer_bochkove_svitle_05_l_glass_parser(self):
        ''' Парсер для пива "Бочкове светлое" 0,5 л в стекле'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-persha-privatna-brovarnia-500ml-ukrayina--04820046960740/',
            'https://varus.ua/pivo-0-5l-4-5-svitle-filtrovane-pasterizovane-bochkove-persha-privatna-brovarnya-pl',
            'https://shop.silpo.ua/product/pyvo-persha-pryvatna-brovarnia-bochkove-svitle-462487',
            'https://auchan.ua/ua/pivo-persha-privatna-brovarnja-bochkovoe-svetloe-fil-trovannoe-4-8-0-5-l-227645-1031783/',
            'https://novus.online/product/pivo-svitle-ppbrovarna-bockove-45-05l',
            'https://metro.zakaz.ua/ru/products/pivo-persha-privatna-brovarnia-500ml-ukrayina--04820046960740/',
            'https://shop.nashkraj.ua/kovel/product/154250-pivo-privatna-brovarnya-0-5l-bochkove-4-8',
            'https://fozzyshop.ua/ru/pivo-svetloe/2923-pivo-ppb-bochkovoe-svetloe-4820046960740.html'
        ])

    def beer_kronenbourg_1664_blanc_svitle_05_l_glass_parser(self):
        ''' Парсер для пива "Пиво Kronenbourg 1664 Blanc" светлое 0,5 л в стекле'''
        return self.prices_parsing([
            'https://varus.ua/pivo-spec-0-46l-blanc-kronenbourg-1664',
            'https://shop.silpo.ua/product/pyvo-kronenbourg-blanc-609226',
            'https://auchan.ua/ua/pivo-kronenbourg-1664-blanc-svetloe-4-8-0-46-l-1031953/',
            'https://metro.zakaz.ua/uk/products/pivo-kronenborg-460ml-ukrayina--04820000455855/',
            'https://shop.nashkraj.ua/kovel/product/215127-pivo-kronenburg-0-46l-1664-blank-4-8',
            'https://fozzyshop.ua/ru/pivo-svetloe/26966-pivo-kronenbourg-1664-blanc-4820000455855.html'
        ])

    def beer_opilla_firmove_nepasterizovane_svitle_05_l_glass_parser(self):
        ''' Парсер для пива "Пиво Опилля Фирменное непастеризованное" светлое 0,5 л в стекле'''
        return self.prices_parsing([
            'https://auchan.ua/ua/pivo-opillja-firmennoe-svetloe-5-7-500-ml-1020689/',
            'https://novus.online/product/pivo-svitle-opilla-firmove-65-05l-sklpl',
            'https://metro.zakaz.ua/uk/products/pivo-opillia-500ml-ukrayina--04820158670056/',
            'https://fozzyshop.ua/ru/pivo-svetloe/37967-pivo-opillya-nepasterizovannoe-4820158670056.html'
        ])

    def beer_yachmenniy_kolos_svitle_05_l_glass_parser(self):
        ''' Парсер для пива "Пиво Ячменный Колос светлое 0,5 л в стекле'''
        return self.prices_parsing([
            'https://fozzyshop.ua/ru/pivo-svetloe/2949-pivo-poltavpivo-yachminnij-kolos-svetloe-4820009362543.html'
        ])

    def beer_opilla_korifey_svitle_05_l_glass_parser(self):
        ''' Парсер для пива "Пиво Опилля Корифей светлое 0,5 л в стекле'''
        return self.prices_parsing([
            'https://varus.ua/pivo-0-5l-3-7-svitle-opillya-korifey-pl',
            'https://auchan.ua/ua/pivo-opillja-korifej-3-7-500-ml-1020677/',
            'https://novus.online/product/pivo-svitle-opilla-korifej-42-05l-sklpl',
            'https://metro.zakaz.ua/uk/products/pivo-opillia-500ml-ukrayina--04820158670018/',
            'https://fozzyshop.ua/ru/pivo-svetloe/37966-pivo-opillya-korifej-4820158670018.html'
        ])

    def beer_chaika_dniprovskaya_svitle_05_l_glass_parser(self):
        ''' Парсер для пива "Пиво Чайка Днепровская светлое 0,5 л в стекле'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-chaika-500ml-ukrayina--04820046964380/',
            'https://shop.silpo.ua/product/pyvo-chaika-dniprovska-svitle-866176',
            'https://novus.online/product/pyvo-svitle-chayka-dniprovska-48-045l-spl',
            'https://metro.zakaz.ua/uk/products/pivo-chaika-500ml-ukrayina--04820046964380/',
            'https://fozzyshop.ua/ru/pivo-svetloe/88457-pivo-chajka-dniprovska-svetloe-4820046964380.html',
        ])

    def beer_chaika_chernomorskaya_svitle_05_l_glass_parser(self):
        ''' Парсер для пива "Пиво Чайка Черноморская светлое 0,5 л в стекле'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-persha-privatna-brovarnia-450ml--04820046964403/',
            'https://shop.silpo.ua/product/pyvo-chaika-chornomorska-svitle-866177',
            'https://novus.online/product/pyvo-svitle-chayka-chornomorska-45-045l-spl',
            'https://metro.zakaz.ua/uk/products/pivo-persha-privatna-brovarnia-450ml--04820046964403/',
            'https://fozzyshop.ua/ru/pivo-svetloe/88461-pivo-chajka-chornomorska-svetloe-4820046964403.html'
        ])

    def beer_uman_waissburg_svitle_1l_plastic_parser(self):
        ''' Парсер для пива "Пиво Умань Waissburg светлое 1 л в пластике'''
        return self.prices_parsing([
            'https://varus.ua/pivo-umanpivo-waissburg-lager-svetloe-filtrovannoe-4-7-1-l',
            'https://auchan.ua/ua/pivo-waissburg-lager-4-7-1-l-1021005/',
            'https://novus.online/product/pivo-svitle-vajsburg-uman-pet1l',
            'https://fozzyshop.ua/ru/pivo-svetloe/2993-pivo-umanpivo-waissburg-svetloe-4820009940376.html'
        ])

    def beer_uman_pshenichnoe_svitle_1l_plastic_parser(self):
        ''' Парсер для пива "Пиво Умань пшеничное светлое 1 л в пластике'''
        return self.prices_parsing([
            'https://novus.online/product/pivo-1l-44-umanske-psenicne-svitle-pet',
            'https://fozzyshop.ua/ru/pivo-svetloe/50286-pivo-umanpivo-pshenichnoe-svetloe-4820009940383.html'
        ])

    def beer_berdichevske_hmilne_svitle_1l_plastic_parser(self):
        ''' Парсер для пива "Пиво Бердичевское хмельное светлое 1 л в пластике'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/pyvo-berdychivske-khmilne-348650',
            'https://novus.online/product/pivo-svitle-hmilne-berdiciv-pet1l',
            'https://fozzyshop.ua/ru/pivo-svetloe/37953-pivo-berdichivske-khmelnoe-4820003210383.html'
        ])

    def beer_berdichevske_lager_svitle_1l_plastic_parser(self):
        ''' Парсер для пива "Пиво Бердичевское хмельное светлое 1 л в пластике'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/pyvo-berdychivske-lager-svitle-425212',
            'https://metro.zakaz.ua/uk/products/pivo-berdichivske-1000ml-ukrayina--04820003210567/',
            'https://fozzyshop.ua/ru/pivo-svetloe/37948-pivo-berdichivske-lager-svetloe-4820003210567.html'
        ])

    def beer_opilla_korifey_11l_plastic_parser(self):
        ''' Парсер для пива "Пиво Опилля Корифей 1.1 л в пластике'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-11-l-opilla-korifej-svitle',
            'https://novus.online/product/pivo-svitle-opilla-korifej-42-1l-pet',
            'https://metro.zakaz.ua/uk/products/pivo-opillia-1000ml-ukrayina--04820001586725/'
        ])

    def beer_obolon_jigulivske_eksportne_15l_plastic_parser(self):
        ''' Парсер для пива "Пиво Оболонь Жигулевское экспортное 1.5 л в пластике'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-15l-obolon-zigulivske-eksportone-svitle'
        ])

    def beer_yantar_svitle_12l_plastic_parser(self):
        ''' Парсер для пива "Пиво Янтарь светлое 1.2 л в пластике'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-12l-antar-svitle',
            'https://auchan.ua/ua/pivo-jantar-svetloe-4-5-1-2-l-1021245/',
            'https://novus.online/product/pivo-svitle-antar-45-1l-pet',
            'https://metro.zakaz.ua/uk/products/pivo-iantar-1000ml-ukrayina--04820034921746/',
            'https://fozzyshop.ua/ru/pivo-svetloe/42649-pivo-yantar-svetloe-4820034921746.html'
        ])

    def beer_jashkovske_pshenichne_1l_plastic_parser(self):
        ''' Парсер для пива "Пиво Жашковское пшеничное нефильтрованное 1.0 л в пластике'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-zhashkivske-1000ml--04820097899396/',
            'https://novus.online/product/pyvo-svitle-zhashkivske-pshenychne-47-pet-1l'
        ])

    def beer_jashkovske_svitle_1l_plastic_parser(self):
        ''' Парсер для пива "Пиво Жашковское светлое нефильтрованное 1.0 л в пластике'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-1000ml--04820097899389/',
            'https://novus.online/product/pyvo-svitle-zhashkivske-svitle-45-pet-1l'
        ])

    def beer_jashkovske_jigulivske_nefilter_1l_plastic_parser(self):
        ''' Парсер для пива "Пиво Жашковское игулевское нефильтрованное 1.0 л в пластике'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-1000ml--04820097899372/',
            'https://shop.silpo.ua/product/pyvo-zhashkivske-zhygulivske-svitle-nefiltrovane-851784',
            'https://novus.online/product/pyvo-svitle-zhashkivske-zhyhulivske-42-pet-1l'
        ])

    def beer_persha_privatna_brovarnya_bochkove_1l_plastic_parser(self):
        ''' Парсер для пива "Пиво Перша приватна броварня Бочкове 1.0 л в пластике'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-persha-privatna-brovarnia-1000ml-ukrayina--04820046960733/',
            'https://novus.online/product/pivo-svitle-ppbrovarna-bockove-45-petplaska-1l'
        ])

    def beer_chayka_dniprovska_1l_plastic_parser(self):
        ''' Парсер для пива "Пиво Чайка днипровська 1.0 л в пластике'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-ukrayina--04820046964724/',
            'https://shop.silpo.ua/product/pyvo-chaika-dniprovska-svitle-874997'
        ])

    def beer_ketchup_torchin_s_chasnikom_parser(self):
        ''' Парсер для кетчупа "Торчин с чесноком 270 грамм'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/ketchup-torchin-270g--07613036162388/',
            'https://varus.ua/ketchup-torchin-z-chasnikom-270-g',
            'https://metro.zakaz.ua/uk/products/ketchup-torchin-270g--07613036162388/',
            'https://fozzyshop.ua/ru/ketchup/56876-ketchup-torchin-s-chesnokom-d-p-7613036162388.html'
        ])

    def mayonez_korolivskiy_smak_korolivskiy_67_300gr_parser(self):
        ''' Парсер для кетчупа Майонез Королевский Смак королевский 67 % 300 гр'''
        return self.prices_parsing([
            'https://atbmarket.com/product/majonez-300-g-korolivskij-smak-korolivskij-67',
            'https://eko.zakaz.ua/uk/products/maionez-korolivskii-smak-300g--04820175669682/',
            'https://varus.ua/majonez-korolivskij-smak-korolevskij-67-300-g',
            'https://novus.online/product/majoneznyj-sous-korolevskij-vkus-korolevskij-67-300g',
            'https://metro.zakaz.ua/uk/products/maionez-korolivskii-smak-380g-ukrayina--04820044096946/',
            'https://fozzyshop.ua/ru/majonez/94730-majonez-korolivskij-smak-korolevskij-67-d-p-4820175669699.html'
        ])

    def sous_chumak_chesnochniy_200gr_parser(self):
        ''' Парсер для кетчупа Соус Чумак чесночный 200 грамм'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/sous-priprava-chumak-200g--04823096002125/',
            'https://varus.ua/sous-chasnikoviy-chumak-dp-200g',
            'https://novus.online/product/cumak-sous-casnikovij-dp-200g'
        ])

    def orbit_banan_polunica_parser(self):
        ''' Парсер для жвачки Orbit банан-полуниця'''
        return self.prices_parsing([
            'https://atbmarket.com/product/zuvalna-gumka-14g-wrigleys-orbit-polunica-banan',
            'https://eko.zakaz.ua/uk/products/gumka-orbit-14g--00000042306740/',
            'https://varus.ua/zhuvalna-gumka-polunicya-banan-rigli-orbit-13-6g',
            'https://auchan.ua/ua/zhevatelnaja-rezinka-orbit-klubnika-banan-14-g-611121/',
            'https://novus.online/product/gumka-zuvalna-orbit-polunicabanan-14g',
            'https://metro.zakaz.ua/uk/products/gumka-orbit-14g--metro00000042306740/',
            'https://shop.nashkraj.ua/kovel/product/149165-zhuv-gumka-orbit-14g-polunitsya-banan',
            'https://fozzyshop.ua/ru/zhevatelnye-rezinki/43850-rezinka-zhevatelnaya-orbit-klubnika-banan-42306740.html'
        ])

    def sigarets_lm_red_parser(self):
        ''' Парсер для сигарет LM красные'''
        return self.prices_parsing([
            'https://auchan.ua/ua/sigarety-l-m-red-label-20-sht-916744/',
            'https://novus.online/product/cigarki-lm-red',
            'https://fozzyshop.ua/ru/sigarety/98991-sigarety-lm-red-label-0250014950994.html'
        ])

    def beer_chernigivske_bile_nefilter_1l_parser(self):
        ''' Парсер для пива Черниговское Белое нефильтрованное 1 литр'''
        return self.prices_parsing([
            'https://novus.online/product/pyvo-svitle-chernihivske-bile-nefiltrovane-48-pet-09l',
            'https://metro.zakaz.ua/uk/products/pivo-chernigivske-1000ml-ukrayina--04820034920329/',
            'https://fozzyshop.ua/ru/pivo-svetloe/100322-pivo-chernigivske-beloe-svetloe-nefiltrovannoe-250015036314.html'
        ])

    def beer_obolon_svitle_1l_parser(self):
        ''' Парсер для пива Оболонь светлое 1 литр'''
        return self.prices_parsing([
            'https://varus.ua/pivo-svitle-obolon-1-1l-ukraina',
            'https://novus.online/product/pyvo-svitle-obolon-45-11l-pet'
        ])

    def beer_rogan_tradiciyne_svitle_1l_parser(self):
        ''' Парсер для пива Рогань традиционное светлое 1 литр'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-1-l-rogan-tradicijne-svitle-pet',
            'https://auchan.ua/ua/pivo-rogan-tradicionnoe-svetloe-4-8-1-l-1021239/',
            'https://novus.online/product/pivo-svitle-rogan-tradicijne-48-1l-pet',
            'https://metro.zakaz.ua/uk/products/pivo-rogan-1000ml-ukrayina--04820034921609/',
            'https://shop.nashkraj.ua/kovel/product/6795-pivo-rogan-1l-traditsiyne-svitle-pet4-8',
            'https://fozzyshop.ua/ru/pivo-svetloe/20248-pivo-rogan-tradicijne-svetloe-4820034921609.html'
        ])

    def beer_jigulivske_svitle_2l_plastic_parser(self):
        ''' Парсер для пива Жигулевское светлое 2 литра в пластике'''
        return self.prices_parsing([
            'https://varus.ua/pivo-zhigulivske-obolon-2-4l',
        ])

    def beer_chayka_dniprovska_2l_plastic_parser(self):
        ''' Парсер для пива Чайка днепровская светлое 2 литра в пластике'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/pyvo-chaika-dniprovska-svitle-832996',
            'https://novus.online/product/pivo-svitle-cajka-dniprovska-48-2l-pet',
            'https://metro.zakaz.ua/uk/products/pivo-chaika-2000ml--04820046964076/',
            'https://fozzyshop.ua/ru/pivo-svetloe/92485-pivo-chajka-dneprovskaya-svetloe-4820046964083.html'
        ])

    def beer_piwny_kebek_svitle_2l_plastic_parser(self):
        ''' Парсер для пива Piwny Kebek светлое 2 литра в пластике'''
        return self.prices_parsing([
            'https://varus.ua/pivo-piwny-kubek-2l',
        ])

    def ketchup_torchin_do_shashliky_270gr_parser(self):
        ''' Парсер для кетчупа Торчин до шашлику 270 грамм'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/ketchup-torchin-270g--07613036160728/',
            'https://varus.ua/ketchup-torchin-do-shashliku-400-g',
            'https://shop.silpo.ua/product/ketchup-torchyn-do-shashlyku-767757',
            'https://auchan.ua/ua/ketchup-chumak-k-shashlyku-doj-pak-270-g-274436/',
            'https://novus.online/product/ketcup-do-sasliku-torcin-dp-270g',
            'https://fozzyshop.ua/ru/ketchup/56869-ketchup-torchin-k-shashlyku-d-p-7613036160728.html'
        ])

    def mayonez_chumak_appetitniy_50_300gr_parser(self):
        ''' Парсер для майонеза Чумак аппетитный 50% 300 грамм'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/maionez-chumak-300g--04823096003412/',
            'https://varus.ua/mayonez-apetitniy-50-chumak-300g-dp',
            'https://shop.silpo.ua/product/maionez-chumak-apetytnyi-50-819161',
            'https://novus.online/product/majonez-apetitnij-50-cumak-dp-300g',
            'https://metro.zakaz.ua/uk/products/maionez-chumak-300g--04823096003412/'
        ])

    def coffee_chorna_karta_50gr_parser(self):
        ''' Парсер для кофе Черная карта 50 грамм'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/kava-chorna-karta--08719325020113/'
        ])

    def beer_arsenal_micne_2l_plastic_parser(self):
        ''' Парсер для пива Арсенал мицне 2 литра в пластике'''
        return self.prices_parsing([
            'https://metro.zakaz.ua/uk/products/pivo-arsenal-ukrayina--04820250940842/',
            'https://shop.nashkraj.ua/kovel/product/33436-pivo-arsenal-2l-mitsne-8',
            'https://fozzyshop.ua/ru/pivo-svetloe/2846-pivo-arsenal-micne-svetloe-4820000451444.html'
        ])

    def beer_ppb_bochkove_svitle_2l_plastic_parser(self):
        ''' Парсер для пива ППБ Бочкове свитле 2 литра в пластике'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-persha-privatna-brovarnia-2000ml-ukrayina--04820046960856/',
            'https://shop.silpo.ua/product/pyvo-persha-pryvatna-brovarnia-bochkove-svitle-474835',
            'https://novus.online/product/pivo-svitle-bockove-ppb-2l',
            'https://metro.zakaz.ua/uk/products/pivo-persha-privatna-brovarnia-2000ml-ukrayina--04820046960856/'
        ])

    def beer_ppb_zakarpatske_svitle_2l_plastic_parser(self):
        ''' Парсер для пива ППБ Закарпатське свитле 2 литра в пластике'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/pyvo-persha-pryvatna-brovarnia-zakarpatske-oryginalne-svitle-660939',
            'https://novus.online/product/pivo-2l-zakarpatskoe-ppb-pet',
            'https://metro.zakaz.ua/uk/products/pivo-persha-privatna-brovarnia-2000ml--04820046961266/'
        ])

    def beer_zibert_svitle_05l_v_banke_parser(self):
        ''' Парсер для пива Зиберт светлое 0,5 л в банке'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05l-zibert-lager-beer-svitle-zb',
            'https://eko.zakaz.ua/uk/products/pivo-zibert-500ml--04820193030303/',
            'https://varus.ua/pivo-zibert-svitle-filtrovane-4-4-0-5-l',
            'https://novus.online/product/pyvo-svitle-zibert-44-05l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-zibert-500ml--04820193030303/'
        ])

    def yogurt_fanni_lisovi_yagodi_1_5_240gr_stakan_parser(self):
        ''' Парсер для пива Зиберт светлое 0,5 л в банке'''
        return self.prices_parsing([
            'https://varus.ua/yogurt-lisyagoda-1-5-fanni-240g-stakan',
            'https://shop.silpo.ua/product/yogurt-fanni-lisova-iagoda-1-5-stakan-854431'
        ])

    def beer_obolon_kievskoe_razlivnoe_svetloe_195l_parser(self):
        ''' Парсер для пива Оболонь Киевское розливное светлое 1,95 литра в пластике'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-obolon-1950ml-ukrayina--04820193032284/',
            'https://varus.ua/pivo-1-95l-3-8-svitle-pasterizovane-kiivske-rozlivne-obolon-ppl',
            'https://novus.online/product/pivo-svitle-obolon-kiivske-rozlivne-38-195l-pet',
            'https://metro.zakaz.ua/uk/products/pivo-obolon-1950ml-ukrayina--04820193032284/'
        ])

    def beer_chernigivske_light_svitle_2l_plastic_parser(self):
        ''' Парсер для Пиво Черниговское light светлое 2,0 л в пластике'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-2-l-cernigivske-light-svitle-pet',
            'https://shop.silpo.ua/product/pyvo-chernigivske-light-svitle-921796',
            'https://metro.zakaz.ua/uk/products/ukrayina--04820034925898/'
        ])

    def beer_opilla_korifey_svitle_2l_plastic_parser(self):
        ''' Парсер для Пиво Опилля Корифей светлое 2,0 л в пластике'''
        return self.prices_parsing([
            'https://auchan.ua/ua/pivo-opillja-korifej-3-7-2-l-1020713/',
            'https://novus.online/product/pyvo-svitle-opillya-koryfey-42-2l-plastykova-plyashka',
            'https://metro.zakaz.ua/uk/products/pivo-opillia-2000ml-ukrayina--04820158671565/'
        ])

    def beer_yantar_svitle_2l_plastic_parser(self):
        ''' Парсер для Пиво Янтарь светлое 2,0 л в пластике'''
        return self.prices_parsing([
            'https://metro.zakaz.ua/uk/products/pivo-iantar-2000ml-ukrayina--04820034920626/'
        ])

    def beer_tuborg_green_svitle_4_banki_05l_parser(self):
        ''' Парсер для Пиво Tuborg Green 4 банки х 0,5 л'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/pyvo-tuborg-green-svitle-z-b-224869',
            'https://auchan.ua/ua/upakovka-piva-tuborg-green-svetloe-fil-trovannoe-4-6-4-sht-h0-5-l-1031988/',
            'https://metro.zakaz.ua/uk/products/pivo-tuborg-2000ml-ukrayina--04820000452687/',
            'https://fozzyshop.ua/ru/pivo-svetloe/2689-pivo-tuborg-green-svetloe-multipak-4820000452687.html'
        ])

    def beer_ppb_zakarpatske_svitle_4_banki_05l_parser(self):
        ''' Парсер для Пиво ППБ Закарпатське 4 банки х 0,5 л'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/pyvo-persha-pryvatna-brovarnia-zakarpatske-oryginalne-svitle-z-b-825769',
            'https://auchan.ua/ua/pivo-persha-privatna-brovarnja-zakarpats-ke-svetloe-4-1-4-sht-h-0-5-l-1031698/',
            'https://novus.online/product/pivo-svitle-ppb-zakarpatske-originalne-44-05l4-zb',
            'https://metro.zakaz.ua/uk/products/pivo-persha-privatna-brovarnia-2000ml-ukrayina--04820046963918/'
        ])

    def beer_ppb_bochkove_svitle_4_banki_05l_parser(self):
        ''' Парсер для Пиво ППБ Бочкове 4 банки х 0,5 л'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/pyvo-persha-pryvatna-brovarnia-bochkove-svitle-z-b-810145',
            'https://novus.online/product/pivo-svitle-ppb-bockove-48-05l4-zb',
            'https://metro.zakaz.ua/uk/products/pivo-persha-privatna-brovarnia-2000ml--04820046963741/'
        ])

    def beer_budweiser_budvar_svitle_05l_parser(self):
        ''' Парсер для Пиво Budweiser Budvar светлое 0,5 л в стекле'''
        return self.prices_parsing([
            'https://varus.ua/pivo-0-5l-5-sv-budweiser-budvar-borig',
            'https://auchan.ua/ua/pivo-budweiser-budvar-svetloe-fil-trovannoe-5-0-5-l-577071-1031543/',
            'https://novus.online/product/pivo-svitle-budweiser-budvar-5-05l-sklpl',
            'https://metro.zakaz.ua/uk/products/pivo-budvaizer-budvar-500ml-chekhiia--08594403110111/'
        ])

    def beer_pilsner_urquell_05l_glass_parser(self):
        ''' Парсер для Пиво Pilsner Urquell светлое 0,5 л в стекле'''
        return self.prices_parsing([
            'https://metro.zakaz.ua/uk/products/pivo-budvaizer-budvar-500ml-chekhiia--08594403110111/'
        ])

    def beer_robert_doms_belgiyskiy_svitle_nefilter_05l_glass_parser(self):
        ''' Парсер для Пиво Robert Doms бельгийский светлое нефильтрованное 0,5 л в стекле'''
        return self.prices_parsing([
            'https://varus.ua/pivo-spec-0-5l-belgiyskiy-robert-doms',
            'https://shop.silpo.ua/product/pyvo-robert-doms-belgiiske-svitle-nefiltrovane-666610',
            'https://metro.zakaz.ua/uk/products/pivo-lvivske-500ml--04820000456401/'
        ])

    def beer_chernigivske_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Черниговское светлое 0,5 л жб'''
        return self.prices_parsing([
            'https://auchan.ua/ua/pivo-chernigivs-ke-svetloe-v-banke-4-8-500-ml-1021107/',
            'https://novus.online/product/pivo-svitle-cernigivske-48-05l-zb',
            'https://fozzyshop.ua/ru/pivo-svetloe/3002-pivo-chernigivske-svetloe-4820000381239.html'
        ])

    def beer_chernigivske_bile_nefilter_05_l_jb_parser(self):
        ''' Парсер для Пиво Черниговское белое нефильтрованное 0,5 л жб'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/pivo-05-l-cepnigivske-bile',
            'https://shop.silpo.ua/product/pyvo-chernigivske-bile-nefiltrovane-z-b-68067',
            'https://auchan.ua/ua/pivo-chernigivs-ke-beloe-svetloe-v-banke-5-500-ml-1021095/',
            'https://metro.zakaz.ua/uk/products/pivo-chernigivske-500ml-ukrayina--04820034920336/',
            'https://fozzyshop.ua/ru/pivo-svetloe/2984-pivo-chernigivske-bile-nefiltrovannoe-4820000380706.html'
        ])

    def beer_velkopopovicky_kozel_temne_05_l_jb_parser(self):
        ''' Парсер для Пиво Velkopopovicky Kozel темное 0,5 л жб'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05l-velkopopovicky-kozel-temne',
            'https://auchan.ua/ua/pivo-kozel-temnoe-v-banke-3-8-500-ml-1021101/',
            'https://novus.online/product/pivo-temne-velkopopovicky-kozel-cerny-38-05l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-velkopopovitskii-kozel-500ml-ukrayina--04820034924211/',
            'https://fozzyshop.ua/ru/pivo-temnoe/64333-pivo-velkopopovitsky-kozel-temnoe-zh-b-4820034924211.html'
        ])

    def beer_edelmeister_pilsner_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Edelmeister Pilsner светлое 0,5 л жб'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05-l-edelmeister-pilsner-svitle-filtrovane-45-polsa'
        ])

    def beer_faxe_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Faxe светлое 0,5 л жб'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05-l-faxe-svitle-filtrovane-46-litva'
        ])

    def beer_livu_pilzenes_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Livu Pilzenes светлое 0,5 л жб'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05l-livu-pilzenes-svitle-filtrovane-44-litva'
        ])

    def beer_velkopopovicky_kozel_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Velkopopovicky Kozel светлое 0,5 л жб'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05l-velkopopovicky-kozel-svitle',
            'https://shop.silpo.ua/product/pyvo-velkopopovitsky-kozel-4-svitle-z-b-786389',
            'https://auchan.ua/ua/pivo-kozel-svetloe-v-banke-4-500-ml-1021131/',
            'https://novus.online/product/pivo-svitle-velkopopovicky-kozel-svetly-40-05l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-velkopopovitskii-kozel-500ml-ukrayina--04820034924174/'
        ])

    def beer_obolon_beermix_limon_05_l_jb_parser(self):
        ''' Парсер для Пиво Obolon Beermix limon светлое 0,5 л жб'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05l-obolon-beermix-limon',
            'https://eko.zakaz.ua/uk/products/pivo-birmiks-500ml-ukrayina--04820000192101/',
            'https://varus.ua/pivo-birmiks-limon-obolon-0-5l-z-b-ukraina',
            'https://shop.silpo.ua/product/pyvo-obolon-beermix-lymon-z-b-59268',
            'https://auchan.ua/ua/pivo-obolon-beermix-limon-svetloe-fil-trovannoe-2-5-0-5-l-1032053/',
            'https://novus.online/product/pivo-specialne-obolon-beermix-lemon-25-05l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-birmiks-500ml-ukrayina--04820000192101/',
            'https://shop.nashkraj.ua/kovel/product/6752-pivo-obolon-birmiks-0-5l-limon-zh-b2-5',
            'https://fozzyshop.ua/ru/slaboalkogolnye-napitki/2901-pivo-obolon-beermix-limon-4820000192101.html'
        ])

    def beer_edelmeister_weizenbier_svitle_nefilter_05_l_jb_parser(self):
        ''' Парсер для Пиво Edelmeister Weizenbier нефильтрованное светлое 0,5 л жб'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05-l-edelmeister-weizenbier-svitle-nefiltrovane-52-polsa'
        ])

    def beer_edelmeister_schwarzbier_temne_05_l_jb_parser(self):
        ''' Парсер для Пиво Edelmeister schwarzbier темное 0,5 л жб'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05-l-edelmeister-schwarzbier-temne-filtrovane-42-polsa'
        ])

    def beer_hike_blanche_nefilter_05_l_jb_parser(self):
        ''' Парсер для Пиво Hike Blanche нефильтрованное 0,5 л жб'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05l-hike-blanche-svitle-nefiltpovane',
            'https://eko.zakaz.ua/uk/products/pivo-khaik-500ml-ukrayina--04820193032314/',
            'https://varus.ua/pivo-blansh-4-9-hayk-0-5l-z-b-ukraina',
            'https://auchan.ua/ua/pivo-hike-blanche-svetloe-nefil-trovannoe-4-9-zh-b-0-5-l-1031618/',
            'https://novus.online/product/pivo-svitle-hike-blans-49-05l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-khaik-500ml-ukrayina--04820193032314/'
        ])

    def beer_zlata_praha_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Zlata Praha светлое 0,5 л жб'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05l-zlata-praha-svitle',
            'https://varus.ua/pivo-0-5l-5-svitle-pasterizovane-zlata-praha-zb',
            'https://auchan.ua/ua/pivo-zlata-praha-svetloe-fil-trovannoe-5-0-0-5-l-1032028/'
        ])

    def beer_thuringer_premium_beer_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Thuringer premium beer светлое 0,5 л жб'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05l-thuringer-premium-beer-svitle-filtrovane-nimeccina'
        ])

    def beer_livu_sencu_beer_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Livu Sencu светлое 0,5 л жб'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05l-livu-sencu-svitle-filtrovane-52-litva'
        ])

    def beer_germanarich_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Germanarich светлое 0,5 л жб'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05-l-germanarich-svetloe'
        ])

    def beer_hike_premium_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Hike Premium светлое 0,5 л жб'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05l-hike-premium-svitle',
            'https://eko.zakaz.ua/uk/products/pivo-khaik-500ml-ukrayina--04820000192514/',
            'https://varus.ua/pivo-hayk-premium-0-5l-z-b',
            'https://shop.silpo.ua/product/pyvo-hike-premium-z-b-196380',
            'https://auchan.ua/ua/pivo-hike-svetloe-fil-trovannoe-4-8-0-5-l-1032038/',
            'https://novus.online/product/pivo-svitle-hike-premium-49-05l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-khaik-500ml-ukrayina--04820000192514/',
            'https://fozzyshop.ua/ru/pivo-svetloe/20156-pivo-hike-premium-4820000192514.html'
        ])

    def beer_obolon_nonalcohol_nefilter_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Obolon безалкогольное нефильтрованное светлое 0,5 л жб'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-bezalkogolne-05l-obolon-0-svitle-nefiltrovane-pastepizovane',
            'https://varus.ua/pivo-specialne-0-5l-0-5-svitle-pasterizovane-0-nefiltrovane-plus-obolon-zb',
            'https://auchan.ua/ua/pivo-0-obolon-bezalkogol-noe-svetloe-nefil-trovannoe-0-5-0-5-l-1031603/'
        ])

    def beer_zibert_bavarskoe_svitle_05_l_jb_parser(self):
        ''' Парсер для Пивo Zibert Баварское светлое 0,5 л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-zibert-500ml--04820193034011/',
            'https://novus.online/product/pyvo-svitle-zibert-bavarske-5-05l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-zibert-500ml--04820193034011/'
        ])

    def beer_bavaria_liquid_apple_ninalco_svitle_05_l_jb_parser(self):
        ''' Парсер для Пивo Bavaria Liquid Apple безалкогольное светлое 0,5 л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo--08714800017602/'
        ])

    def beer_heineken_svitle_05_l_jb_parser(self):
        ''' Парсер для Пивo Heineken светлое 0,5 л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-khaineken-500ml--04820046962010/',
            'https://varus.ua/pivo-0-5l-5-svitle-filtrovane-heineken',
            'https://shop.silpo.ua/product/pyvo-heineken-svitle-z-b-721739',
            'https://auchan.ua/ua/pivo-heineken-svetloe-fil-trovannoe-5-zh-b-0-5-l-1031763/',
            'https://novus.online/product/pivo-svitle-heineken-5-05l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-khaineken-500ml--04820046962010/',
            'https://fozzyshop.ua/ru/pivo-svetloe/46783-pivo-heineken-svetloe-zh-b-4820046962010.html'
        ])

    def beer_rychtar_grant_11_svitle_05_l_jb_parser(self):
        ''' Парсер для Пивo Rychtar Grant 11 светлое 0,5 л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-500ml--08594018930074/'
        ])

    def beer_amstel_svitle_05_l_jb_parser(self):
        ''' Парсер для Пивo Amstel светлое 0,5 л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-amstel-500ml-ukrayina--04820046963109/',
            'https://varus.ua/pivo-0-5l-5-svitle-filtrovane-amstel-zb',
            'https://shop.silpo.ua/product/pyvo-amstel-svitle-z-b-783829',
            'https://auchan.ua/ua/pivo-amstel-svetloe-fil-trovannoe-5-zh-b-0-5-l-1031723/',
            'https://novus.online/product/pivo-svitle-amstel-lager-5-05l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-amstel-500ml-ukrayina--04820046963109/',
            'https://fozzyshop.ua/ru/pivo-svetloe/63281-pivo-amstel-svetloe-zh-b-4820046963109.html'
        ])

    def beer_bavaria_svitle_05_l_jb_parser(self):
        ''' Парсер для Пивo Bavaria светлое 0,5 л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-bavariia-500ml-golandiia--08714800007191/',
            'https://varus.ua/pivo-svitle-bavariya-0-5l-z-b',
            'https://auchan.ua/ua/pivo-bavaria-svetloe-fil-trovannoe-5-0-5-l-1032139/',
            'https://metro.zakaz.ua/uk/products/pivo-bavariia-500ml-golandiia--08714800007191/'
        ])

    def beer_bavaria_svitle_nonalcohol_05_l_jb_parser(self):
        ''' Парсер для Пивo Bavaria светлое безалкогольное 0,5 л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-bavariia-500ml--ekomarket00000026220352/',
            'https://varus.ua/bavariya-pivo-0-5l-z-b-b-a'
        ])

    def beer_edelburg_lager_05_l_jb_parser(self):
        ''' Парсер для Пиво Edelburg Lager світле 5,2% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-500ml-nimechchina--04260684190046/',
            'https://metro.zakaz.ua/uk/products/pivo-500ml-nimechchina--04260684190046/'
        ])

    def beer_donner_pils_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Donner Pils світле 3,5% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-500ml--05900535001488/'
        ])

    def beer_dutch_windmill_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Dutch Windmill світле 4,6% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-500ml--08714800029735/',
            'https://varus.ua/pivo-dach-vindmill-0-5-l-zh-b',
            'https://novus.online/product/pivo-svitle-dutch-windmill-46-05l-zb'
        ])

    def beer_edelburg_hefeweizen_svitle_nefilter_05_l_jb_parser(self):
        ''' Парсер для Пиво Edelburg Hefeweizen світле нефільтроване 5,1% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-500ml-nimechchina--04260684190015/',
            'https://metro.zakaz.ua/uk/products/pivo-500ml-nimechchina--04260684190015/'
        ])

    def beer_edelmeister_unfiltered_svitle_nefilter_05_l_jb_parser(self):
        ''' Парсер для Пиво Edelmeister Unfiltered світле нефільтроване 5,7% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-edelmeister-500ml--05900535016192/'
        ])

    def beer_estrella_damm_barcelona_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Estrella Damm Barcelona світле 4,6% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-estrella-500ml-ispaniia--08410793286123/',
            'https://shop.silpo.ua/product/pyvo-estrella-damm-barcelona-svitle-z-b-489877',
            'https://novus.online/product/pivo-svitle-estrella-damm-barcelona-46-05-zb',
            'https://metro.zakaz.ua/uk/products/pivo-estrella-500ml-ispaniia--08410793286123/',
            'https://fozzyshop.ua/ru/pivo-svetloe/40047-pivo-estrella-damm-barcelona-svetloe-zh-b-8410793286123.html'
        ])

    def beer_halne_jasne_pelne_05_l_jb_parser(self):
        ''' Парсер для Пиво Halne Jasne Pelne з/б 6% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-khalne-500ml-polshcha--05900535009293/',
            'https://novus.online/product/pivo-svitle-halne-pelne-6-05l-zb'
        ])

    def beer_eurotour_hefeweissbier_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Eurotour Hefeweissbier світле 5% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-500ml--04014086086908/'
        ])

    def beer_hollandia_strong_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Hollandia Strong світле 7,5% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-gollandiia-500ml-golandiia--08714800017305/',
            'https://varus.ua/pivo-hollandia-svetloe-filtrovanoe-7-5-0-5-l',
            'https://auchan.ua/ua/pivo-hollandia-strong-svetloe-fil-trovannoe-7-5-0-5-l-1031523/'
        ])

    def beer_lander_brau_premium_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Lander Brau Premium світле 4,9% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-lander-brau-500ml--08714800026697/',
            'https://varus.ua/pivo-lander-brau-premium-pilsner-svetloe-filtrovannoe-4-9-0-5-l',
            'https://metro.zakaz.ua/uk/products/pivo-lander-brau-500ml--08714800026697/'
        ])

    def beer_saku_kuld_05_l_jb_parser(self):
        ''' Парсер для Пиво Saku Kuld 5,2% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo--04740019113259/'
        ])

    def beer_saku_originaal_05_l_jb_parser(self):
        ''' Парсер для Пиво Saku Originaal 4,7% 0,5л л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo--04740019766233/'
        ])

    def beer_stangen_lager_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Stangen Lager світле 5,4% 0,5л л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-500ml-nimechchina--04260556080055/'
        ])

    def beer_van_pur_premium_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Van Pur Premium світле 5% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-500ml--05900535000160/'
        ])

    def beer_bavaria_mango_marakya_nonalco_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Bavaria манго-маракуйя світле безалкогольне 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-500ml--08714800036023/'
        ])

    def beer_bavaria_granat_nonalco_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Bavaria гранат світле безалкогольне 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-bavariia-500ml--08714800040846/'
        ])

    def beer_obolon_beermix_malina_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Оболонь Beermix Малина світле 2,5% 0,5л жб'''
        return self.prices_parsing([
            'https://atbmarket.com/product/pivo-05-l-obolon-beermix-malina',
            'https://eko.zakaz.ua/uk/products/pivo-birmiks-500ml-ukrayina--04820000193238/',
            'https://auchan.ua/ua/pivo-obolon-beermix-malina-svetloe-fil-trovannoe-2-5-0-5-l-1032033/',
            'https://shop.nashkraj.ua/kovel/product/6753-pivo-obolon-birmiks-0-5l-malina-zh-b2-5'
        ])

    def beer_obolon_beermix_vishnya_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Оболонь Beermix Вишня світле 2,5% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-birmiks-500ml-ukrayina--04820000192125/',
            'https://varus.ua/pivo-birmiks-vishnya-obolon-0-5l-z-b',
            'https://shop.silpo.ua/product/pyvo-obolon-beermix-vyshnia-z-b-90894',
            'https://auchan.ua/ua/pivo-obolon-beermix-vishnja-svetloe-fil-trovannoe-2-5-0-5-l-1032048/',
            'https://novus.online/product/pivo-specialne-obolon-beermix-cherry-25-05l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-birmiks-500ml-ukrayina--04820000192125/',
            'https://shop.nashkraj.ua/kovel/product/6750-pivo-obolon-birmiks-0-5l-vishnya-zh-b-2-5',
            'https://fozzyshop.ua/ru/slaboalkogolnye-napitki/2891-pivo-obolon-beermix-vishnya-4820000192125.html'
        ])

    def beer_lomza_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Lomza світле 5,7% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-500ml--05903538900765/'
        ])

    def beer_paderborner_pilsener_05_l_jb_parser(self):
        ''' Парсер для Пиво Paderborner Pilsener світле 4,8% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-paderborner-500ml-nimechchina--04101120015106/',
            'https://shop.silpo.ua/product/pyvo-paderborner-pilsener-svitle-z-b-415766',
            'https://novus.online/product/pivo-svitle-paderborner-pilsener-48-05l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-paderborner-500ml-nimechchina--04101120015106/',
            'https://fozzyshop.ua/ru/pivo-svetloe/76994-pivo-paderborner-zh-b-4101120015106.html'
        ])

    def beer_paderborner_export_05_l_jb_parser(self):
        ''' Парсер для Пиво Paderborner Export світле 5,5% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-paderborner-500ml-nimechchina--04101120004711/',
            'https://shop.silpo.ua/product/pyvo-paderborner-export-svitle-z-b-822648',
            'https://novus.online/product/pivo-svitle-paderborner-export-5505-l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-paderborner-500ml-nimechchina--04101120004711/'
        ])

    def beer_clausthaler_grapefruit_nonalco_05_l_jb_parser(self):
        ''' Парсер для Пиво Clausthaler Grapefruit безалкогольне 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-klaustkhaler-500ml-nimechchina--04053400208312/',
            'https://varus.ua/pivo-bezalkogolne-klauszaler-grejpfrut-05l-z-b',
            'https://metro.zakaz.ua/uk/products/pivo-klaustkhaler-500ml-nimechchina--04053400208312/'
        ])

    def beer_clausthaler_original_nonalco_05_l_jb_parser(self):
        ''' Парсер для Пиво Clausthaler Original безалкогольне 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-klaustkhaler-500ml--04053400001579/',
            'https://varus.ua/pivo-clausthaler-svetloe-filtrovanoe-bezalkogolnoe-0-0-5-l',
            'https://metro.zakaz.ua/uk/products/pivo-klaustkhaler-500ml--04053400001579/'
        ])

    def beer_clausthaler_lemon_nonalco_05_l_jb_parser(self):
        ''' Парсер для Пиво Clausthaler Lemon безалкогольне 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-klaustkhaler-500ml-nimechchina--04053400204918/',
            'https://varus.ua/pivo-bezalkogolne-klauszaler-limon-05l-z-b',
            'https://novus.online/product/pyvo-ba-clausthaler-lemon-0505l-zhb'
        ])

    def beer_forever_rock_n_roll_nefilter_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Forever Rock & Roll світле нефільтроване 7,5% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-forever-500ml-ukrayina--04820183001719/'
        ])

    def beer_forever_black_queen_nefilter_temne_05_l_jb_parser(self):
        ''' Парсер для Пиво Forever Black Queen темне нефільтроване 5,5% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-volinskii-brovar-ukrayina--04820183001481/'
        ])

    def beer_forever_kite_safari_nefilter_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Forever Kite Safari світле нефільтроване 7% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-500ml--04820183001504/'
        ])

    def beer_forever_crazy_nefilter_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Forever Crazy світле нефільтроване 6,5% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-forever-ukrayina--04820183001702/'
        ])

    def beer_hike_light_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Hike Light світле 3,5% 0,5л жб'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/pivo-05-l-hike-light-svitle-zb',
            'https://eko.zakaz.ua/uk/products/pivo-khaik-500ml--04820193035681/',
            'https://varus.ua/pivo-hike-light-svetloe-filtrovannoe-0-5-l',
            'https://shop.silpo.ua/product/pyvo-hike-light-svitle-z-b-909635',
            'https://metro.zakaz.ua/uk/products/pivo-khaik-500ml--04820193035681/'
        ])

    def beer_hike_zero_nonalco_05_l_jb_parser(self):
        ''' Парсер для Пиво Hike Zero безалкогольне 0,5л жб'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/pivo-bezalkogolne-05-l-hike-zero-zb',
            'https://eko.zakaz.ua/uk/products/pivo-khaik-500ml--04820193034349/',
            'https://varus.ua/pivo-hike-zero-svetloe-filtrovannoe-0-0-5-l',
            'https://shop.silpo.ua/product/pyvo-hike-zero-0-0-svitle-bezalkogolne-z-b-856073',
            'https://novus.online/product/pyvo-bezalkoholne-hike-zero-05-05l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-khaik-500ml--04820193034349/',
            'https://fozzyshop.ua/ru/pivo-bezalkogolnoe/88456-pivo-hike-zero-00-svetloe-bezalkogolnoe-zh-b-4820193034349.html'
        ])

    def beer_horn_disel_ice_pilsner_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Horn Disel Ice Pilsner світле 4,7% 0,568л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-volfes-engelmen-568ml-litva--04770301236809/'
        ])

    def beer_horn_disel_original_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Horn Disel Original 5,3% 0,568л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-volfes-engelmen-568ml-litva--04770301229160/'
        ])

    def beer_horn_disel_traditional_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Horn Disel Traditional світле 6% 0,568л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-volfes-engelmen-568ml-litva--04770301231439/'
        ])

    def beer_horn_disel_premium_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Horn Premium Diesel світле 5% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-khorn-disel--04770301234454/'
        ])

    def beer_krusovice_cerne_temne_05_l_jb_parser(self):
        ''' Парсер для Пиво Krusovice Cerne темне 3,8% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-krushovitse-500ml-ukrayina--04820046962140/',
            'https://varus.ua/pivo-0-5l-3-8-temne-filtrovane-pasterizovane-krusovice-cerne-zb',
            'https://shop.silpo.ua/product/pyvo-krusovice-cerne-temne-z-b-743431',
            'https://novus.online/product/pivo-temne-krusovice-cerne-38-05l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-krushovitse-500ml-ukrayina--04820046962140/',
            'https://shop.nashkraj.ua/kovel/product/263774-pivo-krusovice-0-5l-karlov-temn-3-8-zh-b',
            'https://fozzyshop.ua/ru/pivo-temnoe/50296-pivo-krusovice-cerne-temnoe-zh-b-4820046962140.html'
        ])

    def beer_lander_brau_micne_05_l_jb_parser(self):
        ''' Парсер для Пиво Lander Brau міцне 4,9% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-500ml--08714800032582/',
            'https://metro.zakaz.ua/uk/products/pivo-500ml--08714800032582/'
        ])

    def beer_lander_brau_svitle_nefilter_05_l_jb_parser(self):
        ''' Парсер для Пиво Lander Brau світле нефільтроване 4,7% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-500ml--08714800032674/',
            'https://varus.ua/pivo-lander-brau-premium-pilsner-svetloe-filtrovannoe-4-9-0-5-l',
            'https://metro.zakaz.ua/uk/products/pivo-500ml--08714800032674/'
        ])

    def beer_paderborner_pilger_svitle_nefilter_05_l_jb_parser(self):
        ''' Парсер для Пиво Paderborner Pilger світле нефільтроване пастеризоване 5% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-paderborner-500ml--04101120004735/',
            'https://shop.silpo.ua/product/pyvo-paderborner-pilger-svitle-nefiltrovane-z-b-737942',
            'https://novus.online/product/pivo-svitle-nefiltrovane-paderborner-pilger-50-05l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-paderborner-500ml--04101120004735/',
            'https://fozzyshop.ua/ru/pivo-pshenichnoe/52457-pivo-paderborner-pilger-cvetloe-nefiltrovannoe-zhb-4101120004735.html'
        ])

    def beer_platan_jedenactka_11_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Platan Jedenactka 11 світле 4,6% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-500ml--08594044362139/'
        ])

    def beer_praga_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Praga світле фільтроване 4,7% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-praga-500ml-chekhiia--08593875219490/',
            'https://novus.online/product/pivo-svitle-praga-premium-pils-47-05l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-praga-500ml-chekhiia--08593875219490/'
        ])

    def beer_saku_rock_svitle_0568_l_jb_parser(self):
        ''' Парсер для Пиво Saku Rock світле 5,3% 0,568л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-saku-568ml-estoniia--04740019121087/'
        ])

    def beer_sitnan_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Sitnan світле 5% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-sitnan-500ml--08588000080687/',
            'https://novus.online/product/pyvo-svitle-sitnan-12-alk-50-05l-zhbanka'
        ])

    def beer_vienas_premium_golden_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Vienas Premium Golden світле 5% 0,568л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-568ml-litva--04779030610423/'
        ])

    def beer_vienas_premium_traditional_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Vienas Premium Traditional світле 5,8% 0,568л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-568ml-litva--04779030610607/'
        ])

    def beer_volynski_browar_forever_sweet_wit_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Volynski Browar Forever Sweet Wit пшеничне світле нефільтроване 4,5% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-ukrayina--04820183001429/'
        ])

    def beer_zahringer_premium_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Zahringer Преміум світле 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-tsaringer-500ml-nimechchina--04054500131746/'
        ])

    def beer_zahringer_hefeweizen_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Zahringer Hefeweizen світле 0,5л ж'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-tsaringer-500ml-nimechchina--04054500131715/'
        ])

    def beer_jajkivske_nefilter_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Жашківське світле нефільтроване 4,5% 0,5л жб'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/pivo-05-l-zaskivske-svitle-zb',
            'https://eko.zakaz.ua/uk/products/ukrayina--04820252120259/',
            'https://shop.silpo.ua/product/pyvo-zhashkivske-svitle-nefiltrovane-z-b-909105',
            'https://novus.online/product/pyvo-svitle-nefiltrovane-zhashkivske-05-45-zb'
        ])

    def beer_obolon_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Оболонь світле 4,5% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-obolon-500ml-ukrayina--04820000190954/',
            'https://varus.ua/pivo-obolon-svitle-filtrovane-4-5-0-5-l',
            'https://shop.silpo.ua/product/pyvo-obolon-svitle-z-b-861',
            'https://novus.online/product/pivo-svitle-obolon-45-05l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-obolon-500ml-ukrayina--04820000190954/',
            'https://fozzyshop.ua/ru/pivo-svetloe/2918-pivo-obolon-svitle-svetloe-4820000190954.html'
        ])

    def beer_pubster_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Pubster світле 5% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-obolon-500ml--04820193034592/',
            'https://varus.ua/pivo-svitle-pabster-0-5-l-z-b',
            'https://shop.silpo.ua/product/pyvo-pubster-svitle-z-b-872791',
            'https://novus.online/product/pyvo-svitle-obolon-pubster-5-05l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-obolon-500ml--04820193034592/'
        ])

    def beer_chaika_chernomorskaya_05_l_jb_parser(self):
        ''' Парсер для Пиво ППБ Чайка Чорноморська 4,5% 0,5л жб'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-persha-privatna-brovarnia-500ml-ukrayina--04820046964533/',
            'https://shop.silpo.ua/product/pyvo-chaika-chornomorska-svitle-z-b-866178',
            'https://novus.online/product/pyvo-svitle-chayka-chornomorska-45-05l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-persha-privatna-brovarnia-500ml-ukrayina--04820046964533/',
            'https://fozzyshop.ua/ru/pivo-svetloe/88463-pivo-chajka-chornomorska-svitle-zh-b-4820046964533.html'
        ])

    def beer_ppb_zakarpatske_origin_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво ППБ Закарпатське Оригінальне світле 4,4% 0,5л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-radomishl-500ml-ukrayina--04820046963765/',
            'https://varus.ua/pivo-0-5l-4-4-svitle-originalne-zakarpatske-zb',
            'https://shop.silpo.ua/product/pyvo-persha-pryvatna-brovarnia-zakarpatske-oryginalne-svitle-z-b-818888',
            'https://novus.online/product/pivo-svitle-zakarpatske-originalne-44-05l-zb',
            'https://fozzyshop.ua/ru/pivo-svetloe/77006-pivo-persha-privatna-brovarnya-zakarpatskoe-originalnoe-svetloe-zh-b-4820046963765.html'
        ])

    def beer_ppb_bochkove_nefilter_05_l_jb_parser(self):
        ''' Парсер для Пиво ППБ Бочкове Нефільтроване з/б 4,8% 0,5л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-persha-privatna-brovarnia-500ml-ukrayina--04820046963222/',
            'https://shop.silpo.ua/product/pyvo-persha-pryvatna-brovarnia-bochkove-svitle-nefiltrovane-z-b-783830',
            'https://auchan.ua/ua/pivo-persha-privatna-brovarnja-bochkovoe-svetloe-nefil-trovannoe-4-8-0-5-l-1031718/',
            'https://novus.online/product/pivo-svitle-ppb-bockove-specialne-nefiltrovane-48-05l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-persha-privatna-brovarnia-500ml-ukrayina--04820046963222/',
            'https://shop.nashkraj.ua/kovel/product/317722-pivo-privatbrovarnya-0-5l-bochkove-nef-zh-b'
        ])

    def beer_ppb_nefilter_svitle_nonalco_05_l_jb_parser(self):
        ''' Парсер для Пиво ППБ Нефільтроване світле безалкогольне 0,5л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-persha-privatna-brovarnia-500ml-ukrayina--04820046963369/',
            'https://varus.ua/pivo-specialne-0-5l-bezalkogolne-svitle-nefiltrovane-pasterizovane-persha-privatna-brovarnya-zb',
            'https://shop.silpo.ua/product/pyvo-persha-pryvatna-brovarnia-svitle-nefiltrovane-bezalkogolne-z-b-797104',
            'https://novus.online/product/pyvo-bezalkoholne-svitle-nefiltrovane-ppb-zhb-05l',
            'https://metro.zakaz.ua/uk/products/pivo-persha-privatna-brovarnia-500ml--04820046964304/',
            'https://fozzyshop.ua/ru/pivo-bezalkogolnoe/64332-pivo-persha-privatna-brovarnya-svetloe-n-f-b-alk-zh-b-4820046963369.html'
        ])

    def beer_ppb_limon_lime_nonalco_nefilter_05_l_jb_parser(self):
        ''' Парсер для Пиво ППБ Лимон-Лайм безалкогольне нефільтроване 0,5л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-persha-privatna-brovarnia-500ml--04820046964786/',
            'https://varus.ua/pivo-persha-privatna-brovarnya-limon-lajm-bezalkogolne-nefiltrovane-bochkove-05-l',
            'https://novus.online/product/pyvo-bezalkoholne-zi-smakom-lymona-laym-ppb-zhb-05l'
        ])

    def beer_chaika_dniprovskaya_05_l_jb_parser(self):
        ''' Парсер для Пиво Чайка Дніпровська світле фільтроване 4,8% 0,5л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-chaika-500ml-ukrayina--04820046964014/',
            'https://shop.silpo.ua/product/pyvo-chaika-dniprovska-svitle-z-b-836169',
            'https://novus.online/product/pivo-svitle-cajka-dniprovska-48-05l-zb',
            'https://metro.zakaz.ua/uk/products/pivo-chaika-500ml-ukrayina--04820046964014/',
            'https://shop.nashkraj.ua/kovel/product/398516-pivo-chayka-0-5l-dniprovska-zh-b',
            'https://fozzyshop.ua/ru/pivo-svetloe/88459-pivo-chajka-dniprovska-svetloe-zh-b-4820046964014.html'
        ])

    def beer_brok_export_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Brok Export світле 5,2% 0,5л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-brok-500ml-polshcha--05900535004007/',
            'https://novus.online/product/pivo-svitle-brok-export-52-05l-zb'
        ])

    def beer_carling_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Carling світле фільроване з/б 4% 0.5 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/pivo-05-l-carling-svitle-zb',
            'https://varus.ua/pivo-0-5l-4-0-svitle-carling-zb',
            'https://shop.silpo.ua/product/pyvo-sarlihg-z-b-498824',
            'https://novus.online/product/pivo-svitle-carling-40-05l-zb'
        ])

    def beer_keten_brug_blanche_elegant_05_l_jb_parser(self):
        ''' Парсер для Пиво Keten Brug Blanche Elegant 4.8% 0.5 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/pivo-05-l-keten-brug-blanche-elegant-zb',
            'https://varus.ua/pivo-keten-brug-blanche-elegant-4-8-specialne-pasterizovane-0-5-l',
            'https://shop.silpo.ua/product/pyvo-keten-brug-blanche-elegant-z-b-890782',
            'https://novus.online/product/pyvo-svitle-keten-brug-blanche-48-05l-zb'
        ])

    def beer_budweiser_nonalco_05_l_jb_parser(self):
        ''' Парсер для Пиво Budweiser безалкогольне 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-bezalkogolne-budvajzer-05l-z-b',
            'https://shop.silpo.ua/product/pyvo-budweiser-budvar-nealko-svitle-b-alk-z-b-921766'
        ])

    def beer_FeldschlosschenWheatBeer_svitle_nefilter_05_l_jb_parser(self):
        ''' Парсер для Пиво Feldschlosschen Wheat Beer світле нефільтроване 5% 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-feldschlosschen-wheat-beer-svetloe-nefiltrovannoe-5-0-5-l'
        ])

    def beer_teteriv_hmilna_vishnya_napivtemne_05_l_jb_parser(self):
        ''' Парсер для Пиво Тетерів Хмільна Вишня напівтемне фільтроване з/б 8% 0.5 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-radomishl-500ml--04820046963604/',
            'https://varus.ua/pivo-specialne-0-5l-8-hmilna-vishnya-teteriv-zb',
            'https://shop.silpo.ua/product/pyvo-teteriv-khmilna-vyshnia-napivtemne-z-b-803780',
            'https://auchan.ua/ua/pivo-persha-privatna-brovarnja-teterev-hmel-naja-vishnja-polutemnoe-fil-trovannoe-8-0-5-l-1031708/',
            'https://novus.online/product/pivo-specialne-napivtemne-teteriv-hmilna-visna-8-05l-zb',
            'https://shop.nashkraj.ua/kovel/product/333806-pivo-privatnabrov-0-5l-teteriv-vishnya-zh-b'
        ])

    def beer_grotwerg_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Grotwerg світле пастеризоване фільтроване безалкогольне 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-grotwerg-bezalkogolne-05l'
        ])

    def beer_holland_import_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Holland Import світле фільтроване 4.8% 0.5 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-500ml--08714800024471/',
            'https://varus.ua/pivo-holland-import-svitle-filtrovane-48-05l',
            'https://novus.online/product/pivo-svitle-holland-import-48-033l-zb'
        ])

    def beer_golden_castle_export_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Golden Castle Export світле 4.8% 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-svitle-golden-kastle-eksport-05l-z-b',
            'https://shop.silpo.ua/product/pyvo-golden-castle-export-svitle-z-b-879652',
            'https://novus.online/product/pyvo-svitle-golden-castle-48-05l-zb'
        ])

    def beer_5_0_original_craft_beer_nefilter_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво 5.0 Original Craft Beer сітле нефільтроване 4.1% 0.5 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/pivo-500ml-nimechchina--04014086096518/',
            'https://varus.ua/pivo-originalne-kraft-bir-0-5l-z-b'
        ])

    def beer_guinness_draught_temne_044_l_jb_parser(self):
        ''' Парсер для Пиво Guinness Draught темне фільтроване 4.1% 0.44 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-0-44l-4-2-temne-pasterizovane-draught-guinness-zb',
            'https://shop.silpo.ua/product/pyvo-guinness-draught-temne-z-b-104560',
            'https://auchan.ua/ua/pivo-guinness-draught-temnoe-fil-trovannoe-4-1-0-44-l-1031563/',
            'https://metro.zakaz.ua/uk/products/pivo-ginness-440ml-irlandiia--05000213101872/',
            'https://fozzyshop.ua/ru/pivo-temnoe/2739-pivo-guinness-draught-temnoe-5000213014905.html'
        ])

    def beer_grimbergenDoubleAmbree_napivtemne_05_l_jb_parser(self):
        ''' Парсер для Пиво Grimbergen Double Ambree напівтемне фільтроване 6.5% 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-specialne-0-5l-6-5-temne-pasterizovane-double-ambree-grimbergen-zb',
            'https://shop.silpo.ua/product/pyvo-grimbergen-double-ambree-temne-z-b-797415',
            'https://metro.zakaz.ua/uk/products/pivo-grimbergen-500ml-polshcha--03080216049076/',
            'https://fozzyshop.ua/ru/pivo-temnoe/66255-pivo-grimbergen-double-ambree-temnoe-zh-b-3080216049076.html'
        ])

    def beer_warsteinerPremiumVerum_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Warsteiner Premium Verum світле фільтроване 4.8% 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-0-5l-4-8-sv-warsteiner-prem-verum',
            'https://shop.silpo.ua/product/pyvo-warsteiner-premium-svitle-z-b-508486'
        ])

    def beer_dab_temne_05_l_jb_parser(self):
        ''' Парсер для Пиво DAB темне фільтроване 4.9% 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-temne-dab-0-5l-z-b',
            'https://shop.silpo.ua/product/pyvo-dab-dark-temne-z-b-921777',
            'https://metro.zakaz.ua/uk/products/pivo-dab-500ml-nimechchina--04053400277936/'
        ])

    def beer_grimbergenBlanche_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво спеціальне Grimbergen Blanche світле пастеризоване 6% 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-grimbergen-blansh-05l-z-b',
            'https://shop.silpo.ua/product/pyvo-grimbergen-blanche-svitle-z-b-876014',
            'https://metro.zakaz.ua/uk/products/pivo-grimbergen-500ml--05901594001266/',
            'https://fozzyshop.ua/ru/pivo-pshenichnoe/88987-pivo-grimbergen-blanche-svetloe-zh-b-5901594001266.html'
        ])

    def beer_klosterkellerWeissbierChina_nefilter_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Klosterkeller Weissbier China світле нефільтроване 5.4% 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-klosterkeller-weissbier-china-svitle-nefiltrovane-54-05-l'
        ])

    def beer_karpackiePils_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Karpackie Pils світле фільтроване 4% 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-karpackie-pils-svitle-4-05l'
        ])

    def beer_5_0_OriginalPills_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво 5,0 Original Pills світле фільтроване 5% 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-5-0-original-pills-svetloe-filtrovannoe-5-0-5-l'
        ])

    def beer_5_0_Original_lager_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво 5,0 Original Lager світле фільтроване 5.4% 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-5-0-original-lager-svetloe-filtrovannoe-5-4-0-5-l'
        ])

    def beer_5_0_Original_weiss_beer_nefilter_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво 5,0 Original Weiss Beer світле нефільтроване 5% 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-5-0-original-weiss-beer-svetloe-nefiltrovannoe-5-0-5-l'
        ])

    def beer_Fahnen_Brau_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Fahnen Brau світле фільтроване 4.7% 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-0-5l-4-7-svitle-fahnen-brau-z-b',
            'https://novus.online/product/pivo-svitle-fahnen-brau-47-05l-zb'
        ])

    def beer_Gosser_Light_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Gosser Light світле фільтроване 5.2% 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/gesser-pivo-0-5l-z-b',
            'https://shop.silpo.ua/product/pyvo-gosser-svitle-z-b-46523'
        ])

    def beer_Hollandia_Import_svitle_033_l_jb_parser(self):
        ''' Парсер для Пиво Hollandia Import світле фільтроване 4.8% 0.33 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-gollandiya-import-0-33l-zb'
        ])

    def beer_Holsten_Pilsner_048_l_jb_parser(self):
        ''' Парсер для Пиво Holsten Pilsener 4.7% 0.48 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-holsten-pilsener-4-7-svitle-pasterizovane-0-48-l',
            'https://shop.silpo.ua/product/pyvo-holsten-pilsener-svitle-z-b-909343',
            'https://metro.zakaz.ua/uk/products/ukrayina--04820250941412/',
            'https://fozzyshop.ua/ru/pivo-svetloe/100280-pivo-holsten-pilsener-svetloe-zh-b-250014933959.html'
        ])

    def beer_Obolon_Premium_Extra_Brew_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Оболонь Premium Extra Brew світле фільтроване з/б 4.6% 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-0-5l-4-6-svitle-pasterizovane-premium-extra-brew-obolon-zb',
            'https://shop.silpo.ua/product/pyvo-obolon-premium-extra-brew-svitle-z-b-805168'
        ])

    def beer_Lvivske_svitle_48_l_jb_parser(self):
        ''' Парсер для Пиво Львівське світле 4,3% 0,48 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-lvivske-svitle-43-048-l',
            'https://shop.silpo.ua/product/pyvo-lvivske-svitle-z-b-857477',
            'https://metro.zakaz.ua/uk/products/pivo-lvivske-500ml-ukrayina--04820250942303/',
            'https://shop.nashkraj.ua/kovel/product/435152-pivo-lvivske-0-5l-svitle-4-5-zh-b'
        ])

    def beer_Carlsberg_Premium_Pilsner_svitle_05_l_jb_parser(self):
        ''' Парсер для Пиво Carlsberg Premium Pilsner світле фільтроване з/б 5% 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-0-5l-5-svitle-pasterizovane-liverpool-fc-champions-carlsberg-zb',
            'https://shop.silpo.ua/product/pyvo-carlsberg-svitle-z-b-260560'
        ])

    def beer_Carlsberg_Pilsner_05_l_jb_parser(self):
        ''' Парсер для Пиво Carlsberg Pilsner 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/pivo-carlsberg-bezalkogolne-05-l',
            'https://shop.silpo.ua/product/pyvo-carlsberg-pilsner-svitle-bezalkogolne-z-b-908441',
            'https://metro.zakaz.ua/uk/products/pivo-500ml--04820250941962/',
            'https://fozzyshop.ua/ru/pivo-bezalkogolnoe/100275-pivo-carlsberg-pilsner-svetloe-bezalkogolnoe-zh-b-250014915207.html'
        ])

    def banana_parser(self):
        ''' Парсер для Банан, кг'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/banan-1-gat',
            'https://eko.zakaz.ua/uk/products/frukt-banan--ekomarket00000000640016/',
            'https://varus.ua/banan-vag',
            'https://shop.silpo.ua/product/banan-32485',
            'https://novus.online/product/banan-vag',
            'https://metro.zakaz.ua/uk/products/frukt-banan--metro28896500000000/',
            'https://shop.nashkraj.ua/kovel/product/12811-banan-vag',
            'https://fozzyshop.ua/ru/frukty-i-yagody/11745-banan-2732485.html'
        ])

    def orange_parser(self):
        ''' Парсер для Апельсин, кг'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/apelsin-vag-1-gat',
            'https://eko.zakaz.ua/uk/products/frukt-tsitrus--ekomarket00000000640018/',
            'https://varus.ua/apelsin-vag',
            'https://shop.silpo.ua/product/apelsyn-32546',
            'https://novus.online/product/apelsin-velikij-vag',
            'https://metro.zakaz.ua/uk/products/frukt-tsitrus--metro28251600000000/',
            'https://shop.nashkraj.ua/kovel/product/85-apelsini-elitniy-vag',
            'https://fozzyshop.ua/ru/frukty-i-yagody/15494-apelsin-2732546.html'
        ])

    def kiwi_parser(self):
        ''' Парсер для Киви, кг'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/kivi-u-kosiku-2-gat',
            'https://eko.zakaz.ua/uk/products/frukt-kivi--ekomarket00000026000121/',
            'https://varus.ua/kivi-vag',
            'https://shop.silpo.ua/product/kivi-vagovyi-134544',
            'https://metro.zakaz.ua/uk/products/frukt-kivi--metro24273421010170/',
            'https://shop.nashkraj.ua/kovel/product/268330-kivi-koshik-sht',
            'https://fozzyshop.ua/ru/frukty-i-yagody/11769-kivi-2701162.html'
        ])

    def coconut_parser(self):
        ''' Парсер для Кокос, кг'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/kokos',
            'https://varus.ua/kokos-sht',
            'https://shop.silpo.ua/product/kokos-32555',
            'https://metro.zakaz.ua/uk/products/frukt-kokos-400g--metro23280040000090/',
            'https://shop.nashkraj.ua/kovel/product/12766-kokos-sht',
            'https://fozzyshop.ua/ru/frukty-i-yagody/11773-kokos-0250000398267.html'
        ])

    def grapefruit_parser(self):
        ''' Парсер для Грейпфрут, кг'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/grejpfrut-1gat',
            'https://eko.zakaz.ua/uk/products/frukt-tsitrus--ekomarket00000000640019/',
            'https://varus.ua/grejpfrut-pav-vesovoj',
            'https://shop.silpo.ua/product/greipfrut-par-757483',
            'https://novus.online/product/grejpfrut-rozevij-vag',
            'https://metro.zakaz.ua/uk/products/frukt-tsitrus--metro28251800000000/',
            'https://shop.nashkraj.ua/kovel/product/91461-greypfrut-vag',
            'https://fozzyshop.ua/ru/frukty-i-yagody/11757-grejpfrut-2732549.html'
        ])

    def pomegranate_parser(self):
        ''' Парсер для Гранат, кг'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/granat-1gat',
            'https://eko.zakaz.ua/uk/products/frukt-granat--ekomarket00000000641224/',
            'https://varus.ua/granat-peru-sht',
            'https://shop.silpo.ua/product/granat-24',
            'https://metro.zakaz.ua/uk/products/frukt-granat-turechchina--metro28551300000000/',
            'https://fozzyshop.ua/ru/frukty-i-yagody/11725-granat-2700024.html'
        ])

    def mango_parser(self):
        ''' Парсер для Манго, кг'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/mango-vag-1-gat',
            'https://varus.ua/mango-vag',
            'https://shop.silpo.ua/product/mango-49207',
            'https://novus.online/product/mango-dribnij-st-kalibr-a',
            'https://metro.zakaz.ua/uk/products/frukt-mango-300g--metro23280060000070/',
            'https://shop.nashkraj.ua/kovel/product/20996-mango-sht',
            'https://fozzyshop.ua/ru/frukty-i-yagody/11780-mango-0250000443066.html'
        ])

    def tomato_parser(self):
        ''' Парсер для Помидор, кг'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/tomati-teplicni-1-gatunok',
            'https://eko.zakaz.ua/uk/products/ovochi-pomidor--ekomarket00000000666302/',
            'https://varus.ua/pomidor-krasnye-vesovoy',
            'https://metro.zakaz.ua/uk/products/ovochi-pomidor--metro28594900000000/',
            'https://shop.nashkraj.ua/kovel/product/220502-pomidor-gilka-vag',
            'https://fozzyshop.ua/ru/ovoshhi/11543-pomidor-2732589.html'
        ])

    def cucumber_parser(self):
        ''' Парсер для Огурец, кг'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/ogirki-1-gat',
            'https://eko.zakaz.ua/uk/products/ovochi-ogirki-ukrayina--ekomarket00000000677120/',
            'https://varus.ua/ogirok-teplichniy-1-gatunok-vag',
            'https://shop.silpo.ua/product/ogirok-ekstra-142342',
            'https://novus.online/product/ogirok-vag',
            'https://metro.zakaz.ua/uk/products/ovochi-ogirki--metro28700400000000/',
            'https://shop.nashkraj.ua/kovel/product/260827-ogirki-vag',
            'https://fozzyshop.ua/ru/ovoshhi/11535-ogurec-ekstra-2707093.html'
        ])

    def kabachki_parser(self):
        ''' Парсер для Кабачки, кг'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/kabacki-1-gat',
            'https://eko.zakaz.ua/uk/products/ovochi-kabachki--ekomarket00000000640011/',
            'https://varus.ua/kabachki-1-gatunok-importni-vag',
            'https://shop.silpo.ua/product/kabachok-51600',
            'https://novus.online/product/kabacki-vag',
            'https://metro.zakaz.ua/uk/products/ovochi-kabachki--metro28267900000000/',
            'https://shop.nashkraj.ua/kovel/product/13272-kabachok-vag',
            'https://fozzyshop.ua/ru/ovoshhi/11497-kabachok-2734196.html'
        ])

    def red_bolg_papper_parser(self):
        ''' Парсер для Красный болгарский перец, кг'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/perec-solodkij-cervonij-1-gat',
            'https://eko.zakaz.ua/uk/products/paprika-perets--ekomarket00000000640043/',
            'https://shop.silpo.ua/product/perets-chervonyi-32887',
            'https://novus.online/product/perec-cervonij-import-vag',
            'https://metro.zakaz.ua/uk/products/ovochi-perets--metro28330300000000/',
            'https://shop.nashkraj.ua/kovel/product/141302-perets-chervoniy-vag',
            'https://fozzyshop.ua/ru/ovoshhi/11539-perec-krasnyj-2732887.html'
        ])

    def yellow_bolg_papper_parser(self):
        ''' Парсер для Желтый болгарский перец, кг'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/perec-solodkij-zovtij-1-gat',
            'https://shop.silpo.ua/product/perets-zhovtyi-32885',
            'https://novus.online/product/perec-zovtij-import-vag',
            'https://metro.zakaz.ua/uk/products/ovochi-perets--metro28252900000000/',
            'https://shop.nashkraj.ua/kovel/product/39168-perets-zhovtiy-vag',
            'https://fozzyshop.ua/ru/ovoshhi/11538-perec-zheltyj-2732885.html'
        ])

    def asparagus_parser(self):
        ''' Парсер для Спаржа'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/sparza-zelena-250g',
            'https://varus.ua/sparzha-vag',
            'https://shop.silpo.ua/product/sparzha-zelena-sparzha-volyni-907134',
            'https://novus.online/product/sparzha-zelena-250h',
            'https://metro.zakaz.ua/uk/products/ovochi-sparzha-bez-tm-330g-ukrayina--04820235480042/',
            'https://fozzyshop.ua/ru/ovoshhi/78181-sparzha-zelenaya-otechestvennaya-0250008047099.html'
        ])

    def brokoli_parser(self):
        ''' Парсер для Броколі'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kapusta-brokoli-import-448399',
            'https://novus.online/product/kapusta-brokkoli-vag',
            'https://shop.nashkraj.ua/kovel/product/42671-kapusta-brokoli-vag',
            'https://fozzyshop.ua/ru/ovoshhi/47051-kapusta-brokkoli-2733955.html'
        ])

    def captain_morgan_spiced_gold_1L_parser(self):
        ''' Парсер для Captain Morgan Spiced Gold 1 литр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/rom-kapitan-morgan-1000ml-velikobritaniia--05000299223055/',
            'https://varus.ua/rom-oridzhinal-spaysed-gold-kepten-morgan-1l-35-1',
            'https://shop.silpo.ua/product/napii-na-osnovi-romu-captain-morgan-spiced-gold-3920',
            'https://metro.zakaz.ua/uk/products/rom-kapitan-morgan-1000ml-velikobritaniia--05000299223055/',
            'https://fozzyshop.ua/ru/rom/2643-rom-saritan-morgan-spiced-gold-0087000006867.html'
        ])

    def captain_morgan_spiced_gold_05L_parser(self):
        ''' Парсер для Captain Morgan Spiced Gold 0.5 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-05l-captain-morgan-original-spiced-gold-alkogolnij-na-osnovi-romu-35',
            'https://eko.zakaz.ua/uk/products/rom-kapitan-morgan-500ml-velikobritaniia--05000281025360/',
            'https://varus.ua/rom-oridzhinal-spaysed-gold-kepten-morgan-0-5l-35-1',
            'https://shop.silpo.ua/product/napii-na-osnovi-romu-captain-morgan-spiced-gold-437392',
            'https://metro.zakaz.ua/uk/products/rom-kapitan-morgan-500ml-velikobritaniia--05000281025360/',
            'https://shop.nashkraj.ua/kovel/product/151020-napiy-alko-captain-morgan-0-5l-35',
            'https://fozzyshop.ua/ru/rom/2623-rom-captain-morgan-spiced-gold-5000281025360.html'
        ])

    def bells_original_07L_parser(self):
        ''' Парсер для Bells original 0.7 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/nabir-viski-07l-bells-original-40-stakan',
            'https://eko.zakaz.ua/uk/products/viski-bells-700ml-velikobritaniia--05000387905634/',
            'https://varus.ua/viski-bell-s-original-kupazhovaniy-40-0-7-l',
            'https://shop.silpo.ua/product/viski-bell-s-original-400773',
            'https://novus.online/product/viski-bells-40-07l',
            'https://metro.zakaz.ua/uk/products/viski-bells-700ml-velikobritaniia--05000387905474/',
            'https://shop.nashkraj.ua/kovel/product/201687-viski-bells-0-7l-original-40',
            'https://fozzyshop.ua/ru/viski/1789-viski-bells-original-5000387905474.html'
        ])

    def bells_original_1L_parser(self):
        ''' Парсер для Bells original 1 литр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/viski-bells-1000ml-velikobritaniia--05000387905504/',
            'https://varus.ua/viski-bell-s-original-kupazhovaniy-40-1-l',
            'https://shop.silpo.ua/product/viski-bell-s-original-329999',
            'https://novus.online/product/viski-bells-original-40-1l',
            'https://metro.zakaz.ua/uk/products/viski-bells-1000ml-velikobritaniia--05000387905504/',
            'https://fozzyshop.ua/ru/viski/1788-viski-bells-original-5000387905504.html'
        ])

    def bells_spiced_07L_parser(self):
        ''' Парсер для Bells spiced 0.7 литр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/viski-bells-700ml-velikobritaniia--05000387906907/',
            'https://varus.ua/viski-bell-s-spiced-kupazhovaniy-35-0-7-l',
            'https://shop.silpo.ua/product/viski-bell-s-spiced-676597',
            'https://novus.online/product/napij-35-07-alkogolnij-bells-spiced',
            'https://metro.zakaz.ua/uk/products/viski-bells-700ml-velikobritaniia--05000387906907/',
            'https://fozzyshop.ua/ru/viski/37653-viski-bells-spiced-5000387906907.html'
        ])

    def martini_asti_bile_075_L_parser(self):
        ''' Парсер для Martini Asti White 0.75 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/vino-075l-igriste-martini-asti-docg-bile-solodke',
            'https://varus.ua/vino-igriste-martini-asti-bile-solodke-0-75-l',
            'https://shop.silpo.ua/product/vyno-igryste-martini-asti-7-5-14013',
            'https://auchan.ua/ua/vino-igristoe-martini-asti-beloe-sladkoe-7-5-0-75-l-1042149/',
            'https://novus.online/product/vino-igriste-martini-asti-dolce-docg-75-075l',
            'https://metro.zakaz.ua/uk/products/vino-igriste-martini-750ml-italiia--08000570435402/',
            'https://fozzyshop.ua/ru/vina-igristye/1448-vino-igristoe-martini-asti-beloe-polusladkoe-8000570435402.html'
        ])

    def jameson_07_L_parser(self):
        ''' Парсер для Jameson 0.7 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/viski-07-l-jameson-40-ob-skbut',
            'https://varus.ua/viski-jameson-irish-whiskey-kupazhovaniy-40-0-7-l',
            'https://shop.silpo.ua/product/viski-jameson-58113',
            'https://auchan.ua/ua/viski-jameson-40-0-7-l-1044212/',
            'https://novus.online/product/viski-jameson-40-07l',
            'https://metro.zakaz.ua/uk/products/viski-dzheimson-700ml-irlandiia--05011007003005/',
            'https://shop.nashkraj.ua/kovel/product/77970-viski-jameson-0-7l-6-rokiv-40',
            'https://fozzyshop.ua/ru/viski/1822-viski-jameson-5011007003005.html'
        ])

    def jameson_05_L_parser(self):
        ''' Парсер для Jameson 0.5 литр'''
        return self.prices_parsing([
            'https://varus.ua/viski-jameson-irish-whiskey-kupazhovaniy-40-0-5-l',
            'https://shop.silpo.ua/product/viski-jameson-501438',
            'https://auchan.ua/ua/viski-jameson-40-0-5-l-1044218/',
            'https://novus.online/product/viski-jameson-05l',
            'https://metro.zakaz.ua/uk/products/viski-dzheimson-500ml-irlandiia--05011007015534/',
            'https://shop.nashkraj.ua/kovel/product/168713-viski-jameson-0-5l-40'
        ])

    def jw_red_label_05_L_parser(self):
        ''' Парсер для JW Red Label 0.5 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/viski-05l-johnnie-walker-red-label-40',
            'https://eko.zakaz.ua/uk/products/viski-dzhoni-uoker-500ml-velikobritaniia--05000267014401/',
            'https://varus.ua/viski-johnnie-walker-red-label-kupazhovaniy-4-roki-vitrimki-40-0-5-l',
            'https://shop.silpo.ua/product/viski-johnnie-walker-red-label-10026',
            'https://auchan.ua/ua/viski-johnnie-walker-red-label-0-5-l-1175194/',
            'https://novus.online/product/viski-johnnie-walker-red-label-40-05l',
            'https://metro.zakaz.ua/uk/products/viski-dzhoni-uoker-500ml-velikobritaniia--05000267014401/',
            'https://shop.nashkraj.ua/kovel/product/11791-viski-johnnie-walker-0-5l-red-lable-40',
            'https://fozzyshop.ua/ru/viski/1804-viski-johnnie-walker-red-label-5000267014401.html'
        ])

    def ballantines_finest_07_L_parser(self):
        ''' Парсер для Ballantines Finest 0.7 литр'''
        return self.prices_parsing([
            'https://varus.ua/viski-ballantines-finest-kupazhovaniy-40-0-7-l',
            'https://shop.silpo.ua/product/viski-ballantine-s-finest-40-605400',
            'https://auchan.ua/ua/viski-ballantine-s-finest-40-0-7-l-1044248/',
            'https://novus.online/product/viski-40-07l-sotlandskij-kupazovanij-ballantines-finest',
            'https://metro.zakaz.ua/uk/products/viski-balantains-700ml-velikobritaniia--05010106113127/',
            'https://fozzyshop.ua/ru/viski/23665-viski-ballantine-s-finest-ballantajns-fajnest-40-5010106113127.html'
        ])

    def jack_daniels_07_L_parser(self):
        ''' Парсер для Jack Daniels 0.7 литр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/viski-dzhek-deniels-700ml-ssha--05099873089798/',
            'https://varus.ua/viski-jack-daniel-s-old-no-7-tennessi-40-0-7-l',
            'https://novus.online/product/viski-jack-daniels-40-07l',
            'https://metro.zakaz.ua/uk/products/viski-dzhek-deniels-700ml-ssha--05099873089798/',
            'https://shop.nashkraj.ua/kovel/product/130552-viski-jackdaniel-s-0-7l-40',
            'https://fozzyshop.ua/ru/viski/1714-viski-jack-daniels-5099873089798.html'
        ])

    def jack_daniels_1_L_parser(self):
        ''' Парсер для Jack Daniels 1 литр'''
        return self.prices_parsing([
            'https://varus.ua/viski-jack-daniel-s-old-no-7-tennessi-40-1-l',
            'https://shop.silpo.ua/product/viski-jack-daniels-4103',
            'https://novus.online/product/viski-jack-daniels-40-1l',
            'https://metro.zakaz.ua/uk/products/viski-dzhek-deniels-1000ml-ssha--05099873045367/',
            'https://fozzyshop.ua/ru/viski/1801-viski-jack-daniels-5099873045367.html'
        ])

    def jim_beam_white_07L_parser(self):
        ''' Парсер для Jim Beam White 0.7 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/viski-07-l-jim-beam-white-40-ob-skbut',
            'https://varus.ua/burbon-jim-beam-white-4-roki-vitrimki-40-1-l-1',
            'https://shop.silpo.ua/product/viski-jim-beam-4101',
            'https://auchan.ua/ua/viski-jim-beam-white-4-goda-vyderzhki-40-0-7-l-1167255/',
            'https://novus.online/product/viski-jim-beam-white-bourbon-40-4r07l',
            'https://metro.zakaz.ua/uk/products/viski-dzhim-bim-700ml-ssha--05010196091008/',
            'https://fozzyshop.ua/ru/viski/49834-viski-jim-beam-white-5010196091008.html'
        ])

    def borjomi_05L_parser(self):
        ''' Парсер для Borjomi 0.5 литр'''
        return self.prices_parsing([
            'https://varus.ua/voda-mineralna-borzhomi-0-5l'
        ])

    def morshinska_negaz_15L_parser(self):
        ''' Парсер для Моршинська негазована 1.5 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/voda-15l-morsinska-mineralna-negazovana',
            'https://eko.zakaz.ua/uk/products/voda-morshinska-1500ml--04820017000024/',
            'https://varus.ua/voda-negazovana-morshinska-1-5l-ukraina',
            'https://shop.silpo.ua/product/voda-mineralna-morshynska-negazovana-16649',
            'https://auchan.ua/ua/voda-morshins-ka-negazirovannaja-1-5-l-244183/',
            'https://novus.online/product/voda-negazovana-morsinska-15l',
            'https://shop.nashkraj.ua/kovel/product/5971-min-voda-morshinska-1-5l-n-g-pet',
            'https://fozzyshop.ua/ru/voda-mineralnaya-negazirovannaya/12796-voda-mineralnaya-morshinska-n-gaz-4820017000024.html'
        ])

    def morshinska_lowgaz_15L_parser(self):
        ''' Парсер для Моршинська слабогазована 1.5 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/voda-15l-morsinska-mineralna-slabogazovana',
            'https://eko.zakaz.ua/uk/products/voda-morshinska-1500ml--04820017000253/',
            'https://varus.ua/voda-slabogazovana-morshinska-1-5l-ukraina',
            'https://shop.silpo.ua/product/voda-mineralna-morshynska-slabogazovana-39465',
            'https://auchan.ua/ua/voda-morshins-ka-slabogazirovannaja-1-5-l-244182/',
            'https://novus.online/product/voda-slabogazovana-morsinska-15l',
            'https://shop.nashkraj.ua/kovel/product/5973-min-voda-morshinska-1-5l-sl-g-pet',
            'https://fozzyshop.ua/ru/voda-mineralnaya-gazirovannaya/12802-voda-mineralnaya-morshinska-sl-gaz-4820017000253.html'
        ])

    def morshinska_highgaz_15L_parser(self):
        ''' Парсер для Моршинська сильногазована 1.5 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/voda-15l-morsinska-mineralna-silnogazovana',
            'https://eko.zakaz.ua/uk/products/voda-morshinska-1500ml--04820017000055/',
            'https://varus.ua/voda-gazovana-morshinska-1-5l-ukraina',
            'https://shop.silpo.ua/product/voda-mineralna-morshynska-sylnogazovana-36629',
            'https://auchan.ua/ua/voda-sil-nogazirovannaja-morshins-ka-1-5-l-236162/',
            'https://novus.online/product/voda-gazovana-morsinska-15l',
            'https://shop.nashkraj.ua/kovel/product/5972-min-voda-morshinska-1-5l-s-g-pet',
            'https://fozzyshop.ua/ru/voda-mineralnaya-gazirovannaya/12800-voda-mineralnaya-morshinska-s-gaz-4820017000055.html'
        ])

    def nash_sik_apple_grape_02L_parser(self):
        ''' Парсер для Наш Сік яблуко-виноград 0.2 литр'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/nektar-nash-sik-iabluchno-vynogradnyi-osvitlenyi-819228',
            'https://auchan.ua/ua/nektar-jabloko-vinograd-nash-sik-t-p-200ml-689606/',
            'https://novus.online/product/sik-nas-sik-vinogradabluko-osvitlenij-02l',
            'https://fozzyshop.ua/ru/soki-i-nektary/77031-nektar-nash-sik-yablochno-vinogradnyj-osvetlennyj-4820192262750.html'
        ])

    def nash_sik_apple_carrot_02L_parser(self):
        ''' Парсер для Наш Сік яблуко-морква 0.2 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/sik-200-ml-nas-sik-okzdh-ablucno-morkvanij',
            'https://varus.ua/sok-nash-sok-yabloko-i-morkov-0-2-l',
            'https://auchan.ua/ua/sok-morkovno-jablochnyj-s-mjakot-ju-nash-sik-t-p-0-2l-692707/',
            'https://novus.online/product/sik-nas-sik-morkvaabluko-z-makittu-02l',
            'https://fozzyshop.ua/ru/soki-i-nektary/3936-sok-nash-sik-yablochno-morkovnyj-s-myakotyu-02l-4820016250628.html'
        ])

    def nash_sik_orange_02L_parser(self):
        ''' Парсер для Наш Сік апельсин 0.2 литр'''
        return self.prices_parsing([
            'https://varus.ua/nektar-apelsinovij-okzdh-nash-sik-02l',
            'https://novus.online/product/nektar-nash-sik-apelsyn-02-l-tp',
            'https://fozzyshop.ua/ru/soki-i-nektary/103135-nektar-nash-sik-apelsinovyj-0250015069428.html'
        ])

    def nash_sik_multifrukt_02L_parser(self):
        ''' Парсер для Наш Сік мультіфрукт 0.2 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/nektar-02-l-okzdh-nas-sik-multifruktovij-tropicna-seria',
            'https://varus.ua/nektar-nash-sok-multifrukt-0-2-l',
            'https://shop.silpo.ua/product/nektar-nash-sik-multyfruktovyi-584524',
            'https://novus.online/product/sik-nas-sik-multifrukt-02l',
            'https://metro.zakaz.ua/uk/products/nektar-nash-sik-200ml-ukrayina--04820016252738/',
            'https://fozzyshop.ua/ru/soki-i-nektary/43153-nektar-nash-sik-multifruktovyj-4820016252738.html'
        ])

    def nash_sik_apple_peach_02L_parser(self):
        ''' Парсер для Наш Сік яблуко-персик 0.2 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/sik-200-ml-okzdh-nas-sik-ablucno-persikovij-z-makottu-tetpa-pak',
            'https://varus.ua/sik-nash-sik-yabluchno-persikovij-z-myakottyu-200-ml',
            'https://shop.silpo.ua/product/sik-nash-sik-iabluchno-persykovyi-z-m-iakottiu-913808',
            'https://novus.online/product/sik-nas-sik-persik-z-makittu-02l'
        ])

    def nash_sik_pear_apple_02L_parser(self):
        ''' Парсер для Наш Сік груша-яблуко 0.2 литр'''
        return self.prices_parsing([
            'https://varus.ua/sok-nash-sok-yabloko-i-grusha-0-2-l',
            'https://shop.silpo.ua/product/sik-nash-sik-iabluchno-grushevyi-917284',
            'https://novus.online/product/cik-nas-sik-grusevo-ablucnij-02l',
        ])

    def nash_sik_multivitamin_02L_parser(self):
        ''' Парсер для Наш Сік мультівітамін 0.2 литр'''
        return self.prices_parsing([
            'https://varus.ua/sok-nash-sok-multivitamin-0-2-l',
            'https://shop.silpo.ua/product/sik-nash-sik-multyvitaminnyi-z-m-iakottiu-70244',
            'https://auchan.ua/ua/sok-s-mjakot-ju-nash-sik-mul-tivitamin-0-2-l-244161/',
            'https://novus.online/product/sik-nas-sik-multivitaminnij-z-makittu-02l',
            'https://fozzyshop.ua/ru/soki-i-nektary/3971-sok-nash-sik-multivitaminnyj-s-myakotyu-4820016250604.html'
        ])

    def nash_sik_apple_02L_parser(self):
        ''' Парсер для Наш Сік яблуко 0.2 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/nektar-200-ml-nas-sik-abluko-vinograd',
            'https://varus.ua/sok-nash-sok-yablochnyy-0-2-l',
            'https://shop.silpo.ua/product/sik-nash-sik-iabluchnyi-osvitlenyi-819226',
            'https://auchan.ua/ua/sok-osvetlennyj-vosstanovlennyj-jablochnyj-nash-sik-t-p-200ml-692770/',
            'https://novus.online/product/sik-nas-sik-abluko-osvitlenij-02l',
            'https://metro.zakaz.ua/uk/products/sik-nash-sik-200ml--04820192263092/',
            'https://fozzyshop.ua/ru/soki-i-nektary/77029-sok-nash-sik-yablochnyj-osvetlennyj-4820192262668.html'
        ])

    def nash_sik_apple_strawberry_02L_parser(self):
        ''' Парсер для Наш Сік яблуко-клубника 0.2 литр'''
        return self.prices_parsing([
            'https://varus.ua/sok-nash-sok-yabloko-i-klubnika-0-2-l',
            'https://shop.silpo.ua/product/sik-nash-sik-iabluchno-polunychnyi-z-m-iakottiu-155458',
            'https://novus.online/product/sik-nas-sik-polunicno-ablucnij-z-makittu-02l',
            'https://metro.zakaz.ua/uk/products/sik-nash-sik-200ml-ukrayina--04820003680872/',
            'https://fozzyshop.ua/soki-i-nektary/3964-sok-nash-sik-yablochno-klubnichnyj-s-myakotyu-4820016250833.html'
        ])

    def non_stop_original_025L_parser(self):
        ''' Парсер для Non-Stop Original 0.25 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-250-ml-non-stop-bezalkogolnij-energeticnij-silnogazovanij',
            'https://eko.zakaz.ua/uk/products/napii-non-stop-250ml--04820097890317/',
            'https://varus.ua/napiy-energetichniy-non-stop-0-25l-zh-b',
            'https://shop.silpo.ua/product/napii-energetychnyi-non-stop-229390',
            'https://auchan.ua/ua/napitok-jenergeticheskij-non-stop-0-25l-689123/',
            'https://novus.online/product/napij-energeticnij-non-stop-025l',
            'https://metro.zakaz.ua/uk/products/energetik-non-stop-ukrayina--04820252120969/',
            'https://fozzyshop.ua/bezalkogolnye/13173-napitok-energeticheskij-non-stop-4820074180608.html'
        ])

    def non_stop_original_05L_parser(self):
        ''' Парсер для Non-Stop Original 0.5 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-05l-non-stop-bezalkogolnij-energeticnij-silnogazovanij',
            'https://varus.ua/napiy-energetichniy-non-stop-0-5l-z-b',
            'https://shop.silpo.ua/product/napii-energetychnyi-non-stop-sylnogazovanyi-319269',
            'https://auchan.ua/ua/napitok-jenergeticheskij-bezalkogol-nyj-sil-nogazirovannyj-original-non-stop-zh-b-0-5l-689179/',
            'https://novus.online/product/napij-energeticnij-non-stop-zalizna-banka-05l',
            'https://metro.zakaz.ua/uk/products/energetik-non-stop-ukrayina--04820252121188/',
            'https://fozzyshop.ua/bezalkogolnye/13176-napitok-energeticheskij-non-stop-4820097890324.html'
        ])

    def non_stop_jungle_025L_parser(self):
        ''' Парсер для Non-Stop Jungle 0.25 литр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/energetik-non-stop-250ml--04820097897224/',
            'https://varus.ua/napiy-energetichniy-dzhingl-non-stop-0-25-z-b',
            'https://shop.silpo.ua/product/napii-energetychnyi-non-stop-jungle-evolution-fresh-z-b-838902',
            'https://auchan.ua/ua/napitok-jenergeticheskij-bezalkogol-nyj-sil-nogazirovannyj-jevoljushn-fresh-jungle-non-stop-zh-b-0-25l-689214/',
            'https://novus.online/product/napij-energeticnij-non-stop-jungle-025l-zb',
            'https://metro.zakaz.ua/uk/products/energetik-non-stop-250ml--04820252120983/',
            'https://fozzyshop.ua/bezalkogolnye/83579-napitok-energetich-non-stop-jungle-evolyushn-fresh-zh-b-4820097897224.html'
        ])

    def non_stop_boost_05L_parser(self):
        ''' Парсер для Non-Stop Boost 0.5 литр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/energetik-non-stop-500ml--04820097899167/',
            'https://varus.ua/napiy-energetichniy-bust-non-stop-0-5-z-b',
            'https://shop.silpo.ua/product/napii-energetychnyi-non-stop-boost-bezalkogolnyi-sylnogazovanyi-z-b-836170',
            'https://auchan.ua/ua/napitok-jenergeticheskij-bezalkogol-nyj-sil-nogazirovannyj-boost-non-stop-zh-b-0-5l-689144/',
            'https://novus.online/product/napij-energeticnij-non-stop-boost-05l-zb',
            'https://metro.zakaz.ua/uk/products/energetik-non-stop-500ml--04820097899167/',
            'https://fozzyshop.ua/bezalkogolnye/83580-napitok-energeticheskij-non-stop-boost-bezalkogolnyj-silnogazirovannyj-zh-b-4820097899167.html'
        ])

    def non_stop_ultra_05L_parser(self):
        ''' Парсер для Non-Stop Ultra 0.5 литр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/energetik-non-stop-500ml--04820097899952/',
            'https://varus.ua/napij-energetichnij-ultra-non-stop-05-l',
            'https://shop.silpo.ua/product/napii-energetychnyi-non-stop-ultra-bezalkogolnyi-sylnogazovanyi-z-b-912964',
            'https://metro.zakaz.ua/uk/products/energetik-non-stop-500ml--04820097899952/',
            'https://fozzyshop.ua/bezalkogolnye/100302-napitok-energeticheskij-non-stop-ultra-silnogazirovannyj-250015027732.html'
        ])

    def non_stop_boost_025L_parser(self):
        ''' Парсер для Non-Stop Boost 0.25 литр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/ukrayina--04820252120020/',
            'https://varus.ua/napij-energetichnij-non-stop-boost-bezalkogolnij-silnogazovanij-250-ml',
            'https://shop.silpo.ua/product/napii-energetychnyi-non-stop-boost-bezalkogolnyi-sylnogazovanyi-z-b-921763',
            'https://metro.zakaz.ua/uk/products/ukrayina--04820252120020/',
            'https://fozzyshop.ua/bezalkogolnye/101187-napitok-energeticheskij-non-stop-boost-silnogazirovannyj-b-a-0250015135697.html'
        ])

    def burn_classic_025L_parser(self):
        ''' Парсер для Burn Classic 0.25 литр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/energetik-born-250ml--05060466511019/',
            'https://varus.ua/napiy-energetichniy-bern-0-25l-z-b',
            'https://shop.silpo.ua/product/napii-energetychnyi-burn-original-bezalkogolnyi-735013',
            'https://auchan.ua/ua/napitok-jenergeticheskij-bezalkogol-nyj-sil-nogazirovannyj-original-burn-zh-b-250ml-689165/',
            'https://novus.online/product/napij-klasicnij-energeticnij-bezalkogolnij-burn-025l-zb',
            'https://metro.zakaz.ua/uk/products/energetik-born-250ml--05060466511026/',
            'https://fozzyshop.ua/bezalkogolnye/47528-napitok-energeticheskij-burn-original-bezalkogolnyj-zh-b-5060466511019.html'
        ])

    def burn_classic_05L_parser(self):
        ''' Парсер для Burn Classic 0.5 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-05l-burn-energeticnij',
            'https://eko.zakaz.ua/uk/products/energetik-born-500ml--05060466510951/',
            'https://varus.ua/napiy-energetichniy-bern-0-5l',
            'https://shop.silpo.ua/product/napii-energetychnyi-burn-original-bezalkogolnyi-735014',
            'https://auchan.ua/ua/napitok-jenergeticheskij-bezalkogol-nyj-sil-nogazirovannyj-original-burn-zh-b-500ml-689172/',
            'https://novus.online/product/napij-klasicnij-energeticnij-bezalkogolnij-burn-05l-zb',
            'https://metro.zakaz.ua/uk/products/energetik-born-500ml--05060466510968/',
            'https://fozzyshop.ua/bezalkogolnye/47529-napitok-energeticheskij-burn-original-bezalkogolnyj-zh-b-5060466510951.html'
        ])

    def burn_mango_025L_parser(self):
        ''' Парсер для Burn Mango 0.25 литр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-born-250ml--05060466519602/',
            'https://varus.ua/napiy-energetichniy-bern-mango-0-25l-z-b',
            'https://shop.silpo.ua/product/napii-energetychnyi-burn-mango-bezalkogolnyi-800735',
            'https://novus.online/product/napij-energeticnij-bezalkogolnij-burn-mango-025l-zb',
            'https://fozzyshop.ua/bezalkogolnye/63964-napitok-energeticheskij-burn-mango-b-alk-zh-b-5060466519602.html'
        ])

    def burn_apple_kiwi_05L_parser(self):
        ''' Парсер для Burn Apple Kiwi 0.5 литр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/energetik-born-500ml--05060466510982/',
            'https://varus.ua/napiy-energetichniy-bezalkogolniy-silnogazovaniy-apple-kiwi-burn-zb-500ml',
            'https://shop.silpo.ua/product/napii-energetychnyi-burn-apple-kivi-bezalkogolnyi-739062',
            'https://auchan.ua/ua/napitok-jenergeticheskij-bezalkogol-nyj-sil-nogazirovannyj-apple-kiwi-burn-zh-b-500ml-689130/',
            'https://novus.online/product/napij-abluko-kivi-energeticnij-bezalkogolnij-burn-05l-zb',
            'https://metro.zakaz.ua/uk/products/energetik-born-250ml--05060466511057/',
            'https://fozzyshop.ua/bezalkogolnye/47558-napitok-energeticheskij-burn-apple-kivi-bezalkogolnyj-zh-b-5060466510982.html'
        ])

    def burn_dark_energy_025L_parser(self):
        ''' Парсер для Burn Dark Energy 0.25 литр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/energetik-born-250ml--05060608749898/',
            'https://varus.ua/napiy-energetichniy-burn-dark-energy-250-ml',
            'https://shop.silpo.ua/product/napii-energetychnyi-burn-dark-energy-bezalkogolnyi-z-b-883079',
            'https://novus.online/product/napiy-enerhetychnyy-bezalkoholnyy-burn-dark-energy-025l-zb'
        ])

    def red_bull_025L_parser(self):
        ''' Парсер для Red Bull 0.25 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-250-ml-red-bull-energeticnij',
            'https://shop.silpo.ua/product/napii-energetychnyi-red-bull-229392',
            'https://auchan.ua/ua/jenergichnyj-napitok-red-bull-250-ml-1043829/',
            'https://novus.online/product/napij-energeticnij-red-bull-025l',
            'https://metro.zakaz.ua/uk/products/energetik-red-bul-250ml-avstriia--09002490100070/',
            'https://fozzyshop.ua/bezalkogolnye/13179-napitok-energeticheskij-red-bull-9002490219178.html'
        ])

    def red_bull_0355L_parser(self):
        ''' Парсер для Red Bull 0.355 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-355-ml-red-bull-energeticnij-zb',
            'https://varus.ua/napiy-energetichniy-red-bull-0-355l-zh-b',
            'https://shop.silpo.ua/product/napii-red-bull-energetychnyi-314708',
            'https://auchan.ua/ua/napitok-jenergeticheskij-bezalkogol-nyj-sil-nogazirovannyj-s-taurinom-energy-drink-red-bull-zh-b-355ml-689200/',
            'https://novus.online/product/napij-energeticnij-red-bull-0355l',
            'https://metro.zakaz.ua/uk/products/energetik-red-bul-355ml-avstriia--09002490206413/',
            'https://fozzyshop.ua/bezalkogolnye/42602-napitok-energeticheskij-red-bull-9002490206000.html'
        ])

    def red_bull_0473L_parser(self):
        ''' Парсер для Red Bull 0.473 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-473-ml-red-bull-energeticnij',
            'https://varus.ua/napiy-energetichniy-red-bull-0-473l-z-b',
            'https://shop.silpo.ua/product/napii-energetychnyi-red-bull-392086',
            'https://auchan.ua/ua/napitok-jenergeticheskij-bezalkogol-nyj-sil-nogazirovannyj-s-taurinom-energy-drink-red-bull-zh-b-473ml-689207/',
            'https://novus.online/product/napij-energeticnij-red-bull-0473l',
            'https://metro.zakaz.ua/uk/products/napii-red-bul-473ml-avstriia--09002490212100/',
            'https://fozzyshop.ua/bezalkogolnye/13187-napitok-energeticheskij-red-bull-9002490212100.html'
        ])

    def red_bull_0591L_parser(self):
        ''' Парсер для Red Bull 0.591 литр'''
        return self.prices_parsing([
            'https://varus.ua/napiy-energetichniy-red-bull-0-591l-z-b',
            'https://shop.silpo.ua/product/napii-energetychnyi-red-bull-505442',
            'https://novus.online/product/napij-energeticnij-red-bull-0591l',
            'https://fozzyshop.ua/bezalkogolnye/42603-napitok-energeticheskij-red-bull-9002490220310.html'
        ])

    def red_bull_sugar_free_025L_parser(self):
        ''' Парсер для Red Bull Sugar Free 0.25 литр'''
        return self.prices_parsing([
            'https://varus.ua/napiy-energetichniy-bez-cukru-red-bull-0-25l-zh-b',
            'https://shop.silpo.ua/product/napii-energetychnyi-red-bull-bez-tsukru-310713',
            'https://auchan.ua/ua/napitok-jenergeticheskij-red-bull-bezalkogol-nyj-sugarfree-250-ml-735486/',
            'https://novus.online/product/napij-energeticnij-red-bull-bez-cukru-zalizna-banka-025l',
            'https://metro.zakaz.ua/uk/products/napii-red-bul-250ml--metro00000090162800/',
            'https://fozzyshop.ua/bezalkogolnye/81818-napitok-energeticheskij-red-bull-bez-sakhara-90162664.html'
        ])

    def red_bull_red_edition_cavun_025L_parser(self):
        ''' Парсер для Red Bull Red Edition зі смаком кавуна 0.25 литр'''
        return self.prices_parsing([
            'https://varus.ua/napiy-energetichniy-red-bull-summer-edition-kavun-250-ml',
            'https://shop.silpo.ua/product/napii-energetychnyi-red-bull-smak-kavuna-z-b-817030',
            'https://novus.online/product/napiy-enerhetychnyy-red-bull-melon-025l-zb',
            'https://fozzyshop.ua/bezalkogolnye/95085-napitok-energeticheskij-red-bull-vkus-arbuza-zh-b-90448874.html'
        ])

    def red_bull_yellow_edition_tropic_fruits_025L_parser(self):
        ''' Парсер для Red Bull Yellow Edition зі смаком тропічних фруктів 0.25 литр'''
        return self.prices_parsing([
            'https://varus.ua/napiy-energetichniy-tropik-red-bull-0-25l',
            'https://shop.silpo.ua/product/napii-energetychnyi-red-bull-zi-smakom-tropichnykh-fruktiv-z-b-608317',
            'https://auchan.ua/ua/napitok-jenergeticheskij-bezalkogol-nyj-sil-nogazirovannyj-tropical-the-yellow-edition-red-bull-zh-b-250ml-689186/',
            'https://novus.online/product/napij-energeticnij-red-bull-litna-seria-tropikal-250ml',
            'https://metro.zakaz.ua/uk/products/energetik-red-bul-250ml-avstriia--09002490228491/',
            'https://fozzyshop.ua/bezalkogolnye/42604-napitok-energeticheskij-redbull-vkus-tropich-fruk-zhb-9002490231521.html'
        ])

    def monster_0355L_parser(self):
        ''' Парсер для Monster 0.355 литр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-monster-355ml--05060517886721/',
            'https://shop.silpo.ua/product/napii-energetychnyi-monster-energy-bezalkogolnyi-sylnogazovanyi-772340',
            'https://auchan.ua/ua/napitok-jenergeticheskij-bezalkogol-nyj-sil-nogazirovannyj-monster-energy-zh-b-335ml-689158/',
            'https://novus.online/product/napij-energeticnij-silnogazovanij-monster-energy-355ml',
            'https://metro.zakaz.ua/uk/products/energetik-monster-355ml--05060517886738/',
            'https://shop.nashkraj.ua/kovel/product/282172-napiy-monster-energe-0-355l-b-a-s-g-zh-b',
            'https://fozzyshop.ua/bezalkogolnye/57259-napitok-energeticheskij-monster-energy-b-a-sil-g-zhb-5060517886721.html'
        ])

    def monster_the_doctor_0355L_parser(self):
        ''' Парсер для Monster The Doctor 0.355 литр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-monster-355ml--05060639122929/',
            'https://varus.ua/napij-bezalkogolnij-monster-enerdzhi-doctor-0355l-zh-b',
            'https://shop.silpo.ua/product/napii-energetychnyi-monster-energy-the-doctor-bezalkogolnyi-sylnogazovanyi-815697',
            'https://auchan.ua/ua/napitok-bezalkogol-nyj-sil-nogazirovanyj-jenergeticheskij-the-doctor-monster-energy-zh-b-335ml-688927/',
            'https://novus.online/product/napij-energeticnij-monster-energy-the-doctor-0355l-zb',
            'https://metro.zakaz.ua/uk/products/energetik-monster-355ml-niderlandi--05060639122936/',
            'https://shop.nashkraj.ua/kovel/product/357450-napiy-monster-0-355l-energy-the-doctor',
            'https://fozzyshop.ua/bezalkogolnye/74542-napitok-energeticheskij-monster-energy-the-doctor-bezalkogolnyj-zh-b-5060639122929.html'
        ])

    def monster_ultra_zero_0355L_parser(self):
        ''' Парсер для Monster Ultra Zero 0.355 литр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/energetik-monster-355ml--05060639128778/',
            'https://varus.ua/napiy-energetichniy-zero-monster-enerdzhi-0-355-z-b',
            'https://shop.silpo.ua/product/napii-energetychnyi-monster-energy-ultra-bezalkogolnyi-z-b-842232',
            'https://auchan.ua/ua/napitok-bezalkogol-nyj-sil-nogazirovanyj-jenergeticheskij-ultra-monster-energy-zh-b-355ml-688934/',
            'https://novus.online/product/napij-energeticnij-silnogazovanij-monster-energy-ultra-0355ml-zb',
            'https://metro.zakaz.ua/uk/products/energetik-monster-355ml-niderlandi--05060639128754/',
            'https://shop.nashkraj.ua/kovel/product/402003-napiy-monster-0-355l-energy-ultra-zero-zh',
            'https://fozzyshop.ua/bezalkogolnye/93515-napitok-energeticheskij-monster-energy-ultra-bezalkogolnyj-zh-b-5060639128778.html'
        ])

    def monster_juiced_0355L_parser(self):
        ''' Парсер для Monster Juiced 0.355 литр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/energetik-monster-355ml--05060751213062/',
            'https://varus.ua/napiy-energetichniy-mango-loko-monster-0-355l-zhb',
            'https://shop.silpo.ua/product/napii-energetychnyi-monster-energy-mango-loco-bezalkogolnyi-z-b-890962',
            'https://novus.online/product/napiy-monster-energy-manho-0355l-zb',
            'https://metro.zakaz.ua/uk/products/energetik-355ml--05060751213079/',
            'https://shop.nashkraj.ua/kovel/product/478134-napiy-monster-0-355l-energy-mango-loco',
            'https://fozzyshop.ua/bezalkogolnye/101370-napitok-energeticheskij-monster-energy-mangoloco-b-a-0250014621771.html'
        ])

    def pit_bull_coffee_250L_parser(self):
        ''' Парсер для Pit Bull Coffee 0.250 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-250-ml-pit-bull-zi-smakom-kavi-enepgeticnij-bezalkogolnij-zb',
            'https://eko.zakaz.ua/uk/products/ukrayina--04820252121775/',
            'https://shop.silpo.ua/product/napii-energetychnyi-bezalkogolnyi-sylnogazovanyi-pit-bull-coffee-z-b-921761',
            'https://novus.online/product/napiy-enerhetychnyy-pit-bull-powe-kava-025l-zb',
            'https://fozzyshop.ua/bezalkogolnye/101185-napitok-energeticheskij-pit-bull-coffee-silnogazirovannyj-b-a-0250015135703.html'
        ])

    def pit_bull_power_250L_parser(self):
        ''' Парсер для Pit Bull Power 0.250 литр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-250-ml-pit-bull-power-enepgeticnij-bezalkogolnij-zb',
            'https://eko.zakaz.ua/uk/products/ukrayina--04820252121751/',
            'https://varus.ua/napij-energetichnij-pit-bull-power-bezalkogolnij-silnogazovanij-250-ml',
            'https://shop.silpo.ua/product/napii-energetychnyi-bezalkogolnyi-sylnogazovanyi-pit-bull-power-z-b-921762',
            'https://novus.online/product/napiy-enerhetychnyy-pit-bull-power-025l-zb',
            'https://metro.zakaz.ua/uk/products/ukrayina--04820252121751/',
            'https://fozzyshop.ua/bezalkogolnye/101186-napitok-energeticheskij-pit-bull-power-silnogazirovannyj-b-a-0250015135710.html'
        ])

    def pit_bull_X_250L_parser(self):
        ''' Парсер для Pit Bull X 0.250 литр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/energetik-pit-bul-250ml--04820097897804/',
            'https://varus.ua/napiy-bezalkogolniy-energetichniy-pit-bul-iks-0-25l',
            'https://shop.silpo.ua/product/napii-energetychnyi-pit-bull-kh-bezalkogolnyi-sylnogazovanyi-z-b-788834',
            'https://novus.online/product/napij-energeticnij-bezalkogolnij-pit-bul-h-250ml-zb',
            'https://fozzyshop.ua/bezalkogolnye/77893-napitok-energeticheskij-pit-bull-kh-bezalkogolnyj-silnogazirovannyj-zh-b-4820097897804.html'
        ])

    def pit_bull_extra_vitamin_C_250L_parser(self):
        ''' Парсер для Pit Bull Extra Vitamin C 0.250 литр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/energetik-pit-bul-250ml--04820097898986/',
            'https://varus.ua/napiy-energetichniy-ekstra-vitamin-s-pit-bul-0-25l-zhb',
            'https://shop.silpo.ua/product/napii-energetychnyi-pit-bull-extra-vitamin-c-z-b-856489',
            'https://metro.zakaz.ua/uk/products/energetik-pit-bul-250ml--04820097898986/',
            'https://fozzyshop.ua/bezalkogolnye/93516-napitok-energeticheskij-pit-bull-extra-vitamin-c-zh-b-4820097898986.html'
        ])

    def pit_bull_250L_parser(self):
        ''' Парсер для Pit Bull 0.250 литр'''
        return self.prices_parsing([
            'https://varus.ua/napij-energetichnij-pit-bull-coffee-bezalkogolnij-silnogazovanij-250-ml',
            'https://auchan.ua/ua/napitok-jenergeticheskij-sil-nogazirovannyj-pit-bull-250-ml-735507/',
        ])

    def maccoffee_gold_rozch_soft_pack_60_gr_parser(self):
        ''' Парсер для MacCoffee GOLD розчинна чорна у м'якій упаковці 60 гр'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-rozchynna-maccoffee-gold-naturalna-d-p-851695',
            'https://fozzyshop.ua/kofe-rastvorimyj/90180-kofe-rastvorimyj-maccoffee-gold-naturalnyj-d-p-8887290146104.html'
        ])

    def nescafe_gold_rozch_soft_pack_120_gr_parser(self):
        ''' Парсер для Nescafe GOLD розчинна чорна у м'якій упаковці 120 гр'''
        return self.prices_parsing([
            'https://varus.ua/kava-rozchinna-sublimovana-nescafe-gold-120-g',
            'https://shop.silpo.ua/product/kava-rozchynna-nescafe-gold-663485',
            'https://auchan.ua/ua/kofe-rastvorimyj-nescafe-gold-100-g-503789/',
            'https://novus.online/product/kava-naturalna-rozcinna-neskafe-gold-maka-upakovka-120g',
            'https://metro.zakaz.ua/uk/products/kava-neskafe-120g--07613035524811/',
            'https://fozzyshop.ua/kofe-rastvorimyj/12542-kofe-nescafe-gold-140g-7613035524811.html'
        ])

    def grano_dorado_gold_soft_pack_130_gr_parser(self):
        ''' Парсер для Grano Dorado GOLD розчинна чорна у м'якій упаковці 130 гр'''
        return self.prices_parsing([
            'https://fozzyshop.ua/kofe-rastvorimyj/85692-kofe-rastvorimyj-grano-dorado-gold-4820017296069.html'
        ])

    def nescafe_classic_soft_pack_60_gr_parser(self):
        ''' Парсер для Nescafe Classic розчинна чорна у м'якій упаковці 60 гр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/kava-neskafe-60g--07613035585881/',
            'https://varus.ua/kava-naturalna-rozchinna-granulovana-nescafe-classic-60-g',
            'https://shop.silpo.ua/product/kava-rozchynna-nescafe-classic-granulovana-100-naturalna-667662',
            'https://auchan.ua/ua/kofe-rastvorimyj-nescafe-classic-60-g-503659/',
            'https://novus.online/product/kava-naturalna-rozcinna-neskafe-klasik-maka-upakovka-60g',
            'https://metro.zakaz.ua/uk/products/kava-neskafe-60g--07613035585881/',
            'https://fozzyshop.ua/kofe-rastvorimyj/12667-kofe-rastvorimyj-nescafe-classic-7613035585881.html'
        ])

    def chorna_karta_gold_soft_pack_400_gr_parser(self):
        ''' Парсер для Чорна карта Gold розчинна чорна у м'якій упаковці 400 гр'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-rozchynna-chernaia-karta-paket-650455',
            'https://auchan.ua/ua/kofe-rastvorimyj-chorna-karta-gold-400-g-509883/',
            'https://novus.online/product/kava-rozcinna-corna-karta-gold-paket-400g',
            'https://fozzyshop.ua/kofe-rastvorimyj/24028-kofe-rastvorimyj-chernaya-karta-paket-8718868866394.html'
        ])

    def bounty_small_gr_parser(self):
        ''' Парсер для Bounty 57 грамм'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/batoncik-57g-mars-bounty',
            'https://eko.zakaz.ua/uk/products/batonchik-baunti-57g-niderlandi--00058496813048/',
            'https://varus.ua/batonchik-bounty-shokoladnyy-s-kokosom-55-g',
            'https://shop.silpo.ua/product/batonchyk-bounty-z-m-iakottiu-kokosu-u-molochnomu-shokoladi-597388',
            'https://auchan.ua/ua/batonchik-bounty-57-g-215729/',
            'https://novus.online/product/batoncik-bounty-v-molocno-sokoladnij-glazuri-ta-kokosovou-nacinkou-57g',
            'https://metro.zakaz.ua/uk/products/batonchik-baunti-57g--04011100977624/',
            'https://shop.nashkraj.ua/kovel/product/207698-batonchik-bounty-57g',
            'https://fozzyshop.ua/shokolad-i-batonchiki/15610-batonchik-bounty-s-myakotyu-kokosa-v-molochnom-shokolade-40111216.html'
        ])

    def bounty_big_gr_parser(self):
        ''' Парсер для Bounty 85 грамм'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/batoncik-85-mars-bounty-trio-molocnij-sokolad',
            'https://eko.zakaz.ua/uk/products/batonchik-baunti-85g--04011100038653/',
            'https://varus.ua/batonchik-bounty-trio-shokoladnyy-s-kokosom-88-5-g',
            'https://shop.silpo.ua/product/batonchyk-bounty-trio-z-m-iakottiu-kokosu-u-molochnomu-shokoladi-597389',
            'https://auchan.ua/ua/batonchik-bounty-trio-85-g-236148/',
            'https://novus.online/product/batoncik-bounty-triov-molocno-sokoladnij-glazuri-ta-kokosovou-nacinkou-855g',
            'https://metro.zakaz.ua/uk/products/batonchik-baunti-85g--04011100038653/',
            'https://fozzyshop.ua/shokolad-i-batonchiki/15608-batonchik-bounty-trio-s-myakotyu-kokosa-v-molochnom-shokolade-4011100038653.html'
        ])

    def mars_51gr_parser(self):
        ''' Парсер для Mars 51 грамм'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/batonchik-mars-51g--05000159502931/',
            'https://varus.ua/batonchik-mars-shokoladnyy-s-nugoy-i-karamelyu-51-g',
            'https://shop.silpo.ua/product/batonchyk-mars-z-nugoiu-ta-karamelliu-u-molochnomu-shokoladi-719198',
            'https://metro.zakaz.ua/uk/products/batonchik-mars-51g--05000159502931/',
            'https://shop.nashkraj.ua/kovel/product/228489-batonchik-mars-51g-nuga-ta-karamel',
            'https://fozzyshop.ua/shokolad-i-batonchiki/43707-batonchik-mars-s-nugoj-i-karamelyu-v-molochn-shokolad-5000159502931.html'
        ])

    def mars_70gr_parser(self):
        ''' Парсер для Mars 70 грамм'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/batoncik-70g-mars-2-z-nugou-i-karamellu-vkritij-molocnim-sokoladom',
            'https://eko.zakaz.ua/uk/products/batonchik-mars-70g--05000159408301/',
            'https://varus.ua/batonchik-mars-shokoladnyy-s-nugoy-i-karamelyu-2-h-35-g',
            'https://shop.silpo.ua/product/batonchyk-mars-nuga-karamel-u-molochnomu-shokoladi-659822',
            'https://novus.online/product/batoncik-mars2-z-nugou-ta-karamellu-70g',
            'https://metro.zakaz.ua/uk/products/batonchik-mars-70g--05000159408301/',
            'https://shop.nashkraj.ua/kovel/product/228490-batonchik-mars-70g-nuga-ta-karamel',
            'https://fozzyshop.ua/shokolad-i-batonchiki/37601-batonchik-mars-nuga-karamel-v-molochnom-shokolade-5000159408301.html'
        ])

    def nuts_strawberry_parser(self):
        ''' Парсер для Nuts Strawberry'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/batonchik-nats-42g--08593893780576/',
            'https://varus.ua/batonchik-nuts-strawberry-42-g',
            'https://shop.silpo.ua/product/batonchyk-nuts-strawberry-911321',
            'https://auchan.ua/ua/batonchik-nestle-nuts-strawberry-s-klubnichnym-vkusom-42-g-1176093/',
            'https://metro.zakaz.ua/uk/products/batonchik-nats-42g--08593893780576/',
            'https://fozzyshop.ua/shokolad-i-batonchiki/98861-batonchik-nuts-strawberry-0250014951250.html'
        ])

    def nuts_42gr_parser(self):
        ''' Парсер для Nuts 42 гр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/batonchik-nats-42g--08593893745841/',
            'https://varus.ua/batonchik-nuts-shokoladnyy-s-lesnymi-orehami-42-g',
            'https://shop.silpo.ua/product/batonchyk-nuts-shokoladnyi-638804',
            'https://auchan.ua/ua/batonchik-nestle-nuts-47-g-609588/',
            'https://novus.online/product/batoncik-sokoladnij-nuts-single-42g',
            'https://metro.zakaz.ua/uk/products/batonchik-nats-42g--08593893745841/',
            'https://shop.nashkraj.ua/kovel/product/230685-batonchik-nuts-42g-oridzhinal',
            'https://fozzyshop.ua/shokolad-i-batonchiki/27584-batonchik-nuts-shokoladnyj-8593893745841.html'
        ])

    def nuts_king_size_60gr_parser(self):
        ''' Парсер для Nuts King Size 60 гр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/batonchik-nats-60g--08593893745865/',
            'https://varus.ua/batonchik-nuts-king-size-shokoladnyy-s-lesnymi-orehami-60-g',
            'https://auchan.ua/ua/batonchik-nestle-nuts-king-60-g-609623/',
            'https://novus.online/product/batoncik-sokoladnij-nuts-king-size-60g',
            'https://metro.zakaz.ua/uk/products/batonchik-nats-60g--08593893745865/',
            'https://shop.nashkraj.ua/kovel/product/235550-batonchik-nuts-60g-king',
            'https://fozzyshop.ua/shokolad-i-batonchiki/27583-batonchik-nuts-king-size-shokoladnyj-8593893745865.html'
        ])

    def snickers_50gr_parser(self):
        ''' Парсер для Snickers 50 гр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/batoncik-50g-mars-snickers',
            'https://eko.zakaz.ua/uk/products/batonchik-snikers-50g--05000159461122/',
            'https://varus.ua/batonchik-snickers-shokoladnyy-s-nugoy-karamelyu-i-arahisom-50-g',
            'https://shop.silpo.ua/product/batonchyk-snickers-z-arakhisom-u-molochnomu-shokoladi-597390',
            'https://auchan.ua/ua/batonchik-snickers-50-g-215728/',
            'https://novus.online/product/batoncik-snickers-50g',
            'https://metro.zakaz.ua/uk/products/batonchik-snikers-50-5g--04607065001445/',
            'https://shop.nashkraj.ua/kovel/product/207700-batonchik-snickers-50g',
            'https://fozzyshop.ua/shokolad-i-batonchiki/15622-batonchik-snickers-s-arakhisom-v-molochnom-shokolade-5000159461122.html'
        ])

    def snickers_super_112_5gr_parser(self):
        ''' Парсер для Snickers Super 112.5 гр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/batoncik-1125g-mars-snickers-super1',
            'https://varus.ua/batonchik-snickers-super-shokoladnyy-s-nugoy-karamelyu-i-arahisom-112-5-g',
            'https://shop.silpo.ua/product/batonchyk-snickers-super-z-arakhisom-u-molochnomu-shokoladi-664167',
            'https://auchan.ua/ua/batonchik-snickers-super-1-239043/',
            'https://novus.online/product/batoncik-snickers-super-1-1125g',
            'https://metro.zakaz.ua/uk/products/batonchik-snikers-112-50g--05900951261060/',
            'https://shop.nashkraj.ua/kovel/product/228367-batonchik-snickers-super1-112-5g',
            'https://fozzyshop.ua/shokolad-i-batonchiki/28997-batonchik-snickers-super-s-arakhisom-v-molochnom-shokolade-5900951261060.html'
        ])

    def snickers_creamy_peanut_butter_54_75gr_parser(self):
        ''' Парсер для Snickers Creamy Peanut Butter 54_75 гр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/batoncik-5475g-mars-snickers-creamy-z-arahisovim-maslom',
            'https://eko.zakaz.ua/uk/products/54-75g--05900951286612/',
            'https://varus.ua/batonchik-snickers-creamy-peanut-butter-shokoladnyy-s-arahisovoy-pastoy-karamelyu-i-arahisom-3-h-18-25-g',
            'https://shop.silpo.ua/product/batonchyk-snickers-z-arakhisovym-maslom-847012',
            'https://auchan.ua/ua/batonchik-snickers-creamy-peanut-butter-54-75-g-616194/',
            'https://metro.zakaz.ua/uk/products/54-75g--05900951286612/',
            'https://shop.nashkraj.ua/kovel/product/425809-batonchik-snickers-54-75g-creamy-arakh-mas',
            'https://fozzyshop.ua/shokolad-i-batonchiki/84955-batonchik-snickers-s-arakhisovym-maslom-5900951286612.html'
        ])

    def snickers_creamy_peanut_butter_36_5gr_parser(self):
        ''' Парсер для Snickers Creamy Peanut Butter 36_5 гр'''
        return self.prices_parsing([
            'https://varus.ua/batonchik-snickers-creamy-peanut-butter-shokoladnyy-s-arahisovoy-pastoy-karamelyu-i-arahisom-2-h-18-25-g',
            'https://shop.silpo.ua/product/batonchyk-snickers-z-arakhisovym-maslom-847011',
            'https://auchan.ua/ua/batonchik-snickers-creamy-peanut-butter-36-5-g-616187/',
            'https://metro.zakaz.ua/uk/products/batonchik-snikers-36-5g--05900951283963/',
            'https://shop.nashkraj.ua/kovel/product/426614-batonchik-snickers-36-5g-creamy-arakh-masl',
            'https://fozzyshop.ua/shokolad-i-batonchiki/84954-batonchik-snickers-s-arakhisovym-maslom-5900951283963.html'
        ])

    def twix_50gr_parser(self):
        ''' Парсер для Twix 50 гр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/batoncik-50g-mars-twix',
            'https://eko.zakaz.ua/uk/products/batonchik-tviks-50g--05000159459228/',
            'https://varus.ua/batonchik-twix-shokoladnyy-s-pechenem-i-karamelyu-75-g',
            'https://shop.silpo.ua/product/batonchyk-twix-z-pechyvom-ta-karamelliu-u-molochnomu-shokoladi-597393',
            'https://auchan.ua/ua/batonchik-twix-50-g-215730/',
            'https://novus.online/product/batoncik-twix-50g',
            'https://metro.zakaz.ua/uk/products/batonchik-tviks-50g--05000159459228/',
            'https://shop.nashkraj.ua/kovel/product/207701-batonchik-twix-50g-molochniy-shokolad',
            'https://fozzyshop.ua/shokolad-i-batonchiki/15627-batonchik-twix-s-pechenem-i-karamelyu-v-molochnom-shokolade-5000159459228.html'
        ])

    def twix_75gr_parser(self):
        ''' Парсер для Twix 75 гр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/pecivo-75g-mars-twix-ekstra',
            'https://eko.zakaz.ua/uk/products/batonchik-tviks-75g--05900951028502/',
            'https://varus.ua/batonchik-twix-xtra-shokoladnyy-s-pechenem-i-karamelyu-75-g',
            'https://shop.silpo.ua/product/batonchyk-twix-extra-pechyvo-i-karamel-u-molochnomu-shokoladi-659819',
            'https://auchan.ua/ua/batonchik-twix-extra-75-g-236149/',
            'https://novus.online/product/batoncik-twix-xtra-u-molocnomu-sokoladi-75g',
            'https://metro.zakaz.ua/uk/products/batonchik-tviks-75g--05900951028502/',
            'https://shop.nashkraj.ua/kovel/product/228493-batonchik-twix-75g-ekstra-u-molochn-shokol',
            'https://fozzyshop.ua/shokolad-i-batonchiki/28999-batonchik-twix-extra-pechene-karamel-v-molochnom-shokolade-5900951028502.html'
        ])

    def vodka_absolut_05l_parser(self):
        ''' Парсер для водка Absolut 0.5 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-absoliut-500ml-shvetsiia--07312040017072/',
            'https://varus.ua/gorilka-absolut-40-0-5-l',
            'https://shop.silpo.ua/product/gorilka-absolut-28285',
            'https://auchan.ua/ua/vodka-absolut-40-0-5-l-28285-1074421/',
            'https://novus.online/product/gorilka-absolut-gol-40-05l',
            'https://metro.zakaz.ua/uk/products/gorilka-absoliut-500ml-shvetsiia--07312040017072/',
            'https://shop.nashkraj.ua/kovel/product/21963-gorilka-absolut-0-5l-40',
            'https://fozzyshop.ua/vodka/1898-vodka-absolut-7312040017072.html'
        ])

    def vodka_absolut_1l_parser(self):
        ''' Парсер для водка Absolut 1 л'''
        return self.prices_parsing([
            'https://varus.ua/gorilka-absolut-40-1-l',
            'https://shop.silpo.ua/product/gorilka-absolut-31808',
            'https://auchan.ua/ua/vodka-absolut-40-1l-1047284/',
            'https://novus.online/product/gorilka-absolut-gol-40-1l',
            'https://metro.zakaz.ua/uk/products/gorilka-absoliut-1000ml-shvetsiia--07312040017034/',
            'https://fozzyshop.ua/vodka/1923-vodka-absolut-7312040550326.html'
        ])

    def vodka_absolut_07l_parser(self):
        ''' Парсер для водка Absolut 0.7 л'''
        return self.prices_parsing([
            'https://varus.ua/gorilka-absolut-40-0-7-l',
            'https://shop.silpo.ua/product/gorilka-absolut-40-439155',
            'https://auchan.ua/ua/vodka-40-absolut-0-7-l-1249591/',
            'https://novus.online/product/gorilka-absolut-40-07l',
            'https://metro.zakaz.ua/uk/products/gorilka-absoliut-700ml-shvetsiia--07312040017010/',
            'https://fozzyshop.ua/vodka/1840-vodka-absolut-40-7312040017683.html'
        ])

    def vodka_absolut_lime_07l_parser(self):
        ''' Парсер для водка Absolut Lime 0.7 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-absoliut-700ml--07312040551668/',
            'https://shop.silpo.ua/product/gorilka-absolut-lime-794090',
            'https://auchan.ua/ua/vodka-absolut-lime-40-700-ml-887542/',
            'https://novus.online/product/gorilka-absolut-lime-40-07l',
            'https://metro.zakaz.ua/uk/products/gorilka-absoliut-700ml--07312040551668/',
            'https://fozzyshop.ua/vodka/73354-vodka-absolut-lime-7312040551668.html'
        ])

    def vodka_absolut_grapefruit_07l_parser(self):
        ''' Парсер для водка Absolut Grapefruit 0.7 л'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/gorilka-absolut-grapefruit-794091',
            'https://auchan.ua/ua/vodka-absolut-grapefruit-40-700-ml-887535/',
            'https://novus.online/product/gorilka-absolut-grapefruit-40-07l',
            'https://metro.zakaz.ua/uk/products/gorilka-absoliut-700ml--07312040552153/',
            'https://fozzyshop.ua/vodka/73353-vodka-absolut-grapefruit-7312040552153.html'
        ])

    def vodka_absolut_elyx_07l_parser(self):
        ''' Парсер для водка Absolut Elyx 0.7 л'''
        return self.prices_parsing([
            'https://auchan.ua/ua/vodka-absolut-elyx-42-3-700-ml-887570/',
            'https://fozzyshop.ua/vodka/36500-vodka-absolut-elyx-423-7312040217014.html'
        ])

    def vodka_absolut_citron_07l_parser(self):
        ''' Парсер для водка Absolut Citron 0.7 л'''
        return self.prices_parsing([
            'https://varus.ua/gorilka-absolut-citron-40-0-7-l',
            'https://shop.silpo.ua/product/gorilka-absolut-citron-455671',
            'https://auchan.ua/ua/vodka-absolut-sitron-40-700-ml-1164939/',
            'https://novus.online/product/gorilka-absolut-citron-40-07l',
            'https://metro.zakaz.ua/uk/products/gorilka-absoliut-700ml-shvetsiia--07312040090709/',
            'https://fozzyshop.ua/vodka/1841-vodka-absolut-citron-7312040090709.html'
        ])

    def vodka_absolut_kurant_07l_parser(self):
        ''' Парсер для водка Absolut Kurant 0.7 л'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/gorilka-absolut-kurant-40-439153',
            'https://auchan.ua/ua/vodka-absolut-kurant-40-700-ml-1164945/',
            'https://novus.online/product/gorilka-40-absolut-surgant-07l',
            'https://metro.zakaz.ua/uk/products/gorilka-absoliut-700ml-shvetsiia--07312040020706/',
            'https://fozzyshop.ua/vodka/1842-vodka-absolut-kurant-40-7312040020706.html'
        ])

    def vodka_absolut_watermelon_07l_parser(self):
        ''' Парсер для водка Absolut Watermelon 0.7 л'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/gorilka-absolut-watermelon-857471',
            'https://auchan.ua/ua/vodka-absolut-watermelon-38-700-ml-887556/',
            'https://novus.online/product/horilka-absolut-watermelon-38-07l',
            'https://metro.zakaz.ua/uk/products/gorilka-absoliut-700ml--07312040552726/',
            'https://fozzyshop.ua/vodka/93433-vodka-absolut-watermelon-7312040552726.html'
        ])

    def vodka_absolut_mandarin_07l_parser(self):
        ''' Парсер для водка Absolut Mandarin 0.7 л'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/gorilka-absolut-mandarin-459689',
            'https://novus.online/product/gorilka-40-absolut-mandrin-07l',
            'https://fozzyshop.ua/vodka/1843-vodka-absolut-mandarin-7312040050703.html'
        ])

    def vodka_finland_05l_parser(self):
        ''' Парсер для водка Finland 0.5 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/gorilka-05l-finlandia-40',
            'https://eko.zakaz.ua/uk/products/gorilka-finliandiia-500ml-finliandiia--06412709021271/',
            'https://shop.silpo.ua/product/gorilka-finlandia-37541',
            'https://auchan.ua/ua/vodka-finlandia-40-0-5-l-1074606/',
            'https://novus.online/product/gorilka-finlandia-40-05l',
            'https://metro.zakaz.ua/uk/products/gorilka-finliandiia-500ml-finliandiia--06412709021271/',
            'https://shop.nashkraj.ua/kovel/product/22549-gorilka-finlandia-0-5l-40',
            'https://fozzyshop.ua/vodka/2036-vodka-finlandia-6412709021271.html'
        ])

    def vodka_finland_07l_parser(self):
        ''' Парсер для водка Finland 0.7 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-finliandiia-700ml-finliandiia--06412709021776/',
            'https://varus.ua/gorilka-finlandia-40-0-7-l',
            'https://shop.silpo.ua/product/gorilka-finlandia-216183',
            'https://auchan.ua/ua/vodka-finlandia-40-0-7l-1047865/',
            'https://novus.online/product/gorilka-finlandia-40-07l',
            'https://metro.zakaz.ua/uk/products/gorilka-finliandiia-700ml-finliandiia--06412709021776/',
            'https://fozzyshop.ua/vodka/2058-vodka-finlandia-6412709021776.html'
        ])

    def vodka_finland_1l_parser(self):
        ''' Парсер для водка Finland 1 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-finliandiia-1000ml-finliandiia--06412700021027/',
            'https://varus.ua/gorilka-finlandia-40-1-l',
            'https://shop.silpo.ua/product/gorilka-finlandia-9112',
            'https://auchan.ua/ua/vodka-finlandia-40-1l-1047871/',
            'https://novus.online/product/gorilka-finlandia-40-1l',
            'https://metro.zakaz.ua/uk/products/gorilka-finliandiia-1000ml-finliandiia--06412700021027/',
            'https://fozzyshop.ua/vodka/16366-vodka-finlandia-6412700021027.html'
        ])

    def vodka_finland_redberry_05l_parser(self):
        ''' Парсер для водка Finland Redberry 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/gorilka-finlandia-redberry-37-5-0-5-l',
            'https://shop.silpo.ua/product/gorilka-finlandia-chervona-iagoda-241997',
            'https://auchan.ua/ua/vodka-finlandia-kljukva-37-5-0-5-l-48335-1074601/',
            'https://metro.zakaz.ua/uk/products/gorilka-finliandiia-500ml-finliandiia--05099873002223/',
            'https://shop.nashkraj.ua/kovel/product/176253-napiy-alk-finlandia-0-5l-redberry-37-5',
            'https://fozzyshop.ua/vodka/2038-vodka-finlandia-redberry-5099873002223.html'
        ])

    def vodka_finland_redberry_1l_parser(self):
        ''' Парсер для водка Finland Redberry 1 л'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/gorilka-finlandia-chervona-iagoda-255607',
            'https://novus.online/product/gorilka-finlandia-redberri-40-1l',
        ])

    def vodka_finland_cranberry_05l_parser(self):
        ''' Парсер для водка Finland Cranberry 0.5 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/gorilka-05l-finlandia-cranberry-375',
            'https://eko.zakaz.ua/uk/products/gorilka-finliandiia-500ml-finliandiia--05099873001950/',
            'https://shop.silpo.ua/product/gorilka-finlandia-zhuravlyna-47723',
            'https://auchan.ua/ua/vodka-finlandia-kljukva-37-5-0-5-l-1074591/',
            'https://novus.online/product/gorilka-finlandia-zuravlina-bila-375-05l',
            'https://metro.zakaz.ua/uk/products/gorilka-finliandiia-500ml-finliandiia--05099873001950/',
            'https://shop.nashkraj.ua/kovel/product/176251-napiy-alk-finlandia-0-5l-cranberry-37-5',
            'https://fozzyshop.ua/vodka/2059-vodka-finlandia-cranberry-5099873001950.html'
        ])

    def vodka_finland_cranberry_1l_parser(self):
        ''' Парсер для водка Finland Cranberry 1 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-finliandiia-1000ml-finliandiia--05099873001929/',
            'https://shop.silpo.ua/product/gorilka-finlandia-zhuravlyna-14267',
            'https://novus.online/product/gorilka-finlandia-zuravlina-bila-375-1l',
            'https://metro.zakaz.ua/uk/products/gorilka-finliandiia-1000ml-finliandiia--05099873001929/',
            'https://fozzyshop.ua/vodka/2037-vodka-finlandia-cranberry-5099873001929.html'
        ])

    def vodka_finland_grapefruit_05l_parser(self):
        ''' Парсер для водка Finland Grapefruit 0.5 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-finliandiia-500ml-finliandiia--05099873002025/',
            'https://varus.ua/gorilka-finlandia-grapefruit-37-5-0-5-l',
            'https://shop.silpo.ua/product/gorilka-finlandia-grapefruit-462536',
            'https://auchan.ua/ua/vodka-finlandia-grejpfrut-37-5-0-5-l-1164152/',
            'https://novus.online/product/gorilka-finlandia-grejpfrut-375-05l',
            'https://metro.zakaz.ua/uk/products/gorilka-finliandiia-500ml-finliandiia--05099873002025/',
            'https://shop.nashkraj.ua/kovel/product/176252-napiy-alk-finlandia-0-5l-grapefruit37-5',
            'https://fozzyshop.ua/vodka/1656-vodka-finlandia-grapefruit-5099873002025.html'
        ])

    def vodka_finland_lime_05l_parser(self):
        ''' Парсер для водка Finland Lime 0.5 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-finliandiia-500ml-finliandiia--05099873002094/',
            'https://varus.ua/gorilka-finlandia-lime-37-5-0-5-l',
            'https://shop.silpo.ua/product/gorilka-finlandia-lime-506519',
            'https://auchan.ua/ua/vodka-finlandia-lajm-37-5-0-5-l-1074596/',
            'https://novus.online/product/gorilka-finlandia-lajm-375-05l',
            'https://metro.zakaz.ua/uk/products/gorilka-finliandiia-500ml-finliandiia--05099873002094/',
            'https://shop.nashkraj.ua/kovel/product/176250-napiy-alk-finlandia-0-5l-lime-37-5',
            'https://fozzyshop.ua/vodka/26676-vodka-finlandia-lime-5099873002094.html'
        ])

    def vodka_finland_coconut_05l_parser(self):
        ''' Парсер для водка Finland Coconut 0.5 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-finliandiia-500ml--05099873012321/',
            'https://shop.silpo.ua/product/gorilka-finlandia-coconut-792144',
            'https://auchan.ua/ua/vodka-finlandia-kokos-37-5-0-5-l-1074586/',
            'https://novus.online/product/gorilka-finlandia-coconut-375-05l',
            'https://metro.zakaz.ua/uk/products/gorilka-finliandiia-500ml--05099873012321/',
            'https://shop.nashkraj.ua/kovel/product/306225-gorilka-finlandia-0-5l-coconut-37-5',
            'https://fozzyshop.ua/vodka/60397-vodka-finlandia-coconut-5099873012321.html'
        ])

    def vodka_finland_blackcurrant_05l_parser(self):
        ''' Парсер для водка Finland Blackcurrant 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/gorilka-finlandia-balckcurrant-37-5-0-5-l',
            'https://shop.silpo.ua/product/gorilka-finlandia-blackcurrant-590064',
            'https://fozzyshop.ua/vodka/23817-vodka-finlandia-blackcurrant-5099873001899.html'
        ])

    def vodka_finland_lime_1l_parser(self):
        ''' Парсер для водка Finland Lime 1 л'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/gorilka-finlandia-lime-506521',
            'https://novus.online/product/gorilka-finlandia-lime-375-1l',
            'https://metro.zakaz.ua/uk/products/gorilka-finliandiia-1000ml-finliandiia--05099873002063/',
            'https://fozzyshop.ua/vodka/37666-vodka-finlandia-lime-5099873002063.html'
        ])

    def vodka_finland_blackcurrant_1l_parser(self):
        ''' Парсер для водка Finland Blackcurrant 1 л'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/gorilka-finlandia-blackcurrant-590063',
            'https://novus.online/product/gorilka-finlandia-vodka-blackcurrant-375-10l',
            'https://metro.zakaz.ua/uk/products/gorilka-finliandiia-1000ml-finliandiia--05099873001875/',
            'https://fozzyshop.ua/vodka/26675-vodka-finlandia-blackcurrant-5099873001875.html'
        ])

    def vodka_finland_grapefruit_1l_parser(self):
        ''' Парсер для водка Finland Grapefruit 1 л'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/gorilka-finlandia-grapefruit-462537',
            'https://novus.online/product/gorilka-finlandia-grejpfrut-375-1l',
            'https://metro.zakaz.ua/uk/products/gorilka-finliandiia-1000ml-finliandiia--05099873001998/',
            'https://fozzyshop.ua/vodka/37665-vodka-finlandia-grapefruit-5099873001998.html'
        ])

    def vodka_finland_white_175l_parser(self):
        ''' Парсер для водка Finland White 1.75 л'''
        return self.prices_parsing([
            'https://novus.online/product/gorilka-finlandia-40-175l',
            'https://fozzyshop.ua/vodka/92594-vodka-finlandia-belaya-6412709021103.html'
        ])

    def vodka_nemiroff_delicat_soft_05l_parser(self):
        ''' Парсер для водка Nemiroff Delicat Soft 0.5 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/gorilka-05l-nemiroff-delikat-maka-osobliva-40',
            'https://eko.zakaz.ua/uk/products/gorilka-nemiroff-500ml--04820181420437/',
            'https://shop.silpo.ua/product/gorilka-nemiroff-delikat-m-iaka-413758',
            'https://novus.online/product/gorilka-nemiroff-delikat-40-stof-05l',
            'https://metro.zakaz.ua/uk/products/gorilka-nemiroff-500ml-ukrayina--04607805950095/',
            'https://shop.nashkraj.ua/kovel/product/142666-gorilka-nemiroff-0-5l-delikat-shtof-40',
            'https://fozzyshop.ua/vodka/26688-vodka-nemiroff-delikat-myagkaya-4820181420437.html'
        ])

    def vodka_nemiroff_shtof_05l_parser(self):
        ''' Парсер для водка Nemiroff Штоф 0.5 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/gorilka-05l-nemiroff-osobliva-stof-40',
            'https://eko.zakaz.ua/uk/products/gorilka-nemiroff-500ml-ukrayina--04820181420611/',
            'https://varus.ua/gorilka-nemiroff-original-40-0-5-l',
            'https://shop.silpo.ua/product/gorilka-nemiroff-osoblyva-shtof-1132',
            'https://novus.online/product/gorilka-nemiroff-original-40-stof-05l',
            'https://metro.zakaz.ua/uk/products/gorilka-nemiroff-500ml-ukrayina--04607805950019/',
            'https://fozzyshop.ua/vodka/26691-vodka-nemiroff-osobaya-shtof-4820181420611.html'
        ])

    def vodka_nemiroff_ukr_pshen_05l_parser(self):
        ''' Парсер для водка Nemiroff Українська пшенична 0.5 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/gorilka-05-l-nemiroff-psenica-ukrainska-vidbirna-osobliva-stof-40-ob-skbut',
            'https://eko.zakaz.ua/uk/products/gorilka-nemiroff-500ml-ukrayina--04820181420741/',
            'https://varus.ua/gorilka-nemiroff-nemirivska-pshenicya-ukrainska-0-5-l',
            'https://shop.silpo.ua/product/gorilka-nemiroff-ukrainska-pshenytsia-plaska-137397',
            'https://novus.online/product/gorilka-nemiroff-psenicna-ukrainska-vidbirna-40-ploska-05l',
            'https://fozzyshop.ua/vodka/16333-vodka-nemiroff-ukrainskaya-pshenica-ploskaya-butylka-4820181420710.html'
        ])

    def vodka_nemiroff_delux_05l_parser(self):
        ''' Парсер для водка Nemiroff Де Люкс 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/gorilka-nemiroff-de-luxe-40-0-5-l',
            'https://shop.silpo.ua/product/gorilka-nemiroff-de-luxe-765322',
            'https://auchan.ua/ua/vodka-nemiroff-de-luxe-500-ml-958918/',
            'https://novus.online/product/gorilka-osobliva-nemiroff-de-luks-40-05l',
            'https://shop.nashkraj.ua/kovel/product/275553-gorilka-nemiroff-0-5lpremium-de-luxe-40',
            'https://fozzyshop.ua/vodka/64172-vodka-nemiroff-de-lyuks-4820181424886.html'
        ])

    def vodka_nemiroff_lex_05l_parser(self):
        ''' Парсер для водка Nemiroff Lex 0.5 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-nemiroff-500ml-ukrayina--04820181420550/',
            'https://shop.silpo.ua/product/gorilka-nemiroff-lex-152875',
            'https://novus.online/product/gorilka-nemiroff-lexx-40-05l',
            'https://fozzyshop.ua/vodka/26689-vodka-nemiroff-lex-4820181420550.html'
        ])

    def artemivske_bile_napivsolodke_parser(self):
        ''' Парсер для шампанського Артемівське біле напівсолодке'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/vino-075-l-igriste-artwinery-artemivske-bile-vitrimane-napivsolodke-10-135',
            'https://eko.zakaz.ua/uk/products/vino-igriste-azshv-750ml-ukrayina--04820003353332/',
            'https://varus.ua/vino-igriste-artemivske-bile-napivsolodke-chorna-etiketka-0-75-l',
            'https://auchan.ua/ua/vino-igristoe-artemovskoe-beloe-polusladkoe-10-13-5-750-ml-957748/',
            'https://novus.online/product/vino-igriste-artemivske-bile-napivsolodke-135-075l-2',
            'https://metro.zakaz.ua/uk/products/vino-igriste-azshv-750ml-ukrayina--04820003350539/',
            'https://shop.nashkraj.ua/kovel/product/20274-vino-igr-artemivske-0-75l-b-n-sol-13-5',
            'https://fozzyshop.ua/shampanskoe/1491-shampanskoe-azshv-artemovskoe-beloe-polusladkoe-4820003353332.html'
        ])

    def artemivske_rojeve_napivsuhe_parser(self):
        ''' Парсер для шампанського Артемівське рожеве напівсухе'''
        return self.prices_parsing([
            'https://varus.ua/vino-igriste-artemivske-rozheve-napivsuhe-0-75-l',
            'https://shop.silpo.ua/product/vyno-igryste-azshv-artemivske-rozheve-napivsukhe-329581',
            'https://auchan.ua/ua/vino-igristoe-artemovskoe-rozovoe-polusuhoe-10-13-5-750-ml-957778/',
            'https://novus.online/product/vino-igriste-artemivske-rozeve-napivsuhe-135-075l',
            'https://fozzyshop.ua/shampanskoe/1500-shampanskoe-azshv-artemovskoe-rozovoe-polusukhoe-4820003350171.html'
        ])

    def artemivske_bile_brut_parser(self):
        ''' Парсер для шампанського Артемівське біле брют'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/vino-075-l-artwinery-artemivske-igriste-vitrimane-bile-brut-100-135',
            'https://eko.zakaz.ua/uk/products/vino-igriste-artemivske-750ml--04820236722462/',
            'https://varus.ua/vino-igriste-artemivske-bile-bryut-0-75-l',
            'https://shop.silpo.ua/product/vyno-igryste-azshv-artemivske-bile-briut-333666',
            'https://auchan.ua/ua/vino-igristoe-artemovskoe-beloe-brjut-10-13-5-750-ml-957754/',
            'https://novus.online/product/vino-igriste-artemivske-bile-brut-135-075l',
            'https://metro.zakaz.ua/uk/products/vino-igriste-azshv-750ml-ukrayina--04820003350478/',
            'https://shop.nashkraj.ua/kovel/product/22962-vino-igr-artemivske-0-75-l-b-bryut-13-5',
            'https://fozzyshop.ua/shampanskoe/1499-shampanskoe-azshv-artemovskoe-beloe-bryut-4820003353363.html'
        ])

    def artemivske_coll_napivsuhe_parser(self):
        ''' Парсер для шампанського Артемівське коллекційне напівсухе'''
        return self.prices_parsing([
            'https://fozzyshop.ua/shampanskoe/1492-shampanskoe-azshv-artemovskoe-kollekc-polusukhoe-4820003353424.html'
        ])

    def artemivske_chervone_napivsolodke_parser(self):
        ''' Парсер для шампанського Артемівське червоне напівсолодке'''
        return self.prices_parsing([
            'https://varus.ua/vino-igriste-artemivske-chervone-napivsolodke-0-75-l',
            'https://auchan.ua/ua/vino-igristoe-artemovskoe-krasnoe-polusladkoe-10-13-5-750-ml-957784/',
            'https://novus.online/product/vino-igriste-azsv-cervone-napivsolodke-135-075l',
            'https://fozzyshop.ua/shampanskoe/1493-shampanskoe-azshv-artemovskoe-krasnoe-polusladkoe-4820003350041.html'
        ])

    def bagrationi_bile_napivsolodke_parser(self):
        ''' Парсер для шампанського Bagrationi біле напівсолодке'''
        return self.prices_parsing([
            'https://varus.ua/vino-igriste-bagrationi-classic-bile-napivsolodke-0-75-l',
            'https://shop.silpo.ua/product/vyno-igryste-bagrationi-1882-bile-napivsolodke-217114',
            'https://novus.online/product/vino-igriste-bagrationi-semi-sweet-white-12-075l',
            'https://metro.zakaz.ua/uk/products/vino-igriste-bagrationi-750ml-gruziia--04860069010107/',
            'https://fozzyshop.ua/shampanskoe/1503-shampanskoe-bagrationi-beloe-polusladkoe-4860069010107.html'
        ])

    def bagrationi_bile_napivsuhe_parser(self):
        ''' Парсер для шампанського Bagrationi біле напівсухе'''
        return self.prices_parsing([
            'https://varus.ua/vino-igriste-bagrationi-classic-bile-napivsuhe-0-75-l',
            'https://shop.silpo.ua/product/vyno-igryste-bagrationi-1882-bile-napivsukhe-217117',
            'https://novus.online/product/vino-igriste-bagrationi-semi-dry-white-12-075l',
            'https://metro.zakaz.ua/uk/products/vino-igriste-bagrationi-750ml-gruziia--04860069010053/',
            'https://fozzyshop.ua/shampanskoe/1504-shampanskoe-bagrationi-beloe-polusukhoe-4860069010053.html'
        ])

    def bagrationi_bile_brut_parser(self):
        ''' Парсер для шампанського Bagrationi біле брют'''
        return self.prices_parsing([
            'https://varus.ua/vino-igriste-bagrationi-brut-bile-bryut-0-75-l',
            'https://shop.silpo.ua/product/vyno-igryste-bagrationi-1882-bile-briut-217101',
            'https://novus.online/product/vino-igriste-bagrationi-brut-white-12-075l',
            'https://metro.zakaz.ua/uk/products/vino-igriste-bagrationi-750ml-gruziia--04860069010084/',
            'https://fozzyshop.ua/shampanskoe/1502-shampanskoe-bagrationi-beloe-bryut-4860069010084.html'
        ])

    def bagrationi_roj_napivsolod_parser(self):
        ''' Парсер для шампанського Bagrationi рожеве напівсолодке'''
        return self.prices_parsing([
            'https://fozzyshop.ua/shampanskoe/1506-shampanskoe-bagrationi-polusladkoe-rozovoe-4860069010138.html'
        ])

    def bagrationi_gold_napivsolodke_parser(self):
        ''' Парсер для шампанського Bagrationi Gold напівсолодке'''
        return self.prices_parsing([
            'https://fozzyshop.ua/shampanskoe/1505-shampanskoe-bagrationi-gold-polusladkoe-beloe-4860069010022.html'
        ])

    def bolgrad_bile_brut_parser(self):
        ''' Парсер для шампанського Bolgrad біле брют'''
        return self.prices_parsing([
            'https://varus.ua/vino-bolgrad-brut-classic-igristoe-11-5-0-75-l',
            'https://shop.silpo.ua/product/shampanske-bolgrad-classic-bile-briut-556640',
            'https://fozzyshop.ua/shampanskoe/1470-shampanskoe-bolgrad-beloe-bryut-4820013031671.html'
        ])

    def bolgrad_bile_napivsolodke_parser(self):
        ''' Парсер для шампанського Bolgrad біле напівсолодке'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/sampanske-ukraini-075l-bolgrad-bile-napivsolodke-105-125',
            'https://varus.ua/vino-igriste-bolgrad-classic-bile-napivsolodke-0-75-l',
            'https://shop.silpo.ua/product/shampanske-bolgrad-classic-bile-napivsolodke-556637',
            'https://fozzyshop.ua/shampanskoe/1471-shampanskoe-bolgrad-beloe-polusladkoe-4820013031688.html'
        ])

    def bolgrad_nektar_bile_solodke_parser(self):
        ''' Парсер для шампанського Bolgrad Нектар біле солодке'''
        return self.prices_parsing([
            'https://varus.ua/vino-igriste-bolgrad-nectar-bile-solodke-0-75-l',
            'https://fozzyshop.ua/shampanskoe/1469-shampanskoe-bolgrad-nectar-beloe-sladkoe-4820013031695.html'
        ])

    def fran_bulvar_bile_napivsuhe_parser(self):
        ''' Парсер для шампанського Французький Бульвар Біле напівсухе'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/vino-igriste-frantsuzkii-bulvar-750ml-ukrayina--04820004382157/',
            'https://shop.silpo.ua/product/shampanske-frantsuzkyi-bulvar-bile-napivsukhe-329835',
            'https://metro.zakaz.ua/uk/products/vino-igriste-frantsuzkii-bulvar-750ml-ukrayina--04820004382157/',
            'https://fozzyshop.ua/shampanskoe/1585-shampanskoe-francuzskij-bulvar-beloe-polusukhoe-4820004382157.html'
        ])

    def fran_bulvar_bile_brut_parser(self):
        ''' Парсер для шампанського Французький Бульвар Біле брют'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/igriste-shampanske-frantsuzkii-bulvar-750ml-ukrayina--04820004382133/',
            'https://shop.silpo.ua/product/shampanske-frantsuzkyi-bulvar-bile-briut-329833',
            'https://metro.zakaz.ua/uk/products/igriste-shampanske-frantsuzkii-bulvar-750ml-ukrayina--04820004382133/',
            'https://fozzyshop.ua/shampanskoe/1584-shampanskoe-francuzskij-bulvar-beloe-bryut-4820004382133.html'
        ])

    def fran_bulvar_bile_napivsolod_parser(self):
        ''' Парсер для шампанського Французький Бульвар Біле напівсолодке'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/igriste-shampanske-frantsuzkii-bulvar-750ml-ukrayina--04820004383345/',
            'https://shop.silpo.ua/product/vyno-igryste-frantsuzkyi-bulvar-bile-napivsolodke-7362',
            'https://metro.zakaz.ua/uk/products/igriste-shampanske-frantsuzkii-bulvar-750ml-ukrayina--04820004383345/',
            'https://fozzyshop.ua/shampanskoe/1593-shampanskoe-francuzskij-bulvar-beloe-polusladkoe-4820004380283.html'
        ])

    def stariy_kaheti_3_parser(self):
        ''' Парсер для коньяк Старий Кахеті 3 зірки'''
        return self.prices_parsing([
            'https://varus.ua/konyak-staryy-kaheti-3-zvezdy-0-5-l',
            'https://novus.online/product/konak-starij-kaheti-3-40-05l',
            'https://metro.zakaz.ua/uk/products/koniak-starii-kakheti-500ml-gruziia--04860013080514/',
            'https://fozzyshop.ua/konyak-brendi-armanyak/2397-konyak-staryj-kakheti-3-zvezdy-4860013080514.html'
        ])

    def stariy_kaheti_5_parser(self):
        ''' Парсер для коньяк Старий Кахеті 5 зірки'''
        return self.prices_parsing([
            'https://varus.ua/konyak-staryy-kaheti-5-zvezd-0-5-l',
            'https://novus.online/product/konak-starij-kaheti-5-40-05l',
            'https://metro.zakaz.ua/uk/products/koniak-starii-kakheti-500ml-gruziia--04860013080538/',
            'https://fozzyshop.ua/konyak-brendi-armanyak/2401-konyak-staryj-kakheti-5-zvezdy-4860013080538.html'
        ])

    def stariy_kaheti_4_parser(self):
        ''' Парсер для коньяк Старий Кахеті 4 зірки'''
        return self.prices_parsing([
            'https://varus.ua/konyak-staryy-kaheti-4-zvezdy-0-5-l',
            'https://novus.online/product/konak-starij-kaheti-4-40-05l',
            'https://metro.zakaz.ua/uk/products/koniak-starii-kakheti-500ml-gruziia--04860013080521/',
            'https://fozzyshop.ua/konyak-brendi-armanyak/2399-konyak-staryj-kakheti-4-zvezdy-4860013080521.html'
        ])

    def koblevo_extra_old_8_parser(self):
        ''' Парсер для бренді Коблево Extra Old 8 років'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/brendi-koblevo-500ml-ukrayina--04820182221095/',
            'https://novus.online/product/brendi-koblevo-rezerv-ekstra-old-marochnyy-8-rokiv-40-05l',
            'https://fozzyshop.ua/konyak-brendi-armanyak/93442-brendi-koblevo-reserve-extra-old-8-let-4820182221095.html'
        ])

    def shabo_vsop_5_parser(self):
        ''' Парсер для коньяк Shabo VSOP 5*'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/konak-05l-sabo-vsop-5-zirok-40',
            'https://eko.zakaz.ua/uk/products/koniak-shabo-500ml-ukrayina--04820070400809/',
            'https://varus.ua/konyak-shabo-vsop-5-zvezd-0-5-l',
            'https://shop.silpo.ua/product/koniak-shabo-vsop-5-zirok-352655',
            'https://metro.zakaz.ua/uk/products/koniak-shabo-500ml-ukrayina--04820070400809/',
            'https://shop.nashkraj.ua/kovel/product/53042-konyak-shabo-0-5l-5-vsop-40',
            'https://fozzyshop.ua/konyak-brendi-armanyak/2160-konyak-shabo-vsop-5-zvezd-4820070400809.html'
        ])

    def shabo_vs_3_parser(self):
        ''' Парсер для коньяк Shabo VS 3*'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/konak-05l-sabo-vs-3-zirki-40',
            'https://eko.zakaz.ua/uk/products/koniak-shabo-500ml-ukrayina--04820070400816/',
            'https://varus.ua/konyak-shabo-vs-3-zvezdy-0-5-l',
            'https://shop.silpo.ua/product/koniak-shabo-vs-3-zirky-352656',
            'https://novus.online/product/konak-sabo-vsordinarnij-40-05l',
            'https://metro.zakaz.ua/uk/products/koniak-shabo-500ml-ukrayina--04820070400816/',
            'https://shop.nashkraj.ua/kovel/product/53037-konyak-shabo-0-5l-3-vs-40',
            'https://fozzyshop.ua/konyak-brendi-armanyak/2427-konyak-shabo-vs-3-zvezdy-4820070400816.html'
        ])

    def shabo_1788_4_parser(self):
        ''' Парсер для коньяк Shabo 1788 4*'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/konak-05l-sabo-1788-4-zirki-40',
            'https://eko.zakaz.ua/uk/products/koniak-shabo-500ml-ukrayina--04820070400793/',
            'https://varus.ua/konyak-shabo-1788-4-zvezdy-0-5-l',
            'https://shop.silpo.ua/product/koniak-shabo-1788-4-zirky-352657',
            'https://novus.online/product/konak-sabo-1788-ordspecnajm40-05l',
            'https://metro.zakaz.ua/uk/products/koniak-shabo-500ml-ukrayina--04820070400793/',
            'https://fozzyshop.ua/konyak-brendi-armanyak/2159-konyak-shabo-1788-4-zvezdy-4820070400793.html'
        ])

    def shabo_1788_reserv_parser(self):
        ''' Парсер для коньяк Shabo 1788 reserv'''
        return self.prices_parsing([
            'https://fozzyshop.ua/konyak-brendi-armanyak/36521-konyak-shabo-rezerv-1788-4820070404364.html'
        ])

    def shabo_vs_reserv_parser(self):
        ''' Парсер для коньяк Shabo VS reserv'''
        return self.prices_parsing([
            'https://varus.ua/konyak-shabo-reserve-vs-3-zvezdy-0-5-l',
            'https://shop.silpo.ua/product/koniak-shabo-rezerv-v-s-674749',
            'https://novus.online/product/konak-ukraini-sabo-rezerv-vs-40-05l',
            'https://metro.zakaz.ua/uk/products/koniak-shabo-500ml-ukrayina--04820070404340/',
            'https://fozzyshop.ua/konyak-brendi-armanyak/36520-konyak-shabo-rezerv-vs-4820070404340.html'
        ])

    def shabo_vsop_reserv_parser(self):
        ''' Парсер для коньяк Shabo VSOP reserv'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/konak-025-l-shabo-reserve-5-zirok-40',
            'https://eko.zakaz.ua/uk/products/koniak-shabo-500ml-ukrayina--04820070404388/',
            'https://shop.silpo.ua/product/koniak-shabo-rezerv-v-s-o-p-674751',
            'https://novus.online/product/konak-ukraini-sabo-rezerv-vsop-40-05l',
            'https://metro.zakaz.ua/uk/products/koniak-shabo-500ml-ukrayina--04820070404388/',
            'https://fozzyshop.ua/konyak-brendi-armanyak/36522-konyak-shabo-rezerv-vsop-4820070404388.html'
        ])

    def aznauri_3_parser(self):
        ''' Парсер для коньяк Aznauri 3*'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/konak-05-l-aznauri-cuperior-tri-zirocki-40-ukraina',
            'https://eko.zakaz.ua/uk/products/koniak-aznauri-500ml--04820189290094/',
            'https://varus.ua/konyak-aznauri-3-zvezdy-0-5-l',
            'https://shop.silpo.ua/product/koniak-aznauri-3-zirky-690230',
            'https://auchan.ua/ua/kon-jak-aznauri-3-goda-vyderzhki-40-500-ml-893135/',
            'https://novus.online/product/konak-40-05l-ukraini-ordinarnij-aznauri-3-roki-pl',
            'https://metro.zakaz.ua/uk/products/koniak-aznauri-500ml--04820189290094/',
            'https://shop.nashkraj.ua/kovel/product/230802-konyak-aznauri-0-5l-3-40',
            'https://fozzyshop.ua/konyak-brendi-armanyak/42983-konyak-ukrainy-aznauri-05-3-goda-4820189290094.html'
        ])

    def aznauri_5_parser(self):
        ''' Парсер для коньяк Aznauri 5*'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/konak-05-l-aznauri-cuperior-pat-zirocok-40-ukraina',
            'https://eko.zakaz.ua/uk/products/koniak-aznauri-500ml--04820189290117/',
            'https://varus.ua/konyak-aznauri-5-zvezd-0-5-l',
            'https://shop.silpo.ua/product/koniak-aznauri-5-zirok-690231',
            'https://auchan.ua/ua/kon-jak-aznauri-5-let-vyderzhki-40-500-ml-893114/',
            'https://novus.online/product/konak-40-05l-ukraini-ordinarnij-aznauri-5-roki-pl',
            'https://shop.nashkraj.ua/kovel/product/230377-konyak-aznauri-0-5l-5-40',
            'https://fozzyshop.ua/konyak-brendi-armanyak/42985-konyak-ukrainy-aznauri-05-5-let-4820189290117.html'
        ])

    def aznauri_4_parser(self):
        ''' Парсер для коньяк Aznauri 4*'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/koniak-aznauri-500ml--04820189290100/',
            'https://auchan.ua/ua/kon-jak-aznauri-4-goda-vyderzhki-40-500-ml-893128/',
            'https://novus.online/product/konak-40-05l-ukraini-ordinarnij-aznauri-4-roki-pl',
            'https://metro.zakaz.ua/uk/products/koniak-aznauri-500ml--04820189290100/',
            'https://fozzyshop.ua/konyak-brendi-armanyak/42984-konyak-ukrainy-aznauri-05-4-goda-4820189290100.html'
        ])

    def aznauri_black_barrel_5_parser(self):
        ''' Парсер для коньяк Aznauri Black Barrel 5*'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/konak-05-l-aznauri-black-barrel-5-rokiv-40-ob-skbut',
            'https://eko.zakaz.ua/uk/products/koniak-aznauri-500ml-ukrayina--04820189292258/',
            'https://varus.ua/konyak-aznauri-black-barrel-5-zvezd-0-5-l',
            'https://shop.silpo.ua/product/koniak-aznauri-black-barrel-5-rokiv-834517',
            'https://auchan.ua/ua/kon-jak-aznauri-black-barrel-5-let-vyderzhki-40-500-ml-893121/',
            'https://novus.online/product/konyak-aznauri-black-barrel-5-rokiv-40-05l',
            'https://fozzyshop.ua/konyak-brendi-armanyak/83144-konyak-aznauri-black-barrel-5-let-4820189292258.html'
        ])

    def adjari_3_parser(self):
        ''' Парсер для коньяк Adjari 3*'''
        return self.prices_parsing([
            'https://varus.ua/konyak-adjari-3-zvezdy-0-5-l',
            'https://shop.silpo.ua/product/koniak-adjari-3-zirky-711132',
            'https://auchan.ua/ua/brendi-adjari-3-40-0-5-l-1167009/',
            'https://metro.zakaz.ua/uk/products/koniak-adzhari-500ml-ukrayina--04820235321406/',
            'https://fozzyshop.ua/konyak-brendi-armanyak/45574-konyak-adjari-3-4820183101631.html'
        ])

    def adjari_5_parser(self):
        ''' Парсер для коньяк Adjari 5*'''
        return self.prices_parsing([
            'https://varus.ua/konyak-adjari-5-zvezd-0-5-l',
            'https://shop.silpo.ua/product/koniak-adjari-5-zirok-711133',
            'https://auchan.ua/ua/brendi-adjari-5-40-0-5-l-1167015/',
            'https://novus.online/product/konyak-adjari-5-40-05l',
            'https://metro.zakaz.ua/uk/products/koniak-adzhari-500ml-ukrayina--04820235321482/',
            'https://fozzyshop.ua/konyak-brendi-armanyak/45575-konyak-adjari-5-4820183101594.html'
        ])

    def adjari_4_parser(self):
        ''' Парсер для коньяк Adjari 4*'''
        return self.prices_parsing([
            'https://auchan.ua/ua/kon-jak-adjari-kvarteli-4-goda-vyderzhki-40-500-ml-957981/',
            'https://fozzyshop.ua/konyak-brendi-armanyak/73458-konyak-adjari-kvarteli-4-4820183102942.html'
        ])

    def hennesy_vs_parser(self):
        ''' Парсер для коньяк Hennesy VS'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/konak-05l-hennessy-vs-40-u-korobci',
            'https://shop.silpo.ua/product/koniak-hennessy-vs-v-podarunkovii-upakovtsi-591589',
            'https://novus.online/product/konak-hennessy-vs40-05l',
            'https://metro.zakaz.ua/uk/products/koniak-khennessi-500ml-frantsiia--03245990287407/',
            'https://fozzyshop.ua/konyak-brendi-armanyak/17705-konyak-hennessy-vs-v-podarochnoj-upakovke-3245995817111.html'
        ])

    def hennesy_vsop_parser(self):
        ''' Парсер для коньяк Hennesy VSOP'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/koniak-hennessy-vsop-v-podarunkovii-upakovtsi-591591',
            'https://metro.zakaz.ua/uk/products/koniak-khennessi-500ml-frantsiia--03245990018308/',
            'https://fozzyshop.ua/konyak-brendi-armanyak/17707-konyak-hennessy-vsop-v-podarochnoj-upakovke-3245996122511.html'
        ])

    def alexx_gold_vsop_parser(self):
        ''' Парсер для коньяк Alexx Gold VSOP'''
        return self.prices_parsing([
            'https://varus.ua/konyak-alexx-gold-vsop-0-5-l',
            'https://shop.silpo.ua/product/koniak-alexx-gold-vsop-u-tubusi-66504',
            'https://novus.online/product/konak-alexx-gold-40-05l',
            'https://metro.zakaz.ua/uk/products/ukrayina--04823093700437/',
            'https://fozzyshop.ua/konyak-brendi-armanyak/2165-konyak-alexx-gold-vsop-v-tubuse-4820000621182.html'
        ])

    def alexx_silver_vs_parser(self):
        ''' Парсер для коньяк Alexx Silver VS'''
        return self.prices_parsing([
            'https://varus.ua/konyak-alexx-silver-vs-0-5-l',
            'https://shop.silpo.ua/product/koniak-alexx-silver-vs-64225',
            'https://metro.zakaz.ua/uk/products/ukrayina--04823093700352/',
            'https://fozzyshop.ua/konyak-brendi-armanyak/17704-konyak-alexx-silver-vs-4820000621175.html'
        ])

    def ararat_5_parser(self):
        ''' Парсер для коньяк Ararat 5*'''
        return self.prices_parsing([
            'https://varus.ua/konyak-ararat-5-zvezd-0-5-l',
            'https://shop.silpo.ua/product/koniak-ararat-5-zirok-34563',
            'https://auchan.ua/ua/kon-jak-ararat-5-let-40-v-podarochnoj-upakovke-0-5-l-1043692/',
            'https://metro.zakaz.ua/uk/products/koniak-ararat-500ml-virmeniia--04850001000037/',
            'https://fozzyshop.ua/konyak-brendi-armanyak/2277-konyak-ararat-5-4850001001935.html'
        ])

    def ararat_ahtamar_10_parser(self):
        ''' Парсер для коньяк Ararat Ahtamar 10*'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/koniak-ararat-akhtamar-10-rokiv-podarunkova-korobka-1044',
            'https://auchan.ua/ua/brendi-ararat-ahtamar-10-let-vyderzhki-40-v-podarochnoj-upakovke-0-5-l-1077192/',
            'https://fozzyshop.ua/konyak-brendi-armanyak/2263-konyak-ararat-akhtamar-10-let-podarochnaya-korobka-4850001002024.html'
        ])

    def ararat_3_parser(self):
        ''' Парсер для коньяк Ararat 3*'''
        return self.prices_parsing([
            'https://varus.ua/konyak-ararat-3-zvezdy-0-5-l',
            'https://shop.silpo.ua/product/koniak-ararat-3-zirky-1042',
            'https://auchan.ua/ua/brendi-ararat-3-goda-vyderzhki-40-0-5-l-1085762/',
            'https://metro.zakaz.ua/uk/products/koniak-ararat-500ml-virmeniia--04850001000013/',
            'https://shop.nashkraj.ua/kovel/product/23756-brendi-ararat-0-5l-3r-40',
            'https://fozzyshop.ua/konyak-brendi-armanyak/2256-konyak-ararat-3-4850001001904.html'
        ])

    def ararat_nairi_20_parser(self):
        ''' Парсер для коньяк Ararat Nairi 20*'''
        return self.prices_parsing([
            'https://auchan.ua/ua/brendi-ararat-nairi-20-let-vyderzhki-40-v-podarochnoj-upakovke-0-7-l-1077202/',
            'https://fozzyshop.ua/konyak-brendi-armanyak/53163-konyak-nairi-20-let-41-podar-kor-4850001002123.html'
        ])

    def green_day_air_05l_parser(self):
        ''' Парсер для горілка Green Day Air 0.5 л'''
        return self.prices_parsing([
            'https://fozzyshop.ua/vodka/26677-vodka-green-day-air-4820183100429.html'
        ])

    def green_day_ultra_soft_05l_parser(self):
        ''' Парсер для горілка Green Day Ultra Soft 0.5 л'''
        return self.prices_parsing([
            'https://fozzyshop.ua/vodka/45548-vodka-green-day-ultra-soft-40-4820024229937.html'
        ])

    def green_day_organic_life_05l_parser(self):
        ''' Парсер для горілка Green Day Organic Life 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/gorilka-green-day-organic-life-40-0-5-l',
            'https://auchan.ua/ua/vodka-green-day-organic-40-500-ml-1165108/',
            'https://fozzyshop.ua/vodka/26678-vodka-green-day-organic-life-4820073561774.html'
        ])

    def green_day_crystal_05l_parser(self):
        ''' Парсер для горілка Green Day Crystal 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/gorilka-green-day-crystal-40-0-5-l',
            'https://shop.silpo.ua/product/gorilka-green-day-crystal-40-722131',
            'https://auchan.ua/ua/vodka-green-day-crystal-40-500-ml-1165090/',
            'https://metro.zakaz.ua/uk/products/gorilka-grin-dei-500ml-ukrayina--04820024228770/',
            'https://fozzyshop.ua/vodka/45546-vodka-green-day-crystal-40-4820024228770.html'
        ])

    def green_day_05l_parser(self):
        ''' Парсер для горілка Green Day 0.5 л'''
        return self.prices_parsing([
            'https://varus.ua/gorilka-green-day-40-0-5-l',
            'https://shop.silpo.ua/product/gorilka-green-day-536956',
            'https://auchan.ua/ua/vodka-green-day-40-500-ml-1165084/',
            'https://metro.zakaz.ua/uk/products/gorilka-grin-dei-500ml-ukrayina--04820024228763/',
            'https://fozzyshop.ua/vodka/1848-vodka-green-day-4820024228763.html'
        ])

    def medoff_classic_05l_parser(self):
        ''' Парсер для горілка Medoff Classic 0.5 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-medoff-500ml--04820179280470/',
            'https://varus.ua/gorilka-medoff-classic-40-0-5-l',
            'https://shop.silpo.ua/product/gorilka-medoff-klasik-new-253629',
            'https://shop.nashkraj.ua/kovel/product/4732-gorilka-medoff-0-5l-klasik-40',
            'https://fozzyshop.ua/vodka/1855-vodka-medoff-klassik-new-4820179280470.html'
        ])

    def smirnoff_red_05l_parser(self):
        ''' Парсер для горілка Smirnoff Red 0.5 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-smirnoff-500ml-italiia--05410316072014/',
            'https://varus.ua/gorilka-0-5l-40-red-smirnoff-pl',
            'https://shop.silpo.ua/product/gorilka-smirnoff-21-klasychna-49016',
            'https://fozzyshop.ua/vodka/2109-vodka-smirnoff-red-5410316072014.html'
        ])

    def kozacka_rada_classic_05l_parser(self):
        ''' Парсер для горілка Козацька Рада классична 0.5 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/gorilka-05l-kozacka-rada-klasicna-40',
            'https://eko.zakaz.ua/uk/products/gorilka-kozatska-rada-500ml-ukrayina--04820080720386/',
            'https://shop.silpo.ua/product/gorilka-kozatska-rada-klasychna-306954',
            'https://auchan.ua/ua/vodka-kozac-ka-rada-klassicheskaja-40-0-5l-1047919/',
            'https://novus.online/product/gorilka-kozacka-rada-klasicna-40-05l',
            'https://metro.zakaz.ua/uk/products/gorilka-kozatska-rada-500ml-ukrayina--04820080720386/',
            'https://shop.nashkraj.ua/kovel/product/31988-gorilka-kozatska-rada-0-5l-klasichna-40',
            'https://fozzyshop.ua/vodka/1940-vodka-klassicheskaya-kozackaya-rada-4820080720386.html'
        ])

    def kozacka_rada_osobliva_05l_parser(self):
        ''' Парсер для горілка Козацька Рада особлива 0.5 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/gorilka-05-l-kozacka-rada-osobliva-40-ob-skbut',
            'https://eko.zakaz.ua/uk/products/gorilka-kozatska-rada-500ml-ukrayina--04820050031221/',
            'https://varus.ua/gorilka-kozacka-rada-osobliva-40-0-5-l',
            'https://shop.silpo.ua/product/gorilka-kozatska-rada-osoblyva-260',
            'https://novus.online/product/gorilka-kozacka-rada-osobliva-40-05l',
            'https://fozzyshop.ua/vodka/1964-vodka-kozacka-rada-osobaya-4820080720409.html'
        ])

    def zubrowka_bison_grass_05l_parser(self):
        ''' Парсер для горілка Zubrowka Bison Grass 0.5 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/gorilka-05l-bison-grass-tm-zubrowka-375',
            'https://eko.zakaz.ua/uk/products/nastoianka-zubrovka-500ml-polshcha--05900343003674/',
            'https://auchan.ua/ua/nastojka-zubrowka-bison-grass-37-5-500-ml-894079/',
            'https://novus.online/product/gorilka-05l-zubrowka-bison-grass-375',
            'https://metro.zakaz.ua/uk/products/nastoianka-zubrovka-500ml-polshcha--05900343003674/',
            'https://shop.nashkraj.ua/kovel/product/168592-nap-alk-zubrovka-0-5l-grass-37-5',
            'https://fozzyshop.ua/vodka/1896-vodka-zubrowka-5900343003674.html'
        ])

    def zubrowka_biala_05l_parser(self):
        ''' Парсер для горілка Zubrowka Biala 0.5 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/gorilka-05l-biala-tm-zubrowka-40',
            'https://eko.zakaz.ua/uk/products/gorilka-zubrovka-500ml-polshcha--05900343001892/',
            'https://auchan.ua/ua/vodka-zubrowka-biala-40-500-ml-887513/',
            'https://novus.online/product/gorilka-zubrowka-biala-40-05l',
            'https://metro.zakaz.ua/uk/products/gorilka-zubrovka-500ml-polshcha--05900343001892/',
            'https://shop.nashkraj.ua/kovel/product/168591-gorilka-zubrovka-0-5l-byala-40',
            'https://fozzyshop.ua/vodka/1897-vodka-zubrowka-biala-5900343001892.html'
        ])

    def zubrowka_czarna_05l_parser(self):
        ''' Парсер для горілка Zubrowka Czarna 0.5 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-zubrovka-500ml-polshcha--05900343010047/',
            'https://auchan.ua/ua/vodka-zubrowka-czarna-40-500-ml-887534/',
            'https://shop.nashkraj.ua/kovel/product/304719-gorilka-zubrovka-0-5l-chorna-40',
            'https://fozzyshop.ua/vodka/64215-vodka-zubrowka-szarna-5900343010047.html'
        ])

    def vozduh_legka_osobliva_05l_parser(self):
        ''' Парсер для горілка Воздух легка особлива 0.5 л'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/gorilka-vozdukh-legka-osoblyva-652085',
            'https://fozzyshop.ua/vodka/26732-vodka-vozdukh-legkaya-osobaya-4830080728122.html'
        ])

    def vozduh_alpha_05l_parser(self):
        ''' Парсер для горілка Воздух Alpha 0.5 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-vozdukh-500ml--04823098200932/',
            'https://fozzyshop.ua/vodka/57985-vodka-vozdukh-alfa-4823098200932.html'
        ])

    def persha_gildiya_verhovna_05l_parser(self):
        ''' Парсер для горілка Перша Гільдія Верховна 0.5 л'''
        return self.prices_parsing([
            'https://auchan.ua/ua/vodka-persha-gil-dija-verhovnaja-40-500-ml-1022123/',
            'https://novus.online/product/gorilka-persa-gildia-verhovna-40-05l',
            'https://fozzyshop.ua/vodka/2021-vodka-persha-gildiya-verkhovnaya-4820080725893.html'
        ])

    def persha_gildiya_znatna_05l_parser(self):
        ''' Парсер для горілка Перша Гільдія Знатна 0.5 л'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/gorilka-persha-gildiia-znatna-554227',
            'https://auchan.ua/ua/vodka-persha-gil-dija-znatnaja-40-500-ml-1022129/',
            'https://fozzyshop.ua/vodka/2022-vodka-persha-gildiya-znatnaya-4820080725886.html'
        ])

    def persha_gildiya_povajna_05l_parser(self):
        ''' Парсер для горілка Перша Гільдія Поважна 0.5 л'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/gorilka-persha-gildiia-povazhna-554228',
            'https://auchan.ua/ua/vodka-persha-gil-dija-pochtennaja-40-500-ml-1022117/',
            'https://novus.online/product/gorilka-persa-gildia-povazna-40-05l',
            'https://metro.zakaz.ua/uk/products/gorilka-persha-gildiia-500ml-ukrayina--04820080725879/',
            'https://fozzyshop.ua/vodka/2023-vodka-persha-gildiya-povazhna-4820080725879.html'
        ])

    def hlib_dar_classic_05l_parser(self):
        ''' Парсер для горілка Хлібний Дар класична 0.5 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/gorilka-05l-hlibnij-dar-klasicna-40',
            'https://eko.zakaz.ua/uk/products/gorilka-khlibnii-dar-500ml--04810027010922/',
            'https://shop.silpo.ua/product/gorilka-khlibnyi-dar-klasychna-59800',
            'https://auchan.ua/ua/vodka-hlebnyj-dar-klassicheskaja-0-5-l-1074441/',
            'https://metro.zakaz.ua/uk/products/gorilka-khlibnii-dar-500ml-ukrayina--04820080720577/',
            'https://fozzyshop.ua/vodka/2044-vodka-khlibnij-dar-klassicheskaya-4820080725770.html'
        ])

    def hlib_dar_pror_zerno_05l_parser(self):
        ''' Парсер для горілка Хлібний Дар пророщене зерно 0.5 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-khlibnii-dar-500ml-ukrayina--04820080724728/',
            'https://shop.silpo.ua/product/gorilka-khlibnyi-dar-na-proroshchenomu-zerni-467095',
            'https://novus.online/product/gorilka-hlibnij-dar-na-prorosenomu-zerni-40-05l',
            'https://fozzyshop.ua/vodka/2045-vodka-khlibnij-dar-na-proroshhennom-zerne-4820080725831.html'
        ])

    def hlib_dar_jitnya_05l_parser(self):
        ''' Парсер для горілка Хлібний Дар житня 0.5 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-khlibnii-dar-500ml-ukrayina--04820080721529/',
            'https://shop.silpo.ua/product/gorilka-khlibnyi-dar-zhytnia-liuks-73486',
            'https://fozzyshop.ua/vodka/2049-vodka-khlibnij-dar-rzhanaya-4820050030422.html'
        ])

    def hlib_dar_pshenichna_05l_parser(self):
        ''' Парсер для горілка Хлібний Дар пшенична 0.5 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-khlibnii-dar-500ml-ukrayina--04810027011028/',
            'https://shop.silpo.ua/product/gorilka-hlibny-dar-pshenychna-83656',
            'https://novus.online/product/gorilka-hlibnij-dar-psenicna-40-05l',
            'https://fozzyshop.ua/vodka/2047-vodka-khlibnij-dar-pshenichnaya-4820050030415.html'
        ])

    def green_day_organic_life_07l_parser(self):
        ''' Парсер для горілка Green Day Organic Life 0.7 л'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/gorilka-green-day-original-life-569977',
            'https://auchan.ua/ua/vodka-green-day-organic-40-700-ml-1165114/',
            'https://fozzyshop.ua/vodka/26679-vodka-green-day-organic-life-4820073561781.html'
        ])

    def green_day_07l_parser(self):
        ''' Парсер для горілка Green Day 0.7 л'''
        return self.prices_parsing([
            'https://varus.ua/gorilka-green-day-40-0-7-l',
            'https://shop.silpo.ua/product/gorilka-green-day-536958',
            'https://auchan.ua/ua/vodka-green-day-40-700-ml-1165096/',
            'https://fozzyshop.ua/vodka/1872-vodka-green-day-4820024228787.html'
        ])

    def green_day_ultra_soft_07l_parser(self):
        ''' Парсер для горілка Green Day Ultra Soft 0.7 л'''
        return self.prices_parsing([
            'https://fozzyshop.ua/vodka/45549-vodka-green-day-ultra-soft-40-4820024229951.html'
        ])

    def green_day_air_07l_parser(self):
        ''' Парсер для горілка Green Day Air 0.7 л'''
        return self.prices_parsing([
            'https://fozzyshop.ua/vodka/23818-vodka-green-day-air-4820183100436.html'
        ])

    def green_day_crystal_07l_parser(self):
        ''' Парсер для горілка Green Day Crystal 0.7 л'''
        return self.prices_parsing([
            'https://varus.ua/gorilka-green-day-crystal-40-0-7-l',
            'https://shop.silpo.ua/product/gorilka-green-day-crystal-40-722132',
            'https://auchan.ua/ua/vodka-green-day-crystal-40-700-ml-1165102/',
            'https://novus.online/product/horilka-green-day-kristal-40-07l',
            'https://fozzyshop.ua/vodka/45547-vodka-green-day-crystal-40-4820024228794.html'
        ])

    def medoff_classic_07l_parser(self):
        ''' Парсер для горілка Medoff Classic 0.7 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-medoff-700ml--04820179280487/',
            'https://varus.ua/gorilka-medoff-classic-40-0-7-l',
            'https://shop.silpo.ua/product/gorilka-medoff-klasik-166568',
            'https://auchan.ua/ua/vodka-medoff-klassicheskaja-premium-40-0-7-l-1249933/',
            'https://shop.nashkraj.ua/kovel/product/20336-gorilka-medoff-0-7l-klasik-40',
            'https://fozzyshop.ua/vodka/1874-vodka-medoff-klassik-4820179280487.html'
        ])

    def nemiroff_delikat_myaka_07l_parser(self):
        ''' Парсер для горілка Nemiroff Делікат м'яка 0.7 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-nemiroff-700ml-ukrayina--04820181420444/',
            'https://varus.ua/gorilka-nemiroff-delikat-40-0-7-l',
            'https://shop.silpo.ua/product/gorilka-nemiroff-delikat-m-iaka-413766',
            'https://novus.online/product/gorilka-nemiroff-delikat-40-stof-07l',
            'https://metro.zakaz.ua/uk/products/gorilka-nemiroff-700ml-ukrayina--04607805950101/',
            'https://shop.nashkraj.ua/kovel/product/142667-gorilka-nemiroff-0-7l-delikat-shtof-40',
            'https://fozzyshop.ua/vodka/23822-vodka-nemiroff-delikat-myagkaya-4820181420444.html'
        ])

    def nemiroff_osob_shtof_07l_parser(self):
        ''' Парсер для горілка Nemiroff Особлива Штоф 0.7 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/gorilka-07l-nemiroff-osobliva-stof-40',
            'https://shop.silpo.ua/product/gorilka-nemiroff-osoblyva-shtof-36752',
            'https://metro.zakaz.ua/uk/products/gorilka-nemiroff-700ml-ukrayina--04607805950057/',
            'https://fozzyshop.ua/vodka/26692-vodka-nemiroff-osobaya-shtof-4820181420628.html'
        ])

    def nemiroff_deluxe_07l_parser(self):
        ''' Парсер для горілка Nemiroff Deluxe 0.7 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/gorilka-07l-nemiroff-de-luxe-osobliva-40',
            'https://eko.zakaz.ua/uk/products/gorilka-nemiroff-700ml-ukrayina--04820181424916/',
            'https://shop.silpo.ua/product/gorilka-nemiroff-de-luxe-765323',
            'https://auchan.ua/ua/vodka-nemiroff-de-luxe-700-ml-958924/',
            'https://novus.online/product/gorilka-osobliva-nemiroff-de-luks-40-07l',
            'https://metro.zakaz.ua/uk/products/gorilka-nemiroff-700ml-ukrayina--04820181424916/',
            'https://fozzyshop.ua/vodka/64170-vodka-nemiroff-de-lyuks-4820181424916.html'
        ])

    def nemiroff_lex_07l_parser(self):
        ''' Парсер для горілка Nemiroff Lex 0.7 л'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/gorilka-nemiroff-lex-85089',
            'https://novus.online/product/gorilka-nemiroff-lexx-40-07l',
            'https://metro.zakaz.ua/uk/products/gorilka-nemiroff-700ml--04820181420567/',
            'https://fozzyshop.ua/vodka/16326-vodka-nemiroff-lex-4820181420567.html'
        ])

    def zubrowka_bison_grass_07l_parser(self):
        ''' Парсер для горілка Zubrowka Bison Grass 0.7 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/gorilka-07l-bison-grass-tm-zubrowka-375',
            'https://eko.zakaz.ua/uk/products/nastoianka-zubrovka-700ml-polshcha--05900343003698/',
            'https://auchan.ua/ua/nastojka-zubrowka-bison-grass-37-5-700-ml-894086/',
            'https://novus.online/product/gorilka-07l-zubrowka-bison-grass-375',
            'https://shop.nashkraj.ua/kovel/product/168594-nastoyanka-zubrovka-0-7l-37-5',
            'https://fozzyshop.ua/vodka/1919-vodka-zubrowka-5900343003698.html'
        ])

    def zubrowka_czarna_07l_parser(self):
        ''' Парсер для горілка Zubrowka Czarna 0.7 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-zubrovka-700ml-polshcha--05900343010054/',
            'https://auchan.ua/ua/vodka-zubrowka-czarna-40-700-ml-887577/',
            'https://shop.nashkraj.ua/kovel/product/319418-gorilka-zubrovka-0-7l-chorna-40',
            'https://fozzyshop.ua/vodka/60398-vodka-zubrowka-szarna-5900343010054.html'
        ])

    def hetman_07l_parser(self):
        ''' Парсер для горілка Гетьман 0.7 л'''
        return self.prices_parsing([
            'https://varus.ua/gorilka-getman-40-0-7-l',
            'https://shop.silpo.ua/product/gorilka-getman-969',
            'https://novus.online/product/gorilka-getman-40-07l',
            'https://fozzyshop.ua/vodka/84104-vodka-getman-4823001100113.html'
        ])

    def kozacka_rada_classic_07l_parser(self):
        ''' Парсер для горілка Козацька Рада Классік 0.7 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/gorilka-07l-kozacka-rada-klasicna-40',
            'https://eko.zakaz.ua/uk/products/gorilka-kozatska-rada-700ml-ukrayina--04820080726838/',
            'https://shop.silpo.ua/product/gorilka-kozatska-rada-klasychna-590750',
            'https://auchan.ua/ua/vodka-hlibnij-dar-klassicheskaja-40-700-ml-1022183/',
            'https://novus.online/product/gorilka-07l-40-kozacka-rada-klasicna',
            'https://fozzyshop.ua/vodka/16346-vodka-kozacka-rada-klassicheskaya-4820080726838.html'
        ])

    def kozacka_rada_premium_07l_parser(self):
        ''' Парсер для горілка Козацька Рада Преміум 0.7 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-kozatska-rada-700ml-ukrayina--04820080728443/',
            'https://auchan.ua/ua/vodka-kozac-ka-rada-premium-oak-carbon-filtration-40-700-ml-1022177/',
            'https://fozzyshop.ua/vodka/36597-vodka-kozacka-rada-premium-4820080728443.html'
        ])

    def kozacka_rada_osobliva_07l_parser(self):
        ''' Парсер для горілка Козацька Рада Особлива 0.7 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-kozatska-rada-700ml-ukrayina--04820080726852/',
            'https://varus.ua/gorilka-kozacka-rada-osobliva-40-0-7-l',
            'https://auchan.ua/ua/vodka-kozac-ka-rada-osobennaja-40-700-ml-1022171/',
            'https://novus.online/product/gorilka-07l-40-osobliva-kozacka-rada-osobliva',
            'https://fozzyshop.ua/vodka/16347-vodka-kozacka-rada-osobaya-4820080726852.html'
        ])

    def persha_gildiya_povajna_07l_parser(self):
        ''' Парсер для горілка Перша Гільдія Поважна 0.7 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-persha-gildiia-700ml-ukrayina--04820080725909/',
            'https://shop.silpo.ua/product/gorilka-persha-gildiia-povazhna-551051',
            'https://auchan.ua/ua/vodka-persha-gil-dija-pochtennaja-40-700-ml-1022147/',
            'https://fozzyshop.ua/vodka/1993-vodka-persha-gildiyapovazhna-4820080725909.html'
        ])

    def persha_gildiya_verhovna_07l_parser(self):
        ''' Парсер для горілка Перша Гільдія Верховна 0.7 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-persha-gildiia-700ml-ukrayina--04820080725855/',
            'https://shop.silpo.ua/product/gorilka-persha-gildiia-verkhovna-551047',
            'https://auchan.ua/ua/vodka-persha-gil-dija-verhovnaja-40-700-ml-1022135/',
            'https://novus.online/product/gorilka-persa-gildia-verhovna-40-07l',
            'https://fozzyshop.ua/vodka/1990-vodka-persha-gildiya-verkhovnaya-4820080725855.html'
        ])

    def persha_gildiya_znatna_07l_parser(self):
        ''' Парсер для горілка Перша Гільдія Знатна 0.7 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-persha-gildiia-700ml-ukrayina--04820080725862/',
            'https://shop.silpo.ua/product/gorilka-persha-gildiia-znatna-551049',
            'https://auchan.ua/ua/vodka-persha-gil-dija-znatnaja-40-700-ml-1022141/',
            'https://fozzyshop.ua/vodka/1992-vodka-persha-gildiya-znatnaya-4820080725862.html'
        ])

    def hlib_dar_classic_07l_parser(self):
        ''' Парсер для горілка Хлібний Дар Класична 0.7 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/gorilka-07l-hlibnij-dar-klasicna-40',
            'https://eko.zakaz.ua/uk/products/gorilka-khlibnii-dar-700ml-ukrayina--04820080720584/',
            'https://shop.silpo.ua/product/gorilka-khlibnyi-dar-klasychna-93352',
            'https://auchan.ua/ua/vodka-hlebnyj-dar-klassicheskaja-40-0-7-l-1075537/',
            'https://novus.online/product/gorilka-hlibnij-dar-klasicna-40-07l',
            'https://metro.zakaz.ua/uk/products/gorilka-khlibnii-dar-700ml-ukrayina--04820080720584/',
            'https://shop.nashkraj.ua/kovel/product/5001-gorilka-khlibniy-dar-0-7l-klasichna-40',
            'https://fozzyshop.ua/vodka/2064-vodka-khlibnij-dar-klassicheskaya-4820080725787.html'
        ])

    def medoff_classic_1l_parser(self):
        ''' Парсер для горілка Medoff Классик 1 л'''
        return self.prices_parsing([
            'https://shop.nashkraj.ua/kovel/product/20342-gorilka-medoff-1l-klasik-40',
            'https://fozzyshop.ua/vodka/1875-vodka-medoff-klassik-4820179280494.html'
        ])

    def nemiroff_shtof_1l_parser(self):
        ''' Парсер для горілка Nemiroff Штоф 1 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/gorilka-1l-nemiroff-osobliva-stof-40',
            'https://shop.silpo.ua/product/gorilka-nemiroff-osoblyva-shtof-16699',
            'https://shop.nashkraj.ua/kovel/product/4860-gorilka-nemiroff-1l-osobliva-shtof-40',
            'https://fozzyshop.ua/vodka/16330-vodka-nemiroff-osobaya-shtof-4820181420635.html'
        ])

    def nemiroff_delicat_1l_parser(self):
        ''' Парсер для горілка Nemiroff Делікат 1 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-nemiroff-1000ml--04820181420451/',
            'https://varus.ua/gorilka-nemiroff-delikat-40-1-l',
            'https://shop.silpo.ua/product/gorilka-nemiroff-delikat-m-iaka-445401',
            'https://auchan.ua/ua/vodka-nemiroff-deliat-40-1l-1047308/',
            'https://novus.online/product/horilka-nemiroff-shtof-delikat-myaka-40-1l',
            'https://fozzyshop.ua/vodka/16325-vodka-nemiroff-delikat-myagkaya-4820181420451.html'
        ])

    def zubrowka_bison_grass_1l_parser(self):
        ''' Парсер для горілка Zubrowka Bison Grass 1 л'''
        return self.prices_parsing([
            'https://varus.ua/nastoyanka-zubrovka-1l',
            'https://novus.online/product/gorilka-1l-zubrowka-bison-grass-375',
            'https://shop.nashkraj.ua/kovel/product/307052-gorilka-zubrovka-1l-bison-grass-37-5',
            'https://fozzyshop.ua/vodka/1920-vodka-zubrowka-5900343003711.html'
        ])

    def zubrowka_biala_1l_parser(self):
        ''' Парсер для горілка Zubrowka Biala 1 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-zubrovka-1000ml-polshcha--05900343001939/',
            'https://varus.ua/gorilka-byala-zubrivka-1l',
            'https://fozzyshop.ua/vodka/1922-vodka-zubrowka-biala-5900343001939.html'
        ])

    def hetman_1l_parser(self):
        ''' Парсер для горілка Гетьман 1 л'''
        return self.prices_parsing([
            'https://varus.ua/gorilka-getman-40-0-5-l',
            'https://shop.silpo.ua/product/gorilka-getman-854174',
            'https://fozzyshop.ua/vodka/90806-vodka-getman-4820050233816.html'
        ])

    def kozacka_rada_osobliva_1l_parser(self):
        ''' Парсер для горілка Козацька Рада Особлива 1 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-kozatska-rada-1000ml-ukrayina--04820080724087/',
            'https://varus.ua/gorilka-kozacka-rada-osobliva-1-l',
            'https://auchan.ua/ua/vodka-kozac-ka-rada-osobaja-40-1-l-1165060/',
            'https://novus.online/product/gorilka-kozacka-rada-osobliva-40-1l',
            'https://fozzyshop.ua/vodka/1944-vodka-kozacka-rada-osobaya-4820080724087.html'
        ])

    def kozacka_rada_classic_1l_parser(self):
        ''' Парсер для горілка Козацька Рада Класична 1 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/gorilka-1l-kozacka-rada-40',
            'https://eko.zakaz.ua/uk/products/gorilka-kozatska-rada-1000ml-ukrayina--04820080724063/',
            'https://varus.ua/gorilka-kozacka-rada-klasichna-40-1-l',
            'https://shop.silpo.ua/product/gorilka-kozatska-rada-klasychna-436336',
            'https://auchan.ua/ua/vodka-kozac-ka-rada-klassicheskaja-40-1l-1047907/',
            'https://novus.online/product/gorilka-kozacka-rada-klasicna-40-1l',
            'https://fozzyshop.ua/vodka/1973-vodka-kozacka-rada-klassicheskaya-4820080724063.html'
        ])

    def hlib_dar_classic_1l_parser(self):
        ''' Парсер для горілка Хлібний Дар Класична 1 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/gorilka-khlibnii-dar-1000ml-ukrayina--04820080722045/',
            'https://varus.ua/gorilka-hlibniy-dar-klasichna-40-1-l',
            'https://shop.silpo.ua/product/gorilka-khlibnyi-dar-klasychna-337180',
            'https://novus.online/product/gorilka-hlibnij-dar-klasicna-40-1l',
            'https://fozzyshop.ua/vodka/2066-vodka-khlibnij-dar-klassicheskaya-4820080722045.html'
        ])

    def svinne_rebro_parser(self):
        ''' Парсер для свинне ребро'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/rebertsia--ekomarket00000000530055/',
            'https://varus.ua/rebro-svinoe-vesovoe',
            'https://shop.silpo.ua/product/svyniache-rebro-fermerske-757772',
            'https://novus.online/product/rebra-svinni-z-masom-oholodzeni-vag-virobnictvo',
            'https://metro.zakaz.ua/uk/products/rebertsia-tsemiaco-ukrayina--metro28864400000000/',
            'https://shop.nashkraj.ua/kovel/product/110613-svinina-okholodzhena-rebra-myasni',
            'https://fozzyshop.ua/svinina/11248-svinoe-rebro-2732649.html'
        ])

    def salo_parser(self):
        ''' Парсер для сало'''
        return self.prices_parsing([
            'https://varus.ua/svinyache-salo-domashne-tovste-nf-oholvu',
            'https://shop.silpo.ua/product/svyniache-salo-fermerske-767650',
            'https://novus.online/product/salo-svynyache-fermerske',
            'https://shop.nashkraj.ua/kovel/product/9563-svinina-okholodzhena-salo-z-shkiroyu-1kat',
            'https://fozzyshop.ua/svinina/100150-svinoe-salo-fermerskoe-2781506.html'
        ])

    def svinna_gomilka_parser(self):
        ''' Парсер для свинна гомілка'''
        return self.prices_parsing([
            'https://varus.ua/rulka-z-domashnoi-svinini-n-f-ohol-vag',
            'https://metro.zakaz.ua/uk/products/goliashka--metro28835600000000/',
            'https://fozzyshop.ua/svinina/11238-svinaya-golyashka-2732679.html'
        ])

    def svin_pechinka_parser(self):
        ''' Парсер для свинна печінка'''
        return self.prices_parsing([
            'https://varus.ua/pechen-svinaya-razmorozhena-vesovaya',
            'https://shop.nashkraj.ua/kovel/product/3387-svinina-okholodzhena-pechinka',
            'https://fozzyshop.ua/svinina/19928-pechen-svinaya-okhlazhdennaya-2714621.html'
        ])

    def svin_gulyash_parser(self):
        ''' Парсер для свинний гуляш'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/svyniachyi-guliash-32691',
            'https://fozzyshop.ua/svinina/59720-svinoj-gulyash-2732691.html'
        ])

    def svin_pidjarka_parser(self):
        ''' Парсер для свинна піджарка'''
        return self.prices_parsing([
            'https://novus.online/product/pidzarka-zi-svinini-oholodzena-vag',
            'https://fozzyshop.ua/svinina/11244-svinaya-podzharka-2740987.html'
        ])

    def svin_koreyka_parser(self):
        ''' Парсер для свинна корейка'''
        return self.prices_parsing([
            'https://varus.ua/koreyka-z-domashnoi-svinini-z-k-n-f-ohol-vag',
            'https://shop.silpo.ua/product/svyniacha-koreika-fermerska-757766',
            'https://novus.online/product/korejka-svina-bk-oholvag',
            'https://metro.zakaz.ua/uk/products/m-iaso-globino--metro28509400000000/',
            'https://shop.nashkraj.ua/kovel/category/myaso/myaso-svinina?filter=filter&sort=popular&weight=0&range=0&page=3'
        ])

    def svin_virizka_parser(self):
        ''' Парсер для свинна вирізка'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/m-iaso--ekomarket00000000534899/',
            'https://varus.ua/vyrezka-svinaya-vesovaya',
            'https://shop.silpo.ua/product/svyniacha-vyrizka-fermerska-757764',
            'https://metro.zakaz.ua/uk/products/m-iaso--metro28499800000000/',
            'https://fozzyshop.ua/svinina/11236-svinaya-vyrezka-2732716.html'
        ])

    def svin_lopatka_bez_kistki_parser(self):
        ''' Парсер для свинна лопатка без кістки'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/m-iaso--ekomarket00000000530047/',
            'https://varus.ua/lopatka-svinaya-vesovaya',
            'https://shop.silpo.ua/product/svyniacha-lopatka-fermerska-757767',
            'https://metro.zakaz.ua/uk/products/m-iaso--metro28500400000000/',
            'https://fozzyshop.ua/svinina/11242-svinaya-lopatka-bez-kosti-2732700.html'
        ])

    def svin_okist_bez_kistki_parser(self):
        ''' Парсер для свинна окіст без кістки'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/svyniachyi-okist-fermerskyi-757778',
            'https://fozzyshop.ua/svinina/36927-svinoj-okorok-bez-kosti-2712607.html'
        ])

    def svin_farsh_parser(self):
        ''' Парсер для свинний фарш'''
        return self.prices_parsing([
            'https://shop.nashkraj.ua/kovel/product/97844-farsh-svinina-domashniy-okhol-n-f-vag',
            'https://fozzyshop.ua/svinina/11275-farsh-svinoj-2732789.html'
        ])

    def svin_bitok_bez_kosti_parser(self):
        ''' Парсер для свинний биток без кості'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/m-iaso--ekomarket00000000530039/',
            'https://varus.ua/bitok-z-domashnoi-svinini-n-f-ohol-vag',
            'https://shop.silpo.ua/product/svyniachyi-bytok-fermerskyi-757776',
            'https://fozzyshop.ua/svinina/11253-svinoj-bitok-bez-kosti-2732710.html'
        ])

    def svin_ragu_parser(self):
        ''' Парсер для свинне рагу'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/svyniache-ragu-fermerske-757771',
            'https://fozzyshop.ua/svinina/11247-svinoe-ragu-2732683.html'
        ])

    def svin_osheek_bez_kistki_parser(self):
        ''' Парсер для свинне рагу'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/oshiiok--ekomarket00000000530052/',
            'https://varus.ua/sheya-svinaya-vesovaya',
            'https://shop.silpo.ua/product/svyniachyi-oshyiok-fermerskyi-757779',
            'https://novus.online/product/osijok-svinij-bk-oholvag-virobnictvo',
            'https://metro.zakaz.ua/uk/products/svinina--94820245940065/',
            'https://fozzyshop.ua/svinina/11261-svinoj-osheek-bez-kosti-2732694.html'
        ])

    def kuryacha_chetvert_parser(self):
        ''' Парсер для куряча четверть'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/cetvertina-zadna-kurcat-brojleriv-cebaturocka-oholodzena-gazupak',
            'https://eko.zakaz.ua/uk/products/m-iaso--ekomarket00000000531562/',
            'https://varus.ua/chetvertaya-kurica-vesovaya',
            'https://shop.silpo.ua/product/kuriacha-chvert-domashnia-560143',
            'https://shop.nashkraj.ua/kovel/product/12562-kuryatina-okholodzhena-chetvertina-zadnya',
            'https://fozzyshop.ua/kurica/11180-kurinaya-chetvert-2768007.html'
        ])

    def kuryache_stegno_parser(self):
        ''' Парсер для куряче стегно'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/stegno-kurcat-brojleriv-epikur-oholodzene',
            'https://eko.zakaz.ua/uk/products/m-iaso--ekomarket00000000530003/',
            'https://varus.ua/bedro-kurica-vesovoe',
            'https://shop.silpo.ua/product/kuriache-stegno-461762',
            'https://novus.online/product/stegno-kurace-oholodzene-vag',
            'https://metro.zakaz.ua/uk/products/m-iaso-nasha-riaba--metro28704000000000/',
            'https://shop.nashkraj.ua/kovel/product/255909-kuryatina-okholodzhena-stegno-z-khrebt-kistk',
            'https://fozzyshop.ua/kurica/11181-kurinoe-bedro-2739826.html'
        ])

    def kuryache_krilo_parser(self):
        ''' Парсер для куряче крило'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/krilo-kurcat-brojleriv-cebaturocka-oholodzene',
            'https://varus.ua/krylo-kurinoe-vesovoe',
            'https://shop.silpo.ua/product/kuriache-krylo-461793',
            'https://novus.online/product/krilo-kurace-oholodzene-vag',
            'https://metro.zakaz.ua/uk/products/m-iaso-nasha-riaba--metro28634800000000/',
            'https://shop.nashkraj.ua/kovel/product/1655-kuryatina-okholodzhena-krila',
            'https://fozzyshop.ua/kurica/11189-kurinoe-krylo-2739887.html'
        ])

    def kuryache_file_parser(self):
        ''' Парсер для куряче філе'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/file-kurcat-brojleriv-cebaturocka-oholodzene',
            'https://eko.zakaz.ua/uk/products/file--ekomarket00000000530545/',
            'https://varus.ua/file-kurica-vesovoe',
            'https://shop.silpo.ua/product/kuriache-file-461800',
            'https://novus.online/product/file-kurace-oholodzene-vag',
            'https://metro.zakaz.ua/uk/products/m-iaso-nasha-riaba--metro28968100000000/',
            'https://shop.nashkraj.ua/kovel/product/13917-kuryatina-okholodzhena-file',
            'https://fozzyshop.ua/kurica/11196-kurinoe-file-2739899.html'
        ])

    def kuryacha_gomilka_parser(self):
        ''' Парсер для куряча гомілка'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/m-iaso--ekomarket00000000530535/',
            'https://varus.ua/golen-kurinaya-vesovaya',
            'https://shop.silpo.ua/product/kuriacha-gomilka-461752',
            'https://novus.online/product/gomilka-kuraca-oholodzena-vag',
            'https://metro.zakaz.ua/uk/products/m-iaso-nasha-riaba--metro28960100000000/',
            'https://shop.nashkraj.ua/kovel/product/43276-kuryatina-okholodzhena-gomilka',
            'https://fozzyshop.ua/kurica/11171-kurinaya-golen-2739780.html'
        ])

    def coca_cola_original_033_jb_parser(self):
        ''' Парсер для Coca Cola 0.33 в банке'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/search/?q=coca%20cola',
            'https://varus.ua/napiy-coca-cola-silnogazovaniy-0-33-l',
            'https://shop.silpo.ua/product/napii-coca-cola-2500',
            'https://auchan.ua/ua/napitok-bezalkogol-nyj-s-gaz-coca-cola-zh-b-0-33l-688416/',
            'https://novus.online/ru/product/napij-gazovanij-coca-cola-zb-033l',
            'https://metro.zakaz.ua/ru/products/napii-koka-kola-330ml--05449000000996/',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/28662-napitok-coca-cola-banka-5449000000996.html'
        ])

    def coca_cola_zero_033_jb_parser(self):
        ''' Парсер для Coca Cola Zero 0.33 в банке'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-koka-kola-330ml--05449000131805/',
            'https://varus.ua/napiy-coca-cola-zero-silnogazovaniy-0-33-l',
            'https://shop.silpo.ua/product/napii-coca-cola-zero-692606',
            'https://novus.online/ru/product/napij-silnogazovanij-bezalkogolnij-coca-cola-zero-v-zerstanij-banci-033l',
            'https://metro.zakaz.ua/ru/products/napii-koka-kola-330ml--05449000131805/',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/36887-napitok-coca-cola-zero-zh-b-5449000131805.html'
        ])

    def fanta_orange_033_jb_parser(self):
        ''' Парсер для Fanta Orange 0.33 в банке'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-fanta-330ml--05449000011527/',
            'https://varus.ua/napiy-fanta-apelsin-silnogazovaniy-sokovmisniy-0-33-l',
            'https://shop.silpo.ua/product/napii-fanta-orange-z-b-50118',
            'https://auchan.ua/ua/napitok-bezalkogol-nyj-s-gaz-fanta-zh-b-0-33l-688423/',
            'https://novus.online/ru/product/napij-gazapelsfanta-zb-033l',
            'https://metro.zakaz.ua/ru/products/napii-fanta-330ml--05449000011527/',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/28664-napitok-fanta-orange-zh-b-5449000011527.html'
        ])

    def fanta_pineapple_033_jb_parser(self):
        ''' Парсер для Fanta Pineapple 0.33 в банке'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/napii-fanta-pineapple-z-b-908256',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/102026-napitok-fanta-pineapple-zh-b-0250014891198.html'
        ])

    def sprite_033_jb_parser(self):
        ''' Парсер для Sprite 0.33 в банке'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-sprait-330ml--05449000014535/',
            'https://varus.ua/napiy-sprite-silnogazovaniy-0-33-l',
            'https://shop.silpo.ua/product/napii-sprite-z-b-48593'
            'https://auchan.ua/ua/napitok-bezalkogol-nyj-sil-nogazirovanyj-na-aromatizatorah-sprite-p-but-330ml-688899/',
            'https://novus.online/ru/product/napij-gazovanij-sprite-zb-033l',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/28674-napitok-sprite-zh-b-5449000014535.html'
        ])

    def coca_cola_original_025_gl_parser(self):
        ''' Парсер для Coca Cola Original 0.25 л у склі'''
        return self.prices_parsing([
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/12888-napitok-coca-cola-stbut-54490086.html'
        ])

    def coca_cola_zero_025_gl_parser(self):
        ''' Парсер для Coca Cola Zero 0.25 л у склі'''
        return self.prices_parsing([
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/36888-napitok-coca-cola-zero-steklo-90338120.html'
        ])

    def coca_cola_original_05_pl_parser(self):
        ''' Парсер для Coca Cola Original 0.5 л у пластиковій пляшці'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-05-l-coca-cola-bezalkogolnij-silnogazovanij',
            'https://eko.zakaz.ua/uk/products/napii-koka-kola-500ml-ukrayina--00000054491472/',
            'https://varus.ua/napiy-coca-cola-silnogazovaniy-0-5-l',
            'https://shop.silpo.ua/product/napii-coca-cola-665',
            'https://auchan.ua/ua/napitok-coca-cola-500-ml-274333/',
            'https://novus.online/ru/product/napij-gazovanij-coca-cola-05l',
            'https://metro.zakaz.ua/ru/products/napii-koka-kola-500ml--metro00000054491472/',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/12881-napitok-coca-cola-05l-54491472.html'
        ])

    def coca_cola_zero_05_pl_parser(self):
        ''' Парсер для Coca Cola Zero 0.5 л у пластиковій пляшці'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-05-l-coca-cola-zero-bezalkogolnij-silnogazovanij',
            'https://eko.zakaz.ua/uk/products/napii-koka-kola-500ml--05449000131836/',
            'https://varus.ua/napiy-coca-cola-zero-silnogazovaniy-0-5-l',
            'https://shop.silpo.ua/product/napii-coca-cola-zero-692605',
            'https://novus.online/ru/product/napij-silnogazovanij-bezalkogolnij-coca-cola-zero-v-plastikovij-plasci-05l',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/36884-napitok-coca-cola-zero-5449000131836.html'
        ])

    def fanta_orange_05_pl_parser(self):
        ''' Парсер для Fanta Orange 0.5 л у пластиковій пляшці'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-05-l-fanta-apelsin-bezalkogolnij-silnogazovanij',
            'https://eko.zakaz.ua/uk/products/napii-fanta-500ml--00000040822938/',
            'https://varus.ua/napiy-fanta-apelsin-silnogazovaniy-sokovmisniy-0-5-l',
            'https://shop.silpo.ua/product/napii-fanta-orange-668',
            'https://auchan.ua/ua/napitok-bezalkogol-nyj-sil-nogazirovannyj-s-apel-sinovym-sokom-fanta-p-but-0-5l-688675/',
            'https://novus.online/ru/product/napij-gazovanij-fanta-apelsin-05l',
            'https://metro.zakaz.ua/ru/products/napii-fanta-500ml--05449000020123/',
            'https://shop.nashkraj.ua/kovel/product/7688-napiy-fanta-0-5l-apelsin',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/12917-napitok-fanta-orange-05l-40822938.html'
        ])

    def sprite_05_pl_parser(self):
        ''' Парсер для Sprite 0.5 л у пластиковій пляшці'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-05-l-sprite-bezalkogolnij-silnogazovanij',
            'https://eko.zakaz.ua/uk/products/napii-sprait-500ml--00000054491069/',
            'https://varus.ua/napiy-sprite-silnogazovaniy-0-5-l',
            'https://shop.silpo.ua/product/napii-sprite-666',
            'https://auchan.ua/ua/napitok-bezalkogol-nyj-sil-nogazirovanyj-na-aromatizatorah-sprite-p-but-500ml-688906/',
            'https://novus.online/ru/product/napij-gazovanij-sprite-05l',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/12930-napitok-sprite-05l-54491069.html'
        ])

    def coca_cola_original_15_pl_parser(self):
        ''' Парсер для Coca Cola Original 1.5 л у пластиковій пляшці'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-koka-kola-1500ml--05449000000439/',
            'https://varus.ua/napiy-coca-cola-silnogazovaniy-1-5-l',
            'https://shop.silpo.ua/product/napii-coca-cola-486807',
            'https://auchan.ua/ua/napitok-coca-cola-1-5-l-246666/',
            'https://novus.online/ru/product/napij-gazovanij-coca-cola-15l',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/12883-napitok-coca-cola-15l-5449000000439.html'
        ])

    def coca_cola_zero_15_pl_parser(self):
        ''' Парсер для Coca Cola Zero 1.5 л у пластиковій пляшці'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-koka-kola-1500ml--05449000133335/',
            'https://varus.ua/napiy-coca-cola-zero-silnogazovaniy-1-5-l',
            'https://shop.silpo.ua/product/napii-coca-cola-zero-692608',
            'https://auchan.ua/ua/napitok-coca-cola-zero-sugar-1-5-l-246667/',
            'https://metro.zakaz.ua/ru/products/napii-koka-kola-1500ml-ukrayina--05449000143211/',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/36886-napitok-coca-cola-zero-5449000133335.html'
        ])

    def sprite_15_pl_parser(self):
        ''' Парсер для Sprite 1.5 л у пластиковій пляшці'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-sprait-1500ml--05449000012203/',
            'https://varus.ua/napiy-sprite-silnogazovaniy-1-5-l',
            'https://shop.silpo.ua/product/napii-sprite-504407',
            'https://auchan.ua/ua/napitok-sprite-1-5-l-237668/',
            'https://novus.online/ru/product/napij-gazovanij-sprite-15l',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/12969-napitok-sprite-15l-5449000012203.html'
        ])

    def fanta_orange_15_pl_parser(self):
        ''' Парсер для Fanta Orange 1.5 л у пластиковій пляшці'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-fanta-1500ml--05449000052926/',
            'https://varus.ua/napiy-fanta-apelsin-silnogazovaniy-sokovmisniy-1-5-l',
            'https://shop.silpo.ua/product/napii-fanta-orange-486805',
            'https://novus.online/ru/product/napij-gazovanij-apelsin-fanta-15l',
            'https://metro.zakaz.ua/ru/products/napii-fanta-1500ml--05449000052926/',
            'https://shop.nashkraj.ua/kovel/product/160724-napiy-fanta-1-5l-apelsin',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/12919-napitok-fanta-orange-15l-5449000052926.html'
        ])

    def fanta_shokata_15_pl_parser(self):
        ''' Парсер для Fanta Shokata 1.5 л у пластиковій пляшці'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-fanta-1500ml--05449000099655/',
            'https://varus.ua/napiy-fanta-shokata-silnogazovaniy-sokovmisniy-1-5-l',
            'https://shop.silpo.ua/product/napii-sokovmisnyi-fanta-shokata-sylnogazovanyi-812685',
            'https://auchan.ua/ua/napitok-b-a-sil-nogazirovannyj-sokosoderzhaschij-shokata-fanta-p-but-1-5l-688262/',
            'https://novus.online/ru/product/napij-silnogazovanij-fanta-shokata-15l-ppl',
            'https://metro.zakaz.ua/ru/products/ukrayina--05449000163769/',
            'https://shop.nashkraj.ua/kovel/product/353316-napiy-fanta-1-5l-shokata',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/74057-napitok-sokosoderzhashhij-fanta-shokata-silnogazirovannyj-5449000099655.html'
        ])

    def fanta_mandarin_15_pl_parser(self):
        ''' Парсер для Fanta Mandarin 1.5 л у пластиковій пляшці'''
        return self.prices_parsing([
            'https://varus.ua/napiy-fanta-mandarin-silnogazovaniy-1-5-l',
            'https://shop.silpo.ua/product/napii-fanta-mandaryn-569227',
            'https://novus.online/ru/product/napij-gazovanij-fanta-mandarin-plastikova-plaska-15l',
            'https://metro.zakaz.ua/ru/products/napii-fanta-1500ml--05449000183910/',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/19266-napitok-fanta-mandarin-5449000054128.html'
        ])

    def chips_luxe_becon_133gr_parser(self):
        ''' Парсер для чіпси Люкс зі смаком бекону 133 гр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chipsi-liuks-133g--07622210176196/',
            'https://shop.silpo.ua/product/chypsy-liuks-bekon-555287',
            'https://auchan.ua/ua/chipsy-ljuks-bekon-133-g-238976/',
            'https://novus.online/product/cipsi-luks-z-bekonom-133g',
            'https://metro.zakaz.ua/ru/products/chipsi-liuks-133g--07622210176196/',
            'https://shop.nashkraj.ua/kovel/product/178945-chipsi-lyuks-133g-bekon',
            'https://fozzyshop.ua/chipsy/6385-chipsy-lyuks-bekon-7622210176196.html'
        ])

    def chips_luxe_paprika_133gr_parser(self):
        ''' Парсер для чіпси Люкс зі смаком паприки 133 гр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/cipsi-133-g-luks-zi-smakom-papriki-mup',
            'https://eko.zakaz.ua/uk/products/chipsi-liuks-133g--07622210176202/',
            'https://shop.silpo.ua/product/chypsy-liuks-papryka-555288',
            'https://auchan.ua/ua/chipsy-ljuks-paprika-133-g-238977/',
            'https://novus.online/product/cipsi-luks-z-paprikou-133g',
            'https://metro.zakaz.ua/ru/products/chipsi-liuks-133g--07622210176202/',
            'https://shop.nashkraj.ua/kovel/product/178946-chipsi-lyuks-133g-paprika',
            'https://fozzyshop.ua/chipsy/6388-chipsy-lyuks-paprika-7622210176202.html'
        ])

    def chips_luxe_crab_133gr_parser(self):
        ''' Парсер для чіпси Люкс зі смаком краба 133 гр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/cipsi-133-g-luks-zi-smakom-kraba-mup',
            'https://eko.zakaz.ua/uk/products/chipsi-liuks-133g--07622210177261/',
            'https://shop.silpo.ua/product/chypsy-liuks-krab-555291',
            'https://auchan.ua/ua/chipsy-kartofel-nye-ljuks-so-vkusom-kraba-133-g-883335/',
            'https://novus.online/product/cipsi-luks-z-krabom-133g',
            'https://metro.zakaz.ua/ru/products/chipsi-liuks-133g--07622210177261/',
            'https://shop.nashkraj.ua/kovel/product/178949-chipsi-lyuks-133g-krab',
            'https://fozzyshop.ua/chipsy/6387-chipsy-lyuks-krab-7622210177261.html'
        ])

    def chips_luxe_smetana_cibulya_133gr_parser(self):
        ''' Парсер для чіпси Люкс зі смаком сметани та цибулі 133 гр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/cipsi-133-g-luks-zi-smakom-verskovij-sir-i-gribi-smetana-cibula-mup',
            'https://eko.zakaz.ua/uk/products/chipsi-liuks-133g--07622210176219/',
            'https://shop.silpo.ua/product/chypsy-liuks-smetana-tsybulia-555289',
            'https://novus.online/product/cipsi-luks-zi-smetanou-ta-cibuleu-133g',
            'https://metro.zakaz.ua/ru/products/chipsi-liuks-133g--07622210176219/',
            'https://shop.nashkraj.ua/kovel/product/178947-chipsi-lyuks-133g-smetana-tsibulya',
            'https://fozzyshop.ua/chipsy/6432-chipsy-lyuks-smetana-luk-7622210176219.html'
        ])

    def chips_luxe_sir_133gr_parser(self):
        ''' Парсер для чіпси Люкс зі смаком сиру 133 гр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/cipsi-133-g-luks-zi-smakom-siru-mup',
            'https://eko.zakaz.ua/uk/products/chipsi-liuks-133g--07622210176172/',
            'https://shop.silpo.ua/product/chypsy-liuks-syr-555286',
            'https://auchan.ua/ua/chipsy-ljuks-syr-133-g-238975/',
            'https://novus.online/product/cipsi-luks-z-sirom-133g',
            'https://metro.zakaz.ua/ru/products/chipsi-liuks-133g--07622210176172/',
            'https://shop.nashkraj.ua/kovel/product/178944-chipsi-lyuks-133g-sir',
            'https://fozzyshop.ua/chipsy/6433-chipsy-lyuks-syr-7622210176172.html'
        ])

    def chips_luxe_sir_71gr_parser(self):
        ''' Парсер для чіпси Люкс зі смаком сиру 71 гр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chipsi-liuks-71g--07622210175724/',
            'https://varus.ua/chipsi-lyuks-sir-71-g',
            'https://shop.silpo.ua/product/chypsy-liuks-syr-555263',
            'https://novus.online/product/cipsi-luks-z-sirom-71g',
            'https://metro.zakaz.ua/uk/products/chipsi-liuks-71g--07622210175724/',
            'https://fozzyshop.ua/chipsy/6394-chipsy-lyuks-syr-7622210175724.html'
        ])

    def chips_luxe_becon_71gr_parser(self):
        ''' Парсер для чіпси Люкс зі смаком бекону 71 гр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chipsi-liuks-71g--07622210175731/',
            'https://varus.ua/chipsi-zi-smakom-bekona-lyuks-71g',
            'https://shop.silpo.ua/product/chypsy-liuks-bekon-555279',
            'https://metro.zakaz.ua/uk/products/chipsi-liuks-71g--07622210175731/',
            'https://shop.nashkraj.ua/kovel/product/178939-chipsi-lyuks-71g-bekon',
            'https://fozzyshop.ua/chipsy/6367-chipsy-lyuks-bekon-7622210175731.html'
        ])

    def chips_luxe_paprika_71gr_parser(self):
        ''' Парсер для чіпси Люкс зі смаком паприки 71 гр'''
        return self.prices_parsing([
            'https://varus.ua/chipsi-lyuks-paprika-71-g',
            'https://shop.silpo.ua/product/chipsy-liuks-papryka-555280',
            'https://novus.online/product/cipsi-luks-z-paprikou-71g',
            'https://metro.zakaz.ua/uk/products/chipsi-liuks-71g--07622210175748/',
            'https://shop.nashkraj.ua/kovel/product/178940-chipsi-lyuks-71g-paprika',
            'https://fozzyshop.ua/chipsy/6370-chipsy-lyuks-paprika-7622210175748.html'
        ])

    def chips_luxe_crab_71gr_parser(self):
        ''' Парсер для чіпси Люкс зі смаком краба 71 гр'''
        return self.prices_parsing([
            'https://fozzyshop.ua/chipsy/6386-chipsy-lyuks-krab-7622210177247.html'
        ])

    def chips_luxe_smetana_cibulya_71gr_parser(self):
        ''' Парсер для чіпси Люкс зі смаком сметани та цибулі 71 гр'''
        return self.prices_parsing([
            'https://fozzyshop.ua/chipsy/6392-chipsy-lyuks-smetana-luk-7622210176158.html'
        ])

    def chips_luxe_hvil_lisichki_125gr_parser(self):
        ''' Парсер для чіпси Люкс хвилясті за смаком лисичок 125 гр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/cipsi-125-g-luks-zi-smakom-lisicok-mup',
            'https://eko.zakaz.ua/uk/products/chipsi-liuks-125g--07622201769413/',
            'https://varus.ua/chipsi-kartoplyani-lyuks-hvilyasti-zi-smakom-lisichok-125-g',
            'https://shop.silpo.ua/product/chipsy-liuks-khvyliasti-zi-smakom-lysychok-872080',
            'https://auchan.ua/ua/chipsy-riflenye-ljuks-so-vkusom-lisichek-125-g-649651/',
            'https://novus.online/product/chipsy-kartoplyani-ryfleni-zi-smakom-lysychok-lyukc-125h',
            'https://metro.zakaz.ua/uk/products/chipsi-liuks-125g--07622201769413/',
            'https://shop.nashkraj.ua/kovel/product/410092-chipsi-lyuks-125g-lisichki-rifleni',
            'https://fozzyshop.ua/chipsy/92502-chipsy-lyuks-volnistye-so-vkusom-lisichek-7622201769413.html'
        ])

    def chips_luxe_smetana_cibulya_183gr_parser(self):
        ''' Парсер для чіпси Люкс зі смаком сметани та цибулі 183 гр'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chypsy-liuks-zi-smakom-smetany-i-tsybuli-609680',
            'https://auchan.ua/ua/chipsy-ljuks-so-vkusom-smetany-i-luka-183-g-650083/',
            'https://novus.online/product/cipsi-kartoplani-luks-z-smetanou-ta-cibuleu-183g',
            'https://metro.zakaz.ua/uk/products/chipsi-liuks-183g--07622210420152/',
            'https://shop.nashkraj.ua/kovel/product/214979-chipsi-lyuks-183g-smetana-tsibulya',
            'https://fozzyshop.ua/chipsy/43381-chipsy-lyuks-so-vkusom-smetany-i-luka-7622210420152.html'
        ])

    def chips_luxe_becon_183gr_parser(self):
        ''' Парсер для чіпси Люкс зі смаком бекону 183 гр'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chypsy-liuks-zi-smakom-bekonu-609682',
            'https://auchan.ua/ua/chipsy-ljuks-so-vkusom-bekona-183-g-650076/',
            'https://novus.online/product/cipsi-kartoplani-luks-z-bekonom-183g',
            'https://metro.zakaz.ua/uk/products/chipsi-liuks-183g--07622210420145/',
            'https://shop.nashkraj.ua/kovel/product/214977-chipsi-lyuks-183g-bekon',
            'https://fozzyshop.ua/chipsy/33841-chipsy-lyuks-so-vkusom-bekona-7622210420145.html'
        ])

    def chips_luxe_sir_183gr_parser(self):
        ''' Парсер для чіпси Люкс зі смаком сиру 183 гр'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chypsy-liuks-zi-smakom-syru-609679',
            'https://auchan.ua/ua/chipsy-ljuks-so-vkusom-syra-183-g-650069/',
            'https://novus.online/product/cipsi-kartoplani-luks-z-sirom-183g',
            'https://metro.zakaz.ua/uk/products/chipsi-liuks-183g--07622210420138/',
            'https://shop.nashkraj.ua/kovel/product/214978-chipsi-lyuks-183g-sir',
            'https://fozzyshop.ua/chipsy/33840-chipsy-lyuks-so-vkusom-syra-7622210420138.html'
        ])

    def chips_pringles_greece_souce_caciki_185gr_parser(self):
        ''' Парсер для чіпси Pringles Грецький соус та цацики 185 гр'''
        return self.prices_parsing([
            'https://fozzyshop.ua/chipsy/100325-snek-pikantnyj-pringles-grecheskij-sous-caciki-250015045996.html'
        ])

    def chips_pringles_paprika_165gr_parser(self):
        ''' Парсер для чіпси Pringles папріка 165 гр'''
        return self.prices_parsing([
            'https://varus.ua/chipsy-pringles-paprika-165g',
            'https://shop.silpo.ua/product/snek-pikantnyi-pringles-papryka-903305',
            'https://auchan.ua/ua/chipsy-kartofel-nye-pringles-so-vkusom-papriki-165-g-665854/',
            'https://novus.online/product/cipsi-paprika-pringles-paprika-165g',
            'https://metro.zakaz.ua/uk/products/chipsi-pringls-165g--05053990106868/',
            'https://fozzyshop.ua/chipsy/98178-snek-pikantnyj-pringles-paprika-0250014807946.html'
        ])

    def chips_pringles_pizza_peperoni_185gr_parser(self):
        ''' Парсер для чіпси Pringles піца пепероні 185 гр'''
        return self.prices_parsing([
            'https://fozzyshop.ua/chipsy/100683-snek-pikantnyj-pringles-picca-peperoni-0250015045989.html'
        ])

    def chips_pringles_sir_cubylya_165gr_parser(self):
        ''' Парсер для чіпси Pringles зі смаком сиру та цибулі 165 гр'''
        return self.prices_parsing([
            'https://novus.online/product/cipsi-sir-cibula-pringles-cheese-onion-165g',
            'https://metro.zakaz.ua/uk/products/chipsi-pringls-165g--05053990101535/',
            'https://fozzyshop.ua/chipsy/6356-chipsy-pringles-syr-luk-5410076068210.html'
        ])

    def chips_pringles_original_165gr_parser(self):
        ''' Парсер для чіпси Pringles Original 165 гр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chipsi-pringls-165g--05053990101573/',
            'https://varus.ua/chipsi-kartoplyani-originalni-pringles-165g',
            'https://shop.silpo.ua/product/chypsy-pringles-oryginal-423903',
            'https://auchan.ua/ua/chipsy-pringles-original-165-g-241166/',
            'https://novus.online/product/cipsi-original-pringles-original-165g',
            'https://metro.zakaz.ua/uk/products/chipsi-pringls-165g--05053990101573/',
            'https://fozzyshop.ua/chipsy/6381-chipsy-pringles-original-5410076068067.html'
        ])

    def chips_pringles_sir_165gr_parser(self):
        ''' Парсер для чіпси Pringles зі смаком сиру 165 гр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/cipsi-165g-pringles-kartoplani-zi-smakom-siru',
            'https://eko.zakaz.ua/uk/products/chipsi-pringls-165g--05053990106981/',
            'https://varus.ua/chipsi-pringles-cheese-165-g',
            'https://shop.silpo.ua/product/chypsy-pringles-syr-423899',
            'https://auchan.ua/ua/chipsy-pringles-cheese-165-g-241161/',
            'https://novus.online/product/cipsi-sir-pringles-cheese-165g',
            'https://metro.zakaz.ua/uk/products/chipsi-pringls-165g--05053990106981/',
            'https://fozzyshop.ua/chipsy/6384-chipsy-pringles-syr-5410076068241.html'
        ])

    def chips_lays_paprika_120gr_parser(self):
        ''' Парсер для чіпси Lay's папріка 120 гр'''
        return self.prices_parsing([
            'https://varus.ua/chipsy-lays-kartofelnye-so-vkusom-papriki-120g',
            'https://shop.silpo.ua/product/chipsy-lay-s-kartopliani-zi-smakom-papryky-920464',
            'https://novus.online/product/chipsy-kartoplyani-smak-papryky-lays-120h',
            'https://metro.zakaz.ua/uk/products/chipsi-leiz--04823063125451/',
            'https://fozzyshop.ua/chipsy/100361-chipsy-lays-kartofelnye-so-vkusom-papriki-250015119604.html'
        ])

    def chips_lays_crab_120gr_parser(self):
        ''' Парсер для чіпси Lay's краб 120 гр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/cipsi-120-g-lays-kartoplani-zi-smakom-krabu-mup',
            'https://eko.zakaz.ua/uk/products/chipsi-leiz-120g--04823063125314/',
            'https://varus.ua/chipsy-lays-kartofelnye-so-vkusom-kraba-120g',
            'https://shop.silpo.ua/product/chipsy-lay-s-kartopliani-zi-smakom-kraba-920457',
            'https://novus.online/product/chipsy-kartoplyani-smak-kraba-lays-120h',
            'https://metro.zakaz.ua/uk/products/chipsi-leiz-120g--04823063125314/',
            'https://fozzyshop.ua/chipsy/100358-chipsy-lays-kartofelnye-so-vkusom-kraba-250015119550.html'
        ])

    def chips_lays_sir_60gr_parser(self):
        ''' Парсер для чіпси Lay's сир 60 гр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chipsi-leiz-60g--04823063125352/',
            'https://varus.ua/chipsy-lays-kartofelnye-so-vkusom-syra-60g',
            'https://shop.silpo.ua/product/chipsy-lay-s-kartopliani-zi-smakom-syru-920461',
            'https://novus.online/product/chipsy-kartoplyani-syr-lays-60h',
            'https://metro.zakaz.ua/uk/products/chipsi-leiz-60g--04823063125352/',
            'https://fozzyshop.ua/chipsy/100687-chipsy-lays-kartofelnye-so-vkusom-syra-0250015119581.html'
        ])

    def sir_svet_feta_ukr_rozsil_45_1kg_parser(self):
        ''' Парсер для Сир Свет Сыр Фета Українська розсільний 45% в/у'''
        return self.prices_parsing([
            'https://fozzyshop.ua/rassolnyj/36358-syr-svet-syr-feta-ukrainskaya-rassolnyj-45-v-u-2722985.html'
        ])

    def olivki_extra_chorni_bez_kist_300gr_parser(self):
        ''' Парсер для Оливки Extra! чорні без кісточки, 300г'''
        return self.prices_parsing([
            'https://fozzyshop.ua/masliny-olivki/19470-olivki-extra-chernye-bez-kostochki-4824034034734.html'
        ])

    def oliv_oil_povna_chasha_913gr_parser(self):
        ''' Парсер для Оливкове масло Повна Чаша 913 г'''
        return self.prices_parsing([
            'https://fozzyshop.ua/oliya-olivkova/50492-maslo-olivkovoe-povna-chasha-4823096401041.html'
        ])

    def basilik_chervoniy_svij_parser(self):
        ''' Парсер для Базілік червоний свіжий'''
        return self.prices_parsing([
            'https://varus.ua/bazilik-svezhiy-40-g',
            'https://shop.silpo.ua/product/bazylik-chervonyi-505390',
            'https://novus.online/ru/product/bazylik-chervonyy-blister-50hr',
            'https://metro.zakaz.ua/uk/products/zelen-bazilik-50g--metro98690128120460/',
            'https://fozzyshop.ua/zelen/73186-bazilik-vershki-ta-korinci-krasnyj-svezhij-s-kornem-4820224870038.html'
        ])

    def pelmeni_gerkules_firm_400gr_parser(self):
        ''' Парсер для пельмені Геркулес Фірмові 400 гр'''
        return self.prices_parsing([
            'https://varus.ua/pelmeni-firmovi-gerkules-400g',
            'https://shop.silpo.ua/product/pelmeni-gerkules-firmovi-4728',
            'https://novus.online/ru/product/pelmeni-firmovi-gerkules-400g',
            'https://fozzyshop.ua/ru/pelmeni/19844-pelmeni-gerkules-firmennye-4820020710040.html'
        ])

    def pelmeni_gerkules_firm_800gr_parser(self):
        ''' Парсер для пельмені Геркулес Фірмові 800 гр'''
        return self.prices_parsing([
            'https://varus.ua/pelmeni-firmovi-gerkules-800g-ukraina',
            'https://shop.silpo.ua/product/pelmeni-gerkules-firmovi-681380',
            'https://novus.online/ru/product/pelmeni-firmovi-gerkules-800g',
            'https://metro.zakaz.ua/ru/products/pelmeni-gerkules-800g-ukrayina--04820020715465/',
            'https://fozzyshop.ua/ru/pelmeni/44824-pelmeni-gerkules-firmennye-4820020715465.html'
        ])

    def pelmeni_gerkules_indeyka_400gr_parser(self):
        ''' Парсер для пельмені Геркулес з м'ясом індички 400 гр'''
        return self.prices_parsing([
            'https://varus.ua/pelmeni-z-myasom-indichki-gerkules-400g',
            'https://shop.silpo.ua/product/pelmeni-gerkules-z-m-iasom-indychky-512216',
            'https://novus.online/ru/product/pelmeni-z-masom-indicki-gerkules-400g',
            'https://fozzyshop.ua/ru/pelmeni/19843-pelmeni-gerkules-s-myasom-indejki-4820020716035.html'
        ])

    def pelmeni_tri_vedmedi_firm_800gr_parser(self):
        ''' Парсер для пельмені Три Ведмеді Фірмові 800 гр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/pelmeni-085kg-tri-vedmedi-firmovi-zi-svininou-ta-alovicinou',
            'https://varus.ua/pelmeni-tri-medvedya-po-domashnemu-800g',
            'https://shop.silpo.ua/product/pelmeni-try-vedmedi-firmovi-450102',
            'https://novus.online/ru/product/pelmeni-firmovi-tri-vedmedi-800g',
            'https://metro.zakaz.ua/ru/products/pelmeni-tri-vedmedi-800g-ukrayina--04823086113107/',
            'https://fozzyshop.ua/ru/pelmeni/50856-pelmeni-tri-vedmedi-firmennye-4820039464279.html'
        ])

    def pelmeni_tri_vedmedi_mishutka_400gr_parser(self):
        ''' Парсер для пельмені Три Ведмеді Мішутка телятіна 400 гр'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/pelmeni-450g-tri-vedmedi-misutka-z-telatinou',
            'https://eko.zakaz.ua/uk/products/pelmeni-tri-vedmedi-400g-ukrayina--04823086112926/',
            'https://varus.ua/pelmeni-z-telyatinoyu-mishutka-400g',
            'https://shop.silpo.ua/product/pelmeni-try-vedmedi-mishutka-z-teliatynoiu-885574',
            'https://novus.online/ru/product/pelmeni-misutka-telatina-tri-vedmedi-400g',
            'https://metro.zakaz.ua/ru/products/pelmeni-tri-vedmedi-400g--04823086103153/',
            'https://fozzyshop.ua/ru/pelmeni/91219-pelmeni-tri-vedmedi-mishutka-telyatina-4823086112926.html'
        ])

    def pelmeni_extra_firm_800gr_parser(self):
        ''' Парсер для пельмені Extra! фірмові 800 гр'''
        return self.prices_parsing([
            'https://fozzyshop.ua/ru/pelmeni/7743-pelmeni-extra-firmennye-4824034014996.html'
        ])

    def pelmeni_extra_sibir_500gr_parser(self):
        ''' Парсер для пельмені Extra! сибірські 500 гр'''
        return self.prices_parsing([
            'https://fozzyshop.ua/ru/pelmeni/7742-pelmeni-extra-cibirskie-4824034015009.html'
        ])

    def pelmeni_extra_ravioli_dom_800gr_parser(self):
        ''' Парсер для пельмені Extra! равіолі домашні 800 гр'''
        return self.prices_parsing([
            'https://fozzyshop.ua/ru/pelmeni/7776-ravioli-extra-domashnie-4824034011650.html'
        ])

    def seven_up_033_jb_parser(self):
        ''' Парсер для 7UP 0.33 л жб'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-330-ml-7-up-zb',
            'https://eko.zakaz.ua/uk/products/napii-seven-ap-330ml-ukrayina--05900497030243/',
            'https://auchan.ua/ua/napitok-bezalkogol-nyj-sil-nogazirovanyj-s-aromatom-limona-i-lajma-7up-zh-b-0-33l-688913/',
            'https://novus.online/ru/product/napij-gazovanij-7-up-033l-zb',
            'https://metro.zakaz.ua/ru/products/napii-seven-ap-330ml-ukrayina--05900497030243/',
            'https://fozzyshop.ua/ru/voda-sladkaya-gazirovannaya/77869-napitok-7up-bezalkogolnyj-silnogazirovannyj-zh-b-4823063116619.html'
        ])

    def kavun_parser(self):
        ''' Парсер для Кавун, кг'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/kavun-1-gat',
            'https://eko.zakaz.ua/uk/products/iagoda--ekomarket00000000668884/',
            'https://varus.ua/kavun-ukrayina-vagovij',
            'https://shop.silpo.ua/product/kavun-51606',
            'https://novus.online/ru/product/kavun-vag',
            'https://metro.zakaz.ua/ru/products/frukt-kavun-bez-tm--metro28501700000000/',
        ])

    def jivchik_apple_2l_parser(self):
        ''' Парсер для напій Живчік Яблуко 2 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-2-l-zivcik-gazovanij',
            'https://eko.zakaz.ua/uk/products/napii-zhivchik-2000ml--04820000195447/',
            'https://shop.silpo.ua/product/napii-zhyvchyk-z-sokom-iabluka-1820',
            'https://auchan.ua/ua/napitok-gazirovannyj-zhivchik-jabloko-2l-996347/',
            'https://novus.online/ru/product/napij-negazovanij-zivcik-2l',
            'https://metro.zakaz.ua/ru/products/napii-zhivchik-2000ml--04820000191531/',
            'https://fozzyshop.ua/ru/voda-sladkaya-gazirovannaya/12973-napitok-zhivchik-yabloko-2l-4820000195447.html'
        ])

    def jivchik_apple_1l_parser(self):
        ''' Парсер для напій Живчік Яблуко 1 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-1-l-zivcik-gazovanij',
            'https://eko.zakaz.ua/uk/products/napii-zhivchik-1000ml--04820000195430/',
            'https://varus.ua/napiy-zhivchik-silnogazovaniy-1-l',
            'https://shop.silpo.ua/product/napii-zhyvchyk-iz-sokom-iabluka-1158',
            'https://novus.online/ru/product/napij-gazovanij-zivcik-1l',
            'https://metro.zakaz.ua/ru/products/napii-zhivchik-1000ml-ukrayina--14820000195437/',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/12951-napitok-zhivchik-yabloko-4820000195430.html'
        ])

    def jivchik_apple_05l_parser(self):
        ''' Парсер для напій Живчік Яблуко 0.5 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-05l-zivcik-gazovanij',
            'https://eko.zakaz.ua/uk/products/napii-zhivchik-500ml--04820000195423/',
            'https://varus.ua/napiy-zhivchik-silnogazovaniy-0-5-l',
            'https://shop.silpo.ua/product/napii-zhyvchyk-z-sokom-iabluka-64604',
            'https://novus.online/ru/product/napij-gazovanij-zivcik-05l',
            'https://fozzyshop.ua/ru/voda-sladkaya-gazirovannaya/19309-napitok-zhivchik-yabloko-05l-4820000195423.html'
        ])

    def jivchik_grusha_1l_parser(self):
        ''' Парсер для напій Живчік Груша 0.5 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-zhivchik-1000ml--04820000193252/',
            'https://varus.ua/napiy-zhivchik-grusha-silnogazovaniy-1-l',
            'https://shop.silpo.ua/product/napii-zhyvchyk-grusha-304833',
            'https://auchan.ua/ua/napitok-zhivchik-grusha-1-l-994796/',
            'https://novus.online/ru/product/napij-gazovanij-zivcik-grusa-1l',
            'https://fozzyshop.ua/ru/voda-sladkaya-gazirovannaya/12947-napitok-zhivchik-grusha-4820000193252.html'
        ])

    def jivchik_smart_cola_2l_parser(self):
        ''' Парсер для напій Живчік Smart Cola 2 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-zhivchik-2000ml--04820193032857/',
            'https://shop.silpo.ua/product/napii-sokovmisnyi-zhyvchyk-smart-sola-793178',
            'https://auchan.ua/ua/napitok-sokosoderzhaschij-sil-nogazirovannyj-smart-sola-zhivchik-p-but-2l-689109/',
            'https://novus.online/ru/product/napij-gazovanij-sokovmisnij-zivcik-smart-sola-2l-pet',
            'https://fozzyshop.ua/ru/voda-sladkaya-gazirovannaya/63966-napitok-sokosoderzhashhij-zhivchik-smart-sola-4820193032857.html'
        ])

    def jivchik_limon_2l_parser(self):
        ''' Парсер для напій Живчік лімон 2 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-zhivchik-2000ml--04820000191982/',
            'https://varus.ua/napiy-zhivchik-limon-silnogazovaniy-2-l',
            'https://shop.silpo.ua/product/napii-sokovmisnyi-zhyvchyk-leemon-910081',
            'https://auchan.ua/ua/voda-limon-zhivchik-obolon-2l-682242/',
            'https://novus.online/ru/product/napij-gazovanij-zivcik-limon-2l',
            'https://metro.zakaz.ua/ru/products/napii-zhivchik-2000ml--04820000191982/',
            'https://fozzyshop.ua/ru/voda-sladkaya-gazirovannaya/12948-napitok-zhivchik-limon-4820000191982.html'
        ])

    def jivchik_smart_cola_1l_parser(self):
        ''' Парсер для напій Живчік Smart Cola 1 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-zhivchik-1000ml--04820193032871/',
            'https://shop.silpo.ua/product/napii-sokovmisnyi-zhyvchyk-smart-sola-793177',
            'https://auchan.ua/ua/napitok-sokosoderzhaschij-sil-nogazirovannyj-smart-sola-zhivchik-p-but-1l-689102/',
            'https://novus.online/ru/product/napij-gazovanij-sokovmisnij-zivcik-smart-sola-1l-pet',
            'https://fozzyshop.ua/ru/voda-sladkaya-gazirovannaya/63967-napitok-sokosoderzhashhij-zhivchik-smart-sola-4820193032871.html'
        ])

    def biola_strawb_kiwi_2l_parser(self):
        ''' Парсер для напій Біола полуниця-ківі 2 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-2-l-biola-polunica-kivi-bezalkogolnij-sokovmisnij-silnogazovanij',
            'https://novus.online/ru/product/napiy-sylhazyrovanyy-biola-polunytsya-kivi-2l-pet',
            'https://fozzyshop.ua/ru/voda-sladkaya-gazirovannaya/87668-napitok-biola-fruit-water-so-vkusom-klubniki-i-kivi-4820209112245.html'
        ])

    def biola_lemonad_2l_parser(self):
        ''' Парсер для напій Біола лімонад 2 л'''
        return self.prices_parsing([
            'https://varus.ua/napij-biola-fruit-water-limonad-bezalkogolnij-silnogazovanij-na-aromatizatorah-2-l',
            'https://shop.silpo.ua/product/napii-biola-fruktova-voda-lymonad-sylnogazovana-913438',
            'https://novus.online/ru/product/napij-gazovanij-biola-limonad-2l',
            'https://fozzyshop.ua/ru/voda-sladkaya-gazirovannaya/101364-napitok-biola-fruktovaya-voda-limonad-silnogazirovannyj-0250015067462.html'
        ])

    def bon_boisson_limonad_1l_parser(self):
        ''' Парсер для напій Бон Буассон лімонад 1 л'''
        return self.prices_parsing([
            'https://varus.ua/napiy-bon-boisson-limonad-silnogazovaniy-1-l',
            'https://shop.silpo.ua/product/napii-bon-boisson-lymonad-89009',
            'https://auchan.ua/ua/napitok-bon-buasson-limonad-1-l-745722/',
            'https://novus.online/ru/product/napij-gazovanij-bon-buason-limonad-1l',
            'https://shop.nashkraj.ua/kovel/product/19296-napiy-bon-buasson-1l-limonad',
            'https://fozzyshop.ua/ru/voda-sladkaya-gazirovannaya/28659-napitok-bon-boisson-limonad-4820005194339.html'
        ])

    def bon_boisson_limonad_2l_parser(self):
        ''' Парсер для напій Бон Буассон лімонад 2 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-bon-buasson-2000ml-ukrayina--04820203710096/',
            'https://varus.ua/napiy-bon-boisson-limonad-silnogazovaniy-2-l',
            'https://shop.silpo.ua/product/napii-lymonad-4214',
            'https://auchan.ua/ua/napitok-bon-buasson-limonad-2-l-246668/',
            'https://novus.online/ru/product/napij-gazovanij-bon-buason-limonad-2l',
            'https://metro.zakaz.ua/ru/products/napii-bon-buasson-2000ml-ukrayina--04820005197446/',
            'https://shop.nashkraj.ua/kovel/product/6551-napiy-bon-buasson-2l-limonad',
            'https://fozzyshop.ua/ru/voda-sladkaya-gazirovannaya/49832-napitok-bon-buasson-limonad-2l-4820005190379.html'
        ])

    def bon_boisson_lime_mint_2l_parser(self):
        ''' Парсер для напій Бон Буассон лайм-м'ята 2 л'''
        return self.prices_parsing([
            'https://fozzyshop.ua/ru/voda-sladkaya-gazirovannaya/86494-napitok-bon-boisson-so-vkusom-lajm-myata-4820203711239.html'
        ])

    def bon_boisson_baikal_2l_parser(self):
        ''' Парсер для напій Бон Буассон Байкал 2 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-bon-buasson-2000ml-ukrayina--04820203710034/',
            'https://varus.ua/napiy-bon-boisson-baykal-silnogazovaniy-2-l',
            'https://shop.silpo.ua/product/napii-baikal-4538',
            'https://auchan.ua/ua/napitok-bon-buasson-bajkal-2-l-710627/',
            'https://novus.online/ru/product/napij-gazovanij-bon-buason-bajkal-2l',
            'https://metro.zakaz.ua/ru/products/napii-bon-buasson-2000ml-ukrayina--04820005190249/',
            'https://fozzyshop.ua/ru/voda-sladkaya-gazirovannaya/49829-napitok-bon-buasson-bajkal-2l-4820005190249.html'
        ])

    def bon_boisson_tarhun_2l_parser(self):
        ''' Парсер для напій Бон Буассон Тархун 2 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-bon-buasson-tarhun-2-l',
            'https://eko.zakaz.ua/uk/products/napii-bon-buasson-2000ml-ukrayina--04820203710256/',
            'https://varus.ua/napiy-bon-boisson-tarhun-silnogazovaniy-2-l',
            'https://shop.silpo.ua/product/napii-tarkhun-4215',
            'https://auchan.ua/ua/napitok-bon-buasson-tarhun-gazirovannyj-2l-246670/',
            'https://novus.online/ru/product/napij-gazovanij-bon-buason-tarhun-2l',
            'https://metro.zakaz.ua/ru/products/napii-bon-buasson-2000ml-ukrayina--04820005190294/',
            'https://shop.nashkraj.ua/kovel/product/6552-napiy-bon-buasson-2l-tarkhun',
            'https://fozzyshop.ua/ru/voda-sladkaya-gazirovannaya/49831-napitok-bon-buasson-tarkhun-2l-4820005190294.html'
        ])

    def bon_boisson_baikal_1l_parser(self):
        ''' Парсер для напій Бон Буассон Байкал 1 л'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/napii-bon-boisson-baikal-94224',
            'https://auchan.ua/ua/napitok-bon-buasson-bajkal-1-l-745715/',
            'https://novus.online/product/napij-gazovanij-bon-buason-bajkal-1l',
            'https://shop.nashkraj.ua/kovel/product/17165-napiy-bon-buasson-1l-baykal',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/28658-napitok-bon-boisson-bajkal-4820005194322.html'
        ])

    def bon_boisson_mult_sok_1l_parser(self):
        ''' Парсер для напій Бон Буассон Мультівітамін 1 л'''
        return self.prices_parsing([
            'https://varus.ua/napiy-bon-boisson-multivitamin-silnogazovaniy-sokovmisniy-1-l',
            'https://shop.silpo.ua/product/napii-bon-boisson-multyvitamin-z-naturalnym-sokom-89011',
            'https://shop.nashkraj.ua/kovel/product/19298-napiy-bon-buasson-1l-multivitamin',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/42538-napitok-bon-boisson-multivitamin-s-naturalsokom-4820203710591.html'
        ])

    def bon_boisson_mango_2l_parser(self):
        ''' Парсер для напій Бон Буассон Манго 2 л'''
        return self.prices_parsing([
            'https://varus.ua/napiy-bon-boisson-mango-silnogazovaniy-sokovmisniy-2-l',
            'https://shop.silpo.ua/product/napii-bon-boisson-mango-749371',
            'https://novus.online/product/napij-bon-buasson-mango-2l',
            'https://metro.zakaz.ua/uk/products/napii-bon-buasson-2000ml-ukrayina--04820203711123/',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/53282-napitok-bon-boisson-mango-4820203711123.html'
        ])

    def bon_boisson_mohito_2l_parser(self):
        ''' Парсер для напій Бон Буассон Мохито 2 л'''
        return self.prices_parsing([
            'https://varus.ua/napiy-bon-boisson-mohito-silnogazovaniy-sokovmisniy-2-l',
            'https://shop.silpo.ua/product/napii-bon-boisson-mokhito-bezalkogolnyi-sylnogazovanyi-796017',
            'https://metro.zakaz.ua/uk/products/napii-bon-buasson-2000ml-ukrayina--04820203711505/',
            'https://shop.nashkraj.ua/kovel/product/317979-napiy-bon-buasson-2l-mokhito',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/86493-napitok-bon-boisson-mokhito-bezalkogolnyj-silnogazirovannyj-4820203711505.html'
        ])

    def bon_boisson_sitro_2l_parser(self):
        ''' Парсер для напій Бон Буассон Ситро 2 л'''
        return self.prices_parsing([
            'https://varus.ua/napiy-bon-boisson-sitro-silnogazovaniy-2-l',
            'https://novus.online/product/napij-gazovanij-bon-buason-sitro-2l',
            'https://metro.zakaz.ua/uk/products/napii-bon-buasson-2000ml-ukrayina--04820005194711/',
            'https://shop.nashkraj.ua/kovel/product/19307-napiy-bon-buasson-2l-sitro',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/49774-napitok-bon-buasson-sitro-2l-4820005194711.html'
        ])

    def bon_boisson_krem_soda_2l_parser(self):
        ''' Парсер для напій Бон Буассон Крем Сода 2 л'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/napii-krem-soda-nostalzhi-177315',
            'https://auchan.ua/ua/napitok-bon-buasson-krem-soda-2-l-246669/',
            'https://novus.online/product/napij-gazovanij-bon-buason-krem-soda-2l',
            'https://metro.zakaz.ua/uk/products/napii-bon-buasson-2000ml-ukrayina--04820005195312/',
            'https://shop.nashkraj.ua/kovel/product/6549-napiy-bon-buasson-2l-krem-soda',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/49764-napitok-bon-buasson-krem-soda-2l-4820203710157.html'
        ])

    def bon_boisson_mult_sok_2l_parser(self):
        ''' Парсер для напій Бон Буассон Мультивитамин 2 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-bon-buasson-2000ml-ukrayina--04820203710577/',
            'https://novus.online/product/napij-sokovmisnij-gazovanij-multivitamin-bon-buason-2l',
            'https://metro.zakaz.ua/uk/products/napii-bon-buasson-2000ml-ukrayina--04820203710577/',
            'https://shop.nashkraj.ua/kovel/product/19306-napiy-bon-buasson-2l-multivitamin',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/42545-napitok-multivitamin-s-sokom-4820203710577.html'
        ])

    def mirinda_orange_033jb_parser(self):
        ''' Парсер для напій Mirinda Orange 0.33 л'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-330-ml-mirinda-apelsin-zb',
            'https://novus.online/product/napij-033l-gazovanij-mirinda-zb',
            'https://metro.zakaz.ua/uk/products/napii-mirinda-mirinda-330ml-ukrayina--04823063126939/',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/42556-mirinda-apelsin-033l-4823063111812.html'
        ])

    def mirinda_orange_05l_parser(self):
        ''' Парсер для напій Mirinda Orange 0.5 л'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-mirinda-mirinda-500ml-ukrayina--04823063110495/',
            'https://varus.ua/napiy-mirinda-apelsin-silnogazovaniy-0-5-l',
            'https://novus.online/product/napiy-sylnohazovanyy-mirinda-zero-05-l-pb',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/101367-napitok-mirinda-free-so-vkusom-apelsina-5900497040853.html'
        ])

    def schweppes_granat_1l_parser(self):
        ''' Парсер для напій Schweppes Granat 1 л'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/napii-schweppes-granat-sylnogazovanyi-778462',
        ])

    def schweppes_indian_tonic_033jb_parser(self):
        ''' Парсер для напій Schweppes Indian Tonic 0.33'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-shveps-330ml--05449000046390/',
            'https://varus.ua/napiy-schweppes-indian-tonic-water-silnogazovaniy-0-33-l',
            'https://shop.silpo.ua/product/napii-sokovmisnyi-schweppes-indian-tonic-714691',
            'https://auchan.ua/ua/napitok-bezalkogol-nyj-sil-nogazirovannyj-indian-tonic-water-schweppes-zh-b-0-33l-688507/',
            'https://novus.online/product/napij-silnogazovanij-bezalkogolnij-indian-tonic-schweppes-v-zestanij-banci-033l',
            'https://shop.nashkraj.ua/kovel/product/113741-napiy-schweppes-0-33l-tonik-zhb',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/42565-napitok-sokosoderzhashhij-schweppes-indian-tonic-zh-b-5449000046390.html'
        ])

    def schweppes_original_bitter_lemon_033jb_parser(self):
        ''' Парсер для напій Schweppes Original Bitter lemon 0.33'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-shveps-330ml--05449000064110/',
            'https://shop.silpo.ua/product/napii-sokovmisnyi-schweppes-original-bitlemon-714692',
            'https://novus.online/product/napij-silnogazovanij-bezalkogolnij-bitter-lemon-schweppes-v-zestanij-banci-033l',
        ])

    def schweppes_original_bitter_lemon_075l_parser(self):
        ''' Парсер для напій Schweppes Original Bitter lemon 0.75'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/napij-075-l-schweppes-bitter-lemon-bezalkogolnij-silnogazovanij-pet',
            'https://eko.zakaz.ua/uk/products/voda-shveps-750ml--05449000312136/',
            'https://shop.silpo.ua/product/napii-schweppes-bitter-lemon-bezalkogolnyi-sylnogazovanyi-914866',
            'https://novus.online/product/napiy-hazovanyy-schweppes-bitter-lemon-075-plpl',
            'https://metro.zakaz.ua/uk/products/napii-shveps-750ml--05449000312259/',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/100319-napitok-schweppes-bitter-lemon-silnogazirovannyj-250015025707.html'
        ])

    def schweppes_original_bitter_lemon_1l_parser(self):
        ''' Парсер для напій Schweppes Original Bitter lemon 1 l'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/napii-sokovmisnyi-schweppes-original-bitter-lemon-750478',
        ])

    def schweppes_classic_mojito_033jb_parser(self):
        ''' Парсер для напій Schweppes Classic Mojito 0.33'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/napii-shveps-330ml--05449000171351/',
            'https://varus.ua/napiy-schweppes-classic-mojito-silnogazovaniy-0-33-l',
            'https://shop.silpo.ua/product/napii-sokovmisnyi-schweppes-classic-mojito-714690',
            'https://auchan.ua/ua/napitok-bezalkogol-nyj-sil-nogazirovannyj-classic-mojito-schweppes-zh-b-0-33l-688444/',
            'https://novus.online/product/napij-silnogazovanij-bezalkogolnij-taste-of-classic-mojito-schweppes-v-zestanij-banci-033l',
            'https://metro.zakaz.ua/uk/products/napii-shveps-330ml--05449000171351/',
            'https://shop.nashkraj.ua/kovel/product/244062-napiy-schweppes-0-33l-mokhito-zhb',
            'https://fozzyshop.ua/voda-sladkaya-gazirovannaya/42564-napitok-sokosoderzhashhij-schweppes-classic-mojito-zh-b-5449000171351.html'
        ])

    def farsh_govyajiy_parser(self):
        ''' Парсер для фарш гов'яжий'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/fars-05-kg-globino-alovicij-oholodzenij',
            'https://varus.ua/farsh-delikatesnyy-s-govyadinoy-ohlazhdennyy-vesovoy',
            'https://auchan.ua/ua/farsh-govjazhij-skott-smeat-ohlazhdennyj-450-g-1177897/',
            'https://novus.online/product/fars-alovicij-kotletnij-oholvag',
            'https://metro.zakaz.ua/uk/products/farsh-globino-500g--04820112651886/',
            'https://fozzyshop.ua/govyadina-i-telyatina/11153-farsh-govyazhij-2732628.html'
        ])

    def rice_extra_krugl_1kg_parser(self):
        ''' Парсер для ріс круглий Extra! 1 кг'''
        return self.prices_parsing([
            'https://fozzyshop.ua/ris/5927-ris-extra-kruglyj-4824034013265.html'
        ])

    def maslo_sliv_ferma_selyanske_73jir_180gr_parser(self):
        ''' Парсер для Масло сладкосливочное Ферма Сельское 73%, 180г'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/maslo-180-g-ferma-solodkoverskove-selanske-73',
            'https://eko.zakaz.ua/uk/products/maslo-ferma-180g-ukrayina--04820239242653/',
            'https://varus.ua/maslo-solodkovershkove-selyanske-73-ferma-briket-180g',
            'https://shop.silpo.ua/product/maslo-solodkovershkove-ferma-selianske-73-840582',
            'https://novus.online/ru/product/maslo-solodkoverskove-selanske-73-ferma-briket-180g',
            'https://metro.zakaz.ua/ru/products/maslo-ferma-180g-ukrayina--04820234020706/',
            'https://shop.nashkraj.ua/kovel/product/371643-maslo-ferma-73-180g-selyanske',
            'https://fozzyshop.ua/ru/maslo/93829-maslo-sladkoslivochnoe-ferma-selskoe-73-4820239242653.html'
        ])

    def maslo_sliv_ferma_chocolat_62jir_180gr_parser(self):
        ''' Парсер для Масло сладкосливочное Ферма Шоколадное с какао 62.5%, 180 г'''
        return self.prices_parsing([
            'https://varus.ua/maslo-solodkovershkove-z-kakao-shokoladne-62-5-ferma-180g',
            'https://shop.silpo.ua/product/maslo-solodkovershkove-ferma-shokoladne-z-kakao-62-5-840586',
            'https://shop.nashkraj.ua/kovel/product/393090-maslo-ferma-62-5-180g-shokoladne',
            'https://fozzyshop.ua/ru/maslo/102847-maslo-sladkoslivochnoe-ferma-shokoladnoe-s-kakao-625-4820239240451.html'
        ])

    def maslo_sliv_ferma_extra_82_5jir_180gr_parser(self):
        ''' Парсер для Масло сладкосливочное Ферма экстра 82,5%, 180 г'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/maslo-ferma-180g-ukrayina--04820239242721/',
            'https://varus.ua/maslo-solodkovershkove-ekstra-825-ferma-briket-180g',
            'https://shop.silpo.ua/product/maslo-solodkovershkove-ferma-ekstra-82-5-911503',
            'https://metro.zakaz.ua/ru/products/maslo-ferma-180g-ukrayina--04820239242721/',
            'https://fozzyshop.ua/ru/maslo/99721-maslo-sladkoslivochnoe-ferma-ekstra-825-0250014953315.html'
        ])

    def maslo_sliv_ferma_buter_63jir_180gr_parser(self):
        ''' Парсер для Масло сладкосливочное Ферма бутербродне 63%, 180 г'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/maslo-180-g-ferma-solodkoverskove-buterbrodne-63',
            'https://varus.ua/maslo-solodkovershkove-buterbrodne-63-ferma-briket-180g',
            'https://shop.silpo.ua/product/maslo-solodkovershkove-ferma-buterbrodne-63-840585',
            'https://shop.nashkraj.ua/kovel/product/373774-maslo-ferma-63-180g-buterbrodne',
        ])

    def maslo_sliv_ferma_selyanske_73jir_400gr_parser(self):
        ''' Парсер для Масло сладкосливочное Ферма Сельское 73%, 400г'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/maslo-400g-ferma-solodkoverskove-selanske-73',
            'https://eko.zakaz.ua/uk/products/maslo-ferma-400g-ukrayina--04820239242691/',
            'https://shop.silpo.ua/product/maslo-solodkovershkove-ferma-selianske-73-567021',
            'https://shop.nashkraj.ua/kovel/product/178049-maslo-ferma-73-400g-selyanske-soldk',
        ])

    def maslo_sliv_jagotinske_extra_82_5_180gr_parser(self):
        ''' Парсер для Масло сладкосливочное Яготинське Экстра 82,5%, 180г'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/maslo-180-g-agotinske-solodkoverskove-ekstra-825-folga',
            'https://eko.zakaz.ua/uk/products/maslo-iagotin-180g-ukrayina--04823005209065/',
            'https://varus.ua/maslo-82-5-yagotinskoe-180g',
            'https://shop.silpo.ua/product/maslo-solodkovershkove-yagotynske-ekstra-82-5-874616',
            'https://novus.online/ru/product/maslo-825-solodkovershkove-ekstra-yahotyn-180h',
            'https://metro.zakaz.ua/ru/products/maslo-iagotin-200g--04823005202103/',
            'https://shop.nashkraj.ua/kovel/product/449585-maslo-yagotinske-82-5-180g-ekstra',
            'https://fozzyshop.ua/ru/maslo/89006-maslo-sladkoslivochnoe-yagotinske-ekstra-825-4823005209065.html'
        ])

    def maslo_sliv_jagotinske_buter_69_2_200gr_parser(self):
        ''' Парсер для Масло сладкосливочное Яготинське бутербродне 69.2%, 200г'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/maslo-iagotin-200g--04823005202127/',
            'https://shop.silpo.ua/product/maslo-vershkove-yagotynske-69-2-7924',
            'https://fozzyshop.ua/ru/maslo/9926-maslo-slivochnoe-yagotinske-692-4823005202127.html'
        ])

    def maslo_sliv_selyanske_extra_82_180gr_parser(self):
        ''' Парсер для Масло Селянське солодковершкове экстра 82%, 180 г'''
        return self.prices_parsing([
            'https://varus.ua/maslo-ekstra-82-selyanske-200g',
            'https://shop.silpo.ua/product/maslo-selianske-solodkovershkove-ekstra-82-914280',
            'https://novus.online/ru/product/maslo-solodkovershkove-ekstra-volohodske-82-selyanske-180h',
            'https://metro.zakaz.ua/ru/products/maslo-180g-ukrayina--04820254400373/',
            'https://fozzyshop.ua/ru/maslo/99715-maslo-selyanske-solodkovershkove-ekstra-82-0250015016774.html'
        ])

    def maslo_sliv_selyanske_buter_63_180gr_parser(self):
        ''' Парсер для Масло Селянське сладкосливочное бутербродное 63%, 180 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/maslo-selianske-solodkovershkove-buterbrodne-63-914278',
            'https://fozzyshop.ua/ru/maslo/99713-maslo-selyanske-sladkoslivochnoe-buterbrodnoe-63-0250015016750.html'
        ])

    def maslo_sliv_selyanske_72_5_180gr_parser(self):
        ''' Парсер для Масло Селянське сладкосливочное 72.5%, 180 г'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/maslo-selianske--04820254400410/',
            'https://varus.ua/maslo-solodkovershkove-72-5-selyanske-200g',
            'https://metro.zakaz.ua/ru/products/maslo-selianske--04820254400410/'
        ])

    def maslo_sliv_globino_extra_82_500gr_parser(self):
        ''' Парсер для Масло Глобино Экстра сладкосливочное 82%, 500г'''
        return self.prices_parsing([
            'https://fozzyshop.ua/ru/maslo/97905-maslo-globino-ekstra-sladkoslivochnoe-82-4820029570614.html'
        ])

    def maslo_sliv_globino_bezlaktoz_82_180gr_parser(self):
        ''' Парсер для Масло сладкосливочное Глобино безлактозное 82%, 180г'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/maslo-globino-180g--04820029571086/',
            'https://fozzyshop.ua/ru/maslo/96476-maslo-sladkoslivochnoe-globino-bezlaktoznoe-82-9920000017901.html'
        ])

    def maslo_sliv_galichina_82_5_180gr_parser(self):
        ''' Парсер для Масло сладкосливочное Галичина 82,5%, 180г'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/maslo-180-g-galicina-solodkoverskove-ekstra-825',
            'https://eko.zakaz.ua/uk/products/maslo-galichina-180g-ukrayina--04820222762137/',
            'https://varus.ua/maslo-82-5-solodkovershkove-ekstra-galichina-mu-200g',
            'https://shop.silpo.ua/product/maslo-solodkovershkove-galychyna-82-5-892644',
            'https://novus.online/ru/product/maslo-solodkovershkove-ekstra-825-zhyru-halychyna-180h',
            'https://shop.nashkraj.ua/kovel/product/480014-maslo-galichina-82-5-180g-solodkov-eks',
            'https://fozzyshop.ua/ru/maslo/96475-maslo-sladkoslivochnoe-galichina-825-4820222762199.html'
        ])

    def maslo_sliv_galichina_selyanske_72_6_180gr_parser(self):
        ''' Парсер для Масло солодковершкове «Галичина» «Селянське» 72,6%'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/maslo-galichina-180g-ukrayina--04820222762144/',
            'https://varus.ua/maslo-72-6-solodkovershkove-selyanske-galichina-mu-200g',
            'https://shop.silpo.ua/product/maslo-solodkovershkove-galychyna-selianske-72-6-892643',
            'https://novus.online/ru/product/maslo-solodkovershkove-selyanske-726-zhyru-halychyna-180h',
            'https://shop.nashkraj.ua/kovel/product/480015-maslo-galichina-72-6-180g-selyansk-solodk',
        ])

    def maslo_sliv_malokiya_82_180gr_parser(self):
        ''' Парсер для Масло сладкосливочное Молокія Экстра 82%, 180г'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/maslo-180-g-molokia-solodkoverskove-ekstra-82',
            'https://eko.zakaz.ua/uk/products/maslo--04820045705106/',
            'https://shop.silpo.ua/product/maslo-solodkovershkove-molokiia-ekstra-82-878789',
            'https://novus.online/ru/product/maslo-ekstra-82-molokiya-folha-180h',
            'https://metro.zakaz.ua/ru/products/maslo--04820045705106/',
            'https://shop.nashkraj.ua/kovel/product/454586-maslo-molokiya-82-180g-ekstra-folga',
            'https://fozzyshop.ua/ru/maslo/90991-maslo-sladkoslivochnoe-molokiya-ekstra-82-4820045705106.html'
        ])

    def maslo_sliv_farm_fresh_extra_82_180gr_parser(self):
        ''' Парсер для Масло Farm Fresh Екстра вершкове 82%, 180 г'''
        return self.prices_parsing([
            'https://fozzyshop.ua/maslo/101346-maslo-farm-fresh-ekstra-slivochnoe-82-0250015156593.html'
        ])

    def maslo_sliv_farm_fresh_selyanske_73_180gr_parser(self):
        ''' Парсер для Масло Farm Fresh Селянське вершкове 73%, 180 г'''
        return self.prices_parsing([
            'https://fozzyshop.ua/maslo/103719-maslo-farm-fresh-krestyanskoe-slivochnoe-73-0250015156609.html'
        ])

    def maslo_sliv_president_82_200gr_parser(self):
        ''' Парсер для Масло President солодковершкове 82%, 200г'''
        return self.prices_parsing([
            'https://varus.ua/maslo-82-nesolone-prezident-200g',
            'https://shop.silpo.ua/product/maslo-kyslovershkove-president-82-82983',
            'https://novus.online/ru/product/maslo-verskove-president-82-200g',
            'https://metro.zakaz.ua/ru/products/maslo-prezident-200g--03228022910023/',
            'https://fozzyshop.ua/maslo/18695-maslo-president-kisloslivochnoe-82-3228022910023.html'
        ])

    def maslo_sliv_president_82_400gr_parser(self):
        ''' Парсер для Масло President солодковершкове 82%, 400г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/maslo-kyslovershkove-president-ekstra-82-408658',
            'https://metro.zakaz.ua/ru/products/maslo-prezident-400g--04823065700151/',
            'https://fozzyshop.ua/maslo/18697-maslo-president-kisloslivochnoe-ekstra-82-3228022970195.html'
        ])

    def maslo_sliv_president_solone_80_200gr_parser(self):
        ''' Парсер для Масло President солодковершкове солоне 80%, 200г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/maslo-kyslovershkove-president-solone-80-424674',
            'https://fozzyshop.ua/maslo/18696-maslo-president-kisloslivochnoe-solyonoe-80-3228020355741.html'
        ])

    def jacobs_monarch_banka_95gr_parser(self):
        ''' Парсер для Кава розчинна Jacobs Monarch натуральна сублімована с/б, 95г'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/kava-95g-jacobs-monarch-rozcinna-sublimovana',
            'https://eko.zakaz.ua/uk/products/kava-iakobz-95g--04820206290885/',
            'https://varus.ua/kava-naturalna-rozchinna-sublimovana-jacobs-monarch-95-g',
            'https://shop.silpo.ua/product/kava-rozchynna-jacobs-monarch-naturalna-sublimovana-s-b-579161',
            'https://auchan.ua/ua/kofe-rastvorimyj-jacobs-monarch-95-g-242640/',
            'https://novus.online/ru/product/kava-akobz-monarh-rozcinna-95g',
            'https://metro.zakaz.ua/ru/products/kava-iakobz-95g--04820206290885/',
            'https://shop.nashkraj.ua/kovel/product/204698-kava-jacobs-monarkh-95g-rozch-s-b',
            'https://fozzyshop.ua/kofe-rastvorimyj/31329-kofe-rastvorimyj-jacobs-monarch-naturalnyj-sublimirovannyj-s-b-7622210324078.html'
        ])

    def jacobs_monarch_banka_190gr_parser(self):
        ''' Парсер для Кава розчинна Jacobs Monarch натуральна сублімована с/б, 190г'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/kava-190g-jacobs-monarch-rozcinna-sublimovana',
            'https://eko.zakaz.ua/uk/products/kava-iakobz-190g--04820206290908/',
            'https://varus.ua/kava-naturalna-rozchinna-sublimovana-jacobs-monarch-190-g',
            'https://shop.silpo.ua/product/kava-rozchynna-jacobs-monarch-naturalna-sublimovana-s-b-579164',
            'https://novus.online/ru/product/kava-akobz-monarh-rozcinna-190g',
            'https://shop.nashkraj.ua/kovel/product/204702-kava-jacobs-monarkh-190g-rozchinna',
        ])

    def jacobs_monarch_banka_200gr_parser(self):
        ''' Парсер для Кава розчинна Jacobs Monarch натуральна сублімована с/б, 200г'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/kava-200-g-jacobs-monarch-rozcinna-sublimovana',
            'https://eko.zakaz.ua/uk/products/kava-iakobz-200g--08711000513880/',
            'https://auchan.ua/ua/kofe-rastvorimyj-jacobs-monarch-200-g-1079192/'
        ])

    def jacobs_monarch_banka_100gr_parser(self):
        ''' Парсер для Кава розчинна Jacobs Monarch натуральна сублімована с/б, 100г'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/kava-iakobz-100g-nimechchina--08711000513859/',
            'https://auchan.ua/ua/kofe-rastvorimyj-jacobs-monarch-100-g-830698-1083763/',
        ])

    def jacobs_monarch_banka_50gr_parser(self):
        ''' Парсер для Кава розчинна Jacobs Monarch натуральна сублімована с/б, 50г'''
        return self.prices_parsing([
            'https://auchan.ua/ua/kofe-rastvorimyj-jacobs-monarch-v-banke-50-g-503709/',
            'https://novus.online/ru/product/kava-akobz-monarh-rozcinna-48g',
            'https://shop.nashkraj.ua/kovel/product/204701-kava-jacobs-monarkh-48g-rozch'
        ])

    def jacobs_monarch_classico_pack_225gr_parser(self):
        ''' Парсер для Кава мелена Jacobs Monarch Classico 225 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-melena-jacobs-monarch-classico-757346',
            'https://auchan.ua/ua/kofe-molotyj-jacobs-classic-225-g-274192/'
        ])

    def jacobs_barista_strong_pack_225gr_parser(self):
        ''' Парсер для Кава мелена Jacobs Barista Strong 225 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-melena-jacobs-barista-strong-797543',
            'https://auchan.ua/ua/kofe-molotyj-jacobs-barista-editions-strong-225-g-503384/',
            'https://shop.nashkraj.ua/kovel/product/326684-kava-jacobs-225g-barista-strong-mel'
        ])

    def jacobs_kronung_500gr_parser(self):
        ''' Парсер для 	Кава мелена Jacobs Kronung 500 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-melena-jacobs-kronung-896014'
        ])

    def jacobs_monarch_classico_pack_70gr_parser(self):
        ''' Парсер для Кава мелена Jacobs Monarch Classico 70 г'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/kava-iakobz-70g--08714599101834/',
            'https://varus.ua/kava-smazh-mel-monarch-classic-jacobs-70g',
            'https://shop.silpo.ua/product/kava-melena-jacobs-monarch-classico-757345',
            'https://novus.online/product/kava-naturalna-smazena-melena-akobz-monarh-klasik-70g'
        ])

    def jacobs_monarch_intense_200gr_parser(self):
        ''' Парсер для Кава мелена Jacobs Monarch Intense смажена 200 гр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/kava-iakobz-200g--08711000547038/',
            'https://shop.silpo.ua/product/kava-melena-jacobs-monarch-intense-smazhena-924622',
            'https://novus.online/product/kava-naturalna-smazhena-melena-jacobs-monarch-intense-200h',
            'https://metro.zakaz.ua/uk/products/kava-iakobz-200g--08711000547038/',
            'https://shop.nashkraj.ua/kovel/product/272915-kava-jacobs-monarkh-225g-intens-mel'
        ])

    def jacobs_espresso_230gr_parser(self):
        ''' Парсер для Кава мелена Jacobs Espresso 230 г'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/kava-230g-jacobs-monarch-espresso-melena',
            'https://eko.zakaz.ua/uk/products/kava-iakobz-230g--08714599106945/',
            'https://varus.ua/kava-melena-espreso-yakobz-230g',
            'https://shop.silpo.ua/product/kava-melena-jacobs-espresso-823825',
            'https://metro.zakaz.ua/uk/products/kava-iakobz-230g--08714599106945/',
            'https://shop.nashkraj.ua/kovel/product/236903-kava-jacobs-monarkh-230g-espreso-melena'
        ])

    def jacobs_barista_classic_pack_225gr_parser(self):
        ''' Парсер для Кава мелена Jacobs Barista Classic 225 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-melena-jacobs-varista-classic-797544',
            'https://auchan.ua/ua/kofe-molotyj-jacobs-barista-classic-225-g-503389/',
            'https://novus.online/product/kava-naturalna-smazena-melena-jacobs-barista-editions-classic-225g',
            'https://metro.zakaz.ua/uk/products/kava-iakobz-225g--08714599103821/'
        ])

    def jacobs_monarch_intense_400gr_parser(self):
        ''' Парсер для Кава мелена Jacobs Monarch Intense смажена 400 гр'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/kava-iakobz-400g-bolgariia--08711000547069/',
            'https://shop.silpo.ua/product/kava-melena-jacobs-monarch-intense-smazhena-924623',
            'https://auchan.ua/ua/kofe-molotyj-jacobs-monarch-intense-450-g-280914/',
            'https://novus.online/product/kava-naturalna-smazhena-melena-jacobs-monarch-intense-400h',
            'https://metro.zakaz.ua/uk/products/kava-iakobz-400g-bolgariia--08711000547069/'
        ])

    def jacobs_monarch_classico_pack_400gr_parser(self):
        ''' Парсер для Кава мелена Jacobs Monarch Classico 400 г'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/kava-iakobz-400g--08711000499979/',
            'https://shop.silpo.ua/product/kava-melena-jacobs-monarch-classic-smazhena-927091',
            'https://auchan.ua/ua/kofe-molotyj-jacobs-classic-450-g-274191/',
            'https://novus.online/product/kava-naturalna-smazhena-melena-jacobs-monarch-classic-400h',
            'https://metro.zakaz.ua/uk/products/kava-iakobz-400g--08711000499979/'
        ])

    def jacobs_monarch_rozch_60gr_parser(self):
        ''' Парсер для Кава 60г Jacobs Monarch розчинна сублімована'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/kava-60g-jacobs-monarch-rozcinna-sublimovana'
        ])

    def jacobs_monarch_rozch_425gr_parser(self):
        ''' Парсер для Кава 425г Jacobs Monarch розчинна сублімована'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/kava-425g-jacobs-monarch-rozcinna-sublimovana'
        ])

    def nescafe_gold_rozch_pack_165gr_parser(self):
        ''' Парсер для Кава розчинна Nescafe Gold натуральна 165 г'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/kava-neskafe-165g--07613037095982/',
            'https://varus.ua/kava-rozchinna-sublimovana-nescafe-gold-165-g',
            'https://shop.silpo.ua/product/kava-rozchynna-nescafe-gold-naturalna-786157',
            'https://auchan.ua/ua/kofe-rastvorimyj-nescafe-gold-165-g-503804/',
            'https://novus.online/ru/product/kava-rozcinna-neskafe-gold-mu-165g',
            'https://fozzyshop.ua/ru/kofe-rastvorimyj/62482-kofe-rastvorimyj-nescafe-gold-naturalnyj-7613037095982.html'

        ])

    def nescafe_gold_rozch_pack_310gr_parser(self):
        ''' Парсер для Кава розчинна Nescafe Gold натуральна 310 г'''
        return self.prices_parsing([
            'https://varus.ua/kava-nescafe-gold-rozchinna-310-g',
            'https://shop.silpo.ua/product/kava-rozchynna-nescafe-gold-sublimovana-928742',
            'https://novus.online/ru/product/kava-rozchynna-neskafe-hold-310h'
        ])

    def nescafe_classic_rozch_pack_170gr_parser(self):
        ''' Парсер для Кава розчинна Nescafe Classic 170 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-rozchynna-nescafe-classic-813560'
        ])

    def nescafe_gold_rozch_pack_360gr_parser(self):
        ''' Парсер для Кава розчинна Nescafe Gold натуральна сублімована 360 г'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/kava-neskafe-ukrayina--07613035932081/',
            'https://shop.silpo.ua/product/kava-rozchynna-nescafe-gold-naturalna-sublimovana-701592'
        ])

    def nescafe_classic_rozch_pack_30gr_parser(self):
        ''' Парсер для Кава розчинна Nescafe Classic у м'якій упаковці 30 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-rozchynna-nescafe-classic-u-m-iakii-upakovtsi-638371'
        ])

    def nescafe_gold_rozch_pack_30gr_parser(self):
        ''' Парсер для Кава розчинна Nescafe Gold у м'якій упаковці 30 г'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/kava-neskafe-30g--07613035444256/',
            'https://varus.ua/kava-rozchinna-sublimovana-nescafe-gold-30-g',
            'https://shop.silpo.ua/product/kava-rozchynna-nescafe-gold-m-iaka-upakovka-646270',
            'https://auchan.ua/ua/kofe-rastvorimyj-nescafe-gold-30-g-503649/',
            'https://shop.nashkraj.ua/kovel/product/218830-kava-nescafe-30g-gold-mu',
            'https://fozzyshop.ua/ru/kofe-rastvorimyj/12543-kofe-rastvorimyj-nescafe-gold-myagkaya-upakovka-7613035444256.html'
        ])

    def nescafe_gold_rozch_pack_60gr_parser(self):
        ''' Парсер для Кава розчинна Nescafe Gold у м'якій упаковці 60 г'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/kava-neskafe-60g--07613035524835/',
            'https://varus.ua/kava-rozchinna-sublimovana-nescafe-gold-60-g',
            'https://shop.silpo.ua/product/kava-rozchynna-nescafe-gold-663484',
            'https://auchan.ua/ua/kofe-nescafe-gold-60-g-215720/',
            'https://novus.online/ru/product/kava-naturalna-rozcinna-neskafe-gold-maka-upakovka-60g',
            'https://shop.nashkraj.ua/kovel/product/231303-kava-nescafe-60g-gold-m-u',
            'https://fozzyshop.ua/ru/kofe-rastvorimyj/3312-kofe-nescafe-gold-7613035524835.html'
        ])

    def nescafe_classic_rozch_pack_300gr_parser(self):
        ''' Парсер для Кава розчинна Nescafe Classic у м'якій упаковці 300 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-rozchynna-nescafe-classic-m-iaka-upakovka-50-g-bezkoshtovno-686892'
        ])

    def nescafe_gold_rozch_pack_260gr_parser(self):
        ''' Парсер для Кава розчинна Nescafe Gold у м'якій упаковці 260 г'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/kava-neskafe-260g--07613035526259/',
            'https://varus.ua/kava-nescafe-gold-naturalna-rozchinna-sublimovana-260-g',
            'https://shop.silpo.ua/product/kava-rozchynna-nescafe-gold-sublimovana-50-g-bezkoshtovno-686893',
            'https://auchan.ua/ua/kofe-rastvorimyj-nescafe-gold-260-g-503859/',
            'https://fozzyshop.ua/ru/kofe-rastvorimyj/38792-kofe-rastvorimyj-nescafe-gold-sublimir-50g-bespl-7613035526259.html'
        ])

    def carte_noire_pack_rozch_140gr_parser(self):
        ''' Парсер для Кава розчинна Carte Noire натуральна сублімована 140 г'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/kava-140g-carte-noire-rozcinna-sublimovana',
            'https://eko.zakaz.ua/uk/products/kava-kart-nuar-140g--08714599104194/',
            'https://varus.ua/kava-sublimovan-classic-carte-noire-140g',
            'https://shop.silpo.ua/product/kava-rozchynna-carte-noire-naturalna-sublimovana-783913',
            'https://auchan.ua/ua/kofe-rastvorimyj-carte-noire-classic-140-g-503988/',
            'https://novus.online/ru/product/kava-naturalna-rozcinna-sublimovana-kart-nuar-140g',
            'https://metro.zakaz.ua/ru/products/kava-kart-nuar-140g--08714599104194/'
        ])

    def carte_noire_pack_rozch_70gr_parser(self):
        ''' Парсер для Кава розчинна Carte Noire натуральна сублімована 70 г'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/kava-70g-carte-noire-rozcinna-sublimovana',
            'https://eko.zakaz.ua/uk/products/kava-kart-nuar-70g--04820187043654/',
            'https://shop.silpo.ua/product/kava-carte-noire-original-natur-rozch-sublim-p-e-597836',
            'https://novus.online/ru/product/kava-rozcinna-kart-nuar-ekonom-paket-70g',
            'https://metro.zakaz.ua/ru/products/kava-kart-nuar-70g--04820187043654/'
        ])

    def carte_noire_caramel_pack_rozch_120gr_parser(self):
        ''' Парсер для Кава розчинна Carte Noire Caramel сублімована 120 г'''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/kava-120-g-carte-noire-zi-smakom-karameli-naturalna-rozcinna-sublimovana-mup',
            'https://eko.zakaz.ua/uk/products/kava-kart-nuar-120g--08714599620274/',
            'https://shop.silpo.ua/product/kava-rozchynna-carte-noire-caramel-sublimovana-926067',
            'https://novus.online/ru/product/kava-naturalna-rozchynna-sublimovana-kart-nuar-zi-smakom-karameli-120h',
            'https://metro.zakaz.ua/ru/products/kava-kart-nuar-120g--08714599620274/'
        ])

    def carte_noire_rozch_pack_210gr_parser(self):
        ''' Парсер для Кава розчинна Carte Noire натуральна сублімована 210 г'''
        return self.prices_parsing([
            'https://varus.ua/kava-rozchinna-carte-noire-classic-210-g',
            'https://shop.silpo.ua/product/kava-rozchynna-carte-noire-naturalna-sublimovana-783914',
            'https://auchan.ua/ua/kofe-rastvorimyj-carte-noire-classic-210-g-503978/',
            'https://novus.online/ru/product/kava-naturalna-rozcinna-sublimovana-kart-nuar-210g'
        ])

    def carte_noire_rozch_pack_280gr_parser(self):
        ''' Парсер для Кава розчинна Carte Noire натуральна сублімована 280 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-rozchynna-carte-noire-classic-sublimovana-210-70-g-881354',
            'https://auchan.ua/ua/kofe-rastvorimyj-carte-noire-classic-210-g-70-g-927576/',
            'https://metro.zakaz.ua/ru/products/kava-kart-nuar-210g--08714599620014/'
        ])

    def ambassador_premium_rozch_pack_50gr_parser(self):
        ''' Парсер для Кава розчинна Ambassador Premium 50 г'''
        return self.prices_parsing([
            'https://varus.ua/kava-rozchinna-premium-ambassador-50g',
            'https://shop.silpo.ua/product/kava-rozchynna-ambassador-premium-894365',
            'https://auchan.ua/ua/kofe-ambassador-premium-rastvorimyj-50-g-1299004/',
            'https://novus.online/ru/product/kava-rozchynna-ambassador-premium-paket-50h'
        ])

    def ambassador_premium_rozch_pack_100gr_parser(self):
        ''' Парсер для Кава розчинна Ambassador Premium 100 г'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/kava--08720254065663/',
            'https://varus.ua/kava-rozchinna-premium-ambassador-100g',
            'https://shop.silpo.ua/product/kava-rozchynna-ambassador-premium-naturalna-sublimovana-859091',
            'https://auchan.ua/ua/kofe-rastvorimyj-sublimirovannyj-ambassador-premium-100-g-890211/',
            'https://metro.zakaz.ua/ru/products/kava--08720254065663/'
        ])

    def ambassador_premium_rozch_pack_250gr_parser(self):
        ''' Парсер для Кава розчинна Ambassador Premium 250 г'''
        return self.prices_parsing([
            'https://varus.ua/kofe-rastvorimyj-ambassador-premium-200g-50g',
            'https://shop.silpo.ua/product/kava-rozchynna-ambassador-premium-naturalna-sublimovana-859093',
            'https://novus.online/ru/product/kava-naturalna-rozchynna-sublimovana-premium-ambassador-dp-250h',
            'https://metro.zakaz.ua/ru/products/kava-ambassador-250g-ukrayina--08720254065700/'
        ])

    def ambassador_premium_rozch_pack_170gr_parser(self):
        ''' Парсер для Кава розчинна Ambassador Premium 170 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-rozchynna-ambassador-premium-naturalna-sublimovana-859092',
            'https://auchan.ua/ua/kofe-rastvorimyj-ambassador-premium-170-g-784371/',
            'https://metro.zakaz.ua/ru/products/kava-ambassador--08720254065687/'
        ])

    def ambassador_premium_rozch_pack_400gr_parser(self):
        ''' Парсер для Кава розчинна Ambassador Premium 400 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-rozchynna-ambassador-premium-300-100-g-917590',
            'https://auchan.ua/ua/kofe-rastvorimyj-ambassador-premium-400-g-1085591/',
            'https://metro.zakaz.ua/ru/products/kava-ambassador--08720254065427/'
        ])

    def ambassador_premium_rozch_pack_500gr_parser(self):
        ''' Парсер для Кава розчинна Ambassador Premium 500 г'''
        return self.prices_parsing([
            'https://auchan.ua/ua/kofe-ambassador-premium-rastvorimyj-500-g-1299074/',
            'https://metro.zakaz.ua/ru/products/kava-ambassador-500g--08720254065748/'
        ])

    def chorna_carta_gold_rozch_pack_200gr_parser(self):
        ''' Парсер для Кава розчинна «Чорна карта» Gold 200 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-rozchynna-chorna-karta-gold-843946',
            'https://auchan.ua/ua/kofe-natural-nyj-rastvorimyj-sublimirovannyj-gold-chorna-karta-200-g-732173-900246/',
            'https://metro.zakaz.ua/ru/products/kava-chorna-karta-200g--08720254065304/'
        ])

    def chorna_carta_gold_rozch_pack_100gr_parser(self):
        ''' Парсер для Кава розчинна «Чорна карта» Gold 100 г'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/kava--08720254065762/',
            'https://shop.silpo.ua/product/kava-rozchynna-chorna-karta-gold-paket-874035',
            'https://auchan.ua/ua/kofe-rastvorimyj-sublimirovannyj-chorna-karta-gold-100-g-890218/',
            'https://novus.online/ru/product/kava-rozchynna-chorna-karta-gold-paket-100h'
        ])

    def tchibo_gold_selection_rozch_glass_jar_50gr_parser(self):
        ''' Парсер для Кава Tchibo Gold Selection с/б 50 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-tchibo-gold-selection-s-b-199729',
            'https://auchan.ua/ua/kofe-rastvorimyj-tchibo-gold-selection-50-g-503704/',
            'https://novus.online/ru/product/kava-rozcinna-tchibo-gold-select-50g'
        ])

    def tchibo_gold_selection_rozch_glass_jar_100gr_parser(self):
        ''' Парсер для Кава Tchibo Gold Selection с/б 100 г'''
        return self.prices_parsing([
            'https://varus.ua/kava-rozchinna-tchibo-gold-selection-100-g',
            'https://shop.silpo.ua/product/kava-tchibo-gold-selection-199728',
            'https://auchan.ua/ua/kofe-rastvorimyj-tchibo-gold-selection-v-banke-100-g-503809/',
            'https://novus.online/ru/product/kava-rozcinna-tchibo-gold-selection-100g',
            'https://metro.zakaz.ua/ru/products/kava-chibo-100g--04006064010111/'
        ])

    def tchibo_gold_selection_rozch_glass_jar_200gr_parser(self):
        ''' Парсер для Кава Tchibo Gold Selection с/б 200 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-rozchynna-tchibo-gold-selection-737260',
            'https://auchan.ua/ua/kofe-rastvorimyj-tchibo-gold-selection-v-banke-200-g-503854/',
            'https://metro.zakaz.ua/uk/products/kava-chibo-200g-nimechchina--04046234596236/'
        ])

    def tchibo_exclusive_rozch_glass_jar_200gr_parser(self):
        ''' Парсер для Кава Tchibo Exclusive с/б 200 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-tchibo-exclusive-s-b-4502',
            'https://auchan.ua/ua/kofe-rastvorimyj-tchibo-exclusive-v-banke-200-g-503894/'
        ])

    def aroma_gold_decaff_rozch_glass_jar_100gr_parser(self):
        ''' Парсер для Кава Aroma Gold без кофеїну розчинна 100 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-aroma-gold-bez-kofeinu-rozchynna-895294',
            'https://fozzyshop.ua/kofe-rastvorimyj/96877-kofe-aroma-gold-bez-kofeina-rastvorimyj-4771632312002.html'
        ])

    def aroma_gold_freeze_dried_rozch_glass_jar_100gr_parser(self):
        ''' Парсер для Кава Aroma Gold розчинна Freeze-dried 100 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-aroma-gold-rozchynna-895288',
            'https://novus.online/product/kava-rozchynna-cublimovana-aroma-gold-95h',
            'https://shop.nashkraj.ua/kovel/product/471519-kava-aroma-gold-95g-sublimovaniy',
            'https://fozzyshop.ua/kofe-rastvorimyj/97591-kofe-aroma-gold-rastvorimyj-0250014775382.html'
        ])

    def aroma_gold_freeze_dried_rozch_glass_jar_200gr_parser(self):
        ''' Парсер для Кава Aroma Gold розчинна Freeze-dried 200 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-rozchynna-aroma-gold-902627'
        ])

    def maccoffee_arabica_rozch_glass_jar_120gr_parser(self):
        ''' Парсер для Кава розчинна MacCoffee Arabica натуральна сублімована 120 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-rozchynna-maccoffee-arabica-naturalna-sublimovana-857465',
            'https://auchan.ua/ua/kofe-maccoffee-arabica-rastvorimyj-120-g-1299308/',
            'https://novus.online/product/kava-rozchynna-arabika-maccoffee-120h',
            'https://metro.zakaz.ua/uk/products/kava--08887290146135/'
        ])

    def maxwell_house_instant_mild_blend_rozch_glass_jar_100gr_parser(self):
        ''' Парсер для Кава розчинна Maxwell House Instant Mild Blend 100 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-rozchynna-maxwell-house-instant-mild-blend-896113',
            'https://fozzyshop.ua/kofe-rastvorimyj/102041-kofe-rastvorimyj-maxwell-house-instant-mild-blend-8711000516706.html'
        ])

    def maxwell_house_instant_mild_blend_rozch_glass_jar_200gr_parser(self):
        ''' Парсер для Кава розчинна Maxwell House Instant Mild Blend 200 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-rozchynna-maxwell-house-instant-mild-blend-896112',
            'https://fozzyshop.ua/kofe-rastvorimyj/102044-kofe-rastvorimyj-maxwell-house-instant-mild-blend-8711000516881.html'
        ])

    def dallmayr_gold_rozch_glass_jar_100gr_parser(self):
        ''' Парсер для Кава розчинна Dallmayr Gold натуральна сублімована 100 г'''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/kava-rozchynna-dallmayr-gold-naturalna-sublimovana-923324'
        ])

    def dallmayr_gold_rozch_glass_jar_200gr_parser(self):
        ''' Парсер для Кава розчинна Dallmayr Gold натуральна сублімована 200 г'''
        return self.prices_parsing([
            'https://metro.zakaz.ua/uk/products/kava-dallmaier-200g--04008167270508/'
        ])

    def aroma_platinum_fr_dr_rozch_glass_jar_200gr_parser(self):
        ''' Парсер для Кава Aroma Platinum розчинна, 200г'''
        return self.prices_parsing([
            'https://fozzyshop.ua/kofe-rastvorimyj/97565-kofe-aroma-platinum-rastvorimyj-4771632310862.html'
        ])

    def aroma_platinum_fr_dr_rozch_glass_jar_100gr_parser(self):
        ''' Парсер для Кава Aroma Platinum розчинна, 100г'''
        return self.prices_parsing([
            'https://fozzyshop.ua/kofe-rastvorimyj/97564-kofe-aroma-platinum-rastvorimyj-4771632086019.html'
        ])

    def beanies_mince_pie_rozch_glass_jar_50gr_parser(self):
        ''' Парсер для Кава розчинна Beanies Mince Pie с/б, 50г'''
        return self.prices_parsing([
            'https://fozzyshop.ua/kofe-rastvorimyj/102046-kofe-rastvorimyj-beanies-mince-pie-s-b-5060169984264.html'
        ])

    def beanies_cristmas_pudding_rozch_glass_jar_50gr_parser(self):
        ''' Парсер для Кава розчинна Beanies Christmas Pudding с/б, 50г'''
        return self.prices_parsing([
            'https://fozzyshop.ua/kofe-rastvorimyj/102045-kofe-rastvorimyj-beanies-christmas-pudding-s-b-5060169982154.html'
        ])

    def beanies_double_chocolate_rozch_glass_jar_50gr_parser(self):
        ''' Парсер для Кава розчинна Beanies Double Chocolate с/б, 50г'''
        return self.prices_parsing([
            'https://fozzyshop.ua/kofe-rastvorimyj/73892-kofe-rastvorimyj-beanies-double-chocolate-s-b-5060169982031.html'
        ])

    def beanies_cinder_toffee_rozch_glass_jar_50gr_parser(self):
        ''' Парсер для 	Кава розчинна Beanies Cinder Toffee с/б, 50г'''
        return self.prices_parsing([
            'https://fozzyshop.ua/kofe-rastvorimyj/73891-kofe-rastvorimyj-beanies-cinder-toffee-s-b-5060169982116.html'
        ])

    def bushido_kodo_rozch_glass_jar_95gr_parser(self):
        ''' Парсер для 	Кава розчинна Bushido Kodo с/б, 95г'''
        return self.prices_parsing([
            'https://fozzyshop.ua/kofe-rastvorimyj/90305-kofe-rastvorimyj-bushido-kodo-s-b-5060367340176.html'
        ])

    def davidoff_rich_aroma_rozch_glass_jar_100gr_parser(self):
        ''' Парсер для Кава Davidoff Rich Aroma, 100г'''
        return self.prices_parsing([
            'https://auchan.ua/ua/kofe-rastvorimyj-davidoff-cafe-rich-aroma-100-g-503983/',
            'https://novus.online/product/kava-rozcinna-davidoff-rich-aroma-sb-100g',
            'https://fozzyshop.ua/kofe-rastvorimyj/3347-kofe-davidoff-rich-aroma-4006067084188.html'
        ])

    def davidoff_fine_aroma_rozch_glass_jar_100gr_parser(self):
        ''' Парсер для Кава Davidoff Fine Aroma, 100г'''
        return self.prices_parsing([
            'https://auchan.ua/ua/kofe-rastvorimyj-davidoff-cafe-fine-aroma-v-banke-100-g-503998/'
        ])

    def ahmad_tea_eng_breakf_black_pack_100gr_parser(self):
        ''' Чай Ahmad tea «Англійський до сніданку» чорний 100 г лістовий '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-ahmad-tea-angliiskyi-do-snidanku-15186',
        ])

    def ahmad_tea_graf_grey_black_pack_100gr_parser(self):
        ''' Чай Ahmad tea «Граф Грей» чорний 100 г лістовий '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-ahmad-tea-graf-grei-31345'
        ])

    def ahmad_tea_london_black_pack_100gr_parser(self):
        ''' Чай Ahmad tea «Лондон» чорний 100 г лістовий '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-akhmad-100g--00054881025140/',
            'https://varus.ua/chay-ahmad-tea-london-chernyy-melkolistnyy-100-g',
            'https://shop.silpo.ua/product/chai-chornyi-ahmad-tea-london-905492'
        ])

    def ahmad_tea_english_n1_black_pack_100gr_parser(self):
        ''' Чай Ahmad tea «Англійський №1» чорний 100 г лістовий '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai--00054881006293/',
            'https://varus.ua/chay-ahmad-tea-no-1-chorniy-z-bergamotom-100g',
            'https://shop.silpo.ua/product/chai-ahmad-tea-angliiskyi-1-17524'
        ])

    def ahmad_tea_eng_breakf_black_pack_200gr_parser(self):
        ''' Чай Ahmad tea «Англійський до сніданку» чорний 200 г лістовий '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-akhmad-200g--00054881001434/',
            'https://shop.silpo.ua/product/chai-ahmad-tea-angliiskyi-snidanok-138346',
            'https://fozzyshop.ua/chaj-rassypnoj/3866-chaj-ahmad-tea-anglijskij-zavtrak-0054881001434.html'
        ])

    def ahmad_tea_graf_grey_black_pack_200gr_parser(self):
        ''' 	Чай Ahmad tea «Граф Грей» 200 г чорний листовий '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-akhmad-200g--00054881001410/',
            'https://shop.silpo.ua/product/chai-ahmad-tea-graf-grei-100419',
            'https://novus.online/product/caj-cornij-listovij-ahmad-earl-grey-200g',
            'https://fozzyshop.ua/chaj-rassypnoj/3833-chaj-ahmad-tea-graf-grej-0054881001410.html'
        ])

    def ahmad_tea_london_black_pack_100pk_parser(self):
        ''' Чай чорний Ahmad Tea «Лондон» байховий пакетований 100 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-akhmad-200g-ukrayina--00054881025164/',
            'https://varus.ua/chaj-ahmad-tea-london-chernyj-100-2g',
            'https://shop.silpo.ua/product/chai-chornyi-ahmad-tea-london-baikhovyi-879805',
            'https://fozzyshop.ua/chaj-rassypnoj/95812-chaj-chernyj-ahmad-tea-london-bajkhovyj-0250014448569.html'
        ])

    def ahmad_tea_graf_grey_black_pack_40pk_parser(self):
        ''' Чай Ahmad tea «Граф Грей» чорний пакетований 40 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-ahmad-tea-graf-grei-32330'
        ])

    def ahmad_tea_london_black_pack_25pk_parser(self):
        ''' Чай чорний Ahmad Tea «Лондон» байховий чорний пакетований 25 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-akhmad--00054881024969/',
            'https://varus.ua/chaj-ahmad-tea-london-chernyj-25-2g',
            'https://shop.silpo.ua/product/chai-chornyi-ahmad-tea-london-baikhovyi-879803'
        ])

    def ahmad_tea_lavanda_bergamot_black_pack_20pk_parser(self):
        ''' Чай чорний Ahmad tea з лавандою і бергамотом пакетований 20 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-chornyi-ahmad-tea-z-lavandoiu-i-bergamotom-dribnyi-781459'
        ])

    def ahmad_tea_eng_breakf_black_pack_25pk_parser(self):
        ''' Чай Ahmad tea Англійський сніданок чорний пакетований 25 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-akhmad-50g--00054881005906/',
            'https://varus.ua/chay-ahmad-english-breakfast-chorniy-25-paketik-v-po-2g',
            'https://shop.silpo.ua/product/chai-ahmad-tea-angliiskyi-snidanok-17530',
            'https://auchan.ua/ua/chaj-chernyj-ahmad-tea-english-breakfast-25-sht-516815/',
            'https://novus.online/product/caj-cornij-ahmad-anglijskij-do-snidanku-paket-za-2g25st',
            'https://fozzyshop.ua/chaj-v-paketikakh/3837-chaj-ahmad-tea-anglijskij-k-zavtraku-0054881005906.html'
        ])

    def ahmad_tea_english_n1_black_pack_25pk_parser(self):
        ''' Чай Ahmad tea «Англійський» №1 чорний пакетований 25 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-akhmad-50g--00054881005999/',
            'https://varus.ua/chaj-ahmad-english-tea-1-chornij-25-paketiv-po-2-g',
            'https://shop.silpo.ua/product/chai-ahmad-tea-angliiskyi-1-z-nytkoiu-33196',
            'https://novus.online/product/caj-cornij-ahmad-anglijskij-no1-paket-za-2g25st',
            'https://fozzyshop.ua/chaj-v-paketikakh/3867-chaj-ahmad-tea-anglijskij-1-s-nitkoj-0054881005999.html'
        ])

    def ahmad_tea_graf_grey_black_pack_25pk_parser(self):
        ''' Чай Ahmad tea «Граф Грей» чорний пакетований 25 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-ahmad-tea-graf-grei-27857',
            'https://fozzyshop.ua/chaj-v-paketikakh/3862-chaj-ahmad-tea-graf-grej-0054881009690.html'
        ])

    def ahmad_tea_london_black_pack_40pk_parser(self):
        ''' Чай чорний Ahmad Tea «Лондон» пакетований 40 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-akhmad-80g-ukrayina--00054881024976/',
            'https://shop.silpo.ua/product/chai-chornyi-ahmad-tea-london-baikhovyi-879804',
            'https://fozzyshop.ua/chaj-rassypnoj/95814-chaj-chernyj-ahmad-tea-london-bajkhovyj-0250014448552.html'
        ])

    def ahmad_tea_eng_breakf_black_pack_40pk_parser(self):
        ''' Чай Ahmad tea Англійський сніданок чорний пакетований 40 шт '''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/caj-42-fp-h-2-g-ahmad-tea-english-breakfast-cornij',
            'https://eko.zakaz.ua/uk/products/chai-akhmad-80g--00054881009188/',
            'https://varus.ua/chay-ahmad-tea-english-breakfast-chorniy-40-paketik-v-po-2g',
            'https://shop.silpo.ua/product/chai-ahmad-tea-angliiskyi-do-snidanku-31339',
            'https://auchan.ua/ua/chaj-chernyj-ahmad-tea-english-breakfast-40-sht-516850/',
            'https://novus.online/product/caj-cornij-ahmad-anglijskij-do-snidanku-paket-ba-2g40st'
        ])

    def ahmad_tea_english_n1_black_pack_40pk_parser(self):
        ''' Чай Ahmad tea «Англійський» №1 чорний пакетований 40 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-akhmad-80g--00054881006316/',
            'https://shop.silpo.ua/product/chai-ahmad-tea-angliiskyi-1-32332',
            'https://fozzyshop.ua/ru/chaj-v-paketikakh/3836-chaj-ahmad-tea-anglijskij-1-0054881006316.html'
        ])

    def ahmad_tea_eng_breakf_black_pack_100pk_parser(self):
        ''' Чай Ahmad tea Англійський сніданок чорний пакетований 100 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-akhmad-200g--00054881006002/',
            'https://shop.silpo.ua/product/chai-ahmad-tea-angliiskyi-do-snidanku-17531',
            'https://novus.online/product/caj-cornij-ahmad-breakfast-paket-za-2g100st',
            'https://fozzyshop.ua/ru/chaj-v-paketikakh/3835-chaj-ahmad-tea-anglijskij-k-zavtraku-0054881006002.html'
        ])

    def ahmad_tea_graf_grey_black_pack_100pk_parser(self):
        ''' Чай Ahmad tea «Граф Грей» чорний пакетований 100 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-ahmad-tea-graf-grei-465970',
            'https://fozzyshop.ua/ru/chaj-v-paketikakh/3832-chaj-ahmad-tea-graf-grej-0054881005951.html'
        ])

    def lipton_yellow_label_black_pack_25pk_parser(self):
        ''' Чай чорний Lipton Yellow Label пакетований 25 шт '''
        return self.prices_parsing([
            'https://varus.ua/chaj-lipton-yellow-label-chornij-25-2-g',
            'https://shop.silpo.ua/product/chai-chornyi-lipton-yellow-label-35727',
            'https://metro.zakaz.ua/ru/products/chai-lipton--08717163825976/'
        ])

    def lipton_earl_gray_black_pack_25pk_parser(self):
        ''' Чай чорний Lipton Earl Gray пакетований 25 шт '''
        return self.prices_parsing([
            'https://varus.ua/chaj-lipton-earl-grey-chornij-z-aromatom-bergamota-25-1-5-g',
            'https://shop.silpo.ua/product/chai-chornyi-lipton-earl-gray-37911',
            'https://metro.zakaz.ua/ru/products/chai-lipton--08720608016242/'
        ])

    def lipton_eng_breakf_black_pack_25pk_parser(self):
        ''' Чай чорний Lipton English Breakfast пакетований 25 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-chornyi-lipton-english-breakfast-683762'
        ])

    def lipton_gold_tea_black_pack_25pk_parser(self):
        ''' Чай чорний Lipton Gold Tea пакетований 25 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-chornyi-lipton-gold-tea-917450'
        ])

    def lipton_earl_grey_orange_black_pack_25pk_parser(self):
        ''' Чай чорний Lipton Earl Grey Orange пакетований 25 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-chornyi-lipton-earl-grey-orange-917462'
        ])

    def lipton_forest_fruits_black_pack_20pk_parser(self):
        ''' Чай чорний Lipton Forest Fruit з ароматом лісових ягід пакетований 20 шт '''
        return self.prices_parsing([
            'https://varus.ua/chaj-lipton-forest-fruit-chornij-20-1-7-g',
            'https://shop.silpo.ua/product/chai-chornyi-lipton-forest-fruit-z-aromatom-lisovykh-iagid-594013'
        ])

    def lipton_intense_black_black_pack_25pk_parser(self):
        ''' Чай чорний Lipton Intense Black пакетований 25 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-chornyi-lipton-intense-black-917479',
            'https://metro.zakaz.ua/ru/products/chai-lipton--08720608011971/'
        ])

    def lipton_peach_mango_black_black_pack_20pk_parser(self):
        ''' Чай чорний Lipton Peach & Mango пакетований 20 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-chornyi-lipton-peach-mango-734512'
        ])

    def lipton_yellow_label_black_pack_50pk_parser(self):
        ''' Чай чорний Lipton Yellow Label пакетований 50 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chail-chornyi-lipton-yellow-labe-37915',
            'https://metro.zakaz.ua/ru/products/chai-lipton--08711200461646/'
        ])

    def lipton_intense_black_black_pack_92pk_parser(self):
        ''' Чай чорний Lipton Intense Black пакетований 92 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-chornyi-lipton-intense-black-919782'
        ])

    def lipton_gold_tea_black_pack_92pk_parser(self):
        ''' Чай чорний Lipton Gold Tea пакетований 92 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-chornyi-lipton-gold-tea-919783'
        ])

    def lipton_yellow_label_black_pack_100pk_parser(self):
        ''' Чай чорний Lipton Yellow Label пакетований 100 шт '''
        return self.prices_parsing([
            'https://varus.ua/chaj-lipton-yellow-label-chornij-100-2-g'
        ])

    def lipton_earl_gray_black_pack_50pk_parser(self):
        ''' Чай чорний Lipton Earl Gray пакетований 50 шт '''
        return self.prices_parsing([
            'https://varus.ua/chaj-lipton-earl-grey-chornij-z-aromatom-bergamota-50-1-5-g'
        ])

    def lipton_intense_mint_green_pack_20pk_parser(self):
        ''' Чай зелений Lipton Intense Mint пакетований 50 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-zelenyi-lipton-intense-mint-917454'
        ])

    def lipton_raspberry_pomegranate_green_pack_20pk_parser(self):
        ''' Чай зелений Lipton Raspberry&Pomegranate пакетований 50 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-zelenyi-lipton-raspberry-pomegranate-917455'
        ])

    def lipton_classic_green_pack_25pk_parser(self):
        ''' Чай зелений Lipton Classic пакетований 50 шт '''
        return self.prices_parsing([
            'https://varus.ua/chaj-lipton-green-classic-zelenij-25-1-3-g',
            'https://shop.silpo.ua/product/chai-zelenyi-lipton-classic-917461'
        ])

    def batik_korol_std_black_pack_25pk_parser(self):
        ''' Чай чорний Batik Королівський стандарт ф/п 25 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-batik-50g--04820015833204/',
            'https://shop.silpo.ua/product/chai-chornyi-batik-korolivskyi-standart-f-p-360214'
        ])

    def batik_gold_earl_grey_black_pack_25pk_parser(self):
        ''' Чай чорний Batik Gold Ерл Грей з ароматом бергамота пакетований 25 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-batik-50g-polshcha--04820171919569/',
            'https://shop.silpo.ua/product/chai-chornyi-batik-gold-erl-grei-z-aromat-bergamota-926085'
        ])

    def batik_chorniy_barhat_black_pack_25pk_parser(self):
        ''' Чай чорний Batik Чорний бархат купажований дрібний 25 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-batik-50g--04820015837141/',
            'https://shop.silpo.ua/product/chai-chornyi-batik-chornyi-barkhat-kupazhovanyi-dribnyi-926082'
        ])

    def batik_jagidniy_cilynok_black_pack_25pk_parser(self):
        ''' Чай чорний Batik Ягідний цілунок купажований дрібн 25 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-batik-37-5g--04820171916537/',
            'https://shop.silpo.ua/product/chai-chornyi-batik-yagidnyi-tsilunok-kupazhovanyi-dribn-926086',
            'https://auchan.ua/ua/chaj-chernyj-batik-jagodnyj-poceluj-25-sht-515933/'
        ])

    def batik_badyoriy_limon_black_pack_25pk_parser(self):
        ''' Чай чорний Batik Бадьорий лимон купажований дрібн 25 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-batik-37-5g--04820171916612/',
            'https://shop.silpo.ua/product/chai-chornyi-batik-badoryi-lymon-kupazhovanyi-dribn-926083',
            'https://auchan.ua/ua/chaj-chernyj-batik-bodryj-limon-25-sht-515940/'
        ])

    def batik_gold_ceylon_visokogir_black_pack_25pk_parser(self):
        ''' Чай чорний Batik Gold цейлон високогірний дрібний 25 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-batik-50g-polshcha--04820171919552/',
            'https://shop.silpo.ua/product/chai-chornyi-batik-gold-tseilon-vysokogirnyi-dribnyi-926084'
        ])

    def batik_black_granul_standart_sts_100gr_parser(self):
        ''' Чай чорний Batik гранули С.Т.С. 100 грам '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-batik-100g-ukrayina--04820015831279/',
            'https://shop.silpo.ua/product/chai-chornyi-batik-granuly-s-t-s-1799'
        ])

    def batik_korol_std_black_100gr_parser(self):
        ''' Чай чорний Batik Королівський стандарт 100 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-batik-85g--04820015833228/',
            'https://shop.silpo.ua/product/chai-chornyi-batik-korolivskyi-standart-360213'
        ])

    def batik_chorniy_barhat_black_pack_60pk_parser(self):
        ''' Чай чорний Batik Чорний бархат купажований дрібний 60 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-chornyi-batik-chornyi-barkhat-kupazhovanyi-50-10-926087'
        ])

    def batik_korol_std_black_pack_100pk_parser(self):
        ''' Чай чорний Batik Королівський стандарт ф/п 100 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-batik-200g--04820015833785/',
            'https://shop.silpo.ua/product/chai-chornyi-batik-korolivskyi-standart-f-p-441018',
            'https://auchan.ua/ua/chaj-chernyj-batik-royal-standart-100-sht-516892/'
        ])

    def akbar_gold_black_25pk_parser(self):
        ''' Чай чорний Akbar Gold, пакет 25 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-chornyi-akbar-gold-paket-649675',
            'https://auchan.ua/ua/chaj-chernyj-akbar-gold-25-sht-516829/',
            'https://metro.zakaz.ua/ru/products/chai-akbar-50g--05014176014575/'
        ])

    def akbar_limon_lime_twist_black_pack_20pk_parser(self):
        ''' Чай чорний Akbar Lemon&Lime Twist 20 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-chornyi-akbar-lemon-lime-twist-885017',
            'https://auchan.ua/ua/chaj-chernyj-cejlonskij-bajhovyj-akbar-lemon-lime-twist-20h2-g-1098615/'
        ])

    def akbar_peach_passion_punch_black_pack_20pk_parser(self):
        ''' Чай чорний Akbar Peach&Passion Punch 20 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-chornyi-akbar-peach-passion-punch-885019',
            'https://auchan.ua/ua/chaj-chernyj-cejlonskij-akbar-peach-passion-punch-20h2-g-1098629/'
        ])

    def akbar_strawberry_kiwi_black_pack_20pk_parser(self):
        ''' Чай зелений китайський Akbar Strawberry Kiwi, 20х1.5 г '''
        return self.prices_parsing([
            'https://auchan.ua/ua/chaj-zelenyj-kitajskij-akbar-strawberry-kiwi-20h1-5-g-1098622/'
        ])

    def pickwick_english_black_pack_20pk_parser(self):
        ''' Чай чорний Pickwick English 20 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-pikvik--08711000008102/',
            'https://shop.silpo.ua/product/chai-chornyi-pickwick-english-907475',
            'https://auchan.ua/ua/chaj-chernyj-bajhovyj-pickwick-english-20h2-g-1098342/',
            'https://novus.online/ru/product/chay-chornyy-pickwick-english-202h'
        ])

    def pickwick_mango_black_pack_20pk_parser(self):
        ''' Чай чорний Pickwick Mango 20 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-pikvik--08711000296493/',
            'https://shop.silpo.ua/product/chai-chornyi-pickwick-aromatyzovanyi-zi-shmatochkamy-mango-907482',
            'https://auchan.ua/ua/chaj-chernyj-pickwick-mango-aromatizirovannyj-20h1-5-g-1098377/',
            'https://novus.online/ru/product/chay-chornyy-pickwick-mango-2015h',
            'https://metro.zakaz.ua/ru/products/chai-pikvik--08711000296493/'
        ])

    def pickwick_forest_fruit_black_pack_20pk_parser(self):
        ''' Чай чорний Pickwick Forest Fruit 20 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-pikvik-30g--08711000278468/',
            'https://shop.silpo.ua/product/chai-chornyi-pickwick-aromatyzovanyi-zi-shmatochkamy-lisovykh-iagid-907480',
            'https://auchan.ua/ua/chaj-chernyj-pickwick-s-kusochkami-lesnyh-jagod-20h1-5-g-1098601/',
            'https://novus.online/ru/product/chay-pickwick-lisovi-yahody-2015h'
        ])

    def pickwick_earl_grey_black_pack_20pk_parser(self):
        ''' Чай чорний Pickwick Earl Grey 20 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-pikvik--08711000008416/',
            'https://shop.silpo.ua/product/chai-chornyi-pickwick-earl-grey-z-aromatom-bergamota-907477',
            'https://auchan.ua/ua/chaj-chernyj-pickwick-earl-grey-s-aromatom-bergamota-20h2-g-1098356/',
            'https://novus.online/ru/product/chay-pickwick-earl-grey-z-berhamotom-202h'
        ])

    def pickwick_strawberry_black_pack_20pk_parser(self):
        ''' Чай чорний Pickwick Strawberry 20 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-pikvik-30g-niderlandi--08711000278703/',
            'https://varus.ua/chaj-pickwick-strawberry-chernyj-20-15-g',
            'https://shop.silpo.ua/product/chai-chornyi-pickwick-aromatyzovanyi-zi-shmatochkamy-polunytsi-907481',
            'https://auchan.ua/ua/chaj-chernyj-bajhovyj-pickwick-s-kusochkami-klubniki-20h1-5-g-1098608/',
            'https://novus.online/ru/product/chay-chornyy-pickwick-polunytsya-2015h'
        ])

    def pickwick_green_pure_green_pack_20pk_parser(self):
        ''' Чай зелений Pickwick Green 20 шт '''
        return self.prices_parsing([
            'https://auchan.ua/ua/chaj-zelenyj-bajhovyj-pickwick-pure-20h1-5-g-1098349/',
            'https://novus.online/ru/product/chay-zelenyy-pickwick-2015h',
            'https://metro.zakaz.ua/ru/products/chai-pikvik-30g--08711000294215/'
        ])

    def pickwick_mint_green_pack_20pk_parser(self):
        ''' Чай зелений Pickwick Mint 20 шт '''
        return self.prices_parsing([
            'https://auchan.ua/ua/chaj-mjatnyj-pickwick-herbal-20h1-5-g-1098370/',
            'https://novus.online/ru/product/chay-pickwick-myata-2015h',
            'https://metro.zakaz.ua/ru/products/chai-pikvik-30g--08711000336434/'
        ])

    def pickwick_romashka_green_pack_20pk_parser(self):
        ''' Чай зелений Pickwick ромашковий 20 шт '''
        return self.prices_parsing([
            'https://auchan.ua/ua/chaj-romashkovyj-pickwick-herbal-20h1-5-g-1098363/',
            'https://novus.online/ru/product/chay-pickwick-romashka-2015h',
            'https://metro.zakaz.ua/ru/products/chai-pikvik-30g--08711000336342/'
        ])

    def pickwick_spicy_chai_trav_pack_15pk_parser(self):
        ''' Чай зелений Pickwick Spicy Chai 15 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-pikvik--08711000483251/',
            'https://shop.silpo.ua/product/chai-pickwick-roibush-z-prianoshchamy-907486',
            'https://auchan.ua/ua/chaj-s-prjanostjami-pickwick-spicy-chai-joy-of-tea-rojbush-aromatizirovannyj-15h1-75-g-1098405/'
        ])

    def pickwick_romashka_trav_pack_15pk_parser(self):
        ''' Чай трав'яний Pickwick Ромашка 15 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-pikvik--08711000484241/',
            'https://shop.silpo.ua/product/chai-trav-ianyi-pickwick-vitaminnyi-romashka-907488',
            'https://auchan.ua/ua/chaj-fruktovo-travjanoj-aromatizirovannyj-pickwick-super-blends-shine-camomile-peach-liquorice-biotin-15h1-5-g-1098419/',
            'https://novus.online/ru/product/chay-travyanyy-pickwick-blysk-syayannya-1515h'
        ])

    def pickwick_imbir_pryan_trav_pack_15pk_parser(self):
        ''' Чай трав'яний Pickwick Імбірь 15 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-pikvik--08711000483190/',
            'https://shop.silpo.ua/product/chai-trav-ianyi-pickwick-imbirno-prianyi-907485',
            'https://auchan.ua/ua/chaj-travjanoj-pickwick-ginger-spices-joy-of-tea-aromatizirovannyj-15h1-75-g-1098398/'
        ])

    def pickwick_energy_trav_pack_15pk_parser(self):
        ''' Чай трав'яний Pickwick Energy 15 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-pikvik--08711000484272/',
            'https://shop.silpo.ua/product/chai-trav-ianyi-pickwick-vitaminnyi-lemongras-907489',
            'https://auchan.ua/ua/chaj-travjanoj-pickwick-super-blends-energy-curcuma-sea-buckthorn-berry-lemongrass-vitamin-b6-15h1-5-g-1098426/',
            'https://novus.online/ru/product/chay-travyanyy-pickwick-enerhiya-1515h'
        ])

    def pickwick_immunity_trav_pack_15pk_parser(self):
        ''' Чай трав'яний Pickwick Immunity 15 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-pikvik--08711000484302/',
            'https://shop.silpo.ua/product/chai-trav-ianyi-pickwick-vitaminnyi-verbena-ekhinatseia-907490',
            'https://auchan.ua/ua/chaj-travjanoj-aromatizirovannyj-pickwick-super-blends-immunity-ginger-echinacea-lemon-verbena-vitamin-c-15h1-5-g-1098433/',
            'https://novus.online/ru/product/chay-travyanyy-pickwick-imunitet-1515h'
        ])

    def pickwick_earl_grey_citrus_trav_pack_15pk_parser(self):
        ''' Чай трав'яний Pickwick Earl Grey Citrus 15 шт '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/chai-pikvik--08711000483312/',
            'https://novus.online/ru/product/chay-chornyy-pickwick-erl-hrey-tsytrus-15175'
        ])

    def pickwick_citrus_buzina_trav_pack_20pk_parser(self):
        ''' Чай трав'яний Pickwick Citrus-Buzina 20 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-fruktovo-trav-ianyi-pickwick-tsytrus-buzyna-907483',
            'https://novus.online/ru/product/chay-pickwick-tsytrus-ta-buzyna-202h'
        ])

    def pickwick_imbir_lemon_citrus_trav_pack_20pk_parser(self):
        ''' Чай трав'яний Pickwick ginger-lemon-lemongrass 20 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-fruktovo-trav-ianyi-pickwick-imbyr-lemongras-907484'
        ])

    def azerchay_bergamot_black_pack_25pk_parser(self):
        ''' Чай чорний Azercay з ароматом бергамота середньолистовий 25 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-chornyi-azercay-z-aromatom-bergamota-serednolystovyi-580329',
            'https://auchan.ua/ua/chaj-chernyj-azercay-s-bergamotom-25-sht-516213/',
            'https://novus.online/ru/product/caj-cornij-azercay-z-bergamotom-2g25st',
            'https://metro.zakaz.ua/ru/products/chai-azerkai-50g--04760062100938/'
        ])

    def azerchay_buket_black_pack_25pk_parser(self):
        ''' Чай чорний Azercay Buket 25 шт '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/chai-chornyi-azercay-buket-krupnolystovyi-580328',
            'https://auchan.ua/ua/chaj-chernyj-azercay-buket-25-sht-516178/',
            'https://novus.online/ru/product/caj-cornij-azercay-extra-2g25st',
            'https://fozzyshop.ua/ru/chaj-v-paketikakh/61152-chaj-chernyj-azercay-buket-krupnolistovoj-4760062101805.html'
        ])

    def azerchay_chebrec_black_pack_30pk_parser(self):
        ''' Чай (30 ф/п х 2 г) Azercay чорний з чебрецем '''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/caj-30-fp-h-2-g-azercay-cornij-z-cebrecem'
        ])

    def sir_plav_komo_druzba_40_75gr_parser(self):
        ''' Сир плавлений «Комо» «Дружба» 40%'''
        return self.prices_parsing([
            'https://varus.ua/sir-plavlenij-komo-druzhba-40-75-g',
            'https://shop.silpo.ua/product/syr-plavlenyi-komo-druzhba-40-883982',
            'https://novus.online/ru/product/sir-plavlenij-55-druzba-komo-75g',
            'https://metro.zakaz.ua/ru/products/sir-komo-75g-ukrayina--04820039807861/',
            'https://shop.nashkraj.ua/kovel/product/455677-sir-komo-pl-40-75g-druzhba',
            'https://fozzyshop.ua/ru/plavlenyj/96447-syr-plavlenyj-komo-druzhba-40-4820039807878.html'
        ])

    def sir_plav_komo_vershk_40_75gr_parser(self):
        ''' Сир плавлений «Комо» Вершковий 40%'''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/sir-komo-75g-ukrayina--04820039807915/',
            'https://shop.silpo.ua/product/syr-plavlenyi-komo-vershkovyi-40-883980',
            'https://novus.online/ru/product/sir-plavlenij-55-verskovij-komo-75g',
            'https://metro.zakaz.ua/ru/products/sir-komo-75g-ukrayina--04820039807915/',
            'https://shop.nashkraj.ua/kovel/product/455675-sir-komo-pl-40-75g-vershkoviy',
            'https://fozzyshop.ua/ru/plavlenyj/96448-syr-plavlenyj-komo-slivochnyj-40-4820039807922.html'
        ])

    def sir_plav_komo_zelen_chasnik_40_75gr_parser(self):
        ''' Сир плавлений «Комо» з часником та зеленню 40%'''
        return self.prices_parsing([
            'https://varus.ua/sir-plavlenij-komo-z-zelennyu-ta-chasnikom-40-75-g',
            'https://shop.silpo.ua/product/syr-plavlenyi-komo-z-zelenniu-ta-chasnykom-40-883981',
            'https://shop.nashkraj.ua/kovel/product/455680-sir-komo-pl-40-75g-z-zelennyu-i-chasnikom',
            'https://fozzyshop.ua/ru/plavlenyj/96449-syr-plavlenyj-komo-s-zelenyu-i-chesnokom-40-4820039807977.html'
        ])

    def sir_plav_komo_crab_pal_40_75gr_parser(self):
        ''' Сир плавлений «Комо» з крабовими паличками 40%'''
        return self.prices_parsing([
            'https://shop.nashkraj.ua/kovel/product/455684-sir-komo-pl-40-75g-z-krabovimi-palichkami'
        ])

    def sir_plav_komo_grib_40_75gr_parser(self):
        ''' Сир плавлений «Комо» з грибами 40%'''
        return self.prices_parsing([
            'https://shop.nashkraj.ua/kovel/product/455678-sir-komo-pl-40-75g-z-gribami',
            'https://fozzyshop.ua/ru/plavlenyj/98307-syr-plavlenyj-komo-s-gribami-40-4820039807991.html'
        ])

    def milk_jagot_2_6_pl_870gr_parser(self):
        ''' Молоко пастеризоване «Яготинське» 2,6% 870 г '''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/moloko-087-kg-agotinske-26-pbut',
            'https://shop.silpo.ua/product/moloko-pasteryzovane-yagotynske-2-6-866829',
            'https://novus.online/ru/product/moloko-26-agotin-plas-900g',
            'https://metro.zakaz.ua/ru/products/moloko-iagotin-900g-ukrayina--04823005203865/',
            'https://fozzyshop.ua/ru/moloko/90997-moloko-pasterizovannoe-yagotinske-26-but-4823005209379.html'
        ])

    def milk_jagot_3_2_pl_870gr_parser(self):
        ''' Молоко пастеризоване «Яготинське» 3_2% 870 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-iagotin-870g-ukrayina--04823005209386/',
            'https://shop.silpo.ua/product/moloko-pasteryzovane-yagotynske-3-2-872536',
            'https://novus.online/ru/product/moloko-pasteryzovane-32-yahotyn-plyashka-870h'
        ])

    def milk_jagot_1_pl_870gr_parser(self):
        ''' Молоко пастеризоване «Яготинське» 1% 870 г '''
        return self.prices_parsing([
            'https://varus.ua/moloko-yagotinskoe-1-pasterizovannoe-870-g',
            'https://shop.silpo.ua/product/moloko-pasteryzovane-yagotynske-1-876400'
        ])

    def milk_jagot_pryaj_2_6_pl_870gr_parser(self):
        ''' Молоко пряжене «Яготинське» 2,6% 870 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-iagotin-870g--04823005209362/',
            'https://varus.ua/moloko-yagotinskoe-2-6-toplenoe-870-g',
            'https://shop.silpo.ua/product/moloko-yagotynske-priazhene-2-6-880464',
            'https://metro.zakaz.ua/ru/products/moloko-iagotin-900g--04823005203933/'
        ])

    def milk_galichina_ukr_2_5_pl_870gr_parser(self):
        ''' Молоко «Галичина» «Українське» 2,5% 870 г '''
        return self.prices_parsing([
            'https://varus.ua/moloko-galichina-2-5-pasterizovane-870-g',
            'https://shop.silpo.ua/product/moloko-galychyna-ukrainske-2-5-682859',
            'https://novus.online/ru/product/moloko-pasterizovane-25-galicina-pet-870g',
            'https://metro.zakaz.ua/ru/products/moloko-galichina-870g-ukrayina--04820038493829/',
            'https://fozzyshop.ua/ru/moloko/40751-moloko-galichina-ukrainskoe-25-but-4820038493829.html'
        ])

    def milk_premiya_pitne_2_5_pl_900gr_parser(self):
        ''' Молоко «Премія»® питне пастеризоване 2,5% 900 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-premiia-pytne-pasteryzovane-2-5-815586'
        ])

    def milk_premiya_loko_pitne_2_5_pl_900gr_parser(self):
        ''' Молоко «Премія»® LOKO питне пастеризоване 2,5% 900 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-pasteryzovane-premiia-loko-pytne-2-5-pl-935136'
        ])

    def milk_premiya_loko_pitne_2_5_pl_2l_parser(self):
        ''' Молоко «Премія»® питне пастеризоване 2,5% 2 л '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-pasteryzovane-premiia-loko-pytne-2-5-but-935137'
        ])

    def milk_premiya_loko_pitne_3_2_pl_2l_parser(self):
        ''' Молоко «Премія»® питне пастеризоване 3.2% 2 л '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-pasteryzovane-premiia-loko-pytne-3-2-pl-935138'
        ])

    def milk_organic_milk_3_5_1l_parser(self):
        ''' Молоко пастеризоване Organic Milk органічне 3,5% 1 л '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-pasteryzovane-organic-milk-organichne-3-5-576679',
            'https://novus.online/ru/product/moloko-organicne-35-organic-milk-pl1000g',
            'https://metro.zakaz.ua/ru/products/moloko-organik-milk-1000g--04820178810043/',
            'https://fozzyshop.ua/ru/moloko/43952-moloko-organic-milk-pasterizovannoe-35-but-4820178810043.html'
        ])

    def milk_organic_milk_2_5_470gr_parser(self):
        ''' Молоко пастеризоване Organic Milk органічне 2,5% пляшка 470 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-pasteryzovane-organic-milk-organichne-2-5-pliashka-786251'
        ])

    def milk_organic_milk_2_5_1l_parser(self):
        ''' Молоко пастеризоване Organic Milk органічне 2,5% 1 л '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-pasteryzovane-organic-milk-organichne-2-5-576680',
            'https://novus.online/ru/product/moloko-organicne-25-organic-milk-pl1000g',
            'https://metro.zakaz.ua/ru/products/moloko-organik-milk-1000g--04820178810050/',
            'https://fozzyshop.ua/ru/moloko/32637-moloko-pasterizovan-organic-milk-organicheskoe-25-butylka-4820178810050.html'
        ])

    def milk_organic_milk_bezlaktoz_2_5_1l_parser(self):
        ''' Молоко пастеризоване Organic Milk органічне безлактозне 2,5% 1 л '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-organic-milk-bezlaktozne-organichne-2-5-844117'
        ])

    def milk_organic_milk_0_5_1l_parser(self):
        ''' Молоко пастеризоване Organic Milk органічне 0,5% 1 л '''
        return self.prices_parsing([
            'https://metro.zakaz.ua/ru/products/moloko-organik-milk-1000ml--04820178810654/',
            'https://fozzyshop.ua/ru/moloko/63171-moloko-pasterizovanoe-organicmilk-organ-n-zh05but-4820178810654.html',
        ])

    def milk_prostonashe_2_5_870gr_parser(self):
        ''' Молоко пастеризоване Простонаше 2,5% пл 870 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-prostonashe-870g--04820226167716/',
            'https://varus.ua/moloko-prostokvashino-2-5-pasterizovane-870-g',
            'https://shop.silpo.ua/product/moloko-pasteryzovane-prostonashe-2-5-pl-935139',
            'https://metro.zakaz.ua/ru/products/moloko-prostonashe-870g--04820226167716/'
        ])

    def milk_prostonashe_pryaj__2_5_870gr_parser(self):
        ''' Молоко пастеризоване Простонаше пряжене 2,5% пл 870 г '''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/moloko-087-kg-prostonase-prazene-25-pbut',
            'https://eko.zakaz.ua/uk/products/ukrayina--04820226167754/',
            'https://varus.ua/moloko-prostokvashino-2-5-pryazhene-870-g',
            'https://shop.silpo.ua/product/moloko-prostonashe-priazhene-2-5-pl-935141',
            'https://metro.zakaz.ua/ru/products/ukrayina--04820226167754/'
        ])

    def milk_prostonashe_1_870gr_parser(self):
        ''' Молоко пастеризоване Простонаше 1% пл 870 г '''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/moloko-087-kg-prostonase-1-pbut',
            'https://varus.ua/moloko-1-prostokvashino-870g-plyashka',
            'https://shop.silpo.ua/product/moloko-pasteryzovane-prostonashe-1-pl-935140',
            'https://metro.zakaz.ua/ru/products/moloko-prostonashe-870g-ukrayina--04820226167730/'
        ])

    def milk_ferma_2_5_pl_840gr_parser(self):
        ''' Молоко пастеризоване «Ферма» 2,5% 840 г '''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/moloko-084-kg-ferma-25',
            'https://eko.zakaz.ua/uk/products/moloko-ferma-840g-ukrayina--04820272180196/',
            'https://varus.ua/moloko-ferma-2-5-pasterizovane-840-g',
            'https://shop.silpo.ua/product/moloko-pasteryzovane-ferma-2-5-837449',
            'https://novus.online/ru/product/moloko-pasterizovane-25-ferma-pet-840g',
            'https://metro.zakaz.ua/ru/products/moloko-ferma-840g-ukrayina--04820234020805/',
            'https://fozzyshop.ua/ru/moloko/90111-moloko-pasterizovannoe-ferma-25-4820239241137.html'
        ])

    def milk_ferma_3_2_pl_840gr_parser(self):
        ''' Молоко пастеризоване «Ферма» 3.2% 840 г '''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/moloko-084-kg-ferma-32',
            'https://varus.ua/moloko-ferma-3-2-pasterizovane-840-g',
            'https://shop.silpo.ua/product/moloko-pasteryzovane-ferma-3-2-837450',
            'https://novus.online/ru/product/moloko-pasterizovane-32-ferma-pet-840g',
            'https://metro.zakaz.ua/ru/products/moloko-ferma-840g-ukrayina--04820239241175/',
            'https://metro.zakaz.ua/ru/products/moloko-ferma-840g-ukrayina--04820239241175/'
        ])

    def milk_stariy_porick_3_6_pl_1l_parser(self):
        ''' Молоко пастеризоване «Лавка Традицій» «Старий Порицьк» органічне 3,6% 1 л '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-pasteryzovane-lavka-tradytsii-staryi-porytsk-organichne-3-6-711180'
        ])

    def milk_stariy_porick_pryaj_4_pl_1l_parser(self):
        ''' Молоко «Лавка традицій» «Старий Порицьк» пряжене з незбираного молока 4% 1 л '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-lavka-tradytsii-staryi-porytsk-priazhene-z-nezbyranogo-moloka-4-869921'
        ])

    def milk_stariy_porick_2_5_pl_1l_parser(self):
        ''' Молоко пастеризоване «Лавка Традицій» «Старий Порицьк» органічне 2.5% 1 л '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-pasteryzovane-lavka-tradytsii-staryi-porytsk-organichne-2-5-711179'
        ])

    def milk_molkiya_2_5_pl_870gr_parser(self):
        ''' Молоко пастеризоване Молокія 2,5% пл 870 г '''
        return self.prices_parsing([
            'https://varus.ua/moloko-molokiya-pasterizovannoe-2-5-870-g',
            'https://shop.silpo.ua/product/moloko-pasteryzovane-molokiia-2-5-pl-917218',
            'https://novus.online/ru/product/moloko-25-molokiya-870h-plyashka',
            'https://fozzyshop.ua/ru/moloko/99677-moloko-pasterizovannoe-molokiya-25-0250015105256.html'
        ])

    def milk_voloshkove_pole_2_5_pl_900gr_parser(self):
        ''' Молоко пастеризоване «Волошкове поле» 2,5% 900 г '''
        return self.prices_parsing([
            'https://varus.ua/moloko-voloshkove-pole-2-5-pasterizovane-u-plyashci-900-g',
            'https://shop.silpo.ua/product/moloko-pasteryzovane-voloshkove-pole-2-5-755012'
        ])

    def milk_gmz_n1_pl_2_5_1l_parser(self):
        ''' Молоко пастеризоване ГМЗ №1 2,6% 1 л '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-pasteryzovane-gmz-1-2-6-602380'
        ])

    def milk_gmz_pryaj_n1_pl_4_1l_parser(self):
        ''' Молоко «ГМЗ №1» пряжене 4% 1 л '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-gmz-1-priazhene-4-641986'
        ])

    def koz_milk_zolota_koza_3_8_pl_500gr_parser(self):
        ''' Молоко козяче пастеризоване «Лавка традицій» «Золота Коза» 3,8% 0.5 л '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-koziache-pasteryzovane-lavka-tradytsii-koza-3-8-758134'
        ])

    def koz_milk_virtuoso_by_lukachivka_3_pl_500gr_parser(self):
        ''' Молоко козине Virtuoso by Lukachivka незбиране 3% 0.5 л '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-kozyne-virtuoso-by-lukachivka-nezbyrane-3-766726'
        ])

    def milk_svoe_3_4_pl_1l_parser(self):
        ''' Молоко коров'яче «Своє», 3,4% 1 л '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-korov-iache-svoie-3-4-784582',
            'https://novus.online/ru/product/moloko-svoye-34-1l-petplyashka'
        ])

    def milk_ovec_soloviov_lakon_3_8_6_250gr_parser(self):
        ''' Молоко «Лавка традицій» Soloviov овець породи Лакон 3,8-6% 250 гр '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-lavka-tradytsii-soloviov-ovets-porody-lakon-3-8-6-890843'
        ])

    def milk_selyanske_osobl_2_5_pap_pak_950gr_parser(self):
        ''' Молоко ультрапастеризоване «Селянське» особливе 2,5% 950 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-selianske-950g-ukrayina--04820003482407/',
            'https://varus.ua/moloko-selyanske-osoblive-2-5-ultrapasterizovane-950-g',
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-selianske-osoblyve-2-5-716079',
            'https://novus.online/ru/product/moloko-ultrapasterizovane-25-osoblive-selanske-950g',
            'https://metro.zakaz.ua/ru/products/moloko-selianske-950g-ukrayina--04820003482407/',
            'https://shop.nashkraj.ua/kovel/product/12319-moloko-selyanske-2-5-950g-osoblive-t-p',
            'https://fozzyshop.ua/ru/moloko/42124-moloko-selyanske-osobennoe-ultrapasterizovannoe-25-t-d-4820003482407.html'
        ])

    def milk_selyanske_microfil_pitne_2_5_pap_pak_950gr_parser(self):
        ''' Молоко пастеризоване «Селянське» мікрофільтроване питне 2.5% 950 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko--04820254400236/',
            'https://varus.ua/moloko-krestyanskoe-mikrofiltrovannoe-25-950g',
            'https://shop.silpo.ua/product/moloko-pasteryzovane-selianske-mikrofiltrovane-pytne-2-5-917294',
            'https://novus.online/ru/product/moloko-pytne-mikrofiltrovane-pasteryzovane-25-zhyru-selyanske-950h',
            'https://metro.zakaz.ua/ru/products/moloko--04820254400236/',
            'https://fozzyshop.ua/ru/moloko/99717-moloko-pasteriz-selyanske-pitevoe-25-0250015069510.html'
        ])

    def milk_selyanske_3_2_tp_950gr_parser(self):
        ''' Молоко ультрапастеризоване «Селянське» 3,2 % т/п 950 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-selianske-3-2-t-p-705768',
            'https://novus.online/ru/product/moloko-ultrapasterizovane-32-osoblive-selanske-tetrapak-950g',
            'https://metro.zakaz.ua/ru/products/moloko-selianske-950g-ukrayina--04820003482414/',
            'https://shop.nashkraj.ua/kovel/product/243089-moloko-selyanske-3-2-950g-osoblive-t-p',
            'https://fozzyshop.ua/ru/moloko/36776-moloko-ultrapasterizovan-selyanske-32-t-p-4820003486085.html'
        ])

    def milk_selyanske_rodinne_2_5_tp_1500gr_parser(self):
        ''' Молоко ультрапастеризоване «Селянське» «Родинне» 2,5% 1.5 л '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-selianske-1500g-ukrayina--04820003486221/',
            'https://varus.ua/moloko-selyanske-rodinne-2-5-ultrapasterizovane-1-5-l',
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-selianske-rodynne-2-5-724312',
            'https://novus.online/ru/product/moloko-25-osoblive-selanske-1500g',
            'https://metro.zakaz.ua/ru/products/moloko-selianske-1500g-ukrayina--04820003484760/',
            'https://fozzyshop.ua/ru/moloko/44079-moloko-ultrapasterizovannoe-selyanske-rodinne-25-t-p-4820003486221.html'
        ])

    def milk_selyanske_rodinne_2_5_tp_2000gr_parser(self):
        ''' Молоко ультрапастеризоване «Селянське» «Родинне» 2,5% 2 л '''
        return self.prices_parsing([
            'https://varus.ua/moloko-selyanske-semejnoe-ultrapasterizovannoe-2000ml',
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-selianske-simeine-osoblyve-2-5-726270',
            'https://metro.zakaz.ua/ru/products/moloko-selianske-2000g-ukrayina--04820003486115/',
            'https://fozzyshop.ua/ru/moloko/48533-moloko-ultrapaster-selyanske-semejnoe-osoboe-25-4820003486115.html'
        ])

    def milk_selyanske_osobl_1_5_t_p_950gr_parser(self):
        ''' Молоко «Селянське» особливе 1,5% 950 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-selianske-osoblyve-1-5-705675',
            'https://novus.online/ru/product/moloko-ultrapasterizovane-15-osoblive-selanske-tetrapak-950g',
            'https://shop.nashkraj.ua/kovel/product/241161-moloko-selyanske-1-5-950g-osobl-pas-t-p'
        ])

    def milk_selyanske_osoblive_2_5_tp_500gr_parser(self):
        ''' Молоко ультрапастеризоване «Селянське» 2,5% 500 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-selianske-2-5-885638'
        ])

    def milk_selyanske_osoblive_kids_3_2_tp_950gr_parser(self):
        ''' Молоко ультрапастеризоване «Селянське» «Малюкам» для дітей 3,2% 950 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-selianske-maliukam-dlia-ditei-3-2-846423',
            'https://auchan.ua/ua/moloko-ul-trapasterizovannoe-dlja-detej-seljans-ke-malysham-3-2-9m-950-g-907042/',
            'https://novus.online/product/moloko-selyanske-malyukam-dytyache-ultrapasteryzovane-32-950h'
        ])

    def milk_selyanske_osobl_micro_f_3_4_3_8_tp_950gr_parser(self):
        ''' Молоко пастеризоване «Селянське» мікрофільтроване незбиране 3.4-3.8% 950 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-selianske-950g--04820254400496/',
            'https://varus.ua/moloko-krestyanskoe-mikrofiltrovannoe-34-38-950g',
            'https://shop.silpo.ua/product/moloko-pasteryzovane-selianske-mikrofiltrovane-nezbyrane-3-4-3-8-917293',
            'https://novus.online/product/moloko-pytne-mikrofiltrovane-pasteryzovane-nezbyrane-34-38-selyanske-950h',
            'https://metro.zakaz.ua/uk/products/moloko-selianske-950g--04820254400496/',
            'https://fozzyshop.ua/moloko/99716-moloko-pasterizovane-selyanske-34-38-0250015069503.html'
        ])

    def milk_jagot_ultra_2_6_tp_950gr_parser(self):
        ''' Молоко «Яготинське» ультрапастеризоване 2,6% 950 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-iagotin-950g--04823005205234/',
            'https://shop.silpo.ua/product/moloko-yagotynske-ultrapasteryzovane-2-6-646104',
            'https://auchan.ua/ua/moloko-jagotins-ke-2-6-950-g-238916/',
            'https://novus.online/product/moloko-ultrapostarizovane-26-agotin-tetra-pak-0950kg'
        ])

    def milk_jagot_velik_2_6_tp_2000gr_parser(self):
        ''' Молоко «Яготинське» «Велике» 2,6% жиру 2 л '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-iagotin-2000g--04823005204459/',
            'https://shop.silpo.ua/product/moloko-yagotynske-velyke-2-6-zhyru-547009',
            'https://novus.online/product/moloko-26-agotin-2kg',
            'https://metro.zakaz.ua/uk/products/moloko-iagotin-2000g--04823005204459/'
        ])

    def milk_jagot_velik_2_6_tp_1500gr_parser(self):
        ''' Молоко «Яготинське» «Велике» 2,6% жиру 1.5 л '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-iagotin-1500g-ukrayina--04823005204442/',
            'https://shop.silpo.ua/product/moloko-yagotynske-velyke-2-6-547004',
            'https://novus.online/product/moloko-26-agotin-15l',
            'https://fozzyshop.ua/moloko/10019-moloko-yagotinske-bolshoe-26-p-p-4820006531607.html'
        ])

    def Moloko_ultrapasterizovane__Jagotinske__3_2__t_b_950_g_parser(self):
        ''' Молоко ультрапастеризоване «Яготинське» 3,2% т/б 950 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-yagotynske-3-2-t-b-646105',
            'https://fozzyshop.ua/moloko/38833-moloko-ultrapasterizirovannoe-yagotinske-32t-b-4823005205227.html'
        ])

    def Moloko_Galichina_ultrapasterizovane_2_5__950_g_parser(self):
        ''' Молоко «Галичина» ультрапастеризоване 2,5% 950 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-galichina-950ml-ukrayina--04820222760249/',
            'https://varus.ua/moloko-tga-25-950g-galichina',
            'https://shop.silpo.ua/product/moloko-galychyna-ultrapasteryzovane-2-5-815590',
            'https://auchan.ua/ua/moloko-ul-trapasterizovannoe-galichina-2-5-950-g-906986/',
            'https://novus.online/product/moloko-ultrapasterizovane-25-galicina-tga-950g',
            'https://metro.zakaz.ua/uk/products/moloko-galichina-950ml-ukrayina--04820222760249/',
            'https://shop.nashkraj.ua/lutsk/product/350392-moloko-galichina-2-5-950g-t-p',
            'https://fozzyshop.ua/moloko/76612-moloko-galichina-ultrapasterizovannoe-25-t-p-4820222760249.html'
        ])

    def Moloko_Galichina_ultrapasterizovane_3_2__950_g_parser(self):
        ''' Молоко «Галичина» ультрапастеризоване 3,2% 950 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-galichina-950ml-ukrayina--04820222760225/',
            'https://varus.ua/moloko-tga-32-950g-galichina',
            'https://shop.silpo.ua/product/moloko-galychyna-ultrapasteryzovane-3-2-815591',
            'https://auchan.ua/ua/moloko-ul-trapasterizovannoe-galichina-3-2-950-g-906993/',
            'https://novus.online/product/moloko-32-halychyna-tga-950h',
            'https://metro.zakaz.ua/uk/products/moloko-galichina-950ml-ukrayina--04820222760225/',
            'https://shop.nashkraj.ua/lutsk/product/350393-moloko-galichina-3-2-950g-t-p',
            'https://fozzyshop.ua/moloko/76613-moloko-galichina-ultrapasterizovannoe-32-t-p-4820222760225.html'
        ])

    def Moloko_Galichina_ultrapasterizovane_1__t_p_950_g_parser(self):
        ''' Молоко «Галичина» ультрапастеризоване 1% т/п 950 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-galichina-950g-ukrayina--04820222760232/',
            'https://varus.ua/moloko-tga-1-950g-galichina',
            'https://shop.silpo.ua/product/moloko-galychyna-ultrapasteryzovane-1-t-p-815589',
            'https://novus.online/product/moloko-1-halychyna-tga-950h',
            'https://shop.nashkraj.ua/lutsk/product/350391-moloko-galichina-1-950g-t-p'
        ])

    def Moloko_ultrapasterizovane_Na_zdorovja_bezlaktozne_0_5__950_g_parser(self):
        ''' Молоко ультрапастеризоване «На здоров'я» безлактозне 0,5% 950 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-na-zdorov-ia-bezlaktozne-0-5-873839',
            'https://novus.online/product/moloko-05-ultrapasteryzovane-bezlaktozne-na-zdorovya-950hr',
            'https://metro.zakaz.ua/uk/products/moloko-na-zdorov-ia-1000g--04820003486634/',
        ])

    def Moloko_ultrapasterizovane_Na_zdorovja_0_5__950_g_parser(self):
        ''' Молоко ультрапастеризоване «На здоров'я» 0,5% 950 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-na-zdorov-ia-0-5-863530',
            'https://novus.online/product/moloko-05-ultrapasteryzovane-na-zdorovya-950hr',
            'https://metro.zakaz.ua/uk/products/moloko-na-zdorov-ia-1000g--04820003480977/'
        ])

    def Moloko_ditjache_Na_zdorovja_3_2__500_g_parser(self):
        ''' Молоко дитяче «На здоров'я» 3,2% 500 г '''
        return self.prices_parsing([
            'https://varus.ua/moloko-na-zdorov-ya-3-2-ultrapasterizovane-dlya-ditey-500-g',
            'https://shop.silpo.ua/product/moloko-dytiache-na-zdorov-ia-3-2-527083',
            'https://novus.online/product/moloko-sterilizovane-32-na-zdorova-ditace-05l'
        ])

    def Moloko_Na_zdorovja_ultrapasterizovane_2_5__950_g_parser(self):
        ''' Молоко «На здоров'я» ультрапастеризоване 2,5% 950 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-na-zdorov-ia-ultrapasteryzovane-2-5-852602',
            'https://novus.online/product/moloko-na-zdorovya-vitaminizovane-ultrapasteryzovane-25-950h'
        ])

    def Moloko_ultrapasterizovane_Na_zdorovja_bezlaktozne_2_5__950_g_parser(self):
        ''' Молоко ультрапастеризоване «На здоров'я» безлактозне 2,5% 950 г '''
        return self.prices_parsing([
            "https://eko.zakaz.ua/uk/products/moloko-na-zdorov-ia--04820003488522/",
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-na-zdorov-ia-bezlaktozne-2-5-857563',
            'https://novus.online/product/moloko-25-ultrapasteryzovane-bezlaktozne-na-zdorovya-950h',
            'https://metro.zakaz.ua/uk/products/moloko-na-zdorov-ia-1000g-ukrayina--04820003483305/',
            'https://fozzyshop.ua/kislomolochnye-napitki/69568-kefir-na-zdorovya-bezlaktoznyj-25-tetra-top-4820003487310.html'
        ])

    def Moloko_ultrapasterizovane_Na_zdorovja_ditjache_3_2__950_g_parser(self):
        ''' Молоко ультрапастеризоване «На здоров'я» дитяче 3,2% 950 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-na-zdorov-ia-dytiache-3-2-854265',
            'https://novus.online/product/moloko-ultrapasteryzovane-na-zdorovya-dytyache-32-zhyru-tga-950h',
            'https://metro.zakaz.ua/uk/products/moloko-na-zdorov-ia-1000g--04820003481134/',
            'https://fozzyshop.ua/moloko/93812-moloko-ultrapasterizovan-na-zdorovya-detskoe-32-4820003489277.html'
        ])

    def Moloko_ultrapasterizovane_Lactel_bezlact_0_2__950_g_parser(self):
        ''' Молоко ультрапастеризоване Lactel безлактозне 0,2% 950 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-lactel-bezlaktozne-0-2-878541',
            'https://fozzyshop.ua/moloko/99541-moloko-ultrapast-lactel-bezlaktoznoe-02-0250014427908.html'
        ])

    def Moloko_ultrapasterizovane_Lactel_pitne_z_vitaminom_D_3_2__950_g_parser(self):
        ''' Молоко ультрапастеризоване Lactel питне з вітаміном D 3,2% 950 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-laktel-950g-ukrayina--04823065727530/',
            'https://varus.ua/moloko-lactel-s-vitaminom-d-32-950-g',
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-lactel-pytne-z-vitaminom-d-3-2-871984',
            'https://auchan.ua/ua/moloko-ul-trapasterizovannoe-lactel-3-2-950-g-907154/',
            'https://metro.zakaz.ua/uk/products/moloko-laktel-1000g--04823065702360/',
            'https://shop.nashkraj.ua/lutsk/product/446720-moloko-lactel-3-2-950g-z-vitaminom-d3',
            'https://fozzyshop.ua/moloko/87961-moloko-ultrapasterizovannoe-lactel-s-vitaminom-d-32-4823065727530.html'
        ])

    def Moloko_ultrapasterizovane_Lactel_pitne_bezlaktozne_1_5__950_g_parser(self):
        ''' Молоко ультрапастеризоване Lactel питне безлактозне 1,5% 950 г '''
        return self.prices_parsing([
            'https://varus.ua/moloko-lactel-1-5-bezlaktozne-ultrapasterizovane-1-l',
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-lactel-pytne-bezlaktozne-1-5-892639',
            'https://auchan.ua/ua/moloko-ul-trapasterizovannoe-bezlaktoznoe-lactel-1-5-950-g-907182/',
            'https://novus.online/product/moloko-pytne-bezlaktozne-ultrapasteryzovane-15-lactel-950h'
        ])

    def Moloko_ultrapasterizovane_Lactel_pitne_z_vіtamіnom_D_0_5__950_g_parser(self):
        ''' Молоко ультрапастеризоване Lactel питне з вітаміном D 0,5% 950 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-laktel-950g-ukrayina--04823065727516/',
            'https://varus.ua/moloko-lactel-s-vitaminom-d-05-950-g',
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-lactel-pytne-z-vitaminom-d-0-5-871982',
            'https://auchan.ua/ua/moloko-ul-trapasterizovannoe-lactel-0-5-950-g-907140/',
            'https://novus.online/product/moloko-05-pytne-ultrapasteryzovane-z-vitaminom-d3-laktel-sih-kombiblok-0950h',
            'https://metro.zakaz.ua/uk/products/moloko-laktel-1000g--04823065702322/',
            'https://shop.nashkraj.ua/lutsk/product/446718-moloko-lactel-0-5-950g-z-vitaminom-d3',
            'https://fozzyshop.ua/moloko/87959-moloko-ultrapasterizovannoe-lactel-s-vitaminom-d-05-4823065727516.html'
        ])

    def Moloko_ultrapasterizovane_Lactel_bezlaktozne_2_5__950_g_parser(self):
        ''' Молоко ультрапастеризоване Lactel безлактозне 2,5% 950 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-lactel-bezlaktozne-2-5-878542',
            'https://auchan.ua/ua/moloko-ul-trapasterizovannoe-bezlaktoznoe-lactel-2-5-950-g-907189/',
            'https://novus.online/product/moloko-25-bezlaktozne-ultrapasterizovane-laktel-950g',
            'https://shop.nashkraj.ua/lutsk/product/460098-moloko-lactel-2-5-950g-bezlaktozne-t-p',
            'https://fozzyshop.ua/moloko/96473-moloko-ultrapasterizovannoe-lactel-bezlaktoznoe-25-4823065728827.html'
        ])

    def Moloko_superpasterizovane_Buronka_3_2__1000_g_parser(self):
        ''' Молоко суперпастеризоване «Бурьонка» 3,2% 1000 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-superpasteryzovane-buronka-3-2-539325',
            'https://auchan.ua/ua/moloko-bur-onka-ul-trapasterizovannoe-3-2-1-l-906576/',
            'https://novus.online/product/moloko-ultrapasterizovane-32-burenka-1l',
            'https://metro.zakaz.ua/uk/products/moloko-burenka-1000g--04820003481783/',
            'https://fozzyshop.ua/moloko/10003-moloko-burenka-superpasterizovannoe-32-4820003483763.html'
        ])

    def Moloko_pitne_ultrapasterizovane_Buronka_2_5__1000_g_parser(self):
        ''' Молоко питне ультрапастеризоване «Бурьонка» 2,5% 1000 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-pytne-ultrapasteryzovane-buronka-2-5-70262',
            'https://auchan.ua/ua/moloko-bur-onka-ul-trapasterizovannoe-2-5-1-5-l-906548/',
            'https://novus.online/product/moloko-ultrapasterizovane-25-burenka-1000g',
            'https://metro.zakaz.ua/uk/products/moloko-burenka-1000g-ukrayina--04820003480717/',
            'https://fozzyshop.ua/moloko/43996-moloko-buronka-ultrapasterizovane-25-4820003480717.html'
        ])

    def Moloko_Buronka_ultrapasterizovane_3_2__1500_g_parser(self):
        ''' 	Молоко «Бурьонка» ультрапастеризоване 3,2% 1500 г '''
        return self.prices_parsing([
            'https://varus.ua/moloko-buronka-3-2-ultrapasterizovane-1-5-l',
            'https://shop.silpo.ua/product/moloko-buronka-ultrapasteryzovane-3-2-255332',
            'https://auchan.ua/ua/moloko-bur-onka-ul-trapasterizovannoe-3-2-1-5-l-906555/',
            'https://novus.online/product/moloko-ultrapasterizovane-32-burenka-15l',
            'https://metro.zakaz.ua/uk/products/moloko-burenka-1500g--04820003481332/',
            'https://fozzyshop.ua/moloko/91001-moloko-ultrapasterizovannoe-buronka-32-4820003481332.html'
        ])

    def Moloko_Buronka_pitne_ultrapasterizovane_2_5__1500_g_parser(self):
        ''' Молоко «Бурьонка» питне ультрапастеризоване 2,5% 1500 г '''
        return self.prices_parsing([
            'https://varus.ua/moloko-buronka-2-5-ultrapasterizovane-1-5-l',
            'https://shop.silpo.ua/product/moloko-buronka-pytne-ultrapasteryzovane-2-5-255333',
            'https://auchan.ua/ua/moloko-bur-onka-ul-trapasterizovannoe-2-5-1-5-l-906548/',
            'https://novus.online/product/moloko-ultrapasterizovane-25-burenka-15l',
            'https://metro.zakaz.ua/uk/products/moloko-burenka-1500ml--04820003481349/',
            'https://fozzyshop.ua/moloko/71522-moloko-burenka-pitevoe-ultrapasterizovannoe-25-4820003481349.html'
        ])

    def Moloko_ultrapasterizovane_Organic_Milk_organіchne_2_5__1000_g_parser(self):
        ''' Молоко ультрапастеризоване Organic Milk органічне 2,5% 1000 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-organic-milk-organichne-2-5-923745',
            'https://novus.online/product/moloko-korovyache-orhanichne-ultrapasteryzovane-organic-milk-25-tp-1000h',
            'https://metro.zakaz.ua/uk/products/moloko-organik-milk-1000g--04820178810968/'
        ])

    def Moloko_ultrapasterizovane_Slovjanochka_3_2__1000_g_parser(self):
        ''' Молоко ультрапастеризоване «Слов'яночка» 3,2% 1000 г '''
        return self.prices_parsing([
            'https://varus.ua/moloko-pitne-ultra-pasterizovane-3-2-slovyanochka-1000g',
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-slov-ianochka-3-2-677647',
            'https://auchan.ua/ua/moloko-ul-trapasterizovannoe-slov-janochka-3-2-1-kg-906646/'
        ])

    def Moloko_ultrapasterizovane_Slovjanochka_2_5__1000_g_parser(self):
        ''' Молоко ультрапастеризоване «Слов'яночка» 2,5% 1000 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-slov-ianochka-1000g-ukrayina--04823061319937/',
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-slov-ianochka-2-5-677646',
            'https://auchan.ua/ua/moloko-ul-trapasterizovannoe-slov-janochka-2-5-1-kg-906639/',
            'https://novus.online/product/moloko-slovyanochka-ultrapasteryzovane-25-1000h',
            'https://shop.nashkraj.ua/lutsk/product/233835-moloko-slovyanochka-2-5-1000ml-t-p'
        ])

    def Moloko_Slovjanochka_Dlja_idealnoi_pinki_2_5__1000_g_parser(self):
        ''' Молоко «Слов’яночка» «Для ідеальної пінки» 2,5% 1000 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-slovianochka-ukrayina--04823061322838/',
            'https://shop.silpo.ua/product/moloko-slov-ianochka-dlia-idealnoi-pinky-2-5-824909'
        ])

    def Moloko_ultrapasterizovane_Ferma_2_5__t_p_980_g_parser(self):
        ''' Молоко ультрапастеризоване «Ферма» 2,5% т/п 980 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-ferma-ukrayina--04820239247757/',
            'https://varus.ua/moloko-ferma-2-5-ultrapasterizovane-980-g',
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-ferma-2-5-t-p-859171',
            'https://auchan.ua/ua/moloko-ul-trapasterizovannoe-ferma-2-5-980-g-907112/',
            'https://novus.online/product/moloko-ferma-ultrapasteryzovane-25-980h',
            'https://metro.zakaz.ua/uk/products/moloko-ferma-ukrayina--04820239247757/',
            'https://fozzyshop.ua/moloko/99720-moloko-ultrapasterizovannoe-ferma-25-0250014657695.html'
        ])

    def Moloko_ultrapasterizovane_OKZDH_Nashe_moloko_2_5__950_g_parser(self):
        ''' Молоко ультрапастеризоване ОКЗДХ Наше молоко 2,5% 950 г '''
        return self.prices_parsing([
            'https://varus.ua/moloko-nashe-moloko-ultrapasterizovannoe-dlya-detej-ot-3-h-let-25-950g',
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-okzdkh-nashe-moloko-dlia-ditei-vid-3-rokiv-2-5-933069',
        ])

    def Moloko_ultrapasterizovane_OKZDH_Nashe_moloko_3_2__950_g_parser(self):
        ''' Молоко ультрапастеризоване ОКЗДХ Наше молоко 3,2% 950 г '''
        return self.prices_parsing([
            'https://varus.ua/moloko-nashe-moloko-ultrapasterizovannoe-dlya-detej-ot-3-h-let-32-950g',
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-okzdkh-nashe-moloko-3-2-933067'
        ])

    def Moloko_ultrapasterizovane_Loko_Moko_vіd_3_rokіv_2_5__1000_g_parser(self):
        ''' Молоко ультрапастеризоване «Локо Моко» від 3 років 2,5% 1000 г '''
        return self.prices_parsing([
            'https://varus.ua/moloko-loko-moko-25-z-vitaminami-dlya-ditej-vid-3-h-rokiv-1000-g',
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-loko-moko-vid-3-rokiv-2-5-777584',
            'https://shop.nashkraj.ua/lutsk/product/284863-moloko-loko-moko-2-5-1l-t-p'
        ])

    def Moloko_Seljanske_pitne_ultrapasterizovane_2_5__900_g_parser(self):
        ''' Молоко «Селянське» питне ультрапастеризоване 2,5% 900 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-selianske-900g-ukrayina--04820003481547/',
            'https://varus.ua/moloko-selyanske-2-6-ultrapasterizovane-900-g',
            'https://shop.silpo.ua/product/moloko-selianske-pytne-ultrapasteryzovane-2-5-28734',
            'https://novus.online/product/moloko-25-selanske-900g',
            'https://metro.zakaz.ua/uk/products/moloko-selianske-900g-ukrayina--04820003481547/',
            'https://shop.nashkraj.ua/lutsk/product/38505-moloko-selyanske-2-5-900g-superp-t-f',
            'https://fozzyshop.ua/moloko/42123-moloko-selyanske-pitevoe-ultrapasterizovannoe-25-4820003480113.html'
        ])

    def Moloko_Seljanske_ultrapasterizovane_0_5__900_g_parser(self):
        ''' Молоко «Селянське» ультрапастеризоване 0,5% 900 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-selianske-ultrapasteryzovane-0-5-774674',
            'https://auchan.ua/ua/moloko-ul-trapasterizovannoe-seljans-ke-0-5-900-g-906937/',
            'https://metro.zakaz.ua/uk/products/moloko-selianske-900g-ukrayina--04820003486610/'
        ])

    def Moloko_ultrapasterizovane_Seljanske_1__900_g_parser(self):
        ''' Молоко ультрапастеризоване «Селянське» 1% 900 г '''
        return self.prices_parsing([
            'https://varus.ua/moloko-selyanske-1-ultrapasterizovane-900-g',
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-selianske-1-827093',
            'https://auchan.ua/ua/moloko-ul-trapasterizovanoe-seljans-ke-1-900-g-910773/',
            'https://novus.online/product/moloko-10-ultrapasteryzovane-selyanske-tfa-900h',
            'https://metro.zakaz.ua/uk/products/moloko-selianske-900g-ukrayina--04820003488409/',
            'https://fozzyshop.ua/moloko/93099-moloko-ultrapasterizovannoe-selyanske-1-4820003488409.html'
        ])

    def Moloko_Seljanske_ultrapasterizovane_3_2__900_g_parser(self):
        ''' Молоко «Селянське» ультрапастеризоване 3,2% 900 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-selianske-900g-ukrayina--04820003481554/',
            'https://varus.ua/moloko-selyanske-3-2-ultrapasterizovane-900-g-1',
            'https://shop.silpo.ua/product/moloko-selianske-ultrapasteryzovane-3-2-857479',
            'https://auchan.ua/ua/moloko-seljans-ke-ul-trapasterizovannoe-3-2-900-g-906569/',
            'https://novus.online/product/moloko-superpasterizovane-32-selanske-09l',
            'https://metro.zakaz.ua/uk/products/moloko-selianske-900g-ukrayina--04820003481554/',
            'https://shop.nashkraj.ua/lutsk/product/38506-moloko-selyanske-3-2-900g-ult-past-t-f'
        ])

    def Moloko_Seljanske_maljukam_vіd_3_rokіv_2_5__900_g_parser(self):
        ''' Молоко «Селянське» малюкам від 3 років 2,5% 900 г '''
        return self.prices_parsing([
            'https://varus.ua/moloko-selyanske-malyukam-2-5-ultrapasterizovane-900-g',
            'https://shop.silpo.ua/product/moloko-selianske-maliukam-vid-3-rokiv-2-5-719167',
            'https://auchan.ua/ua/moloko-ul-trapasterizovannoe-seljans-ke-dlja-detej-2-5-900-g-906688/',
            'https://novus.online/product/moloko-ultrapasterizovane-ditace-malukam-selanske-25-900g',
            'https://shop.nashkraj.ua/lutsk/product/232848-moloko-selyanske-2-5-900g-dityache-t-f',
            'https://fozzyshop.ua/moloko/44077-moloko-selyanske-malyukam-vid-3-rokiv-ultrapasterizovane-25-4820003486160.html'
        ])

    def Moloko_ultrapasterizovane_Jagotinske_2_6__900_g_parser(self):
        ''' Молоко ультрапастеризоване «Яготинське» 2,6% 900 г '''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/moloko-09-kg-agotinske-ultrapasterizovane-26',
            'https://eko.zakaz.ua/uk/products/moloko-iagotin-900g--04823005208259/',
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-yagotynske-2-6-848613',
            'https://auchan.ua/ua/moloko-jagotins-ke-2-6-900-g-1378503/',
            'https://novus.online/product/moloko-ultrapasteryzovane-26-yahotyn-900-h-tetrafino',
            'https://fozzyshop.ua/moloko/86228-moloko-ultrapasterizovannoe-yagotinske-26-4823005208259.html'
        ])

    def Moloko_Jagotinske_2_6__p_e_900_g_parser(self):
        ''' Молоко «Яготинське» 2,6% п/е 900 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-iagotin-900g--04823005203889/',
            'https://shop.silpo.ua/product/moloko-yagotynske-2-6-p-e-548446',
            'https://auchan.ua/ua/moloko-jagotins-ke-2-6-900-g-1378503/',
            'https://novus.online/product/moloko-26-agotin-pl-900g',
            'https://metro.zakaz.ua/uk/products/moloko-iagotin-900g--04823005203889/',
            'https://fozzyshop.ua/moloko/10016-moloko-yagotinske-26-p-e-4823005203889.html'
        ])

    def Moloko_Jagotinske_3_2__p_e_900_g_parser(self):
        ''' Молоко «Яготинське» 3,2% п/е 900 г '''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/moloko-09-kg-agotinske-32',
            'https://eko.zakaz.ua/uk/products/moloko-iagotin-900g--04823005203919/',
            'https://shop.silpo.ua/product/moloko-yagotynske-3-2-p-e-548448',
            'https://metro.zakaz.ua/uk/products/moloko-iagotin-900g--04823005203919/',
            'https://fozzyshop.ua/moloko/10018-moloko-yagotinske-32-p-e-4823005203919.html'
        ])

    def Moloko_ultrapasterizovane_Jagotinske_3_2__900_g_parser(self):
        ''' Молоко ультрапастеризоване «Яготинське» 3,2% 900 г '''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/moloko-09-kg-agotinske-ultrapasterizovane-32-tetra-fino',
            'https://eko.zakaz.ua/uk/products/moloko-iagotin-900g--04823005208266/',
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-yagotynske-3-2-848614',
            'https://fozzyshop.ua/moloko/86229-moloko-ultrapasterizovannoe-yagotinske-32-4823005208266.html'
        ])

    def Moloko_Jagotinske_prjazhene_2_6__p_e_900_g_parser(self):
        ''' Молоко «Яготинське» пряжене 2,6% п/е 900 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-yagotynske-priazhene-2-6-p-e-647784',
            'https://auchan.ua/ua/moloko-prjazhene-jagotins-ke-2-6-900-g-1378587/',
            'https://novus.online/product/moloko-prazene-26-agotin-plivka-900g'
        ])

    def Moloko_Galichina_Z_chistih_Karpat_2_5__900_g_parser(self):
        ''' Молоко «Галичина» «З чистих Карпат» 2,5% 900 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-galichina-900g-ukrayina--04820038493812/',
            'https://shop.silpo.ua/product/moloko-galychyna-z-chystykh-karpat-2-5-716286',
            'https://auchan.ua/ua/moloko-ul-trapasterizovannoe-galichina-2-5-900-g-906653/',
            'https://novus.online/product/moloko-tf-25-galicina-900g',
            'https://shop.nashkraj.ua/lutsk/product/179024-moloko-galichina-2-5-900g-karpat-t-f'
        ])

    def Moloko_Galichina_Іz_chistih_Karpat_1__900_g_parser(self):
        ''' Молоко «Галичина» «Із чистих Карпат» 1% 900 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-galichina-900g-ukrayina--04820038494123/',
            'https://varus.ua/moloko-galichina-1-900g',
            'https://shop.silpo.ua/product/moloko-galychyna-iz-chystykh-karpat-1-716285',
            'https://auchan.ua/ua/moloko-ul-trapasterizovannoe-galichina-1-900-g-906695/',
            'https://shop.nashkraj.ua/lutsk/product/272470-moloko-galichina-1-900ml-t-f',
            'https://fozzyshop.ua/moloko/44030-moloko-galichina-iz-chistykh-karpat-1-tetra-fina-4820038494123.html'
        ])

    def Moloko_Galichina_ultrapasterizovane_3_2___t_f_900_g_parser(self):
        ''' Молоко «Галичина» ультрапастеризоване 3,2%, т/ф 900 г '''
        return self.prices_parsing([
            'https://varus.ua/moloko-galichina-900g',
            'https://shop.silpo.ua/product/moloko-galychyna-ultrapasteryzovane-3-2-t-f-771997',
            'https://auchan.ua/ua/moloko-ul-trapasterizovannoe-galichina-3-2-900-g-906923/',
            'https://shop.nashkraj.ua/lutsk/product/248398-moloko-galichina-3-2-900g-t-f'
        ])

    def Moloko_Premіja_ultrapasterizovane_1__900_g_parser(self):
        ''' Молоко «Премія» ультрапастеризоване 1% 900 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-premiia-ultrapasteryzovane-1-799507',
            'https://fozzyshop.ua/moloko/85033-moloko-ultrapasterizovannoe-premiya-1-t-f-4823096414584.html'
        ])

    def Moloko_Premіja_ultrapasterizovane_2_5__900_g_parser(self):
        ''' Молоко «Премія» ультрапастеризоване 2,5% 900 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-premiia-ultrapasteryzovane-2-5-799508',
            'https://fozzyshop.ua/moloko/85034-moloko-ultrapasterizovannoe-premiya-25-t-f-4823096414591.html'
        ])

    def Moloko_pitne_Povna_Chasha_pasterizovane_2_5__900_g_parser(self):
        ''' Молоко питне «Повна Чаша» пастеризоване 2,5% 900 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-pytne-povna-chasha-pasteryzovane-2-5-541677'
        ])


    def Moloko_pitne_Povna_Chasha_pasterizovane_2_5__450_g_parser(self):
        ''' Молоко питне «Повна Чаша» пастеризоване 2,5% 450 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/moloko-povna-chasha-pasteryzovane-pytne-2-5-793005'
        ])


    def Moloko_ultrapasterizovane_Voloshkove_pole_2_5__900_g_parser(self):
        ''' Молоко ультрапастеризоване «Волошкове поле» 2,5% 900 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/moloko-voloshkove-pole-900g-ukrayina--04820004237846/',
            'https://varus.ua/moloko-voloshkove-pole-2-5-ultrapasterizovane-v-paketi-900-g',
            'https://shop.silpo.ua/product/moloko-ultrapasteryzovane-voloshkove-pole-2-5-777178',
            'https://auchan.ua/ua/moloko-ul-trapasterizovannoe-voloshkove-pole-2-5-900-g-906972/'
        ])


    def Moloko_Zlagoda_ditjache_3_2___p_e_400_g_parser(self):
        ''' Молоко «Злагода» дитяче 3,2%, п/е 400 г '''
        return self.prices_parsing([
            'https://varus.ua/moloko-zlagoda-malyatko-3-2-sterilizovane-400-g',
            'https://shop.silpo.ua/product/moloko-zlagoda-dytiache-kharchuvannia-vid-9-misiatsiv-3-2-p-e-785544'
        ])


    def Jogurt_Galichina_zlaki_2_2__zhiru_300_g_PET_parser(self):
        ''' Йогурт «Галичина» злаки 2,2% жиру 300 г ПЕТ '''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/jogurt-300g-galicina-zlaki-22',
            'https://varus.ua/yogurt-karpatskiy-z-zlakami-2-2-galichina-300g-plyashka',
            'https://shop.silpo.ua/product/yogurt-galychyna-z-napovniuvachem-zlaky-2-2-zhyru-709896',
            'https://novus.online/product/jogurt-22-zlaki-galicina-pet-300g',
            'https://metro.zakaz.ua/uk/products/iogurt-galichina-350g-ukrayina--04820038493287/'
        ])


    def Jogurt_Galichina_malina_2_2__300_g_PET_parser(self):
        ''' Йогурт «Галичина» малина 2,2% 300 г ПЕТ '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/yogurt-galychyna-malyna-2-2-709898'
        ])


    def Jogurt_Galichina_lіsova_jagoda_2_2__PET_300_g_parser(self):
        ''' Йогурт «Галичина» лісова ягода 2,2% ПЕТ 300 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/iogurt-galichina-300g-ukrayina--04820038493997/',
            'https://shop.silpo.ua/product/yogurt-galychyna-lisova-iagoda-2-2-709897',
            'https://metro.zakaz.ua/uk/products/iogurt-galichina-350g-ukrayina--04820038493263/',
            'https://shop.nashkraj.ua/lutsk/product/241140-yogurt-galichina-2-2-300g-lis-yag-pet',
            'https://fozzyshop.ua/deserty-i-jogurty/40687-jogurt-galichina-lesnaya-yagoda-22-but-4820038493997.html'
        ])


    def Jogurt_Galichina_polunitsja_2_2__PET_300_g_parser(self):
        ''' Йогурт «Галичина» полуниця 2,2% ПЕТ 300 г '''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/jogurt-300g-galicina-polunica-22',
            'https://shop.silpo.ua/product/yogurt-galychyna-polunytsia-2-2-709900',
            'https://shop.nashkraj.ua/lutsk/product/240989-yogurt-galichina-2-2-300g-polunits-pl'
        ])


    def Jogurt_Galichina_abrikos_2_2__PET_300_g_parser(self):
        ''' Йогурт «Галичина» абрикос 2,2% ПЕТ 300 г '''
        return self.prices_parsing([
            'https://shop.silpo.ua/product/yogurt-galychyna-abrykos-2-2-709895',
            'https://metro.zakaz.ua/uk/products/iogurt-galichina-350g-ukrayina--04820038493294/'
        ])


    def Jogurt_Galichina_Karpatskij_bez_tsukru_2_2__PET_300_g_parser(self):
        ''' Йогурт ««Галичина»» «Карпатський» без цукру 2,2% ПЕТ 300 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/iogurt-galichina-300g-ukrayina--04820038494444/',
            'https://varus.ua/yogurt-karpatskiy-bez-cukru-2-2-galichina-300g-plyashka',
            'https://shop.silpo.ua/product/yogurt-galychyna-karpatskyi-bez-tsukru-2-2-758546',
            'https://novus.online/product/jogurt-22-karpatskij-bez-cukru-galicina-pet-300g',
            'https://metro.zakaz.ua/uk/products/iogurt-galichina-420g-ukrayina--04820038491146/',
            'https://shop.nashkraj.ua/lutsk/product/268832-yogurt-galichina-2-2-300g-karp-b-tsuk',
            'https://fozzyshop.ua/deserty-i-jogurty/54136-jogurt-galichina-karpatskij-bez-sakhara-22-but-4820038494444.html'
        ])


    def Jogurt_Galichina_Karpatskij_vishnja_2_2__PET_300_g_parser(self):
        ''' Йогурт «Галичина» «Карпатський» вишня 2,2% ПЕТ 300 г '''
        return self.prices_parsing([
            'https://varus.ua/yogurt-vishnya-2-2-galichina-300g-pet',
            'https://shop.silpo.ua/product/yogurt-galychyna-karpatskyi-vyshnia-2-2-802294',
            'https://novus.online/product/jogurt-22-visna-galicina-pet-300g',
            'https://metro.zakaz.ua/uk/products/iogurt-galichina-300g-ukrayina--04820222760164/',
            'https://shop.nashkraj.ua/lutsk/product/331539-yogurt-galichina-2-2-300g-vishnya-pl'
        ])


    def Jogurt_Galichina_chornitsja_2_2__PET_300_g_parser(self):
        ''' Йогурт «Галичина» чорниця 2,2% ПЕТ 300 г '''
        return self.prices_parsing([
            'https://eko.zakaz.ua/uk/products/iogurt-galichina-300g-ukrayina--04820038494017/',
            'https://varus.ua/yogurt-karpatskiy-z-chorniceyu-2-2-galichina-300g-plyashka',
            'https://shop.silpo.ua/product/yogurt-galychyna-chornytsia-2-2-709899',
            'https://metro.zakaz.ua/uk/products/iogurt-galichina-350g-ukrayina--04820038493362/',
            'https://shop.nashkraj.ua/lutsk/product/242370-yogurt-galichina-2-2-300g-chornits-pet'
        ])


    def Jogurt_Galichina_chornitsja_zlaki_2_2__zhiru_PET_300_g_parser(self):
        ''' Йогурт «Галичина» чорниця-злаки 2,2% жиру ПЕТ 300 г '''
        return self.prices_parsing([
            'https://varus.ua/yogurt-chornicya-zlaki-2-2-galichina-300g-plyashka',
            'https://shop.silpo.ua/product/yogurt-galychyna-chornytsia-zlaky-2-2-zhyru-709893',
            'https://novus.online/product/jogurt-22-zlaki-cornica-galicina-pet-300g',
            'https://shop.nashkraj.ua/lutsk/product/241613-yogurt-galichina-2-2-300g-chornzl-pl',
            'https://fozzyshop.ua/deserty-i-jogurty/40692-jogurt-galichina-chernika-zlaki-22-but-4820038494055.html'
        ])


    def Jogur_Galichina_Karpatskij_bez_tsukru_bezlaktoznij_2_2__PET_300g_parser(self):
        ''' Йогур Галичина Карпатський без цукру безлактозний 2,2% ПЕТ 300г '''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/jogurt-300-g-galicina-bezlaktoznij-bez-cukru-22-pbut',
            'https://eko.zakaz.ua/uk/products/iogurt-galichina-300g-ukrayina--04820222760447/',
            'https://varus.ua/yogurt-2-2-bezlaktozniy-karpatskiy-galichina-ppl-300g',
            'https://novus.online/product/jogurt-22-bezlaktoznij-bez-cukru-karpatskij-galicina-petplaska-300g',
            'https://metro.zakaz.ua/uk/products/iogurt-galichina-300g-ukrayina--04820222760447/',
            'https://fozzyshop.ua/deserty-i-jogurty/92982-jogurt-galichina-karpatskij-bez-sakhara-bezlaktoznyj-22-pet-4820222760447.html'
        ])


    def Jogurt_Galichina_chornitsja_zlaki_2_2__pet__550g_parser(self):
        ''' Йогурт Галичина чорниця злаки 2,2% пет, 550г '''
        return self.prices_parsing([
            'https://varus.ua/yogurt-2-2-chornicya-zlaki-galichina-ppl-550g',
            'https://novus.online/product/jogurt-22-cornica-zlaki-galicina-pet-600g',
            'https://fozzyshop.ua/deserty-i-jogurty/88607-jogurt-galichina-chernika-zlaki-22-pet-4820038494079.html'
        ])


    def Jogurt_Galichina_Karpatskij_bez_tsukru_2_2__pet__550g_parser(self):
        ''' Йогурт Галичина Карпатський без цукру 2,2% пет, 550г '''
        return self.prices_parsing([
            'https://www.atbmarket.com/product/jogurt-055-kg-galicina-karpatskij-bez-cukru-22',
            'https://varus.ua/yogurt-karpatskiy-bez-cukru-2-2-galichina-550g-plyashka',
            'https://novus.online/product/jogurt-karpatskij-bez-cukru-22-galicina-pet-550g',
            'https://metro.zakaz.ua/uk/products/iogurt-galichina-600g-ukrayina--04820038494437/',
            'https://fozzyshop.ua/deserty-i-jogurty/88605-jogurt-galichina-karpatskij-bez-sakhara-22-pet-4820038494437.html'
        ])





# class Dishes:
#     '''Класс в котором собраны парсеры для блюд'''
#     # количество доступных маркетов
#
#     # добавочные ингридиенты
#     TOMAT_PASTE_VALUE, OIL_VALUE, LIMON_ACID_VALUE, SOLT_VALUE, LAVR_LIST_VALUE = 1, 1, 1, 1, 1
#     def dish_red_borsh_parser(self):
#         '''Парсинг цены красного борща в доступных супермаркетах'''
#         # соберем все цены ингридиентов для приготовления борща
#         water = self.water_in_6l_bottle_parser()
#         pork = self.pork_lopatka_parser()
#         potato = self.potato_parser()
#         beet = self.beet_parser()
#         carrot = self.carrot_parcer()
#         onion = self.onion_parcer()
#         cabbage = self.cabbage_parcer()
#
#         results = []
#         for i in range(self.COUNT_MARKETS):
#             result = round((float(water[i]) / 3 + float(pork[i]) * 0.8 +
#                             float(potato[i]) / 2 + float(beet[i]) / 10 +
#                             float(carrot[i]) / 10 + float(onion[i]) * 0.2 +
#                             float(cabbage[i]) * 0.4 + self.TOMAT_PASTE_VALUE +
#                             self.OIL_VALUE + self.LIMON_ACID_VALUE +
#                             self.SOLT_VALUE + self.LAVR_LIST_VALUE) / 6, 2)
#             results.append(result)
#         return results
#
#     def dish_vareniki_s_kartoshkoy_parser(self):
#         '''Парсинг цены вареников с картошкой в доступных супермаркетах'''
#         # соберем все цены ингридиентов для приготовления вареников с картошкой
#         flour = self.four_parser()
#         water = self.water_in_6l_bottle_parser()
#         eggs = self.egg_parcer()
#         eggs[0] = eggs[0] / 10  # атб яйца разделить на 10
#         oil = self.oil_for_dishes_parser()
#         onion = self.onion_parcer()
#         smetana = self.sour_cream_for_dishes_parser()
#         potato = self.potato_parser()
#
#         results = []
#         for i in range(self.COUNT_MARKETS):
#             result = round((float(flour[i]) * 0.4 + float(water[i]) * 0.033 +
#                             float(eggs[i]) + float(oil[i]) * 0.05 +
#                             float(onion[i]) * 0.2 + float(smetana[i]) +
#                             float(potato[i]) * 0.6 + self.SOLT_VALUE) / 5, 2)
#             results.append(result)
#         return results
#
#     def dish_vareniki_s_kapustoy_parser(self):
#         '''Парсер для вареников с капустой'''
#         # соберем все цены ингридиентов для приготовления вареников с капустой
#         flour = self.four_parser()
#         water = self.water_in_6l_bottle_parser()
#         eggs = self.egg_parcer()
#         eggs[0] = eggs[0] / 10  # атб яйца разделить на 10
#         oil = self.oil_for_dishes_parser()
#         onion = self.onion_parcer()
#         smetana = self.sour_cream_for_dishes_parser()
#         cabbage = self.cabbage_parcer()
#
#         results = []
#         for i in range(self.COUNT_MARKETS):
#             result = round((float(flour[i]) * 0.4 + float(water[i]) * 0.033 +
#                             float(eggs[i]) + float(oil[i]) * 0.05 +
#                             float(onion[i]) * 0.2 + float(smetana[i]) +
#                             float(cabbage[i]) * 0.6 + self.SOLT_VALUE) / 5, 2)
#             results.append(result)
#         return results


# class ProductParsers:
#     '''Класс для хранения парсеров для всех продуктов приложения'''
#     ATB_CLASS = 'product-price__top'
#     EKO_CLASS = 'jsx-161433026 Price__value_title'
#     EKO_DISCOUNT_CLASS = 'jsx-161433026 Price__value_title Price__value_discount'
#     VARUS_CLASS = 'sf-price__regular'
#     VARUS_SPECIAL_CLASS = 'sf-price__special'
#     VARUS_DISCOUNT_CLASS = 'jsx-161433026 Price__value_title Price__value_discount'
#
#     HEADERS = {
#         'Accept': '*/*',
#         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'
#     }
#
#     def price_parcing_find_next(self, page_url: str, class_: str):
#         url = page_url
#         headers = self.HEADERS
#         req = requests.get(url, headers=headers)
#         src = req.text
#         soup = BeautifulSoup(src, 'html.parser')
#         price = soup.find(class_=class_).find_next().text
#         return price
#
#     def price_parcing(self, page_url: str, class_: str):
#         url = page_url
#         headers = self.HEADERS
#         req = requests.get(url, headers=headers)
#         src = req.text
#         soup = BeautifulSoup(src, 'html.parser')
#         price = soup.find(class_=class_).text
#         return price
#
#     def obolon_premium_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Оболонь Премиум Экстра 1.1 л"'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/pivo-11l-obolon-premium-extra-brew-svitle-alk-46',
#             self.ATB_CLASS)
#
#         # # прописываем адресс страницы с пивом Оболонь Премиум Экстра 1.1 л
#         # url = 'https://www.atbmarket.com/product/pivo-11l-obolon-premium-extra-brew-svitle-alk-46'
#         #
#         # # создадим заголовки
#         # headers = {
#         #     'Accept': '*/*',
#         #     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'
#         # }
#         #
#         # # переменная req будет нам возвращать результат работы метода get библиотеки requests.
#         # # В аргументах указываем url сайта и наши заголовки:
#         # req = requests.get(url, headers=headers)
#         #
#         # # сохраним в переменную src полученный объект и вызовем у него метод text:
#         # src = req.text
#         #
#         # # далее сохраним нашу страницу в файл.
#         # # Т.к. многие сайты не любят, когда их парсят и велика вероятность получения бана
#         # # или ограничения по времени за большое количество запросов.
#         # # А сохранив страницу мы всегда можем продолжить работать с ней дальше.
#         # # with open('products_data/obolon_premium_(1.1).html','w') as f:
#         # #     f.write(src)
#         # #
#         # # #Далее откроем, прочитаем и сохраним наш файл страницы в переменную:
#         # # with open('products_data/obolon_premium_(1.1).html') as f:
#         # #     src=f.read()
#         #
#         # # создадим объект BeautifulSoup и передадим ему нашу переменную src
#         # # и парсер html.parser приступим к сбору данных:
#         # soup = BeautifulSoup(src, 'html.parser')
#         #
#         # # получаем цену пива:
#         # obolon_price = soup.find(class_='product-price__top').find_next().text
#         #
#         # return obolon_price
#
#     def beer_obolon_premium_ekomarket_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Пиво Оболонь Премиум 1.1 л в Эко-Маркете"'''
#         return self.price_parcing('https://eko.zakaz.ua/uk/products/pivo-obolon-1100ml-ukrayina--04820000190008/',
#                                   self.EKO_CLASS)
#
#     def vodka_getman_ICE_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Водка Гетьман ICE 0,7 л"'''
#         return self.price_parcing_find_next('https://www.atbmarket.com/product/gorilka-05l-getman-ice-40',
#                                             self.ATB_CLASS)
#
#     def coca_cola_2l_parcer(self):
#         '''Парсер для сбора данных о цене продукта "напиток Coca-Cola 2 л"'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/napij-225-l-coca-cola-bezalkogolnij-silnogazovanij',
#             self.ATB_CLASS)
#
#     def coca_cola_2l_ekomarket_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Пиво Оболонь Премиум 1.1 л в Эко-Маркете"'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/napii-koka-kola-2000ml--05449000009067/',
#             self.EKO_CLASS
#         )
#
#     def coca_cola_2l_varus_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Пиво Оболонь Премиум 1.1 л в Эко-Маркете"'''
#         return self.price_parcing(
#             'https://varus.ua/napiy-coca-cola-silnogazovaniy-2-l',
#             self.VARUS_CLASS
#         )[:5]
#
#     def garlik_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Чеснок, кг" в АТБ'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/casnik-import-1-gat',
#             self.ATB_CLASS
#         )
#
#     def garlik_eko_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Чеснок, кг" в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/ovochi-chasnik--ekomarket00000000640012/',
#             self.EKO_CLASS
#         )
#
#     def garlik_varus_parcer(self):
#         '''Парсер для сбора данных о цене продукта чеснок из Varus'''
#         return self.price_parcing(
#             'https://varus.ua/chasnik-vag',
#             self.VARUS_CLASS
#         )[:5]
#
#     def tea_minutka_black_40_b_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Чай Минутка, 40 п, черный"'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/caj-40-fp-h-14-g-minutka-black-tea-cornij-z-bergamotom-polsa',
#             self.ATB_CLASS
#         )
#
#     def tea_minutka_black_40_b_ekomarket_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Чай Минутка 40 пак чорный" в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/chai-56g--05900396000972/',
#             self.EKO_DISCOUNT_CLASS
#         )
#
#     def apple_golden_parcer(self):
#         '''Парсер для сбора данных о цене продукта яблоко Голден из АТБ'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/abluko-golden-1-gat',
#             self.ATB_CLASS
#         )
#
#     def apple_golden_ekomarket_parcer(self):
#         '''Парсер для сбора данных о цене продукта яблоко Голден из ЭКО-МАРКЕТА'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/frukt-iabluka--ekomarket00000000641182/',
#             self.EKO_CLASS
#         )
#
#     def apple_golden_varus_parcer(self):
#         '''Парсер для сбора данных о цене продукта яблоко Голден из Varus'''
#         return self.price_parcing(
#             'https://varus.ua/yabluko-golden-1-gatunok-vag',
#             self.VARUS_CLASS
#         )[:5]
#
#     def kent_8_ekomarket_parcer(self):
#         '''Парсер для сбора данных о цене продукта сигареты Кент 8 из ЭКО-МАРКЕТА'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/tsigarki-kent--04820192683371/',
#             self.EKO_CLASS
#         )
#
#     def kent_8_atb_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Kent 8" в АТБ'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/sigareti-kent-silver-25',
#             self.ATB_CLASS
#         )
#
#     def kent_8_varus_parcer(self):
#         '''Парсер для сбора данных о цене продукта сигареты Kent 8'''
#         return self.price_parcing(
#             'https://varus.ua/cigarki-kent-navy-blue-4-0-8-08',
#             self.VARUS_CLASS
#         )[:5]
#
#     def coffee_aroma_gold_ekomarket_parcer(self):
#         '''Парсер для сбора данных о цене продукта кофе растовримый Арома Голд'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/kava--04771632312880/',
#             self.EKO_DISCOUNT_CLASS
#         )
#
#     def oil_shedriy_dar_850_atb_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Масло подсолнечное рафинированное Щедрый Дар 850 мл"'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/olia-085l-sedrij-dar-sonasnikova-rafinovana',
#             self.ATB_CLASS
#         )
#
#     def oil_shedriy_dar_850_ekomarket_parcer(self):
#         '''Парсер для сбора данных о цене продукта
#          масло подсолнечное рафинированное Щедрый Дар 850 мл из Эко-Маркета'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/oliia-shchedrii-dar-850ml--04820078575769/',
#             self.EKO_CLASS
#         )
#
#     def fairy_limon_500_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта "Fairy лимон, 500 млг"'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/zasib-miucij-dla-posudu-05l-fairy-sokovitij-limon',
#             self.ATB_CLASS
#         )
#
#     def fairy_limon_500_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта "Fairy лимон, 500 млг"'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/zasib-feiri-500ml-ukrayina--05413149313842/',
#             self.EKO_CLASS
#         )
#
#     def fairy_limon_500_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта "Fairy лимон, 500 млг"'''
#         return self.price_parcing(
#             'https://varus.ua/zasib-d-posudu-sokovit-limon-fairy-500ml',
#             self.VARUS_SPECIAL_CLASS
#         )[:5]
#
#     def onion_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта лук в АТБ'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/cibula-ripcasta-1-gat',
#             self.ATB_CLASS
#         )
#
#     def onion_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта лук в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/ovochi-tsibulia--ekomarket00000000647281/',
#             self.EKO_CLASS
#         )
#
#     def onion_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта лук в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/cibulya-ripchasta-1-gatunok-vag',
#             self.VARUS_CLASS
#         )[:5]
#
#     def apple_black_prince_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта "Яблоко Черный Принц" в АТБ'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/abluko-red-princ-1gat',
#             self.ATB_CLASS
#         )
#
#     def apple_black_prince_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта "Яблоко Черный принц" в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/frukt-iabluka-bez-tm--ekomarket00000000645795/',
#             self.EKO_CLASS
#         )
#
#     def apple_black_prince_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта "Яблоко Черный принц" в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/yabloko-princ-vag',
#             self.VARUS_CLASS
#         )[:5]
#
#     def smetana_stolica_smaky_400_20_VARUS(self):
#         '''Парсер для сбора данных о цене продукта "Сметана Столиця Смаку 400 гр 20% жирности" в Varus'''
#         return self.price_parcing(
#             'https://varus.zakaz.ua/uk/products/ukrayina--04820194043531/',
#             self.VARUS_DISCOUNT_CLASS
#         )[:5]
#
#     def limon_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта лимон в АТБ'''
#         return self.price_parcing_find_next(
#             'https://atbmarket.com/product/limon-1-gat',
#             self.ATB_CLASS
#         )
#
#     def limon_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта лимон в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/frukt-tsitrus--ekomarket00000000650210/',
#             self.EKO_CLASS
#         )
#
#     def limon_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта лимон в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/limon-vag',
#             self.VARUS_SPECIAL_CLASS
#         )[:5]
#
#     def oil_oleyna_neraf_850_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта "Масло подсолнечное Олейна нерафинированное 850 гр" в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/oliia-oleina-900ml--04820077083500/',
#             self.EKO_CLASS
#         )
#
#     def tea_monomah_black_kenya_90_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта "Чай черный листовой Мономах Кения 90 гр" в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/chai-monomakh-90g--04820097812197/',
#             self.EKO_CLASS
#         )
#
#     def arko_cool_200_bonus100_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта "Пена для бритья ARKO Cool 300 млг+100млг бонус" в АТБ'''
#         return self.price_parcing_find_next(
#             'https://atbmarket.com/product/pina-dla-golinna-200100-ml-arko-men-cool',
#             self.ATB_CLASS
#         )
#
#     def arko_cool_200_bonus100_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта "Пена для бритья ARKO Cool 200 млг+100млг бонус" в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/pina-arko-200ml--08690506090029/',
#             self.EKO_CLASS
#         )
#
#     def arko_cool_200_bonus100_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта "Пена для бритья ARKO Cool 300 млг+100млг бонус" в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/pina-dlya-golinnya-kul-arko-200ml',
#             self.VARUS_SPECIAL_CLASS
#         )[:5]
#
#     def arko_sensitive_200_bonus100_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта "Пена для бритья ARKO Cool 300 млг+100млг бонус" в АТБ'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/pina-dla-golinna-200100-ml-arko-men-sensitive-promo',
#             self.ATB_CLASS
#         )
#
#     def arko_sensitive_200_bonus100_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта "Пена для бритья ARKO Cool 200 млг+100млг бонус" в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/pina-arko-200ml--08690506090043/',
#             self.EKO_CLASS
#         )
#
#     def arko_sensitive_200_bonus100_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта "Пена для бритья ARKO Cool 300 млг+100млг бонус" в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/pina-dlya-golinnya-ekstra-sensitiv-arko-200ml',
#             self.VARUS_SPECIAL_CLASS
#         )[:5]
#
#     def carrot_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта "Пена для бритья ARKO Cool 300 млг+100млг бонус" в АТБ'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/morkva-1gat',
#             self.ATB_CLASS
#         )
#
#     def carrot_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта "Пена для бритья ARKO Cool 200 млг+100млг бонус" в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/ovochi-morkva--ekomarket00000000640007/',
#             self.EKO_CLASS
#         )
#
#     def carrot_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта "Пена для бритья ARKO Cool 300 млг+100млг бонус" в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/morkva-1-gatunok-vag',
#             self.VARUS_CLASS
#         )[:5]
#
#     def cabbage_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта капуста в АТБ'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/kapusta-1-gat',
#             self.ATB_CLASS
#         )
#
#     def cabbage_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта капуста в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/ovochi-kapusta--ekomarket00000000667930/',
#             self.EKO_CLASS
#         )
#
#     def cabbage_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта капуста в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/kapusta-1-gatunok-vag',
#             self.VARUS_CLASS
#         )[:5]
#
#     def egg_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта яйца куринные в АТБ'''
#         return float(self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/ajce-kurace-10-st-ukraina-1-kategoria-fas',
#             self.ATB_CLASS
#         )) / 10
#
#     def egg_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта яйца куринные в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/iaitse--ekomarket00000026102825/',
#             self.EKO_CLASS
#         )
#
#     def egg_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта яйца куринные в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/yayce-kuryache-1sht',
#             self.VARUS_CLASS
#         )[:5]
#
#     def mayonez_detsk_shedro_67_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта "Майонез детский Щедро 67%" в АТБ'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/majonez-190g-sedro-domasnij-dla-ditej-67',
#             self.ATB_CLASS
#         )
#
#     def mayonez_detsk_shedro_67_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта "Майонез детский Щедро 67%" в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/maionez-shchedro-190g--04820184020054/',
#             self.EKO_CLASS
#         )
#
#     def mayonez_detsk_shedro_67_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта "Майонез детский Щедро 67%" в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/mayonez-domashniy-dlya-ditey-67-schedro-190g-d-p-ukraina',
#             self.VARUS_CLASS
#         )[:5]
#
#     def rexona_aloe_vera_w_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта "Дезодорант Rexona Aloe Vera женский" в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/dezodorant-reksona-150ml-velikobritaniia--08712561844338/',
#             self.EKO_DISCOUNT_CLASS
#         )
#
#     def marloboro_red_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта сигареты Мальборо красные в АТБ'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/sigareti-marlboro-27',
#             self.ATB_CLASS
#         )
#
#     def marloboro_red_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта сигареты Мальборо красные в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/tsigarki-malboro-25g--04823003205557/',
#             self.EKO_CLASS
#         )
#
#     def marloboro_red_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта сигареты Мальборо красные в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/cigarki-marlboro',
#             self.VARUS_CLASS
#         )[:5]
#
#     def beer_lvivske_svitle_24l_VARUS(self):
#         '''Парсер для сбора данных о цене продукта сигареты Мальборо красные в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/pivo-2-4l-4-5-svitle-pasteriz-lvivske',
#             self.VARUS_CLASS
#         )[:5]
#
#     def smetana_stolica_smaky_400_15_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта сметана "Столица Смаку 400 гр 15%" в Varus'''
#         return self.price_parcing(
#             'https://varus.zakaz.ua/ru/products/ukrayina--04820194043517/',
#             self.VARUS_DISCOUNT_CLASS
#         )[:5]
#
#     def dollar_value_parcer(self):
#         '''Парсер для отображения текущего курса доллара в обменниках'''
#         return self.price_parcing(
#             'https://finance.ua/ru/',
#             'fua-xrates__value'
#         )
#
#
# class AllDishParsers:
#     '''Класс в котором собраны парсеры для борща'''
#
#     # создадим заголовки
#     headers = {
#         'Accept': 'image/avif,image/webp,*/*',
#         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0'
#     }
#
#     def dish_red_borsh_parser_atb(self):
#         '''Парсер для борща'''
#         # прописываем адресс страницы:
#         # для воды:
#         water_url = 'https://www.atbmarket.com/product/voda-6-l-karpatska-dzerelna-negazovana'
#         # для свинины:
#         pork_url = 'https://www.atbmarket.com/product/okist-lembergmit-svinacij-oholodzenij-vakupak'
#         # для картошки
#         potato_url = 'https://www.atbmarket.com/product/kartopla-1-gat'
#         # для буряка
#         beet_url = 'https://www.atbmarket.com/product/burak-1-gat'
#         # для морковки
#         carrot_url = 'https://www.atbmarket.com/product/morkva-1gat'
#         # для лука
#         onion_url = 'https://www.atbmarket.com/product/cibula-ripcasta-1-gat'
#         # для капусты
#         cabbage_url = 'https://www.atbmarket.com/product/kapusta-1-gat'
#
#         # переменная req будет нам возвращать результат работы метода get библиотеки requests.
#         # В аргументах указываем url сайта и наши заголовки:
#         water_req = requests.get(water_url, headers=self.headers)
#         pork_req = requests.get(pork_url, headers=self.headers)
#         potato_req = requests.get(potato_url, headers=self.headers)
#         beet_req = requests.get(beet_url, headers=self.headers)
#         carrot_req = requests.get(carrot_url, headers=self.headers)
#         onion_req = requests.get(onion_url, headers=self.headers)
#         cabbage_req = requests.get(cabbage_url, headers=self.headers)
#
#         # сохраним в переменную src полученный объект и вызовем у него метод text:
#         water_src = water_req.text
#         pork_src = pork_req.text
#         potato_src = potato_req.text
#         beet_src = beet_req.text
#         carrot_src = carrot_req.text
#         onion_src = onion_req.text
#         cabbage_src = cabbage_req.text
#
#         # создадим объект BeautifulSoup и передадим ему нашу переменную src
#         # и парсер html.parser приступим к сбору данных:
#         water_soup = BeautifulSoup(water_src, 'html.parser')
#         pork_soup = BeautifulSoup(pork_src, 'html.parser')
#         potato_soup = BeautifulSoup(potato_src, 'html.parser')
#         beet_soup = BeautifulSoup(beet_src, 'html.parser')
#         carrot_soup = BeautifulSoup(carrot_src, 'html.parser')
#         onion_soup = BeautifulSoup(onion_src, 'html.parser')
#         cabbage_soup = BeautifulSoup(cabbage_src, 'html.parser')
#
#         # получаем цены всех ингридиентов:
#         water_value = float(water_soup.find(class_='product-price__top').find_next().text) / 3
#         pork_value = float(pork_soup.find(class_='product-price__top').find_next().text) * 0.8
#         potato_value = float(potato_soup.find(class_='product-price__top').find_next().text) / 2
#         beet_value = float(beet_soup.find(class_='product-price__top').find_next().text) / 10
#         carrot_value = float(carrot_soup.find(class_='product-price__top').find_next().text) / 10
#         onion_value = float(onion_soup.find(class_='product-price__top').find_next().text) * 0.2
#         cabbage_value = float(cabbage_soup.find(class_='product-price__top').find_next().text) * 0.4
#         tomat_paste_value = 1
#         oil_value = 1
#         limon_acid_value = 1
#         solt_value = 1
#         lavr_list_value = 1
#
#         total_sum = (water_value + pork_value +
#                      potato_value + beet_value +
#                      carrot_value + onion_value +
#                      cabbage_value + tomat_paste_value +
#                      oil_value + limon_acid_value +
#                      solt_value + lavr_list_value) / 6
#
#         return total_sum
#
#     def dish_red_borsh_parser_eko(self):
#         '''Парсер для борща Эко-маркет'''
#
#         find_class = 'jsx-161433026 Price__value_title Price__value_discount'
#
#         water_url = 'https://eko.zakaz.ua/uk/products/voda-karpatska-dzherelna-6000ml--04820051240240/'
#         pork_url = 'https://eko.zakaz.ua/uk/products/m-iaso--ekomarket00000000535086/'
#         potato_url = 'https://eko.zakaz.ua/uk/products/ovochi-kartoplia--ekomarket00000000667970/'
#         beet_url = 'https://eko.zakaz.ua/uk/products/ovochi-buriak--ekomarket00000000646097/'
#         carrot_url = 'https://eko.zakaz.ua/uk/products/ovochi-morkva--ekomarket00000000640007/'
#         onion_url = 'https://eko.zakaz.ua/uk/products/ovochi-tsibulia--ekomarket00000000647281/'
#         cabbage_url = 'https://eko.zakaz.ua/uk/products/ovochi-kapusta--ekomarket00000000667930/'
#
#         water_soup = BeautifulSoup(requests.get(water_url, headers=self.headers).text, 'html.parser')
#         pork_soup = BeautifulSoup(requests.get(pork_url, headers=self.headers).text, 'html.parser')
#         potato_soup = BeautifulSoup(requests.get(potato_url, headers=self.headers).text, 'html.parser')
#         beet_soup = BeautifulSoup(requests.get(beet_url, headers=self.headers).text, 'html.parser')
#         carrot_soup = BeautifulSoup(requests.get(carrot_url, headers=self.headers).text, 'html.parser')
#         onion_soup = BeautifulSoup(requests.get(onion_url, headers=self.headers).text, 'html.parser')
#         cabbage_soup = BeautifulSoup(requests.get(cabbage_url, headers=self.headers).text, 'html.parser')
#
#         water_value = float(water_soup.find(class_=find_class).text) / 3
#         pork_value = float(pork_soup.find(class_='jsx-161433026 Price__value_title').text) * 0.8
#         potato_value = float(potato_soup.find(class_='jsx-161433026 Price__value_title').text) / 2
#         beet_value = float(beet_soup.find(class_='jsx-161433026 Price__value_title').text) / 10
#         carrot_value = float(carrot_soup.find(class_='jsx-161433026 Price__value_title').text) / 10
#         onion_value = float(onion_soup.find(class_='jsx-161433026 Price__value_title').text) * 0.2
#         cabbage_value = float(cabbage_soup.find(class_='jsx-161433026 Price__value_title').text) * 0.4
#         tomat_paste_value = 1
#         oil_value = 1
#         limon_acid_value = 1
#         solt_value = 1
#         lavr_list_value = 1
#
#         total_sum = (water_value + pork_value +
#                      potato_value + beet_value +
#                      carrot_value + onion_value +
#                      cabbage_value + tomat_paste_value +
#                      oil_value + limon_acid_value +
#                      solt_value + lavr_list_value) / 6
#
#         return total_sum
#
#     def dish_red_borsh_parser_varus(self):
#         '''Парсер для борща Varus'''
#
#         find_class = 'sf-price__regular'
#
#         water_url = 'https://varus.ua/voda-vygoda-negazirovannaya-vygoda-6-l'
#         pork_url = 'https://varus.ua/lopatka-svinaya-vesovaya'
#         potato_url = 'https://varus.ua/kartoplya-1-gatunok-vag'
#         beet_url = 'https://varus.ua/buryak-1-gatunok-vag'
#         carrot_url = 'https://varus.ua/morkva-1-gatunok-vag'
#         onion_url = 'https://varus.ua/cibulya-ripchasta-1-gatunok-vag'
#         cabbage_url = 'https://varus.ua/kapusta-1-gatunok-vag'
#
#         water_soup = BeautifulSoup(requests.get(water_url, headers=self.headers).text, 'html.parser')
#         pork_soup = BeautifulSoup(requests.get(pork_url, headers=self.headers).text, 'html.parser')
#         potato_soup = BeautifulSoup(requests.get(potato_url, headers=self.headers).text, 'html.parser')
#         beet_soup = BeautifulSoup(requests.get(beet_url, headers=self.headers).text, 'html.parser')
#         carrot_soup = BeautifulSoup(requests.get(carrot_url, headers=self.headers).text, 'html.parser')
#         onion_soup = BeautifulSoup(requests.get(onion_url, headers=self.headers).text, 'html.parser')
#         cabbage_soup = BeautifulSoup(requests.get(cabbage_url, headers=self.headers).text, 'html.parser')
#
#         water_value = (water_soup.find(class_=find_class).text)
#         pork_value = (pork_soup.find(class_='sf-price__special').text)
#         potato_value = (potato_soup.find(class_='sf-price__special').text)
#         beet_value = (beet_soup.find(class_='sf-price__special').text)
#         carrot_value = (carrot_soup.find(class_=find_class).text)
#         onion_value = (onion_soup.find(class_=find_class).text)
#         cabbage_value = (cabbage_soup.find(class_=find_class).text)
#         tomat_paste_value = 1
#         oil_value = 1
#         limon_acid_value = 1
#         solt_value = 1
#         lavr_list_value = 1
#
#         total_sum = ((float(water_value[:5]) / 3) + (float(pork_value[:5]) * 0.8) +
#                      (float(potato_value[:5]) / 2) + (float(beet_value[:5]) / 10) +
#                      (float(carrot_value[:5]) / 10) + (float(onion_value[:5]) * 0.2) +
#                      (float(cabbage_value[:5]) * 0.4) + tomat_paste_value + oil_value +
#                      limon_acid_value + solt_value + lavr_list_value) / 6
#
#         return total_sum
#
#     def dish_variniki_s_kartoshkoy_atb(self):
#         '''Парсер для вареников с картошкой АТБ'''
#
#         find_class = 'product-price__top'  # класс div по которому будем искать цену
#
#         flour_url = 'https://www.atbmarket.com/product/borosno-1-kg-hutorok-psenicne-visij-gatunok'
#         water_url = 'https://www.atbmarket.com/product/voda-6-l-karpatska-dzerelna-negazovana'
#         egg_url = 'https://www.atbmarket.com/product/ajce-kurace-10-st-ukraina-1-kategoria-fas'
#         oil_url = 'https://www.atbmarket.com/product/olia-085l-olejna-tradicijna-sonasnikova-rafinovana'
#         onion_url = 'https://www.atbmarket.com/product/cibula-ripcasta-1-gat'
#         sour_cream_url = 'https://www.atbmarket.com/product/smetana-300-g-agotinska-15-pstakan'
#         potato_url = 'https://www.atbmarket.com/product/kartopla-1-gat'
#
#         flour_soup = BeautifulSoup(requests.get(flour_url, headers=self.headers).text, 'html.parser')
#         water_soup = BeautifulSoup(requests.get(water_url, headers=self.headers).text, 'html.parser')
#         egg_soup = BeautifulSoup(requests.get(egg_url, headers=self.headers).text, 'html.parser')
#         oil_soup = BeautifulSoup(requests.get(oil_url, headers=self.headers).text, 'html.parser')
#         onion_soup = BeautifulSoup(requests.get(onion_url, headers=self.headers).text, 'html.parser')
#         sour_cream_soup = BeautifulSoup(requests.get(sour_cream_url, headers=self.headers).text, 'html.parser')
#         potato_soup = BeautifulSoup(requests.get(potato_url, headers=self.headers).text, 'html.parser')
#
#         flour_value = float(flour_soup.find(class_=find_class).find_next().text) * 0.4
#         water_value = float(water_soup.find(class_=find_class).find_next().text) * 0.033
#         egg_value = float(egg_soup.find(class_=find_class).find_next().text) * 0.1
#         oil_value = float(oil_soup.find(class_=find_class).find_next().text) * 0.05
#         onion_value = float(onion_soup.find(class_=find_class).find_next().text) * 0.2
#         sour_cream_value = float(sour_cream_soup.find(class_=find_class).find_next().text)
#         potato_value = float(potato_soup.find(class_=find_class).find_next().text) * 0.6
#         solt_value = 1
#
#         total_sum = (flour_value + water_value +
#                      egg_value + oil_value +
#                      onion_value + sour_cream_value +
#                      solt_value + potato_value) / 5
#
#         return total_sum
#
#     def dish_variniki_s_kartoshkoy_eko(self):
#         '''Парсер для вареников с картошкой ЭКО-МАркет'''
#
#         find_class = 'jsx-161433026 Price__value_title'
#
#         flour_url = 'https://eko.zakaz.ua/uk/products/boroshno-khutorok-1000g-ukrayina--04820101710204/'
#         water_url = 'https://eko.zakaz.ua/uk/products/voda-karpatska-dzherelna-6000ml--04820051240240/'
#         egg_url = 'https://eko.zakaz.ua/uk/products/iaitse--ekomarket00000026102825/'
#         oil_url = 'https://eko.zakaz.ua/uk/products/oliia-oleina-850ml--04820001115567/'
#         onion_url = 'https://eko.zakaz.ua/uk/products/ovochi-tsibulia--ekomarket00000000647281/'
#         sour_cream_url = 'https://eko.zakaz.ua/uk/products/smetana-iagotin-300g--04823005209584/'
#         potato_url = 'https://eko.zakaz.ua/uk/products/ovochi-kartoplia--ekomarket00000000667970/'
#
#         flour_soup = BeautifulSoup(requests.get(flour_url, headers=self.headers).text, 'html.parser')
#         water_soup = BeautifulSoup(requests.get(water_url, headers=self.headers).text, 'html.parser')
#         egg_soup = BeautifulSoup(requests.get(egg_url, headers=self.headers).text, 'html.parser')
#         oil_soup = BeautifulSoup(requests.get(oil_url, headers=self.headers).text, 'html.parser')
#         onion_soup = BeautifulSoup(requests.get(onion_url, headers=self.headers).text, 'html.parser')
#         sour_cream_soup = BeautifulSoup(requests.get(sour_cream_url, headers=self.headers).text, 'html.parser')
#         potato_soup = BeautifulSoup(requests.get(potato_url, headers=self.headers).text, 'html.parser')
#
#         flour_value = float(flour_soup.find(class_=find_class).text) * 0.4
#         water_value = float(water_soup.find(class_=find_class).text) * 0.033
#         egg_value = float(egg_soup.find(class_=find_class).text)
#         oil_value = float(oil_soup.find(class_=find_class).text) * 0.05
#         onion_value = float(onion_soup.find(class_=find_class).text) * 0.2
#         sour_cream_value = float(sour_cream_soup.find(class_=find_class).text)
#         potato_value = float(potato_soup.find(class_='jsx-161433026 Price__value_title').text) * 0.6
#         solt_value = 1
#
#         total_sum = (flour_value + water_value +
#                      egg_value + oil_value +
#                      onion_value + sour_cream_value +
#                      potato_value + solt_value) / 5
#
#         return total_sum
#
#     def dish_variniki_s_kartoshkoy_varus(self):
#         '''Парсер для вареников с картошкой Varus'''
#
#         find_class = 'sf-price__regular'
#
#         flour_url = 'https://varus.ua/boroshno-pshenichne-vigoda-1-kg'
#         water_url = 'https://varus.ua/voda-vygoda-negazirovannaya-vygoda-6-l'
#         egg_url = 'https://varus.ua/yayce-kuryache-1sht'
#         oil_url = 'https://varus.ua/maslo-podsolnechnoe-oleyna-tradicionnaya-rafinirovannoe-850-ml'
#         onion_url = 'https://varus.ua/cibulya-ripchasta-1-gatunok-vag'
#         sour_cream_url = 'https://varus.ua/smetana-yagotinska-15-450g'
#         potato_url = 'https://varus.ua/kartoplya-1-gatunok-vag'
#
#         flour_soup = BeautifulSoup(requests.get(flour_url, headers=self.headers).text, 'html.parser')
#         water_soup = BeautifulSoup(requests.get(water_url, headers=self.headers).text, 'html.parser')
#         egg_soup = BeautifulSoup(requests.get(egg_url, headers=self.headers).text, 'html.parser')
#         oil_soup = BeautifulSoup(requests.get(oil_url, headers=self.headers).text, 'html.parser')
#         onion_soup = BeautifulSoup(requests.get(onion_url, headers=self.headers).text, 'html.parser')
#         sour_cream_soup = BeautifulSoup(requests.get(sour_cream_url, headers=self.headers).text, 'html.parser')
#         potato_soup = BeautifulSoup(requests.get(potato_url, headers=self.headers).text, 'html.parser')
#
#         flour_value = (flour_soup.find(class_=find_class).text)
#         water_value = (water_soup.find(class_=find_class).text)
#         egg_value = (egg_soup.find(class_=find_class).text)
#         oil_value = (oil_soup.find(class_=find_class).text)
#         onion_value = (onion_soup.find(class_=find_class).text)
#         sour_cream_value = (sour_cream_soup.find(class_=find_class).text)
#         potato_value = (potato_soup.find(class_='sf-price__special').text)
#         solt_value = 1
#
#         total_sum = ((float(flour_value[:5]) * 0.4) + (float(water_value[:5]) * 0.033) +
#                      (float(egg_value[:5])) + (float(oil_value[:5]) * 0.05) +
#                      (float(onion_value[:5]) * 0.02) + (float(sour_cream_value[:5])) +
#                      (float(potato_value[:5]) * 0.6) + solt_value) / 5
#
#         return total_sum
#
#     def dish_variniki_s_kapustoy_atb(self):
#         '''Парсер для вареников с капустой'''
#
#         flour_url = 'https://www.atbmarket.com/product/borosno-1-kg-hutorok-psenicne-visij-gatunok'
#         water_url = 'https://www.atbmarket.com/product/voda-6-l-karpatska-dzerelna-negazovana'
#         egg_url = 'https://www.atbmarket.com/product/ajce-kurace-10-st-ukraina-1-kategoria-fas'
#         oil_url = 'https://www.atbmarket.com/product/olia-085l-olejna-tradicijna-sonasnikova-rafinovana'
#         onion_url = 'https://www.atbmarket.com/product/cibula-ripcasta-1-gat'
#         sour_cream_url = 'https://www.atbmarket.com/product/smetana-300-g-agotinska-15-pstakan'
#         cabbage_url = 'https://www.atbmarket.com/product/kapusta-1-gat'
#
#         flour_soup = BeautifulSoup(requests.get(flour_url, headers=self.headers).text, 'html.parser')
#         water_soup = BeautifulSoup(requests.get(water_url, headers=self.headers).text, 'html.parser')
#         egg_soup = BeautifulSoup(requests.get(egg_url, headers=self.headers).text, 'html.parser')
#         oil_soup = BeautifulSoup(requests.get(oil_url, headers=self.headers).text, 'html.parser')
#         onion_soup = BeautifulSoup(requests.get(onion_url, headers=self.headers).text, 'html.parser')
#         sour_cream_soup = BeautifulSoup(requests.get(sour_cream_url, headers=self.headers).text, 'html.parser')
#         cabbage_soup = BeautifulSoup(requests.get(cabbage_url, headers=self.headers).text, 'html.parser')
#
#         flour_value = float(flour_soup.find(class_='product-price__top').find_next().text) * 0.4
#         water_value = float(water_soup.find(class_='product-price__top').find_next().text) * 0.033
#         egg_value = float(egg_soup.find(class_='product-price__top').find_next().text) * 0.1
#         oil_value = float(oil_soup.find(class_='product-price__top').find_next().text) * 0.05
#         onion_value = float(onion_soup.find(class_='product-price__top').find_next().text) * 0.2
#         sour_cream_value = float(sour_cream_soup.find(class_='product-price__top').find_next().text)
#         cabbage_value = float(cabbage_soup.find(class_='product-price__top').find_next().text) * 0.6
#         solt_value = 1
#         carrot_value = 1
#
#         total_sum = (flour_value + water_value +
#                      egg_value + oil_value +
#                      onion_value + sour_cream_value +
#                      solt_value + cabbage_value + carrot_value) / 5
#
#         return total_sum
#
#     def dish_variniki_s_kapustoy_eko(self):
#         '''Парсер для вареников с капустой Эко-маркет'''
#
#         find_class = 'jsx-161433026 Price__value_title'
#
#         flour_url = 'https://eko.zakaz.ua/uk/products/boroshno-khutorok-1000g-ukrayina--04820101710204/'
#         water_url = 'https://eko.zakaz.ua/uk/products/voda-karpatska-dzherelna-6000ml--04820051240240/'
#         egg_url = 'https://eko.zakaz.ua/uk/products/iaitse--ekomarket00000026102825/'
#         oil_url = 'https://eko.zakaz.ua/uk/products/oliia-oleina-850ml--04820001115567/'
#         onion_url = 'https://eko.zakaz.ua/uk/products/ovochi-tsibulia--ekomarket00000000647281/'
#         sour_cream_url = 'https://eko.zakaz.ua/uk/products/smetana-iagotin-300g--04823005209584/'
#         cabbage_url = 'https://eko.zakaz.ua/uk/products/ovochi-kapusta--ekomarket00000000667930/'
#
#         flour_soup = BeautifulSoup(requests.get(flour_url, headers=self.headers).text, 'html.parser')
#         water_soup = BeautifulSoup(requests.get(water_url, headers=self.headers).text, 'html.parser')
#         egg_soup = BeautifulSoup(requests.get(egg_url, headers=self.headers).text, 'html.parser')
#         oil_soup = BeautifulSoup(requests.get(oil_url, headers=self.headers).text, 'html.parser')
#         onion_soup = BeautifulSoup(requests.get(onion_url, headers=self.headers).text, 'html.parser')
#         sour_cream_soup = BeautifulSoup(requests.get(sour_cream_url, headers=self.headers).text, 'html.parser')
#         cabbage_soup = BeautifulSoup(requests.get(cabbage_url, headers=self.headers).text, 'html.parser')
#
#         flour_value = float(flour_soup.find(class_=find_class).text) * 0.4
#         water_value = float(
#             water_soup.find(class_='jsx-161433026 Price__value_title Price__value_discount').text) * 0.033
#         egg_value = float(egg_soup.find(class_=find_class).text) * 0.1
#         oil_value = float(oil_soup.find(class_=find_class).text) * 0.05
#         onion_value = float(onion_soup.find(class_=find_class).text) * 0.2
#         sour_cream_value = float(sour_cream_soup.find(class_=find_class).text)
#         cabbage_value = float(cabbage_soup.find(class_=find_class).text) * 0.6
#         solt_value = 1
#         carrot_value = 1
#
#         total_sum = (flour_value + water_value +
#                      egg_value + oil_value +
#                      onion_value + sour_cream_value +
#                      solt_value + cabbage_value + carrot_value) / 5
#
#         return total_sum
#
#     def dish_variniki_s_kapustoy_varus(self):
#         '''Парсер для вареников с капустой Эко-маркет'''
#
#         find_class = 'sf-price__regular'
#
#         flour_url = 'https://varus.ua/boroshno-pshenichne-vigoda-1-kg'
#         water_url = 'https://varus.ua/voda-vygoda-negazirovannaya-vygoda-6-l'
#         egg_url = 'https://varus.ua/yayce-kuryache-1sht'
#         oil_url = 'https://varus.ua/maslo-podsolnechnoe-oleyna-tradicionnaya-rafinirovannoe-850-ml'
#         onion_url = 'https://varus.ua/cibulya-ripchasta-1-gatunok-vag'
#         sour_cream_url = 'https://varus.ua/smetana-yagotinska-15-450g'
#         cabbage_url = 'https://varus.ua/kapusta-1-gatunok-vag'
#
#         flour_soup = BeautifulSoup(requests.get(flour_url, headers=self.headers).text, 'html.parser')
#         water_soup = BeautifulSoup(requests.get(water_url, headers=self.headers).text, 'html.parser')
#         egg_soup = BeautifulSoup(requests.get(egg_url, headers=self.headers).text, 'html.parser')
#         oil_soup = BeautifulSoup(requests.get(oil_url, headers=self.headers).text, 'html.parser')
#         onion_soup = BeautifulSoup(requests.get(onion_url, headers=self.headers).text, 'html.parser')
#         sour_cream_soup = BeautifulSoup(requests.get(sour_cream_url, headers=self.headers).text, 'html.parser')
#         cabbage_soup = BeautifulSoup(requests.get(cabbage_url, headers=self.headers).text, 'html.parser')
#
#         flour_value = (flour_soup.find(class_=find_class).text)
#         water_value = (water_soup.find(class_=find_class).text)
#         egg_value = (egg_soup.find(class_=find_class).text)
#         oil_value = (oil_soup.find(class_=find_class).text)
#         onion_value = (onion_soup.find(class_=find_class).text)
#         sour_cream_value = (sour_cream_soup.find(class_=find_class).text)
#         cabbage_value = (cabbage_soup.find(class_=find_class).text)
#         solt_value = 1
#
#         total_sum = ((float(flour_value[:5]) * 0.4) + (float(water_value[:5]) * 0.033) +
#                      (float(egg_value[:5])) + (float(oil_value[:5]) * 0.05) +
#                      (float(onion_value[:5]) * 0.02) + (float(sour_cream_value[:5])) +
#                      (float(cabbage_value[:5]) * 0.6) + solt_value) / 5
#
#         return total_sum

# def best_price_parcer(self):
#     '''Парсер для сбора данных о акционной цене на некий товар'''
#
#     # прописываем адресс страницы с пивом Оболонь Премиум Экстра 1.1 л
#     url_1 = 'https://www.atbmarket.com/product/sokolad-90g-millennium-poristij-bilij'
#     url_2='https://www.atbmarket.com/product/vinograd-susenij-150g-svoa-linia-kismis-zolotistij'
#     url_3='https://www.atbmarket.com/product/vino-075l-igriste-asti-salute-bile-solodke-9-12'
#
#
#
#     # создадим заголовки
#     headers={
#          'Accept':'*/*',
#          'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'
#     }
#
#     # переменная req будет нам возвращать результат работы метода get библиотеки requests.
#     # В аргументах указываем url сайта и наши заголовки:
#     req_1=requests.get(url_1,headers=headers)
#     req_2=requests.get(url_2,headers=headers)
#     req_3 = requests.get(url_3, headers=headers)
#
#     #сохраним в переменную src полученный объект и вызовем у него метод text:
#     src_1=req_1.text
#     soup_1=BeautifulSoup(src_1,'html.parser')
#
#     src_2 = req_2.text
#     soup_2 = BeautifulSoup(src_2, 'html.parser')
#
#     src_3 = req_3.text
#     soup_3 = BeautifulSoup(src_3, 'html.parser')
#
#     #получаем цену товара:
#     product_1_price=soup_1.find(class_='product-price__top').find_next().text
#     product_2_price = soup_2.find(class_='product-price__top').find_next().text
#     product_3_price = soup_3.find(class_='product-price__top').find_next().text
#
#     #получем название товара:
#     product_1_name=soup_1.find(class_='page-title product-page__title').text
#     product_2_name = soup_2.find(class_='page-title product-page__title').text
#     product_3_name = soup_3.find(class_='page-title product-page__title').text
#
#     return product_1_price, product_1_name,\
#         product_2_price, product_2_name,\
#         product_3_price, product_3_name
