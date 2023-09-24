pos=-1
def search(list):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i+=1
    return False

list=[1,2,3,4,5,6,11,8,9,10]
n=12
if search(list):
    print("Found at ",pos+1)
else:
    print("Not Found")