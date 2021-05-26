def fizzBuzz():
    for num in (range(1,101)):
        if num % 3 == 0:
            print("Fizz")
        if num % 5 == 0:
            print("Buzz")
        print(num)
