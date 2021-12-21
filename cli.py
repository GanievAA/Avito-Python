import click
import random
import pizza
from typing import Callable


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    if delivery:
        click.echo(bake(pizza))
        click.echo(deliver(pizza))
    else:
        click.echo(bake(pizza))


@cli.command()
def menu():
    """Выводит меню"""
    click.echo('-Margarita : tomato sauce, mozzarella, tomatoes')
    click.echo('-Pepperoni : tomato sauce, mozzarella, pepperoni')
    click.echo('-Hawaiian : tomato sauce, mozzarella, chicken, pineapple')


def log(text: str):
    def wrapper(func: Callable):
        def inner_wrapper(*args, **kwargs):
            n = random.randint(1, 50)
            print(text.format(n))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper


@log('Приготовили за {}с!')
def bake(pizza):
    return f'Приготовили пиццу {pizza}'


@log('Доставили за {}с!')
def deliver(pizza):
    return f'Доставили пиццу {pizza}'


# bake(pizza.Margarita(size='L'))
# deliver(pizza.Margarita(size='L'))

if __name__ == '__main__':
    cli()
