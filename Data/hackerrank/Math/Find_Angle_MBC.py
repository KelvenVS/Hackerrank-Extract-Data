import math

def find_angle_mbc(AB, BC):
    theta = math.degrees(math.atan(BC / AB))
    return 90-round(theta)

AB = int(input())
BC = int(input())

degree = '\u00B0'
print(f"{find_angle_mbc(AB, BC)}{degree}")
