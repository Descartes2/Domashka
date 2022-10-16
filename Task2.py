def Triangle(a):
    for i in range(0,a+1,1):
        S=' '*(a-i)+(i*2+1)*'*'+' '*(a-i)
        print (S)
   
def Distanse(hist1, hist2):
    Dim=len(hist1)
    Summ=0
    for i in range(0,Dim,1):
        Summ+=(hist1[i]-hist2[i])**2
    Ro=Summ**0.5
    return(Ro)   
        
a=3
hist1=[0,2,5]
hist2=[0,6,2]
Ro=Distanse(hist1, hist2)

Triangle(a)
print(Ro)
