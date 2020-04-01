def fizzbuzz(n):
    if n % 3 == 0:
        if n % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    else:
        if  n % 5 == 0:
            print("Buzz")
        else:
            print(n)