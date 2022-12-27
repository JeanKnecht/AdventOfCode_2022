def check(l):
    for i in l:
        if l.count(i) > 1:
            return True
    return False

def bestand(input_path):
    with open(input_path, 'r') as ifp:
        buffer = ifp.read().replace('\n', '')
    #buffer = "nppdvjthqldpwncqszvftbrmjlhg" #test buffer
    for i,e in enumerate(buffer):
        if i >= 13:
            if check(buffer[i-13:i+1]):
                continue
            print(i+1)
            break
bestand('input.txt')