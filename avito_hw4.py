import json

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
    def __repr__(self):
        return f'\033[0;{self.repr_color_code};{self.repr_color_code}m{self.title} | {self.price} ₽\n'



class Advert(ColorizeMixin):
    
    """Класс объяслений, который показывает название, цену тип и другие параметры объявления"""
    
    repr_color_code = 32
    
    def __init__(self, adv: json):
        adv_info = json.loads(adv)
        self.__dict__.update(adv_info)
    
    @property        
    def class_(self):
        self.__dict__['class'] = self.__dict__.get('class', None)
        return self.__dict__['class']
         
    @property
    def price(self):
        self.__dict__['price'] = self.__dict__.get('price', 0)
        if self.__dict__['price'] < 0:
            return ValueError('price must be >= 0')
        else:
            return self.__dict__['price']
        

if __name__ == '__main__':
    lesson = Advert(lesson_str)
    iphone = Advert(iphone_ad)
    dog_ad = Advert(dog_ad)
