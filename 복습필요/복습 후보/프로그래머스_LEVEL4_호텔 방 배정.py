def findParentRoom(room, checkInRoom):
    if room not in checkInRoom:
        checkInRoom[room] = room + 1
        return room
    empty = findParentRoom(checkInRoom[room], checkInRoom)
    checkInRoom[room] = empty + 1
    return empty

def solution(k, room_number):
    checkInRoom = {}
    for wantedRoom in room_number:
        findParentRoom(wantedRoom, checkInRoom)
    return list(checkInRoom.keys())

k = 10
room_number = [3, 3, 1, 3]
print(solution(k, room_number))