# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    choise = input().rstrip()
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    if choise == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    else:
        with open('./tests/06', 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    
    # this is the sample return, notice the rstrip function
    return pattern, text 

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    p = 10**9+7
    x = 263
    m = len(pattern)
    n = len(text)
    if m>n:
        return[]
    h = pow(x, m-1,p)
    p_hash = 0
    t_hash = 0
    ind = []
    for i in range(m):
        p_hash = (p_hash * x + ord(pattern[i]))%p
        t_hash = (t_hash * x + ord(text[i]))%p
    for i in range (n-m+1):
        if p_hash == t_hash and pattern == text[i:i+m]:
            ind.append(i)
        if i<n-m:
            t_hash = (t_hash - h*ord(text[i]))%p
            t_hash = (t_hash*x + ord(text[i+m]))%p
            t_hash = (t_hash + p)%p

    # and return an iterable variable
    return ind


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

