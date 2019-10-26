a,b,c = map(int,input().split())

wo = b-a-1
no = c-b-1
if(wo<no):
    print(no)
else:
    print(wo)