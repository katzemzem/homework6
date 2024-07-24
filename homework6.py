my_dict = {'Ivan': 2001, 'Liza': 2000, 'Sasha': 2004, 'Lena': 1998}
print(my_dict)
print(my_dict.get('Stepan'),',', my_dict['Lena'])
my_dict.update({'Susan': 1987, 'Denis': 1986})
print(my_dict)
print(my_dict.pop('Ivan'))
print(my_dict)

my_set = {1, 4, 6, 3, (2, 7, 8), 1, 1, 6, 4, 1, 3, 'Ivan', 'Ivan', True}
my_set = set(my_set)
print(my_set)
my_set.update({78, 9})
my_set.discard(1)
print(my_set)
