def read_file():
    with open ("6.txt", 'r' ) as file:
        return file.read().split('\n\n')

def counter(l):
    total=0
    for i in range(0,len(l)):
        l2=l[i].split('\n')
        if len(l2)==1:
            total+=len(l2[0])
        else:
            for char in l2[0]:
                if ("").join(l2).count(char) == len(l2):
                    total+=1
    return total

print(counter(read_file()))