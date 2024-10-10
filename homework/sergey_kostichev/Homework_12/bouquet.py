import flowers


def decor(txt):
    def inner_decor(func):
        def wrapper(*args, **kwargs):  # сюда попадает какой-то пустой кортеж (,), не разобрался, поставил этот костыль
            print("Sorted by", txt)
            return func(*args, **kwargs)
        return wrapper
    return inner_decor


class Bouquet:
    def __init__(self, *args):
        self.flowers = list(args)
        self.__price = self.__give_price()
        self.__lifetime = self.__define_expiration()


    @property
    def price(self):
        return self.__price

    @property
    def lifetime(self):
        return self.__lifetime

    def __give_price(self):
        sum = 0
        for flower in self.flowers:
            sum += flower.price
        return round(sum, 2)

    def __define_expiration(self): # определяет время его увядания по среднему времени жизни всех цветов в букете.
        expiration_time = 0
        for flower in self.flowers:
            expiration_time += flower.lifetime
        expiration_time = expiration_time / len(self.flowers)
        return  round(expiration_time)

    @decor("lifetime")
    def sort_by_fresh(self):
       self.flowers.sort(key=lambda flower: flower.lifetime, reverse=True)

    @decor("price")
    def sort_by_price(self):
       self.flowers.sort(key=lambda flower: flower.price, reverse=True)

    @decor("length")
    def sort_by_length(self):
        self.flowers.sort(key=lambda flower: flower.stem_length, reverse=True)

    @decor("color")
    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color, reverse=True)

    def search_flower(self): # поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни)
        ...


    def __show_details(self):
        text = ""
        for flower in self.flowers:
            text += str(flower) + "\n"
        return text

    def __str__(self):
        template = self.__show_details()
        return f"This bouquet consists from {len(self.flowers)} flowers:\n" + template


    def __repr__(self):
        return ""
