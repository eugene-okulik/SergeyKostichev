PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_list = list(PRICE_LIST.split("\n"))

new_dict = {key.split()[0]: key.split()[1][:-1] for key in new_list}

# Или через список
# alternative_list = [(x.split()[0], x.split()[1][:-1]) for x in list(PRICE_LIST.split("\n"))]
# alternative_dict = dict(alternative_list)
# print(alternative_dict)
print(new_dict)
