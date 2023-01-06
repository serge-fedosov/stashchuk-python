def route_info(info):
    if 'distance' in info and isinstance(info['distance'], int):
        return f"Distance to your destination is {info['distance']}"
    elif 'speed' in info and 'time' in info:
        return f"Distance to your destination is {info['speed'] * info['time']}"
    else:
        return "No distance info is available"


distance_info_1 = {
    'distance': 100
}

distance_info_2 = {
    'speed': 10,
    'time': 2
}

distance_info_3 = {
    'error': 1
}

print(route_info(distance_info_1))
print(route_info(distance_info_2))
print(route_info(distance_info_3))
