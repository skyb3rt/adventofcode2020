
def read_file():
    with open ("9.txt", 'r' ) as f:
        return [int(i) for i in f.readlines()]

def find_nr(l,preamble):

    for x in range (preamble,len(l)):
        l_prev=l[x-preamble:x]
        nr=l[x]
        found=[]
        for j in l_prev:
            found.append(nr-int(j) in l_prev)
        if found.count(True) == 0:
            return nr

print(find_nr(read_file(),25))