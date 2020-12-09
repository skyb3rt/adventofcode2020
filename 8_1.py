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
            break
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
    return(acc)

print(run_instruction(read_file()))