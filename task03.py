new_dict = {}

key_1 = input('Input key 1: ')
value_1 = input('Input value 1: ')
new_dict[key_1] = value_1

key_2 = input('Input key 2: ')
value_2 = input('Input value 2: ')
new_dict[key_2] = value_2

key_3 = input('Input key 3: ')
value_3 = input('Input value 3: ')
new_dict[key_3] = value_3

print(new_dict)

del new_dict[key_2]

print(new_dict)
