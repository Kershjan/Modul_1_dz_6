my_dict = {'Alex' : 1990, 'Misha' : 1965, 'Nikita' : 2002}
print(my_dict)
print(my_dict['Alex'])
print(my_dict.get('Denis'))
my_dict['Pasha'] = 1995
my_dict['Dasha'] = 1999
a = my_dict.pop('Nikita')
print(a)
print(my_dict)

my_set = {1,2,2,5,5, 'Hello', False}
print(my_set)
my_set.add('book')
my_set.add(9)
my_set.remove(1)
print(my_set)
