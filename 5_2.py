import math

def read_file():
    with open ("5.txt", 'r' ) as file:
        return file.read().split('\n')

def find_row(code):
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

def find_column(code):
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
    return (find_row(code)*8+find_column(code))

def find_missing_seat_id(l):
    seat_id_list=[]
    for i in range (0,len(l)):
        seat_id_list.append(int(seat_id(l[i])))
    for j in range(min(seat_id_list),max(seat_id_list)+1):
        try:
            seat_id_list.index(j)
        except ValueError:
            return j
    return seat_id_list

print(find_missing_seat_id(read_file()))

