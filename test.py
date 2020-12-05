import re

my_string = 'abcdefrf156468'

for tegn in my_string:
    if tegn not in ('a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9'):
        print (tegn)


pattern=re.compile("[a-f0-9]+")
print(pattern.fullmatch(my_string))