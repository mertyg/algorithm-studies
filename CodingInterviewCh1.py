#Problem1

#with additional structure
def is_unique(str):
    letter_set = set()
    for char in str:
        if char not in letter_set:
            letter_set.add(char)
        else:
            return False
    return True

from bitarray import bitarray
#using bit array
def is_unique2(str):
    maxChar = ord(max(str))
    minChar = ord(min(str))
    b = bitarray(maxChar-minChar+1)
    b.setall(0)
    for char in str:
        pos = ord(char) - minChar
        if b[pos]==1:
            return False
        else:
            b[pos]=1
    return True

#sorting based NlogN solution
def check_permutation(str1,str2):
    str1 = sorted(str1)
    str2 = sorted(str2)
    return str1==str2

#O(N) solution
from collections import Counter

def check_permutation2(str1,str2):
    char_dict = Counter()
    for char in str1:
        char_dict[char]+=1
    for char in str2:
        if char_dict[char] == 0:
            return False
        else:
            char_dict[char]-=1
    return True

def URLify(str,length):
    last=len(str)-1
    for pos in reversed(range(length)):
        if str[pos]!=' ':
            str[last]=str[pos]
            last-=1
        else:
            str[last]='0'
            str[last-1]='2'
            str[last-2]='%'
            last-=3
    return str

def palindrome_permutation(str):
    str = str.lower()
    bitvec = bitarray([0 for i in range(128)])
    for char in str:
        bitvec[ord(char)]= not(bitvec[ord(char)])
    count = 0
    for pos in range(128):
        if bitvec[pos] == 1 and pos!=ord(" "):
            count+=1
            if count>1:
                return False
    return True

def one_away(str1,str2):
    diff = len(str1)-len(str2)
    if abs(diff)>1:
        return False
    if diff<0:
        short = str1
        long = str2
    else:
        short = str2
        long = str1
    i,j = (0,0)
    done = False
    while i<len(short) and j<len(long):
        if short[i]!=long[j]:
            if done:
                return False
            done = True
            if diff!=0:
                j+=1
            else:
                (i, j) = (i + 1, j + 1)
        else:
            (i,j) = (i+1,j+1)
    return True

def string_compression(string):
    current = string[0]
    length = len(string)
    counter = 0
    comp = list()
    for pos in range(length):
        if string[pos]==current:
            counter+=1
        else:
            comp.append(current+str(counter))
            current = string[pos]
            counter=1
    comp.append(current+str(counter))
    compd = "".join(comp)
    if len(compd)>length:
        return string
    return compd


def matrix_rotation(matrix):
    N = len(matrix[0])
    for place in range(N // 2):
        for shell in reversed(range(place, N-place-1)):
            temp = matrix[place][shell]
            matrix[place][shell] = matrix[N-shell-1][place]
            matrix[N-shell-1][place] = matrix[N-place-1][N-shell-1]
            matrix[N-place-1][N-shell-1] = matrix[shell][N-place-1]
            matrix[shell][N-place-1] = temp
    return matrix

def zero_matrix(matrix):
    rows = set()
    cols = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                rows.add(i)
                cols.add(j)
    for i in rows:
        for j in range(len(matrix[0])):
            matrix[i][j]=0
    for j in cols:
        for i in range(len(matrix)):
            matrix[i][j]=0
    return matrix


def string_rotation(string1,string2):
    if len(string1)!=len(string2):
        return False
    all = "".join(list([string1,string1]))
    return all.find(string2)>=0
