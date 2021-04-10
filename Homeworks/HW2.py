#Creating a list
aRandomList = list(range(0,24))

#Swapping the first half of the list with second half
half = int(len(aRandomList)/2)
swappedList = aRandomList[half:]
swappedList += aRandomList[:half]

#Printing the swapped list to screen
print(swappedList)



#Asking user for one digit number
one_digit_number = int(input("Type a single-digit number:"))



#Printing all of the even numbers 0 to n (including n)
if one_digit_number<10:
    print("Even numbers between 0 to {a} (including {a}):".format(a=one_digit_number))
    for number in range(0,one_digit_number+1):
        if number%2==0:
            print(number,end=" ")
else:
    print("Your number is not a single-digit number. You typed",one_digit_number)
#Done!
