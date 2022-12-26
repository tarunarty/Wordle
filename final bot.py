from wordleprep import *

dataset = '5_upper'



#[3973, 'STEAL'], [3973, 'STALE'], [3973, 'SLATE'], [3973, 'LEAST']

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
    #m.sort(reverse = True)
    #print(m[:100])
    return data[table.index(max(table))]
          
#MANUAL LOGIC STATEMENTS        


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




L = import_dict(fname = dataset)

#MAIN BOT

def play_bot (alpha,k):
    #This final function plays the game
    
    
    
    L = import_dict(dataset)
    
    flag = 0
    
    fname = dataset
    data_b = import_dict(fname)
    #ans = choose(data_b)
    ans = k
    #print(ans + '\n')
    
    for i in range(6):
        if i == 0:
            word = alpha
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
        

win = 0
win_avg = 0
d = {1:0,2:0,3:0,4:0,5:0,6:0}



result = []
D=import_dict('2.txt')
for x in D:
            
    
    win = 0
    win_avg = 0
    d = {1:0,2:0,3:0,4:0,5:0,6:0}
   
    for k in L:
        
        res = play_bot(x,k)
        if res > 0:
            d[res] += 1
            win += 1
            win_avg += res
    
    win_avg = win_avg/win
    #lost = n - win
    result.append([win_avg,x])
    print(result[-1])
    
    
result.sort()
