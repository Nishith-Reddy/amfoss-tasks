s=input()
a=[]
i=0
while(i<len(s)-):
    if(s[i]=="."):
        a.append("0")
        i=i+1
    elif((s[i]=="-")and(s[i+1]==".")):
        i=i+3
        a.append("1")
    else:
        a.append("2")
        i=i+3
temp=""
temp=temp.join(a)
print(temp)

        
        
    
