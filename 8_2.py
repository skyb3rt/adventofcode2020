import csv
def read_file():
    l=[]
    with open ("8.txt") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        for row in csv_reader:
            l.append({row[0]:row[1]})
    return l

def run_instruction(l):
    antall=[0]*len(l)
    acc=0
    i=0
    while True:
        antall[i]+=1
        if antall.count(2)==1:
            return(False)
        if i==len(l)-1:
            print('aac :',acc)
            return(True)
        d=l[i]
        for key in d.keys():
            value=int(d.get(key))
            if key == 'nop':
                i+=1
            if key == 'acc':
                acc+=value
                i+=1
            if key == 'jmp':
                i+=value 

def change_instruction(l):
    for x in range(0,len(l)):
        m=l.copy()
        d=m[x]
        for key in d.keys():
            value=int(d.get(key))
            if key =='jmp':
                m[x]={'nop':value}
                if run_instruction(m):
                    return (x+1,key,value)
            if key =='nop':
                m[x]={'jmp':value}
                if run_instruction(m):
                    return (x+1,key,value)        
    return('Not found')

print(change_instruction(read_file()))