from typing import Union


class Espresso:
    """Эспрессо."""

    def __init__(self, volume: Union[int, float]):
        self.volume = volume


class Milk:
    """Молоко."""

    def __init__(self, volume: Union[int, float]):
        self.volume = volume


class MilkFoam:
    """Молочная пена."""

    def __init__(self, volume: Union[int, float]):
        self.volume = volume


class IceCream:
    """Мороженное."""

    def __init__(self, volume: Union[int, float]):
        self.volume = volume


class Coffee:
    """Кофейный напиток."""

    def __init__(
        self,
        name: str,
        espresso: Espresso,
        milk: Milk = None,
        milk_foam: MilkFoam = None,
        ice_cream: IceCream = None,
    ):
        self.name = name
        self.espresso = espresso
        self.milk = milk
        self.milk_foam = milk_foam
        self.ice_cream = ice_cream

    def __str__(self):
        return f'Coffee("{self.name}")'


class CoffeeMachine:
    """Кофемашина."""

    @staticmethod
    def get_cappuccino() -> Coffee:
        """Делает капучино."""
        espresso = Espresso(volume=1 / 3)
        milk = Milk(volume=1 / 3)
        milk_foam = MilkFoam(volume=1 / 3)

        return Coffee(
            name="Капучино", espresso=espresso, milk=milk, milk_foam=milk_foam
        )

    @staticmethod
    def get_latte() -> Coffee:
        """Делает латте."""
        espresso = Espresso(volume=1 / 4)
        milk = Milk(volume=2 / 4)
        milk_foam = MilkFoam(volume=1 / 4)

        return Coffee(name="Латте", espresso=espresso, milk=milk, milk_foam=milk_foam)

    @staticmethod
    def get_iced_coffee() -> Coffee:
        """Делает глясе."""
        espresso = Espresso(volume=1 / 2)
        ice_cream = IceCream(volume=1 / 2)

        return Coffee(name="Глясе", espresso=espresso, ice_cream=ice_cream)


if __name__ == "__main__":
    cappuccino = CoffeeMachine.get_cappuccino()
    latte = CoffeeMachine.get_latte()
    iced_coffee = CoffeeMachine.get_iced_coffee()

    print("Кофе 1:", cappuccino)
    print("Кофе 2:", latte)
    print("Кофе 3:", iced_coffee)
