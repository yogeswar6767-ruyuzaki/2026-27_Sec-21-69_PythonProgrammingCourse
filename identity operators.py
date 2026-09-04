# identity operators excersice 
a = [1,2,3,]
b = a
result = a is  b # identity operator
print("result of ",a, "is  ",b, "is : ", result) #answer is true because both a and b point to the same object in memory 

c = [1,2,3,4]
d = [1,2,3,4]
result = c is  d # identity operator 
print("result of ",c, "is ",d, "is : ", result) #answer is false because both c and d point to different objects in memory even though they have the same values

e = [1,2,3,]
f = e
result = e is not  f # identity operator
print("result of ",e, "is not ",f, "is : ", result) # answer is false because both e and f point to the same object in memory 

g = [1,2,3,4]
h = [1,2,3,4]
result = g is not  h # identity operator 
print("result of ",g, "is not ",h, "is : ", result) # answer is true because both g and h point to different objects in memory