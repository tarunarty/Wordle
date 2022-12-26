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
        word = input("Enter Word:  ").upper()
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

play()
