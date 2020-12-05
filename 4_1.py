def read_file():
    with open ("4.txt", 'r' ) as file:
        return ''.join(file.readlines()).split('\n\n')

def create_dict(l):
    l_dict={'dict':[]}
    for x in range(0,len(l)):
        mydict={}
        l[x]=l[x].replace('\n',' ')
        my_list=l[x].split(' ')
        for x in range(0,len(my_list)):
            my_string_parts = my_list[x].split(':')
            mydict.update({my_string_parts[0]:my_string_parts[1]})
        l_dict['dict'].append(mydict)
    return l_dict

def counter(my_dict):
    antall = 0
    for x in range(0,len(my_dict['dict'])):
        d=my_dict['dict'][x]
        d.pop('cid',None)
        if len(d.keys()) ==7:
            antall+=1
    return antall


print(counter(create_dict(read_file())))
