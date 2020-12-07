def read_file():
    with open ("6.txt", 'r' ) as file:
        return file.read().split('\n\n')



def counter(l):
    total=0
    for i in range(0,len(l)):
        antall =0
        value=str(l[i]).replace('\n','')
        #print (value)
        while len(value) !=0:
            antall+=1
            value=value.replace(value[0],'')
        total+=antall
    return total

print(counter(read_file()))