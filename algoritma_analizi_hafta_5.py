import sys
my_L_1=[]
size_1=sys.getsizeof(my_L_1)
print("ba�lang�� boyutu : ",size_1,end="")
print()
for i in range(20000):
    my_L_1.append(str(i)+" test")
    if(size_1!=sys.getsizeof(my_L_1)):
        print("dizi yer de�i�tirdi , amortized cost ",end=" ")
        size_1=sys.getsizeof(my_L_1)
        print("size: ",size_1)