
def read_file():
    with open ("1.txt", 'r' ) as file:
        return [int(x) for x in file]


def finn_to(verdi,listen):
    for x in range(0,len(listen)):
        tall= verdi - listen[x]
        if tall in listen[x:]:  
            return (tall*listen[x])

print(finn_to(2020,read_file()))
