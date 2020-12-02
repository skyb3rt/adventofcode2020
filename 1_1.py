
def read_file():
    with open ("1.txt", 'r' ) as file:
        return [int(x) for x in file]

def finn_to(verdi,listen):
    for x in range(0,len(listen)):
        tall1= verdi - listen[x]
        if tall1 in listen[x:]:  
            tall2=listen[x]
            return (tall1*tall2)

print(finn_to(2020,read_file()))
