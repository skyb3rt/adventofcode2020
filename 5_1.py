import math

def read_file():
    with open ("5.txt", 'r' ) as file:
        return file.read().split('\n')

def finn_row(code):
    low = 0
    high = 127
    for x in range (0,7):
        if code[x] == 'F':
            high = high-(math.ceil((high-low)/2))
        if code[x] == 'B':
            low = low+(math.ceil((high-low)/2))
    if low == high:
        return low
    return 0

def finn_column(code):
    low = 0
    high = 7
    for x in range (7,len(code)):
        if code[x] == 'L':
            high = high-(math.ceil((high-low)/2))
        if code[x] == 'R':
            low = low+(math.ceil((high-low)/2))
    if low == high:
        return low
    return 0

def seat_id(code):
    return (finn_row(code)*8+finn_column(code))

def find_highest_seat_id(l):
    highest_seat_id=0
    for x in range (0,len(l)):
        highest_seat_id=max(seat_id(l[x]),highest_seat_id)
    return highest_seat_id

print(find_highest_seat_id(read_file()))


