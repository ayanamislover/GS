import math

def calculate_distance(lat1, lon1, lat2, lon2):
    """计算两个坐标点之间的距离"""
    R = 6371  # 地球平均半径，单位公里
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(math.radians(lat1)) * math.cos(
        math.radians(lat2)) * math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

def is_within_distance(lat1, lon1, lat2, lon2, threshold):
    """判断两个坐标点之间的距离是否在限制范围内"""
    distance = calculate_distance(lat1, lon1, lat2, lon2)
    return distance <= threshold
