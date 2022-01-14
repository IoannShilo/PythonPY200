class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        if not isinstance(day, int):
            raise TypeError
        if not isinstance(month, int):
            raise TypeError
        if not isinstance(year, int):
            raise TypeError
        self.day = day
        self.month = month
        self. year = year

    def __repr__(self) -> str:
        return f'Date({self.day}, {self.month}, {self.year})'

    def __str__(self) -> str:
        return f'{self.day:02}/{self.month:02}/{self.year}'


if __name__ == '__main__':

    date = Date(1, 3, 1991)

    print(date)
