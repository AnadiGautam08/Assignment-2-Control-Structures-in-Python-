#Uses a for loop to iterate over numbers from 1 to 50.
# Calculates the sum of all integers in this range.
#Displays the final sum.


result=0
for x in range(1,51):
    result+=x
print("The sum of numbers from 1 to 50 is:",result)


'''
Another way to do this :
    print("The sum of numbers from 1 to 50 is:",sum(range(1,51)))
'''