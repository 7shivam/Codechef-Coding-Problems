t=int(input())
for i in range(t):
    n=int(input())#7
    p=input()
    l=p.split()
    gd=0
    inf=999

    for i in range(0, len(l)):
        l[i] = int(l[i])

    for i in range(5):
        l.insert(i,inf)


    n=len(l)

    for i in range(5,n):
        if l[i] < l[i-1]:
            if l[i] < l[i-2]:
                if l[i] < l[i-3]:
                    if l[i] < l[i-4]:
                        if l[i] <l [i-5]:
                            gd=gd+1
        
            
        
        
    print(gd)
    
      
    
        


        

    
        
            
        
    
        
        
        
        


