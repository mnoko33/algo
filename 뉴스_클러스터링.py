import re

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    A, B, I = [], [], []
    regex = re.compile('[^a-zA-Z]')
    for i in range(len(str1) - 1):
        if regex.search(str1[i]) == None and regex.search(str1[i+1]) == None:
            A.append(str1[i]+str1[i+1])
    for i in range(len(str2) - 1):
        if regex.search(str2[i]) == None and regex.search(str2[i+1]) == None:
            B.append(str2[i]+str2[i+1])
    total = len(A) + len(B)
    while A:
        a = A.pop(-1)
        if a in B:
            I.append(a)
            B.remove(a)
    I = len(I)
    U = total - I
    
    if not U:
        return 65536
    
    return int(65536*I/U)