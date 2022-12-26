import random


'''
Genetic Algorithm -

    1. Create a population:
        
        a. random
        b. size of every seq in pop == len(items)

    2. Compute score for every seq in population:
        
        a. Remove the seq that died
        b. No seq left == dead population
        
        C. In every gen, show best score
        
    3. Then we select any two random surviving seq (n/2) times and 
        make two babies
    
        a. make_baby()
'''




weights = [3,2,1,1,1]
val = [4,3,2,2,2]
n = len(weights)


w = 5
#weight


def score (l):
    
    s = 0
    v = 0
    for i in range(n):
        if l[i] == 0:
            continue
    
        s += weights[i]
        v += val[i]
        if s > w:
            return -1
        
    return v
    

def make_baby (p1,p2):
    n = len(p1)
    
    l = []
    for i in range(n):
        gene = random.choice([p1[i],p2[i]])
        j = random.random()
        m_factor = 0.05
        if j <= m_factor:
            gene = [1,0][gene]
        l.append(gene)
        
        
    
    return l
    

k = (2**(n-1))

P = []
#initialise population
for i in range(k):
    
    l = []
    #random seq
    for i in range(n):
        l.append(random.randint(0, 1))
    
    P.append(l)



for q in range(100):
    table = []
    for i in P:
        if score(i) != -1:
            table.append([score(i),i])
    
    table.sort(reverse = True)
    print("MAX SCORE = ",table[0][0])
    
    
    
    P = []
    for i in range(k//2):
        
    
        a = random.choice(table)
        b = random.choice(table)
        
        if a[0] >= b[0]:
            p1 = a[1]
        else:
            p1 = b[1]
            
        
        a = random.choice(table)
        b = random.choice(table)
        
        if a[0] >= b[0]:
            p2 = a[1]
        else:
            p2 = b[1]
            
        b1 = make_baby(p1, p2)
        b2 = make_baby(p1, p2)
        
        m_factor = 0.05
        
       
            
        
        P.append(b1)
        P.append(b2)
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
