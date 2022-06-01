def fibo(amount):
    number1 = 0
    number2 = 1
    countdown = 0

    list = []

    if amount <= 0:
        print("more than 0")

    elif amount == 1:
        print(number1)

    else:
        while countdown < amount:
            list.append(number1)
            fib = number1 + number2
            number1 = number2
            number2 = fib
            countdown += 1
        return (list)


