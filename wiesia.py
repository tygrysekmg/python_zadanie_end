from collections import Counter
from pip._vendor.progress import counter
class Grzegorz:
    """Main class"""
    
    def __init__(self):
        print("zadanie staz")
    def read(self,total,dictp,kop,bruce,w,s):
        self.total = 0
        self.dict = {}
        self.kop = []
        self.bruce = 0
        self.w = []
        self.s = 0;
        h = 0
        
        print("podaj 1 2 lub 3   ")
        hoo = int(input())
        
        
        
        
        
        text_file = open("piotr.txt","r")
        lines = text_file.readlines()
        for line in lines:
            for word in line.split():
                
                total += 1
                
                
                
                kop.append(word)

            
        
        
        
        
        
        
        
        
            
            
        j = Counter(kop)      
        for z in j:
            
            
            dictp[z] = j[z]
        nb = list(dictp.values())
        k = max(nb)
        f = ''
        if (hoo == 1):
            print(k)
        if ( hoo == 2):
            print("podaj slowo   ")
            hoo2 = input()
            
            f = dictp[hoo2]
            print(f)
            

            
        
            
            
            
            
            
        
        
            
            
            
            
            
            
            
                
                    
        print(str(dictp))
        
        



      
piotr = Grzegorz()
piotr.read(0,{},[],1,[],-1)


