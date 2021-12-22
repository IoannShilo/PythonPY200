from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)
        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)
        self.add_water_to_glass(occupied_volume)

    def init_capacity_volume(self, capacity_volume: Union[int, float]) -> None:
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume >= 1:
            raise ValueError
        self.capacity_volume = capacity_volume

    def init_occupied_volume(self, occupied_volume: Union[int, float]) -> None:
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume
        if occupied_volume > self.capacity_volume:
            raise ValueError

    def add_water_to_glass(self, water: Union[int, float]) -> None:
        if self.occupied_volume > self.capacity_volume:
            raise ValueError("Объем вливаемой жидкости больше объема стакана")
        self.occupied_volume

    def remove_water_from_glass(self, water: Union[int, float]) -> None:
        if occupied_volume < self.capacity_volume:
            raise ValueError("")







if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)
    glass.add_water_to_glass(50)
    print(glass.capacity_volume, glass.occupied_volume)