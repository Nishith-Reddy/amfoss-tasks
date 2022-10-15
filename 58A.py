s = input()
test = 0
for i in range(len(s)):
     if(s[i]=='h' and test==0):
         test=test+1
     elif(s[i]=='e' and test==1):
         test=test+1
     elif(s[i]=='l' and test==2):
         test=test+1
     elif(s[i]=='l' and test==3):
         test=test+1
     elif(s[i]=='o' and test==4):
         test=test+1
     if(test==5):
         break
if(test==5):
    print("YES\n")
else:
    print("NO\n")


        
    
