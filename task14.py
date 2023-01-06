test_dict = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
}

new_dict = {k: v.upper() for k, v in test_dict.items()}

print(test_dict)
print(new_dict)
