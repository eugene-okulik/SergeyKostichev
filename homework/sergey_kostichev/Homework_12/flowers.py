class Flower:
    def __init__(self, name, color, length, lifetime, price):
        self.__name = name
        self.__color = color
        self.__stem_length = length
        self.__lifetime = lifetime
        self.__price = price

    @property
    def price(self):
        return self.__price

    @property
    def lifetime(self):
        return self.__lifetime

    @property
    def stem_length(self):
        return self.__stem_length

    @property
    def color(self):
        return self.__color

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return (f'{self.color} {self.name} is {self.stem_length} cm long, '
                f'its lifetime reaches up to {self.lifetime} days. It costs {self.price}$.').capitalize()

    def __repr__(self):
        return (f'{self.color} {self.name} is {self.stem_length} cm long, '
                f'its lifetime reaches up to {self.lifetime}. It costs {self.price}$.').capitalize()


class Daisy(Flower):

    def __init__(self, color, length, lifetime, price, is_fresh):
        self.__name = "Daisy"
        super().__init__(self.__name, color, length, lifetime, price)
        self.is_fresh = is_fresh

    def __str__(self):
        if self.is_fresh:
            return super().__str__() + ' This flower is fresh.'
        return super().__str__()

    def __repr__(self):
        if self.is_fresh:
            return super().__repr__() + ' This flower is fresh.'
        return super().__repr__()


class Rose(Flower):
    def __init__(self, color, length, lifetime, price, is_spiky):
        self.__name = "Rose"
        super().__init__(self.__name, color, length, lifetime, price)
        self.is_spiky = is_spiky

    def __str__(self):
        if self.is_spiky:
            return super().__str__() + ' This flower has thorns.'
        return super().__str__()

    def __repr__(self):
        if self.is_spiky:
            return super().__repr__() + ' This flower has thorns.'
        return super().__repr__()


class Anduwanchik(Flower):
    def __init__(self, color, length, lifetime, price, is_fluffy):
        self.__name = "Dandelion"
        super().__init__(self.__name, color, length, lifetime, price)
        self.is_fluffy = is_fluffy

    def __str__(self):
        if self.is_fluffy:
            return super().__str__() + ' This flower is already fluffy.'
        return super().__str__()

    def __repr__(self):
        if self.is_fluffy:
            return super().__repr__() + ' This flower is already fluffy.'
        return super().__repr__()
