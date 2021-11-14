import json
import keyword

lesson_str = """{
                "title": "python",
                "location": {
                            "address": "город Москва, Лесная, 7",
                            "metro_stations": ["Белорусская"]
                            }
                }"""

iphone_ad = """{
                "title": "iPhone X",
                "price": 100,
                "location": {
                "address": "город Самара, улица Мориса Тореза, 50",
                "metro_stations": ["Спортивная", "Гагаринская"]
                            }
                }"""

dog_ad = """{
            "title": "Вельш-корги",
            "price": 1000,
            "class": "dogs",
            "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
                        }
            }"""


class ColorizeMixin:
    """Класс который перекрашивает цвет текста объявления"""
    def __repr__(self):
        text = super().__repr__()
        return f'\033[0;{self.repr_color_code};{self.repr_color_code}m{text}\n'

    
class BaseAdvert:
    """Класс, который преобразовывает json в dict """
    def __repr__(self):
        return f'{self.title} | {self.price}₽'
    

class JsonParser:
    def __init__(self, adv):
        adv_info = json.loads(adv)
        
        for key, value in adv_info.items():
            if isinstance(value, dict):
                value = JsonParser(json.dumps(value))
            
            if keyword.iskeyword(key):
                key = key + '_'
            
            self.__dict__[key] = value

            
class Advert(ColorizeMixin, JsonParser, BaseAdvert):
    
    """Класс объяслений, который показывает название, цену тип и другие параметры объявления"""
    
    repr_color_code = 32
            
    @property
    def price(self):
        self.__dict__['price'] = self.__dict__.get('price', 0)
        if self.__dict__['price'] < 0:
            raise ValueError('price must be >= 0')
        else:
            return self.__dict__['price']         
            