
def merge_lists_to_dic(list1, list2):
    return dict(zip(list1, list2))

list_a = ['key1', 'key2', 'key3']
list_b = ['val1', 'val2', 'val3']

print(merge_lists_to_dic(list_a, list_b))
