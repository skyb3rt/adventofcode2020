
def read_file():
    with open ("1.txt", 'r' ) as file:
        return [int(x) for x in file]

def finn_tre(verdi,listen):
    for i in range(0,len(listen)):
        tall=verdi-listen[i]

        for j in range(i+1,len(listen)):
            tall2 = listen[j]
            tall3 = tall-listen[j]
            if tall3 in listen:  
                tall1 = verdi-tall2-tall3
                return (tall1*tall2*tall3)

print(finn_tre(2020,read_file()))