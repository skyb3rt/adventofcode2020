def read_file():
    with open ("7.txt", 'r' ) as file:
        return file.read().split('\n')

def write_file(value):
    with open("7.json","w") as file:
        file.write(value)

def list_to_dict(l):
    d ={}
    for i in l:
        my_list= (i.split(' bags contain'))
        key= my_list[0]
        value_list=my_list[1].replace('bags','').replace('bag','').replace(' .','').strip().split(',')
        d.update({key:value_list})
    for key in d:
        l=[]
        for i in d.get(key):
            j= ((' ').join(i.strip().split(' ')[1:]))
            l.append(j)
        d[key]=l
    #print(d)
    return(d)



def behandle_dict(d):
    for key in d:
        #print(d.get(key))
        l={}
        for i in range(0,len(d.get(key))):
            d_value=d.get(d.get(key)[i])
            l.update({d[key][i]:d_value})
        d[key]=l
    return d



def find_value_in_dict(d,value):
    total=0
    for key in d:
        if str(key).count(value)>0:
            total+=1
        if (str(d.get(key))).count(value)>0:
            total+=1
    print(total)



d=behandle_dict(list_to_dict(read_file()))
write_file(str(d).replace('\'','\"').replace('None','none'))
find_value_in_dict(d,'gold')
