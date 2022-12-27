def instructions(input_path):
    with open (input_path, 'r') as ifp:
        l = [e[:-1] for e in ifp]
    l = l[l.index('')+1:]
    x = []
    for i in l:
        t = []
        for j in i.split(' '):
            try:
                t.append(int(j))
            except ValueError:
                continue
        x.append(t)
    return x

def start(input_path):
    with open (input_path, 'r') as ifp:
        l = [e[:-1] for e in ifp] 
    s = l[:l.index('')-1]
    nr = l[l.index('')-1].split(" ")[-2] #number of columns
    columns = []
    
    return len(s[0]), s[0]
print(start('input.txt'))