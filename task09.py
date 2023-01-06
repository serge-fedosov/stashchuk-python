def image_info(info):
    if 'image_id' not in info:
        raise TypeError("В словаре нет ключа 'image_id'")
    if 'image_title' not in info:
        raise TypeError("В словаре нет ключа 'image_title'")

    return f"Image '{info['image_title']} has id {info['image_id']}"


image_dict = {
    'image_id': 100,
    'image_title': 'my image'
}

print(image_info(image_dict))
