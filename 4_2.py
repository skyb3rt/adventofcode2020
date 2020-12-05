import re

def read_file():
    with open ("4.txt", 'r' ) as file:
        return ''.join(file.readlines()).split('\n\n')

def create_dict(l):
    l_dict={'dict':[]}
    for x in range(0,len(l)):
        mydict={}
        l[x]=str(l[x]).replace('\n',' ')
        my_list=str(l[x]).split(' ')
        for x in range(0,len(my_list)):
            my_string_parts = str(my_list[x]).split(':')
            mydict.update({my_string_parts[0]:my_string_parts[1]})
        l_dict['dict'].append(mydict)
    return l_dict

def is_between(number, low,high):
    return number in range(low,high+1)

def is_valid(d):
    byr= d.get('byr')
    iyr= d.get('iyr')
    eyr= d.get('eyr')
    hgt= d.get('hgt')
    hcl= d.get('hcl')
    ecl= d.get('ecl')
    pid= d.get('pid')
    
    if not is_between(int(byr),1920,2002): return False
    if not is_between(int(iyr),2010,2020): return False
    if not is_between(int(eyr),2020,2030): return False
    
    if str(hgt).endswith('in'):
        if not is_between(int((hgt).replace('in','')),59,76): return False
    elif str(hgt).endswith('cm'):
        if not is_between(int((hgt).replace('cm','')),150,193): return False
    else: 
        return False    

    if not ecl in ('amb','blu','brn','gry','grn','hzl','oth'): return False
    
    if not len(hcl) == 7 or not hcl[0] =='#': return False 
    hcl_pattern=re.compile("[a-f0-9]+")
    if hcl_pattern.fullmatch(hcl[1:])==None : return False

    if not len(pid) == 9: return False

    return True

def counter(my_dict):
    antall = 0
    for x in range(0,len(my_dict['dict'])):
        d=my_dict['dict'][x]
        d.pop('cid',None)
        if len(d.keys()) ==7 and is_valid(d):
            antall+=1
    return antall

print(counter(create_dict(read_file())))