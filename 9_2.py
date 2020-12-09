

def read_file():
    with open ("9.txt", 'r' ) as f:
        return [int(i) for i in f.readlines()]


def find_nr(l,total):
    for x in range (0,len(l)):
        sum_l=[]
        for j in range(x,len(l)):
            sum_l.append(l[j])
            if sum(sum_l) == total:
                return (min(sum_l)+max(sum_l))
            if sum(sum_l) > total:
                break        

print(find_nr(read_file(),15353384))