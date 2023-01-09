
num = int(input("Enter a number: "))

for number in range(1, num+1):
    if number % 3 == 0 and number % 5 ==0:
    # if number in range is divisible by 3 and 5, in output in prints "FizzBuzz" instead of number
         print("FizzBuzz")
    elif number % 3 == 0:
    # if number in range is divisible by 3, in output in prints "Fizz" instead of number
        print("Fizz")
    elif number % 5 == 0:
    # if number in range is divisible by 5, in output in prints "Buzz" instead of number
        print("Buzz")
    else:
    # if number in range is not divisible by 3 or 5, it just prints the number
        print(number)