import json

test_dict = {
    'key1': 'value 1',
    'key2': 2,
    'key3': 45.5,
    'key4': [1, 2],
    'key5': None
}


json_str = json.dumps(test_dict, indent=2)

print(json_str)
print(type(json_str))
