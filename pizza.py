class Pizza(object):
    """Класс пиццы"""
    def __init__(self, size: str, cheese: str, sauce: str, toppings: tuple):
        self.cheese = cheese
        self._size = size
        self.sauce = sauce
        self.toppings = toppings

    def dict(self):
        return {self.cheese, self.sauce, *self.toppings}

    def __eq__(self, other):
        if isinstance(self, Pizza) and isinstance(other, Pizza):
            return self.size == other.size and self.cheese == other.cheese and self.sauce == other.sauce and\
                   self.toppings == other.toppings
        else:
            return 'Objects are incomparable'

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value: str):
        if value not in ['L', 'XL']:
            raise ValueError('The size of the pizza should be "L" or "XL"')
        else:
            self._size = value


# toppings tuple так как предполагаю, что рецепт пиццы не меняется
class Margarita(Pizza):
    def __init__(self, size: str, cheese='mozzarella', sauce='tomato sauce', toppings=('tomatoes',)):
        super().__init__(size, cheese, sauce, toppings)

    def __str__(self):
        return 'Margarita'


class Pepperoni(Pizza):
    def __init__(self, size: str, cheese='mozzarella', sauce='tomato sauce', toppings=('pepperoni',)):
        super().__init__(size, cheese, sauce, toppings)

    def __str__(self):
        return 'Pepperoni'


class Hawaiian(Pizza):
    def __init__(self, size: str, cheese='mozzarella', sauce='tomato sauce', toppings=('chicken', 'pineapple')):
        super().__init__(size, cheese, sauce, toppings)

    def __str__(self):
        return 'Hawaiian'


if __name__ == '__main__':
    hawaiian_pizza = Hawaiian(size='XL')
    pepperoni_pizza = Pepperoni(size='L')
    print(Pizza(size='L', cheese='mozzarella', sauce='tomato sauce', toppings=('pepperoni', )) == pepperoni_pizza)
