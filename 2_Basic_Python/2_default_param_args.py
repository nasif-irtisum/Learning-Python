def sum (num1, num2, num3 = 0):
    result = num1 + num2;
    return result


#args
def all_sum (num1, num2, *numbers):
    print (numbers)
    for num in numbers:
        print (num)

    print (numbers[2])
    return num1+num2


total = all_sum (45, 46, 47, 50, 51, 52);
print ("Sum of first two: ", total)