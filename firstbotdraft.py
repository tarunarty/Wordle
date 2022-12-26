from wordleprep import *
import time
t=time.time()
import random

#Module - Back-end Functions

def import_dict(fname):
    '''This function imports database of 5 letter words and returns a list '''
    

    f = open(fname,'r')
    L = f.read().split()
    f.close()
    
    return L


def choose (L):
    '''This function accepts the database and returns a random 5 letter word'''
    
    n = len(L)
    index = random.randrange(0,n)
    return L[index]


def check(word,ans):
    '''This function gives result for each of the 6 choices in the form 
    of a list (see meaning of values below)  OR "SUCCESS" for right answer'''

    if word == ans:
        return "SUCCESS"
    
    result = []
    '''
    1 - perfect match
    0 - letter present but index mismatch
    -1 - letter not present
    '''
    
    for i in range(5):
        if word[i] == ans[i]:
            result.append(1)
        elif word[i] in ans:
            result.append(0)
        else:
            result.append(-1)
    
    '''
    no of corrections = #char in word - #char in ans
    
    CAUTION: we dont consider corrections symmetrically
    
    chars = set(word.split())
    
    for each distinct character in word, we check no of corrections required
    
    '''
                    
    chars = set(word)
    
    for x in chars:
        freq_w = word.count(x)
        freq_a = ans.count(x)
        
        n = freq_w - freq_a
        #no of corrections req for the character x
        
        if( n > 0):
            
            for i in range(5):
                
                if x != word[i] or result[i] == 1:
                    continue
                result[i] = -1
                n -= 1
                
                if n == 0:
                    break
        
    return result

#MAIN MODULE OF THE GAME

def play ():
    '''This final function plays the game''' 
    flag = 0
    
    fname = 'five'
    data_b = import_dict(fname)
    ans = choose(data_b)

    
    for i in range(6):
        word = input("Enter Word:  ")
        res = check(word,ans)
        print()
        print(res)
        print()
        
        if res == "SUCCESS":
            flag = 1
            print("GAME WON in",i+1,"steps")
            break

    if not(flag):
        print(ans)




#Module 1 - Imports database of 5 letter words, and also gives freq dist
def import_dict(fname):
    '''This function imports database of 5 letter words and returns a list '''
    

    f = open(fname,'r')
    L = f.read().split()
    f.close()
    
    return L

def freq_dist (data):
    
    D = {}
    
    
    meta = ''
    for word in data:
        meta += word
        
    for i in range(26):
       x = meta.count(chr(i+65))
       y = chr(i + 65)
       D[y] = x 
    return D

#Module 2 - MAIN ALGORITHM: 
    
    #1. Uses Freq Dist
    
def best_guess (data):
    '''Accepts dynamic dataset and returns best possible guess for next word'''
    
    '''
    Assumptions:
        
        1. Filtering of data on the basis of result of previous attempt has already
        been performed
        2. Best means word with max freq points
    '''
    
    freq_d = freq_dist(data)
    
    table = []
    m = []
    
    
    
    for word in data:
        point = 0
        for char in set(word):
            point += freq_d[char]
        table.append(point)
        m.append([point,word])
##    m.sort(reverse = True)
##    return m
    return data[table.index(max(table))]
          


def best_guess_2(L):
    return None
    












       


def minus1 (word,i, dataset):
    
    ans = []
    
    for x in dataset:
        if word[i] not in x:
            ans.append(x)
    
    return ans


def plus1 (word,i, dataset):

    ans = []
    
    for x in dataset:
        if word[i] == x[i]:
            ans.append(x)
    
    return ans

def zero (word, i, dataset):
    
    ans = []
    
    for x in dataset:
        if word[i] not in x:
            continue
        if word[i] == x[i]:
            continue
        ans.append(x)
        
    return ans



def reduce_d (word, answer, dataset):
    '''Takes word put into last try, answer received, and dataset used in last
    try. Returns reduced dataset which eliminates using minus1, zero, and plus
    1 functions'''
    
    d = dataset
    
    for i in range(5):
        if answer[i] == -1:
            flag = 1
            char = word[i]
            
            for k in range(5):
                if word[k] == char and answer[k] != -1:
                    flag = 0
                    break
            if (flag):
                d = minus1(word, i, d)
        elif answer[i] == 0:
            d = zero(word, i, d)
        elif answer[i] == 1:
            d = plus1(word, i, d)
        
    return d




L = import_dict(fname = 'five')

#MAIN BOT

def play_bot (ans):
    #This final function plays the game
    
    
    
    L = import_dict('five')
    
    flag = 0
    
    fname = 'five'
    data_b = import_dict(fname)
    #ans = choose(data_b)
    #print(ans + '\n')
    
    for i in range(6):
        if i == 0:
            word = 'STALE'
        #elif i == 1:
            #word = 'CHOIR'
        else:
            word = best_guess(L)
        
        res = check(word,ans)
        #print()
        #print(word)
        #print(res)
        #print()

        
        if res == "SUCCESS":
            flag = 1
            return i + 1
            #print("GAME WON in",i+1,"steps")
            break
        
        L = reduce_d(word, res, L)
        
    if not(flag):
        return -1
        #print(ans)
        
#brute force
def brute(data):
    freq_d = freq_dist(data)
        
    table = []
    m = []
    
    
    
    for word in data:
        point = 0
        for char in set(word):
            point += freq_d[char]
        table.append(point)
        m.append([point,word])
    m.sort(reverse = True)
    return m[-5:]
lis=[]
for elem in brute(L):
    lis.append(elem[1])




#lis=["REALSs"]
n = 5000
liststart=lis.copy()
k=len(lis)
win = 0
win_avg = 0
d = {1:0,2:0,3:0,4:0,5:0,6:0}
for i in range(n):
    ans=choose(L)
##    for x in range(len(liststart)):
    res = play_bot(ans)
    if res > 0:
        d[res] += 1
        win += 1
        win_avg += res
print(win_avg/win)
print("Time take to run",time.time()-t)
print()
winprint=[]
lost=[]
##
##for z in range(k):
##    winprint.append(win_avg[z]/win[z])
##    lost.append(n - win[z])
##        
##    print(f'AVERAGE STEPS - {winprint[-1]}')
##    #print(f'WIN RATE -      {winprint[-1]/n}')
##    print()
##    #print(d)

































      


    
    
