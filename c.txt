print('linear seach')
n=int(input('enter the size of list n='))
num=[]
flag=0
print('enter the numbers')
for i in range(n):
  num.append(int(input()))
search=int(input('enter the num to be searched=')) 
for i in range(n):
  if(num[i]==search):
    print('number ',num[i],'is found at the index',i)
    flag=1
if(flag==0):
    print('The number you searched is not in the list')
