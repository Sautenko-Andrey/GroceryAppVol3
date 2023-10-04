from transliterate import translit

class AutoCode:


    # for the groceryappNNtext.py
    __PATH_to_groceryappNNtext = "../GroceryAppVol3/FBApp/my_app/groceryappNNtext.py"
    __INSERT_ROW_groceryappNNtext = 39

    # for the utils.py
    __PATH_to_utils = "../GroceryAppVol3/FBApp/my_app/utils.py"

    # for the parsers.py
    __PATH_to_parsers = "../GroceryAppVol3/FBApp/my_app/parsers.py"

    # for the product_prices_DATA_batches.py
    __PATH_to_product_prices_DATA_batches = "../GroceryAppVol3/FBApp/my_app/product_prices_DATA_batches.py"

    #for the tags.py
    __PATH_to_tags = "../GroceryAppVol3/FBApp/my_app/templatetags/my_app_tags.py"

    #for item_full_names.py
    __PATH_to_item_names = "../GroceryAppVol3/FBApp/my_app/items_full_names.py"

    #for testerRNN
    __PATH_to_tester_RNN = "../GroceryAppVol3/FBApp/my_app/tester_for_groceryappNN_TEXT.py"


    __slots__ = ("__item_full_name", "__pk", "__index", "prepeared_text")

    def __init__(self, item_full_name: str, pk: int, index: int):
        self.__item_full_name = item_full_name   #full name of item
        self.__pk = pk   #for tags
        self.__index = index   #index in tester RNN
        self.prepeared_text = self.code_litters()

    def __call__(self, item_amount: int, line_num_utils: int,
                 line_num_parsers: int, line_product_prices_data: int, *args, **kwargs):

        # changing value of items in line №40 groceryappNNtext.py
        self.__open_read_write_save(
            self.__PATH_to_groceryappNNtext,
            self.__INSERT_ROW_groceryappNNtext,
            f"    ITEMS_AMOUNT = {item_amount}\n"
        )
        # end of operation

        # appending new lines in the utils.py
        self.__open_read_write_save(
            self.__PATH_to_utils,
            line_num_utils,
            f"        elif nn_respond == {self.prepeared_text.upper()}:\n            result = self.getting_prices('{self.prepeared_text}', get_{self.prepeared_text})"
        )
        # end of operation

        # appending new lines in the parsers.py
        self.__open_read_write_save(
            self.__PATH_to_parsers,
            line_num_parsers,
            f"    def {self.prepeared_text}_parser(self):\n        ''' {self.__item_full_name} '''\n        return self.prices_parsing([])"
        )
        # end of operation

        # appending new lines in the product_prices_DATA_batches.py
        self.__open_read_write_save(
            self.__PATH_to_product_prices_DATA_batches,
            line_product_prices_data,
            "            {'" + f"{self.prepeared_text}':" + "{}},"
        )
        # end of operation

        #appending code into tags.py, items_full_names.py and testerRNN
        self.__write_code()
        #end

    def __open_read_write_save(self, path: str, line: int, new_text: str):
        with open(path, "r") as file:
            data = file.readlines()

        data[line] = new_text

        with open(path, "w") as file:
            file.writelines(data)

    def code_litters(self) -> str:
        eng_text = translit(self.__item_full_name, language_code='ru', reversed=True)
        new = []
        for let in eng_text:
            if let == " " or let == "," or let == "%" or let == "/":
                new.append("_")
                continue
            elif let == "'" or let == "«" or let == "»":
                new.append("")
                continue
            new.append(let)
        new_text = "".join(new)

        return new_text

    def __write_code(self):

        # writting code for tags
        with open(self.__PATH_to_tags, "a") as file:
            file.write(
                f"""'''Тэг,возвращающий информацию о "{self.__item_full_name}"'''\nget_{self.prepeared_text} = tag.create_tag(ItemsPicsFromNet,{self.__pk})\n""")

        # writting code for item_names
        with open(self.__PATH_to_item_names, "a") as file:
            file.write(f'{self.prepeared_text.upper()} = "{self.__item_full_name}"\n')

        # writting code for tester_RNN
        with open(self.__PATH_to_tester_RNN, "a") as file:
            file.write(f"        elif np.argmax(result) == {self.__index}:\n            return {self.prepeared_text.upper()}\n")





add_item = AutoCode(
    "Молоко ультрапастеризоване «На здоров'я» дитяче 3,2% 950 г",
    755,   #+1
    751  #+1
)

add_item(
    752,  #+1
    1842,  #+2
    7049,  #+15
    5466  #+10
)

