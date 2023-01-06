def dict_to_list(input_dict):
    res_list = []
    for k, v in input_dict.items():
        if isinstance(v, int):
            v *= 2
        res_list.append((k, v))

    return res_list

test_dict = {
    'key1': 10,
    'key2': 'qwerty',
    'key3': 23.5
}

print(dict_to_list(test_dict))
