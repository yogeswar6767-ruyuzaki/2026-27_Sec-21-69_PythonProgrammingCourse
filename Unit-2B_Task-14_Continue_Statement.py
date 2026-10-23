#program to demonstrate use of continue statement using for loop 
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

#program to demonstrate use of continue statement using while loop
j = 1
while j < 11:
    if j == 5:
        j += 1
        continue
    print(j)
    j += 1