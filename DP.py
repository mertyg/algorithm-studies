import sys

#basic version
def coin_change(n, coins):
    W = dict()
    syn = dict()
    W[0] = 0
    syn[0] = [0]
    for i in range(1,n+1):
        W[i] = sys.maxsize
    for i in range(1,n+1):
        for c in coins:
            if i>=c and W[i]>W[i-c]:
                W[i] = 1+W[i-c]
                syn[i] = syn[i-c] + [c] 
    return syn[n][1:]

n = 20
coins = [1,2,4]

#with using a coin at most 2 times.
def limited_coin_change(n,coins):
    W = dict()
    W[0,0] = 0
    for i in range(1,n+1):
        W[i,0] = sys.maxsize
    for c in range(len(coins)):
        W[0,c+1] = 0
    for c in range(len(coins)):
        for i in range(1,n+1):
            use1, use2 = sys.maxsize, sys.maxsize
            if coins[c]<=i:
                use1 = 1+W[i-coins[c],c]
            if 2*coins[c]<=i:
                use2 = 2+W[i-2*coins[c],c]
            min_all = min(use1,use2,W[i,c])
            W[i,c+1] = min_all
    return W[n,len(coins)]

print(limited_coin_change(n,coins))


def pred(i,jobs):
    j = i
    while jobs[j][1]>jobs[i][0] and j>-1:
        j-=1
    return j+1

def weighted_job_scheduling(jobs):
    jobs = sorted(jobs,key = lambda x: x[1])
    print(jobs)
    W, m = dict(),dict()
    W[0] = 0
    m[0] = []
    for i in range(1,len(jobs)+1):
        W[i] = max(jobs[i-1][2]+W[pred(i-1,jobs)],W[i-1])
    return W[len(jobs)]

jobs = [(3, 10, 20), (1, 2, 50), (6, 19, 100), (2, 100, 200)]


def prev(i,t,jobs):
    pick_from = min(jobs[i-1][0],t)
    pos = 0
    while jobs[pos][1]<pick_from:
        pos+=1
    return max(0,pos-1)

def prev_2(i,t,jobs):
    if jobs[i-1][0]<t:
        pos = i-1
        while jobs[i-1][0]<jobs[pos][1] and pos>=0:
            pos-=1
        return max(0,pos)
    else:
        return i-1

#this time with 2 machines
def weighted_job_2_scheduling(jobs):
    jobs = sorted(jobs,key = lambda x: x[1])
    print(jobs)
    W, overlaps, schedules = dict(), list([0]),dict()
    W[0] = dict()
    schedules[0] = dict()
    for i in range(jobs[-1][1]+1):
        W[0][i] = 0
        schedules[0][i] = []
    for i in range(1,len(jobs)+1):
        W[i] = dict()
        schedules[i] = dict()
        for t in range(jobs[-1][1]+1):
            not_assigned = W[i-1][t]
            assigned = W[prev_2(i,t,jobs)][jobs[i-1][0]]+jobs[i-1][2]
            if assigned>not_assigned:
                W[i][t] = assigned
                schedules[i][t] = schedules[prev_2(i,t,jobs)][jobs[i-1][0]]+[jobs[i-1]]
            else:
                W[i][t] = not_assigned
                schedules[i][t] = schedules[i-1][t]
    maxi = 0
    maxs = []
    for key,value in W[len(jobs)].items():
        if value>maxi:
            maxi = value
            maxs = schedules[len(jobs)][key]
    print(maxs)

I = list()
I.append((0, 3, 3))
I.append((1, 4, 2))
I.append(( 0, 5, 4))
I.append(( 3, 6, 1))
I.append(( 4, 7, 2))
I.append(( 3, 9, 5))
I.append(( 5, 10, 2))
I.append(( 8, 10, 1))

weighted_job_2_scheduling(jobs)
weighted_job_2_scheduling(I)
