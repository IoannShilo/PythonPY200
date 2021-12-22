from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        #  TODO заменить на метод
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume  # объем стакана

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume  # объем жидкости в стакане

#  TODO создать метод, который будет инициализировать атрибут capacity_volume


if __name__ == "__main__":
    ...  # TODO инициализировать экземпляр класса Glass
    print(...)  # TODO распечатать атрибут capacity_volume
    print(...)  # TODO распечатать атрибут occupied_volume
