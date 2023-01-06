def filter_list(input_list, input_type):
    result_list = []
    for value in input_list:
        if isinstance(value, input_type):
            result_list.append(value)

    return result_list


test_list = [0, 5, 'qwerty', 45.5, -7, [2], {}]
print(filter_list(test_list, int))
print(filter_list(test_list, float))
print(filter_list(test_list, list))
print(filter_list(test_list, dict))
