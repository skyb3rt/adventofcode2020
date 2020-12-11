def read_file():
    with open ("10.txt", 'r' ) as f:
        return sorted([int(i) for i in f.readlines()])


def jolt_adapters(l):
    one_jolt_diff=0
    tree_jolt_diff=0
    current =0
    l.append(max(l)+3)
    for x in range(0,len(l)):
        if l[x]-current ==1:
            one_jolt_diff+=1
        if l[x]-current ==3:
            tree_jolt_diff+=1
        current=l[x]
    return one_jolt_diff*tree_jolt_diff

print(jolt_adapters(read_file()))