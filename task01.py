new_list = [1, 2.0, 'abc', True, [23, 7], {'type': 1, 'sort': 2}]
print(new_list)

del new_list[3]
print(new_list)

print(len(new_list))

new_list.reverse()

print(new_list)

other_list = ['q', -12]

# new_list.append(other_list)
new_list = new_list + other_list
print(new_list)
