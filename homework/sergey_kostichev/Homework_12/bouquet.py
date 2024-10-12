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

    def __define_expiration(self):  # определяет время его увядания по среднему времени жизни всех цветов в букете.
        expiration_time = 0
        for flower in self.flowers:
            expiration_time += flower.lifetime
        expiration_time = expiration_time / len(self.flowers)
        return round(expiration_time)

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

    def find_by_color(self, color):
        found_flowers = []

        for flower in self.flowers:
            if flower.color == color:
                found_flowers.append(flower)

        if len(found_flowers) > 0:
            flowers_txt = ", ".join([flower.name for flower in found_flowers])
            print("There are", len(found_flowers), color, "flowers in the bouquet: ", flowers_txt)
        else:
            print("There are no", color, "flowers in the bouquet")

    def find_by_price(self, price):
        found_flowers = []
        for flower in self.flowers:
            if flower.price <= price:
                found_flowers.append(flower)

        if len(found_flowers) > 0:
            flowers_txt = ", ".join([f"{flower.name} {flower.price}$" for flower in found_flowers])
            print(f"There are {len(found_flowers)} flowers in the bouquet with under {price}: {flowers_txt}")
        else:
            print("There are no flowers in the bouquet with such price")

    def __show_details(self):
        text = ""
        for flower in self.flowers:
            text += str(flower) + "\n"
        average_lifetime = f"The average lifetime of this beautiful bouquet is {self.__lifetime} days.\n"
        return text + average_lifetime

    def __str__(self):
        template = self.__show_details()
        return f"This bouquet consists from {len(self.flowers)} flowers:\n" + template

    def __repr__(self):
        template = self.__show_details()
        return f"This bouquet consists from {len(self.flowers)} flowers:\n" + template
