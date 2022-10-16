Interval=[0,0,0,0,0,0,0,0,0,0]
Massiv=[]

for i in range(0,1000000,1):
    Massiv.append(156)

def Gistogramma(Massiv):
    Interval=[0,0,0,0,0,0,0,0,0,0]
    
    for i in range(0,1000000,1):
        Interval[Massiv[i]//100]+=1
        
    return(Interval)

Interval=Gistogramma(Massiv)
print(Interval)

