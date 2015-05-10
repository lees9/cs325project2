v = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
a = 2000

def changegreedy(v, a):
    temp = [] #denominations backwards
    temp2 = [] #temp denominations counter
    
    c = [] #buckets
    coins_added = [] #coins added
    m = 0 #number of coins

    for i in range((len(v)), 0, -1):
        temp.append(v[i-1])

    for i in range(0, len(v)):
        temp2.append(0)

    while a != 0:
        for i in range(0, len(v)):
            if temp[i] <= a:
                coins_added.append(temp[i])
                m += 1
                a -= temp[i]
                temp2[i] += 1
                break

    for i in range((len(temp2)), 0, -1):
        c.append(temp2[i-1])
        
    
    print c[:]            
    print m


#start main
for i in range(a, 2201):
    print "For A: " + str(i)
    changegreedy(v, i)
