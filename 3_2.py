def read_file():
    geology=[]
    with open ("3.txt", 'r' ) as input_file:
        for line in input_file:
            geology.append(list(line.strip()))
    return geology

def trees(geology,right,down):
    j=0
    nr_of_trees=0
    for i in range(0,len(geology),down):
        if geology[i][j] == '#':
            nr_of_trees+=1
        j+=right
        if j>=(len(geology[0])):
            j-=(len(geology[0]))
    return(nr_of_trees)  

def multiply(geology,slopes):
    total=1
    for x,y in slopes:
        total*=trees(geology,x,y)
    return(total)

geology=read_file()
slopes=[[1,1],[3,1],[5,1],[7,1],[1,2]]
print(multiply(geology,slopes))

