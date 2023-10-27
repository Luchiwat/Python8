my_set1 = {10,20,True,10,'sau',(20,'iot')}

for data in my_set1 :
    print(data)

my_list = list ( my_set1 )
print(my_list)
my_list[2] = 'IOT'
print(my_list)
my_set1= set(my_list)
print(my_set1)

# set method
my_set1.add(999)
my_set1.add("IOT")
print(my_set1)
my_set1.pop()
print(my_set1)
my_set2=my_set1.copy()
print(my_set2)
my_set1.remove(999)
print(my_set1)

# set function
# len()
print(len(my_set1))
#min() , max()
my_set3={10,20,30,50,40}
print(min(my_set3))
print(max(my_set3))