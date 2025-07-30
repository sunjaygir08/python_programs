# i=1     #i is initializing
# while (i<=20):      #conditional expression
#     print(i, end=' ') #printing i with space
#     i+=1  #incrementing i by 1
# print()  #printing a new line after the loop ends

# while loop to print numbers from 1 to 100 that are divisible by both 4 and 5
i=1
while i <= 100:
    if (i%4==0 and i%5==0):
        print(i, end=' ')
    i +=1

#count the numbers of digits in given value

num=int(input("\n Enter any value : "))
count=0
while num > 0:
    num = num // 10  # integer division to remove the last digit
    count += 1  # increment the count for each digit
print("Number of digits:", count)  # print the total count of digits