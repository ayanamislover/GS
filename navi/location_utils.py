import math
from usersinformation.models import PlayerProfile
def calculate_distance(lat1, lon1, lat2, lon2):
    # Calculate the distance between two coordinate points
    R = 6371  
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(math.radians(lat1)) * math.cos(
        math.radians(lat2)) * math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

def is_within_distance(lat1, lon1, lat2, lon2, threshold):
    # Determine if the distance between two coordinate points is within the limits
    distance = calculate_distance(lat1, lon1, lat2, lon2)
    return distance <= threshold
