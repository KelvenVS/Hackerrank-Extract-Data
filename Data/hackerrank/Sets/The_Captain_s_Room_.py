from collections import Counter

def whitch_room(num_room,rooms):
    counter_rooms = Counter(rooms)
    for room, count in counter_rooms.items():
        if count == 1:
            return room

if __name__ ==  '__main__':
    num_room = int(input())
    rooms = map(int, input().split())
    print(whitch_room(num_room,rooms))
