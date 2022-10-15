n = int(input())
cnt = 0
cnt1 = 0
while(n>0):
    l = n%10
    n = n/10
    if((l == 4)or(l == 7)):
        cnt1 = cnt1 +1
    cnt = cnt + 1
print(cnt)
print(cnt1)
if(cnt == cnt1):
    print("lucky number")
else:
    print("unlucky number")
